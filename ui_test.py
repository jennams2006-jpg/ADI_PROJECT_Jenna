
"""
Specification Toolchain Dashboard
==================================

Single-page Streamlit dashboard that wires together the three pieces of the
toolchain:

    1. Extractor.py        -> turns a spec PDF into a structured document.json
    2. Comparator.py       -> diffs two document.json files ("Inconsistency Check")
    3. Quality_Check.py    -> scores a document.json for completeness / accuracy /
                               table & figure capture ("Quality Checker")

...plus a placeholder "V-Plan Related Material Filter" section. That module
(VPlan.py) doesn't exist yet -- the hook below is intentionally minimal. Once
a VPlan.py that exposes `filter_material(document, requirement_text)` is
dropped next to this file, the pipeline will call straight into it. Until
then this section renders a clearly-labelled placeholder preview so the rest
of the UI can be built and demoed end-to-end.
"""

import json
import os
import tempfile
import types
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

import Comparator
import Quality_Check

# Load OPENAI_API_KEY from a local .env file (never committed, never shown
# in the UI) BEFORE Extractor is imported. This has to happen first: if we
# set the placeholder below before loading .env, load_dotenv() would refuse
# to override the placeholder and your real key would be silently ignored.
load_dotenv()

# Extractor.py builds its OpenAI client at IMPORT time
# (client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])), so importing it
# with no key set at all would crash the app before the UI can even render.
# Seed a placeholder ONLY if .env (or the real environment) didn't already
# provide a key; the sidebar remains available as a manual override.
os.environ.setdefault("OPENAI_API_KEY", "placeholder-set-key-in-sidebar")
import Extractor

# VPlan.py doesn't exist yet -- optional future module, see docstring above.
try:
    import VPlan
except ImportError:
    VPlan = None


# ==========================================================
# PAGE CONFIG + THEME
# ==========================================================

st.set_page_config(
    page_title="Specification Toolchain",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strict neutral palette -- white / grey / near-black only. The one place
# color carries real meaning (added/removed text in the diff viewer, and a
# flag on a failing quality metric) keeps a muted, desaturated accent; every
# other element in the interface is grayscale.
INK = "#111827"        # near-black, primary text / primary actions
INK_SOFT = "#374151"   # secondary text
MUTED = "#6b7280"      # tertiary / label text
FAINT = "#9ca3af"      # placeholder / disabled text
LINE = "#e5e7eb"       # borders
LINE_SOFT = "#eef0f2"  # hairline dividers
SURFACE = "#ffffff"
SURFACE_SUNK = "#f9fafb"
SURFACE_RAISED = "#f3f4f6"

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

.block-container {{
    padding-top: 1.4rem;
    padding-bottom: 2.5rem;
    max-width: 1500px;
}}

h1, h2, h3 {{ color: {INK}; }}

/* ---------- top masthead ---------- */
.masthead {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    padding-bottom: 14px;
    margin-bottom: 22px;
    border-bottom: 1px solid {LINE};
}}
.masthead-title {{
    font-size: 1.5rem;
    font-weight: 800;
    color: {INK};
    letter-spacing: -0.01em;
}}
.masthead-sub {{
    font-size: 0.82rem;
    color: {MUTED};
    margin-top: 2px;
}}
.masthead-meta {{
    font-size: 0.72rem;
    color: {FAINT};
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
}}

/* ---------- generic panel ---------- */
.panel {{
    background: {SURFACE};
    border: 1px solid {LINE};
    border-radius: 10px;
    padding: 20px 22px 22px 22px;
    margin-bottom: 16px;
}}
.panel-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.98rem;
    font-weight: 700;
    color: {INK};
    padding-bottom: 14px;
    margin-bottom: 16px;
    border-bottom: 1px solid {LINE_SOFT};
}}
.icon-badge {{
    width: 28px; height: 28px;
    min-width: 28px;
    border-radius: 7px;
    background: {SURFACE_RAISED};
    border: 1px solid {LINE};
    display: flex; align-items: center; justify-content: center;
    color: {INK};
}}
.icon-badge svg {{ width: 15px; height: 15px; }}

.section-label {{
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.07em;
    color: {MUTED};
    text-transform: uppercase;
    margin: 2px 0 10px 0;
}}

