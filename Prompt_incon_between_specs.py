from openai import OpenAI
from collections import Counter, defaultdict
import json
import os

# ==========================
# Configuration
# ==========================

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-5.5"

SPEC1 = "riscv-2025.pdf"
SPEC2 = "riscv-2026.pdf"

NUM_AGENTS = 6

# How many of the 6 agents must agree on a finding (by normalized key)
# for it to be treated as "majority consensus" (i.e. > half of NUM_AGENTS).
MAJORITY_THRESHOLD = (NUM_AGENTS // 2) + 1

PROMPT = """
Compare these two versions of the same specification document.

Find every difference between them: additions, removals, and modifications
of content across both documents.

Return ONLY a JSON object with a single top-level key "differences", whose
value is an array of objects. Each object must contain exactly these fields:

- page_first: page number in the first document (integer, or null if the
  content does not exist in the first document, e.g. for an Added item)
- page_second: page number in the second document (integer, or null if the
  content does not exist in the second document, e.g. for a Removed item)
- section: the section name or heading the difference belongs to
- type: one of "Added", "Removed", "Modified"
- description: a clear, specific description of what changed

Be exhaustive and precise. Do not summarize or group unrelated changes
together. Output only valid JSON matching this schema - no markdown
fences, no commentary, no extra top-level keys.
"""

# ==========================
# Strict JSON schema (Structured Outputs)
# ==========================
# Using json_schema output enforcement means the model literally cannot
# return malformed JSON, prose, or markdown fences - this was the main
# cause of some agents producing "proper" output and others not.

DIFF_SCHEMA = {
    "type": "json_schema",
    "name": "spec_diff",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "differences": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "page_first": {"type": ["integer", "null"]},
                        "page_second": {"type": ["integer", "null"]},
                        "section": {"type": "string"},
                        "type": {
                            "type": "string",
                            "enum": ["Added", "Removed", "Modified"]
                        },
                        "description": {"type": "string"}
                    },
                    "required": [
                        "page_first",
                        "page_second",
                        "section",
                        "type",
                        "description"
                    ],
                    "additionalProperties": False
                }
            }
        },
        "required": ["differences"],
        "additionalProperties": False
    }
}


# ==========================
# Upload PDFs
# ==========================

print("Uploading files...")

file1 = client.files.create(
    file=open(SPEC1, "rb"),
    purpose="user_data"
)

file2 = client.files.create(
    file=open(SPEC2, "rb"),
    purpose="user_data"
)

print("Files uploaded.")


# ==========================
# Run six independent agents
# ==========================

agent_results = []  # list of parsed dicts (only valid ones kept)

for i in range(NUM_AGENTS):

    print(f"Running agent {i+1}/{NUM_AGENTS}...")

    try:
        response = client.responses.create(
            model=MODEL,
            
                              # while still allowing 6 independent samples
            text={"format": DIFF_SCHEMA},
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": PROMPT
                        },
                        {
                            "type": "input_file",
                            "file_id": file1.id
                        },
                        {
                            "type": "input_file",
                            "file_id": file2.id
                        }
                    ]
                }
            ]
        )

        result_text = response.output_text

        # Save the FULL, untruncated output for inspection/debugging.
        with open(f"agent_{i+1}.json", "w", encoding="utf-8") as f:
            f.write(result_text)

        # Validate immediately. Structured Outputs should guarantee valid
        # JSON, but we still guard against empty/truncated responses
        # (e.g. if the model hit max_output_tokens).
        parsed = json.loads(result_text)

        if "differences" not in parsed or not isinstance(parsed["differences"], list):
            raise ValueError("Missing or malformed 'differences' array")

        agent_results.append(parsed["differences"])
        print(f"  agent {i+1}: {len(parsed['differences'])} findings parsed OK")

    except Exception as e:
        print(f"  agent {i+1} FAILED validation: {e}")
        # Do not append a broken result - better to have 5 good agents
        # than 6 agents where 1 silently corrupts the vote.

print(f"\n{len(agent_results)}/{NUM_AGENTS} agents produced valid, parseable JSON.")

if len(agent_results) == 0:
    raise RuntimeError("No agent produced valid JSON. Aborting.")


# ==========================
# Deterministic majority vote (done in Python, not by an LLM)
# ==========================
#
# Each finding is normalized into a key based on the fields that should be
# stable across independent re-runs (page numbers, section, type). The
# free-text "description" is expected to vary in wording between agents,
# so it is NOT part of the voting key - only used afterward for merging.

def normalize_key(item):
    return (
        item.get("page_first"),
        item.get("page_second"),
        (item.get("section") or "").strip().lower(),
        (item.get("type") or "").strip().lower(),
    )

# Group all findings across all agents by their normalized key.
grouped = defaultdict(list)  # key -> list of description strings
vote_counter = Counter()     # key -> number of agents that reported it

for agent_findings in agent_results:
    seen_keys_this_agent = set()
    for item in agent_findings:
        key = normalize_key(item)
        grouped[key].append(item.get("description", ""))
        # Count each agent at most once per key, even if it listed the
        # same finding twice.
        if key not in seen_keys_this_agent:
            vote_counter[key] += 1
            seen_keys_this_agent.add(key)

# Keep only findings that a real majority of agents agreed on.
majority_keys = [k for k, count in vote_counter.items() if count >= MAJORITY_THRESHOLD]

print(f"{len(vote_counter)} unique findings total; "
      f"{len(majority_keys)} reached majority ({MAJORITY_THRESHOLD}/{NUM_AGENTS} agents).")

majority_findings = []
for key in majority_keys:
    page_first, page_second, section, type_ = key
    majority_findings.append({
        "page_first": page_first,
        "page_second": page_second,
        "section": section,
        "type": type_,
        "descriptions": grouped[key],  # all worded variants, to merge next
        "agent_votes": vote_counter[key],
    })


# ==========================
# LLM merge pass: only rewrites wording, does NOT decide inclusion
# ==========================
# By this point inclusion/exclusion has already been decided deterministically
# in Python. The LLM's only job here is to produce one clean description per
# finding from the (possibly slightly differently worded) agent descriptions.

merge_prompt = f"""
For each finding below, you are given several agent-written descriptions of
the SAME already-confirmed difference. Merge them into a single clear,
accurate description. Do not add, remove, or reinterpret findings - only
consolidate wording. Keep page_first, page_second, section, and type exactly
as given.

Return ONLY a JSON object with a single top-level key "differences", an
array of objects with fields: page_first, page_second, section, type,
description.

Findings:
{json.dumps(majority_findings, indent=2)}
"""

print("Running merge pass on majority-consensus findings...")

merge_response = client.responses.create(
    model=MODEL,
    text={"format": DIFF_SCHEMA},
    input=merge_prompt,
)

merge_text = merge_response.output_text

# Validate the merge output too, before trusting it as final.
try:
    merged_parsed = json.loads(merge_text)
    if "differences" not in merged_parsed:
        raise ValueError("Missing 'differences' key in merge output")
    final_output = merged_parsed
except Exception as e:
    print(f"Merge pass produced invalid JSON ({e}); "
          f"falling back to raw majority findings without wording cleanup.")
    final_output = {
        "differences": [
            {
                "page_first": f["page_first"],
                "page_second": f["page_second"],
                "section": f["section"],
                "type": f["type"],
                # fall back to the first agent's wording
                "description": f["descriptions"][0] if f["descriptions"] else "",
            }
            for f in majority_findings
        ]
    }

with open("majority_result.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2)

print("Finished.")
print(f"{len(final_output.get('differences', []))} consensus differences written.")
print("Output saved as majority_result.json")