/* ---------- pipeline step cards ---------- */
.step-card {{
    border-radius: 9px;
    padding: 14px 16px;
    margin-bottom: 12px;
    border: 1px solid {LINE};
    border-left: 3px solid {LINE};
    background: {SURFACE};
    display: flex;
    gap: 12px;
    align-items: flex-start;
    transition: border-color 0.15s ease;
}}
.step-card.is-done {{
    border-left-color: {INK};
    background: {SURFACE_SUNK};
}}
.step-icon {{
    width: 32px; height: 32px;
    min-width: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    background: {SURFACE_RAISED};
    border: 1px solid {LINE};
    color: {FAINT};
}}
.step-card.is-done .step-icon {{ color: {INK}; background: {SURFACE}; border-color: {INK}; }}
.step-icon svg {{ width: 16px; height: 16px; }}
.step-title {{
    font-weight: 700;
    font-size: 0.92rem;
    color: {INK};
    margin-bottom: 3px;
}}
.step-desc {{
    font-size: 0.8rem;
    color: {MUTED};
    line-height: 1.4;
}}
.step-status {{
    margin-left: auto;
    font-size: 0.64rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    padding: 3px 9px;
    border-radius: 999px;
    white-space: nowrap;
    background: {SURFACE_RAISED};
    color: {FAINT};
    border: 1px solid {LINE};
}}
.step-card.is-done .step-status {{
    background: {INK};
    color: {SURFACE};
    border-color: {INK};
}}

/* ---------- results section ---------- */
.result-title-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
}}
.result-title {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.98rem;
    font-weight: 700;
    color: {INK};
}}
.output-path-label {{
    font-size: 0.68rem;
    color: {FAINT};
    font-weight: 700;
    letter-spacing: 0.06em;
    text-align: right;
    margin-bottom: 3px;
    text-transform: uppercase;
}}
.meta-box {{
    background: {SURFACE_SUNK};
    border: 1px solid {LINE};
    border-radius: 8px;
    padding: 13px 15px;
}}
.meta-row {{
    display: flex;
    justify-content: space-between;
    font-size: 0.81rem;
    padding: 6px 0;
    border-bottom: 1px solid {LINE_SOFT};
}}
.meta-row:last-child {{ border-bottom: none; }}
.meta-row .k {{ color: {MUTED}; }}
.meta-row .v {{ font-weight: 600; color: {INK}; }}

.placeholder-banner {{
    background: {SURFACE_SUNK};
    border: 1px solid {LINE};
    border-left: 3px solid {INK_SOFT};
    color: {INK_SOFT};
    border-radius: 6px;
    padding: 9px 13px;
    font-size: 0.78rem;
    margin-bottom: 12px;
    line-height: 1.5;
}}
.placeholder-banner code {{
    background: {SURFACE_RAISED};
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 0.76rem;
}}

.page-list-btn-hint {{ font-size: 0.72rem; color: {FAINT}; margin-bottom: 8px; }}

.legend-box {{
    border: 1px solid {LINE};
    border-radius: 8px;
    padding: 13px 15px;
    background: {SURFACE_SUNK};
}}
.legend-title {{ font-size: 0.7rem; font-weight: 700; color: {MUTED}; margin-bottom: 9px; letter-spacing: 0.06em; text-transform: uppercase; }}
.legend-row {{ display:flex; align-items:center; gap:9px; font-size:0.8rem; margin-bottom:7px; color:{INK_SOFT};}}
.legend-swatch {{ width: 11px; height: 11px; border-radius: 3px; }}

.diff-pane {{
    border: 1px solid {LINE};
    border-radius: 8px;
    padding: 13px 15px;
    line-height: 1.7;
    font-size: 0.85rem;
    max-height: 340px;
    overflow-y: auto;
    background: {SURFACE};
    color: {INK_SOFT};
}}
.diff-pane-header {{
    font-size: 0.72rem;
    font-weight: 700;
    color: {MUTED};
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}}

/* ---------- quality checker ---------- */
.gauge-wrap {{ display:flex; flex-direction:column; align-items:center; }}
.gauge {{
    width: 124px; height: 124px; border-radius: 50%;
    display:flex; align-items:center; justify-content:center;
}}
.gauge-inner {{
    width: 96px; height: 96px; border-radius: 50%;
    background: {SURFACE};
    display:flex; flex-direction:column; align-items:center; justify-content:center;
}}
.gauge-value {{ font-size: 1.85rem; font-weight: 800; color: {INK}; line-height:1; }}
.gauge-max {{ font-size: 0.68rem; color: {FAINT}; font-weight:600; }}
.gauge-label {{
    margin-top: 10px;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: {MUTED};
    text-transform: uppercase;
}}

.stat-box {{ text-align:left; }}
.stat-label {{ font-size: 0.76rem; color:{MUTED}; font-weight:600; margin-bottom:5px;}}
.stat-value {{ font-size: 1.3rem; font-weight:800; color:{INK}; margin-bottom:7px;}}
.stat-bar-track {{ background:{SURFACE_RAISED}; border-radius: 999px; height:6px; width:100%; overflow:hidden; }}
.stat-bar-fill {{ height:100%; border-radius:999px; background:{INK}; }}

.issue-row {{ display:flex; gap:9px; align-items:flex-start; font-size:0.82rem; margin-bottom:10px; color:{INK_SOFT};}}
.issue-dot {{ width:7px; height:7px; border-radius:50%; margin-top:5px; flex-shrink:0; }}
.issue-value {{ color:{FAINT}; }}

/* ---------- input column ---------- */
.file-row {{
    display:flex; align-items:center; justify-content:space-between;
    background:{SURFACE_SUNK}; border:1px solid {LINE}; border-radius:8px;
    padding:9px 12px; margin-bottom:8px; font-size:0.84rem; color:{INK_SOFT};
}}
.file-row .fname {{ display:flex; align-items:center; gap:9px; font-weight:600; color:{INK}; }}
.file-tag {{
    font-size: 0.62rem; font-weight:700; letter-spacing:0.04em;
    color: {MUTED}; background:{SURFACE_RAISED}; border:1px solid {LINE};
    padding: 1px 6px; border-radius: 4px; text-transform: uppercase;
}}
.file-size {{ color:{FAINT}; font-size:0.78rem; }}

/* run button + remove buttons: restyle Streamlit's default buttons */
div.stButton > button {{
    border-radius: 8px !important;
    border: 1px solid {LINE} !important;
    color: {INK_SOFT} !important;
    font-weight: 600 !important;
    background: {SURFACE} !important;
}}
div.stButton > button:hover {{
    border-color: {INK} !important;
    color: {INK} !important;
}}
.run-btn-wrap div.stButton > button {{
    background: {INK} !important;
    color: {SURFACE} !important;
    font-weight: 700 !important;
    border: 1px solid {INK} !important;
    padding: 0.62rem 0 !important;
    letter-spacing: 0.02em;
}}
.run-btn-wrap div.stButton > button:hover {{
    background: #000000 !important;
}}
.remove-btn-wrap div.stButton > button {{
    padding: 0.15rem 0.5rem !important;
    font-size: 0.75rem !important;
    color: {FAINT} !important;
    border-color: {LINE} !important;
}}
.page-btn-wrap div.stButton > button {{
    width: 100%;
    text-align: left !important;
    justify-content: flex-start !important;
    background: {SURFACE} !important;
    font-weight: 600 !important;
}}
.page-btn-wrap.is-active div.stButton > button {{
    background: {INK} !important;
    color: {SURFACE} !important;
    border-color: {INK} !important;
}}

hr {{ border-color: {LINE_SOFT} !important; }}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==========================================================
# ICONS  -- minimal monochrome line icons (stroke = currentColor)
# ==========================================================

def _svg(paths):
    return (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
        + paths + "</svg>"
    )

ICONS = {
    "input": _svg('<path d="M12 15V4"/><path d="M7 8l5-4 5 4"/><rect x="3" y="15" width="18" height="5" rx="1.2"/>'),
    "results": _svg('<rect x="3" y="3" width="7" height="7" rx="1.2"/><rect x="14" y="3" width="7" height="7" rx="1.2"/>'
                    '<rect x="3" y="14" width="7" height="7" rx="1.2"/><rect x="14" y="14" width="7" height="7" rx="1.2"/>'),
    "extraction": _svg('<path d="M7 3h7l5 5v12a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/>'
                        '<path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h6"/>'),
    "filter": _svg('<path d="M4 6h16"/><path d="M7 12h10"/><path d="M10.5 18h3"/>'),
    "compare": _svg('<rect x="3" y="4" width="8" height="16" rx="1.2"/><rect x="13" y="4" width="8" height="16" rx="1.2"/>'
                     '<path d="M11 10h2"/><path d="M11 14h2"/>'),
    "shield": _svg('<path d="M12 3l7 3v6c0 4.4-3 7.4-7 9-4-1.6-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>'),
    "doc": _svg('<path d="M7 3h7l5 5v12a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M14 3v5h5"/>'),
    "chevron": _svg('<path d="M9 6l6 6-6 6"/>'),
    "close": _svg('<path d="M6 6l12 12"/><path d="M18 6L6 18"/>'),
}


def icon(name, size=15):
    return f'<span style="display:inline-flex;width:{size}px;height:{size}px">{ICONS[name]}</span>'


# ==========================================================
# SMALL HTML HELPERS
# ==========================================================

def panel_header(icon_name, title):
    st.markdown(
        f"""<div class="panel-header">
        <span class="icon-badge">{icon(icon_name)}</span>
        {title}
        </div>""",
        unsafe_allow_html=True,
    )


def step_card(icon_name, title, desc, status_done):
    done_cls = "is-done" if status_done else ""
    status_text = "DONE" if status_done else "PENDING"
    st.markdown(
        f"""
        <div class="step-card {done_cls}">
            <div class="step-icon">{icon(icon_name, 16)}</div>
            <div style="flex:1">
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
            <div class="step-status">{status_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def result_title_row(icon_name, title, output_path):
    col_title, col_path = st.columns([2.4, 2])
    with col_title:
        st.markdown(
            f"""<div class="result-title">
            <span class="icon-badge">{icon(icon_name)}</span>
            {title}</div>""",
            unsafe_allow_html=True,
        )
    with col_path:
        st.markdown("<div class='output-path-label'>Output path</div>", unsafe_allow_html=True)
        st.code(output_path, language=None)


def meta_box(rows):
    html = "<div class='meta-box'>"
    for k, v in rows:
        html += f"<div class='meta-row'><span class='k'>{k}</span><span class='v'>{v}</span></div>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def gauge(percentage, size_label):
    percentage = max(0, min(100, percentage))
    if percentage >= 90:
        label = "Excellent"
    elif percentage >= 75:
        label = "Good"
    elif percentage >= 60:
        label = "Fair"
    else:
        label = "Needs attention"

    st.markdown(
        f"""
        <div class="gauge-wrap">
            <div class="gauge" style="background: conic-gradient({INK} {percentage}%, {LINE} 0)">
                <div class="gauge-inner">
                    <span class="gauge-value">{percentage:.0f}</span>
                    <span class="gauge-max">/{size_label}</span>
                </div>
            </div>
            <span class="gauge-label">{label}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def stat_bar(label, percentage):
    st.markdown(
        f"""
        <div class="stat-box">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{percentage:.0f}%</div>
            <div class="stat-bar-track">
                <div class="stat-bar-fill" style="width:{max(0,min(100,percentage))}%"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def human_size(num_bytes):
    for unit in ("B", "KB", "MB", "GB"):
        if num_bytes < 1024:
            return f"{num_bytes:.0f} {unit}" if unit == "B" else f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} TB"


def render_word_diff(old_text, new_text):
    """Word-level diff -> HTML. Removed words are struck-through with a
    muted red tint on the old side; added words get a muted green tint on
    the new side. This is the one place color carries real information."""
    old_words = old_text.split()
    new_words = new_text.split()
    matcher = SequenceMatcher(None, old_words, new_words)

    old_parts, new_parts = [], []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        old_chunk = " ".join(old_words[i1:i2])
        new_chunk = " ".join(new_words[j1:j2])
        if tag == "equal":
            old_parts.append(old_chunk)
            new_parts.append(new_chunk)
        elif tag == "delete":
            old_parts.append(f'<span style="background:#fbe9e9;color:#9a3131;text-decoration:line-through">{old_chunk}</span>')
        elif tag == "insert":
            new_parts.append(f'<span style="background:#eaf3ea;color:#2f6b3a">{new_chunk}</span>')
        elif tag == "replace":
            old_parts.append(f'<span style="background:#fbe9e9;color:#9a3131;text-decoration:line-through">{old_chunk}</span>')
            new_parts.append(f'<span style="background:#eaf3ea;color:#2f6b3a">{new_chunk}</span>')

    return " ".join(old_parts), " ".join(new_parts)


# ==========================================================
# BACKEND HOOKS
# ==========================================================

def run_extraction(pdf_path, label):
    """Run Extractor.parse_pdf on a saved PDF, isolating each run in its own
    temp folder by monkeypatching Extractor's module-level output globals."""
    out_dir = os.path.join(os.path.dirname(pdf_path), f"{label}_extract_output")
    image_dir = os.path.join(out_dir, "images")
    table_dir = os.path.join(out_dir, "tables")
    figure_dir = os.path.join(out_dir, "figures")
    for d in (image_dir, table_dir, figure_dir):
        os.makedirs(d, exist_ok=True)

    Extractor.OUTPUT_DIR = out_dir
    Extractor.IMAGE_FOLDER = image_dir
    Extractor.TABLE_FOLDER = table_dir
    Extractor.FIGURE_FOLDER = figure_dir

    Extractor.parse_pdf(pdf_path)

    json_path = os.path.join(out_dir, "document.json")
    with open(json_path, "r", encoding="utf-8") as f:
        document = json.load(f)
    return document, json_path


def run_vplan_filter(document, requirement_text):
    """Hook for the not-yet-built VPlan module. See module docstring."""
    if VPlan is not None and hasattr(VPlan, "filter_material"):
        return VPlan.filter_material(document, requirement_text), True

    # --- placeholder branch: VPlan.py hasn't been written yet ---
    candidate_sections = [
        s for s in document.get("sections", [])
        if Extractor.is_valid_vplan_section(s.get("id"))
    ][:5]

    if not candidate_sections:
        candidate_sections = document.get("sections", [])[:3]

    placeholder = {
        "document": document.get("document_name"),
        "vplan_related_material": [
            {"section": s.get("id", "?"), "content": (s.get("title") or "")[:80]}
            for s in candidate_sections
        ],
        "metadata": {"total_items": len(candidate_sections)},
    }
    return placeholder, False


def run_inconsistency_check(old_document, new_document):
    return Comparator.compare_documents(old_document, new_document)


def run_quality_check(json_path, pdf_path):
    args = types.SimpleNamespace(
        json=json_path,
        pdf=pdf_path,
        csv=None,
        gold_json=None,
        threshold=95.0,
    )
    return Quality_Check.build_report(args)


# ==========================================================
# SESSION STATE
# ==========================================================

if "excluded_files" not in st.session_state:
    st.session_state.excluded_files = set()
if "results" not in st.session_state:
    st.session_state.results = None
if "selected_page" not in st.session_state:
    st.session_state.selected_page = None


# ==========================================================
# SIDEBAR -- API KEY
# ==========================================================

with st.sidebar:
    st.subheader("Extractor settings")

    key_from_env = os.environ.get("OPENAI_API_KEY", "")
    key_is_placeholder = key_from_env.startswith("placeholder")

    if not key_is_placeholder:
        st.success("OpenAI API key loaded from .env")
    else:
        st.warning("No .env key found -- paste one below, or upload document.json files instead of PDFs.")

    api_key_input = st.text_input(
        "OpenAI API key (manual override)",
        type="password",
        value="",
        placeholder="sk-..." if key_is_placeholder else "using key from .env",
        help="Only needed if you don't want to use a .env file, or want to override it for this session. Needed for PDF extraction -- not needed if you upload already-extracted document.json files.",
    )
    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input
        Extractor.client = OpenAI(api_key=api_key_input)

    st.divider()
    st.caption(
        "V-Plan module status: "
        + ("connected (VPlan.py found)" if VPlan is not None else "not connected -- showing placeholder output")
    )


st.markdown(
    """<div class="masthead">
        <div>
            <div class="masthead-title">Specification Toolchain</div>
            <div class="masthead-sub">Extraction &nbsp;\u2192&nbsp; V-Plan Filtering &nbsp;\u2192&nbsp; Inconsistency Check &nbsp;\u2192&nbsp; Quality Check</div>
        </div>
        <div class="masthead-meta">Internal Tool</div>
    </div>""",
    unsafe_allow_html=True,
)

col_input, col_pipeline, col_results = st.columns([1.05, 1.05, 2.5], gap="large")


# ==========================================================
# COLUMN 1 -- INPUT
# ==========================================================

with col_input:
    with st.container(border=False):
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        panel_header("input", "Input")

        st.markdown('<div class="section-label">1. Select Files</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "Choose Files",
            type=["pdf", "json"],
            accept_multiple_files=True,
            label_visibility="collapsed",
            help="Upload the OLD spec first, then the NEW spec. PDFs will be extracted automatically; document.json files are used as-is.",
        )

        active_files = [f for f in (uploaded_files or []) if f.name not in st.session_state.excluded_files]

        st.markdown(
            f'<div class="section-label" style="margin-top:16px">Selected Files ({len(active_files)})</div>',
            unsafe_allow_html=True,
        )

        if not active_files:
            st.caption("No files selected yet.")
        else:
            for f in active_files:
                tag = "PDF" if f.name.lower().endswith(".pdf") else "JSON"
                row_col, btn_col = st.columns([5, 1])
                with row_col:
                    st.markdown(
                        f"""<div class="file-row">
                        <span class="fname"><span class="file-tag">{tag}</span>{f.name}</span>
                        <span class="file-size">{human_size(f.size)}</span>
                        </div>""",
                        unsafe_allow_html=True,
                    )
                with btn_col:
                    st.markdown('<div class="remove-btn-wrap">', unsafe_allow_html=True)
                    if st.button("Remove", key=f"remove_{f.name}", help="Remove file"):
                        st.session_state.excluded_files.add(f.name)
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:16px">2. User Requirement (Natural Language)</div>', unsafe_allow_html=True)
        requirement_text = st.text_area(
            "requirement",
            placeholder="Enter your requirements in natural language...",
            max_chars=2000,
            height=160,
            label_visibility="collapsed",
        )
        st.caption("Describe what information you want to extract, filter, or what inconsistencies you want to check.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="run-btn-wrap">', unsafe_allow_html=True)
        run_clicked = st.button("Run Pipeline", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if len(active_files) != 2 and run_clicked:
            st.error("Please select exactly two files -- an old spec and a new spec -- to run the full pipeline.")

        st.markdown('</div>', unsafe_allow_html=True)


# ==========================================================
# COLUMN 2 -- PIPELINE STEPS
# ==========================================================

done = st.session_state.results is not None

with col_pipeline:
    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    step_card(
        "extraction", "Extraction",
        "Extract content from the selected files and convert to structured JSON.",
        done,
    )
    step_card(
        "filter", "V-Plan Related Material Filter",
        "Filter and extract verification-plan related materials and output as JSON.",
        done,
    )
    step_card(
        "compare", "Inconsistency Check",
        "Compare documents and identify inconsistencies between versions.",
        done,
    )
    step_card(
        "shield", "Quality Checker",
        "Assess the quality and completeness of extracted data and highlight issues.",
        done,
    )


# ==========================================================
# PIPELINE EXECUTION
# ==========================================================

if run_clicked and len(active_files) == 2:
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            documents, json_paths, pdf_paths = [], [], []

            for label, f in zip(("old", "new"), active_files):
                dest = Path(tmp_dir) / f"{label}_{f.name}"
                dest.write_bytes(f.getvalue())

                if f.name.lower().endswith(".pdf"):
                    if os.environ.get("OPENAI_API_KEY", "").startswith("placeholder"):
                        st.error("Enter your OpenAI API key in the sidebar to extract PDFs, or upload document.json files instead.")
                        st.stop()
                    with st.spinner(f"Extracting {label} PDF (this calls the vision model per figure)..."):
                        document, json_path = run_extraction(str(dest), label)
                    pdf_path = str(dest)
                else:
                    with open(dest, "r", encoding="utf-8") as fh:
                        document = json.load(fh)
                    json_path = str(dest)
                    pdf_path = None

                documents.append(document)
                json_paths.append(json_path)
                pdf_paths.append(pdf_path)

            old_document, new_document = documents
            old_json_path, new_json_path = json_paths
            _, new_pdf_path = pdf_paths

            with st.spinner("Filtering V-Plan related material..."):
                vplan_result, vplan_connected = run_vplan_filter(new_document, requirement_text)

            with st.spinner("Checking for inconsistencies..."):
                changes = run_inconsistency_check(old_document, new_document)

            with st.spinner("Running quality checks..."):
                quality_report = run_quality_check(new_json_path, new_pdf_path)

            # persist artifacts to a stable location so widgets can re-read
            # them across reruns (the TemporaryDirectory above is cleaned up
            # once this block exits)
            persist_dir = Path(tempfile.mkdtemp(prefix="pipeline_results_"))
            old_extract_path = persist_dir / "extraction_old.json"
            new_extract_path = persist_dir / "extraction_new.json"
            vplan_path = persist_dir / "vplan_material.json"
            inconsistency_path = persist_dir / "inconsistencies.json"
            quality_path = persist_dir / "quality_report.json"

            old_extract_path.write_text(json.dumps(old_document, indent=2, ensure_ascii=False), encoding="utf-8")
            new_extract_path.write_text(json.dumps(new_document, indent=2, ensure_ascii=False), encoding="utf-8")
            vplan_path.write_text(json.dumps(vplan_result, indent=2, ensure_ascii=False), encoding="utf-8")
            inconsistency_path.write_text(json.dumps(changes, indent=2, ensure_ascii=False), encoding="utf-8")
            quality_path.write_text(json.dumps(quality_report, indent=2, ensure_ascii=False), encoding="utf-8")

            st.session_state.results = {
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "old_document": old_document,
                "new_document": new_document,
                "old_name": active_files[0].name,
                "new_name": active_files[1].name,
                "new_extract_path": str(new_extract_path),
                "new_extract_size": new_extract_path.stat().st_size,
                "vplan_result": vplan_result,
                "vplan_connected": vplan_connected,
                "vplan_path": str(vplan_path),
                "vplan_size": vplan_path.stat().st_size,
                "changes": changes,
                "inconsistency_path": str(inconsistency_path),
                "quality_report": quality_report,
                "quality_path": str(quality_path),
            }
            st.session_state.selected_page = None
            st.rerun()

    except Exception as exc:
        st.error(f"Pipeline failed: {exc}")


# ==========================================================
# COLUMN 3 -- RESULTS
# ==========================================================

with col_results:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    panel_header("results", "Results")

    results = st.session_state.results

    if results is None:
        st.info("Select an old and new spec on the left, then click **Run Pipeline** to see results here.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # ---------------- Extraction ----------------
        result_title_row("extraction", "Extraction Result", "/results/" + Path(results["new_extract_path"]).name)
        preview_col, meta_col = st.columns([2.4, 1.3])
        with preview_col:
            st.caption("Extracted JSON File Preview (new document)")
            st.code(json.dumps(results["new_document"], indent=2, ensure_ascii=False)[:1200] + "\n...", language="json")
        with meta_col:
            meta_box([
                ("File Name", Path(results["new_extract_path"]).name),
                ("File Size", human_size(results["new_extract_size"])),
                ("Total Pages", results["new_document"].get("total_pages", "?")),
                ("Generated At", results["generated_at"]),
            ])

        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

        # ---------------- V-Plan filter ----------------
        result_title_row("filter", "V-Plan Related Material Filter Result", "/results/" + Path(results["vplan_path"]).name)
        if not results["vplan_connected"]:
            st.markdown(
                "<div class='placeholder-banner'>VPlan.py hasn't been added to the project yet -- "
                "this is a placeholder preview built from tagged sections in the extracted JSON. "
                "Drop in a <code>VPlan.py</code> exposing <code>filter_material(document, requirement_text)</code> "
                "to replace this with real output.</div>",
                unsafe_allow_html=True,
            )
        preview_col2, meta_col2 = st.columns([2.4, 1.3])
        with preview_col2:
            st.caption("Filtered JSON File Preview")
            st.code(json.dumps(results["vplan_result"], indent=2, ensure_ascii=False)[:1200], language="json")
        with meta_col2:
            meta_box([
                ("File Name", Path(results["vplan_path"]).name),
                ("File Size", human_size(results["vplan_size"])),
                ("Total Items", results["vplan_result"].get("metadata", {}).get("total_items", "?")),
                ("Generated At", results["generated_at"]),
            ])

        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

        # ---------------- Inconsistency check ----------------
        result_title_row("compare", "Inconsistency Check Result", "/results/" + Path(results["inconsistency_path"]).name)

        changes = results["changes"]
        # page identifiers can come through as either int or str depending on
        # which part of Comparator produced the change -- normalise to str so
        # "1" and 1 don't become two distinct (but identically-labelled) entries
        pages_with_changes = sorted(
            {str(c["page"]) for c in changes if c.get("page") not in (None, "")},
            key=lambda v: (int(v) if v.isdigit() else float("inf"), v),
        )

        if not changes:
            st.success("No differences were found between the old and new document.")
        elif not pages_with_changes:
            st.info(f"{len(changes)} change(s) found, but none are tied to a specific page (see metadata/section-level changes below).")
            with st.expander("View non-page-specific changes"):
                st.json(changes[:50])
        else:
            list_col, diff_col, legend_col = st.columns([1, 2.6, 1])

            with list_col:
                st.markdown("<div class='section-label'>Pages with Inconsistencies</div>", unsafe_allow_html=True)
                if st.session_state.selected_page not in pages_with_changes:
                    st.session_state.selected_page = pages_with_changes[0]
                for p in pages_with_changes:
                    is_active = p == st.session_state.selected_page
                    active_cls = "is-active" if is_active else ""
                    st.markdown(f'<div class="page-btn-wrap {active_cls}">', unsafe_allow_html=True)
                    if st.button(f"Page {p}", key=f"page_btn_{p}", use_container_width=True):
                        st.session_state.selected_page = p
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)

            selected_page = st.session_state.selected_page

            old_pages = {p.get("page_number"): p.get("text", "") for p in results["old_document"].get("pages", [])}
            new_pages = {p.get("page_number"): p.get("text", "") for p in results["new_document"].get("pages", [])}

            with diff_col:
                st.markdown(f"<div class='section-label'>Differences for Page {selected_page}</div>", unsafe_allow_html=True)
                try:
                    page_num = int(selected_page)
                except (TypeError, ValueError):
                    page_num = None

                old_text = old_pages.get(page_num, "")
                new_text = new_pages.get(page_num, "")
                old_html, new_html = render_word_diff(old_text, new_text)

                sub_old, sub_new = st.columns(2)
                with sub_old:
                    st.markdown(f"<div class='diff-pane-header'>Original ({results['old_name']})</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='diff-pane'>{old_html or '<i>No text on this page.</i>'}</div>", unsafe_allow_html=True)
                with sub_new:
                    st.markdown(f"<div class='diff-pane-header'>New Version ({results['new_name']})</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='diff-pane'>{new_html or '<i>No text on this page.</i>'}</div>", unsafe_allow_html=True)

            with legend_col:
                st.markdown(
                    """<div class="legend-box">
                    <div class="legend-title">Legend</div>
                    <div class="legend-row"><span class="legend-swatch" style="background:#fbe9e9"></span>Removed</div>
                    <div class="legend-row"><span class="legend-swatch" style="background:#eaf3ea"></span>Added</div>
                    <div class="legend-row"><span class="legend-swatch" style="background:#f3f0e2"></span>Modified</div>
                    </div>""",
                    unsafe_allow_html=True,
                )

            with st.expander(f"All {len(changes)} tracked changes"):
                st.dataframe(changes, use_container_width=True)

        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

        # ---------------- Quality checker ----------------
        result_title_row("shield", "Quality Checker Result", "/results/" + Path(results["quality_path"]).name)

        report = results["quality_report"]
        scores = report["scores"]

        gauge_col, stats_col, issues_col = st.columns([1, 2, 1.4])

        with gauge_col:
            st.markdown("<div class='section-label' style='text-align:center'>Quality Overview</div>", unsafe_allow_html=True)
            gauge(report["overall_percentage"], "100")

        with stats_col:
            st.markdown("<br>", unsafe_allow_html=True)
            b1, b2, b3 = st.columns(3)
            score_defs = [
                ("Completeness", scores.get("completeness", {}).get("percentage", 0)),
                ("Accuracy (vs. source)", scores.get("accuracy", {}).get("percentage", 0)),
                ("Table & Figure Capture", scores.get("table_figure_capture", {}).get("percentage", 0)),
            ]
            for box, (label, pct) in zip((b1, b2, b3), score_defs):
                with box:
                    stat_bar(label, pct)

        with issues_col:
            st.markdown("<div class='section-label'>Top Issues</div>", unsafe_allow_html=True)
            issues = []
            for score_name, score_data in scores.items():
                for detail_name, detail_value in score_data.get("details", {}).items():
                    if detail_value < report["inputs"]["threshold"]:
                        friendly = detail_name.replace("_score", "").replace("_", " ").title()
                        severity = "#9a3131" if detail_value < 60 else MUTED
                        issues.append((severity, friendly, detail_value))
            issues.sort(key=lambda x: x[2])
            if not issues:
                st.markdown(f"<div class='issue-row'><span class='issue-dot' style='background:{MUTED}'></span>No issues above the threshold.</div>", unsafe_allow_html=True)
            else:
                for severity, friendly, value in issues[:6]:
                    st.markdown(
                        f"<div class='issue-row'><span class='issue-dot' style='background:{severity}'></span>"
                        f"<span>{friendly} <span class='issue-value'>({value:.0f}%)</span></span></div>",
                        unsafe_allow_html=True,
                    )
            with st.expander("View Full Report"):
                st.json(report)

        st.markdown('</div>', unsafe_allow_html=True)
