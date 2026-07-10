import difflib
import json
import os
import tempfile
from pathlib import Path

import streamlit as st
from openai import OpenAI

from Comparator import run_design_tool

# Extractor.py builds its OpenAI client at IMPORT time
# (client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])), so importing it
# with no key set would crash the app before the sidebar can even render.
# Seed a placeholder so import succeeds; the PDF tab's sidebar swaps in the
# real client once the user enters a key.
os.environ.setdefault("OPENAI_API_KEY", "placeholder-set-key-in-sidebar")
import Extractor

st.set_page_config(page_title="Specification Version Comparator", layout="wide")
st.title("Specification Version Comparator")

pdf_tab, json_tab = st.tabs(["PDF Specs (Extract First)", "Already-Extracted JSON Files"])


# ==========================================================
# SHARED HELPERS
# ==========================================================

def run_extractor_on_pdf(pdf_file, label):
    """Save an uploaded PDF to disk, then run Extractor.parse_pdf on it.

    Extractor.py itself doesn't take an output_dir argument -- it writes to
    module-level globals (OUTPUT_DIR, IMAGE_FOLDER, TABLE_FOLDER,
    FIGURE_FOLDER) that are hardcoded in the file. Since we can't edit that
    file, we monkeypatch those globals on the already-imported module before
    calling parse_pdf(), so each run (old/new) gets its own folder instead of
    both overwriting "amba_a2_OUTPUT". The functions inside Extractor.py look
    these names up as module globals at call time, so this redirect works
    without touching the source file.
    """
    tmp_dir = tempfile.mkdtemp(prefix=f"extract_{label}_")
    pdf_path = Path(tmp_dir) / pdf_file.name
    pdf_path.write_bytes(pdf_file.getvalue())

    output_dir = os.path.join(tmp_dir, "extract_output")
    image_dir = os.path.join(output_dir, "images")
    table_dir = os.path.join(output_dir, "tables")
    figure_dir = os.path.join(output_dir, "figures")

    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(table_dir, exist_ok=True)
    os.makedirs(figure_dir, exist_ok=True)

    Extractor.OUTPUT_DIR = output_dir
    Extractor.IMAGE_FOLDER = image_dir
    Extractor.TABLE_FOLDER = table_dir
    Extractor.FIGURE_FOLDER = figure_dir

    Extractor.parse_pdf(str(pdf_path))

    return os.path.join(output_dir, "document.json")


def load_json_upload(uploaded_file):
    """Parse an uploaded document.json file into a Python dict."""
    return json.loads(uploaded_file.getvalue().decode("utf-8"))


def page_text_lookup(document):
    """Map page_number -> raw page text for a parsed document.json."""
    return {
        page.get("page_number"): page.get("text", "")
        for page in document.get("pages", [])
    }


def render_word_diff(old_text, new_text):
    """Build side-by-side HTML with word-level diff highlighting.

    Removed words are struck through in red on the old side; added words
    are highlighted green on the new side; unchanged words are shown plain
    on both sides.
    """
    old_words = old_text.split()
    new_words = new_text.split()
    matcher = difflib.SequenceMatcher(None, old_words, new_words)

    old_parts, new_parts = [], []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        old_chunk = " ".join(old_words[i1:i2])
        new_chunk = " ".join(new_words[j1:j2])

        if tag == "equal":
            old_parts.append(old_chunk)
            new_parts.append(new_chunk)
        elif tag == "delete":
            old_parts.append(
                f'<span style="background-color:#ffd6d6;text-decoration:line-through">{old_chunk}</span>'
            )
        elif tag == "insert":
            new_parts.append(
                f'<span style="background-color:#d6ffd6">{new_chunk}</span>'
            )
        elif tag == "replace":
            old_parts.append(
                f'<span style="background-color:#ffd6d6;text-decoration:line-through">{old_chunk}</span>'
            )
            new_parts.append(
                f'<span style="background-color:#d6ffd6">{new_chunk}</span>'
            )

    return " ".join(old_parts), " ".join(new_parts)


def render_full_comparison_output(result_log, md_path):
    """Shared output block: log, downloads, markdown preview."""
    csv_path = Path("comparison_output/version_differences.csv")
    json_path = Path("comparison_output/version_differences.json")
    md_path = Path(md_path)

    st.subheader("Results Log")
    st.text_area("Log", value=result_log, height=300)

    st.subheader("Download Reports")
    col1, col2, col3 = st.columns(3)

    with col1:
        if csv_path.exists():
            st.download_button(
                "Download CSV", csv_path.read_bytes(), csv_path.name, "text/csv"
            )
    with col2:
        if json_path.exists():
            st.download_button(
                "Download JSON", json_path.read_bytes(), json_path.name, "application/json"
            )
    with col3:
        if md_path.exists():
            st.download_button(
                "Download Markdown", md_path.read_text(encoding="utf-8"), md_path.name, "text/markdown"
            )

    if md_path.exists():
        st.subheader("Markdown Report Preview")
        st.markdown(md_path.read_text(encoding="utf-8"))


# ==========================================================
# TAB 1: PDF SPECS -> EXTRACT -> COMPARE
# ==========================================================

with pdf_tab:
    st.header("Extract & Compare PDFs")

    old_pdf = st.file_uploader("Old PDF", type=["pdf"], key="old_pdf")
    new_pdf = st.file_uploader("New PDF", type=["pdf"], key="new_pdf")

    with st.sidebar:
        st.subheader("Extractor settings")
        api_key_input = st.text_input(
            "OpenAI API key",
            type="password",
            value=os.environ.get("OPENAI_API_KEY", ""),
            help="Needed for PDF extraction -- the extractor calls the OpenAI vision API for each figure/image.",
        )
        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            # Extractor.client was already built at import time with
            # whatever key was present then, so setting os.environ alone
            # does nothing for calls the module makes internally -- rebuild
            # the client object it actually uses.
            Extractor.client = OpenAI(api_key=api_key_input)

    st.caption(
        "PDFs are run through the extractor first to produce a document.json "
        "for each, then compared. This calls the OpenAI vision API for every "
        "figure/image, so it can take a while on large specs."
    )

    extract_and_compare = st.button("Extract & Compare", key="pdf_generate")

    if extract_and_compare:
        if not old_pdf:
            st.error("Please upload the old PDF.")
        elif not new_pdf:
            st.error("Please upload the new PDF.")
        elif os.environ.get("OPENAI_API_KEY", "").startswith("placeholder"):
            st.error("Enter your OpenAI API key in the sidebar to run PDF extraction.")
        else:
            try:
                with st.spinner("Extracting old PDF (this calls the vision model per figure)..."):
                    old_json_path = run_extractor_on_pdf(old_pdf, "old")
                with st.spinner("Extracting new PDF (this calls the vision model per figure)..."):
                    new_json_path = run_extractor_on_pdf(new_pdf, "new")

                with st.spinner("Comparing documents..."):
                    result_log, result_md_path = run_design_tool(old_json_path, new_json_path)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
            else:
                render_full_comparison_output(result_log, result_md_path)


# ==========================================================
# TAB 2: ALREADY-EXTRACTED JSON -> COMPARE + PAGE DIFF VIEWER
# ==========================================================

with json_tab:
    st.header("Compare Extracted document.json Files")

    old_json_file = st.file_uploader("Old document.json", type=["json"], key="old_json")
    new_json_file = st.file_uploader("New document.json", type=["json"], key="new_json")

    uploaded_files = st.file_uploader(
        "Select Files",
        type=["py", "cpp", "h", "hpp", "txt"],
        accept_multiple_files=True,
        key="json_extra_files",
    )

    st.subheader("Full Document Comparison")
    run_full_compare = st.button("Generate Full Comparison Report", key="json_generate")

    if run_full_compare:
        if not old_json_file or not new_json_file:
            st.error("Please upload both the old and new document.json files.")
        else:
            try:
                with tempfile.TemporaryDirectory() as tmp_dir:
                    old_path = Path(tmp_dir) / "old_document.json"
                    new_path = Path(tmp_dir) / "new_document.json"
                    old_path.write_bytes(old_json_file.getvalue())
                    new_path.write_bytes(new_json_file.getvalue())

                    with st.spinner("Comparing documents..."):
                        result_log, result_md_path = run_design_tool(str(old_path), str(new_path))
            except Exception as e:
                st.error(f"Something went wrong: {e}")
            else:
                render_full_comparison_output(result_log, result_md_path)

    st.divider()
    st.subheader("Page-by-Page Diff Viewer")
    st.caption(
        "Pick a page number to see word-level differences between the old "
        "and new spec on that page. Removed words are struck through in "
        "red; added words are highlighted in green."
    )

    if not old_json_file or not new_json_file:
        st.info("Upload both document.json files above to enable the page diff viewer.")
    else:
        try:
            old_document = load_json_upload(old_json_file)
            new_document = load_json_upload(new_json_file)
        except Exception as e:
            st.error(f"Couldn't parse one of the JSON files: {e}")
        else:
            old_pages = page_text_lookup(old_document)
            new_pages = page_text_lookup(new_document)
            all_page_numbers = sorted(
                {p for p in old_pages if p is not None}
                | {p for p in new_pages if p is not None}
            )

            if not all_page_numbers:
                st.info("No pages found in the uploaded JSON files.")
            else:
                selected_page = st.selectbox("Page number", all_page_numbers, key="diff_page_select")
                show_page_diff = st.button("Show Page Differences", key="show_page_diff")

                if show_page_diff:
                    if selected_page not in old_pages:
                        st.warning(f"Page {selected_page} doesn't exist in the old document (it was added in the new version).")
                    elif selected_page not in new_pages:
                        st.warning(f"Page {selected_page} doesn't exist in the new document (it was removed in the new version).")

                    old_text = old_pages.get(selected_page, "")
                    new_text = new_pages.get(selected_page, "")

                    if old_text.strip() == new_text.strip():
                        st.success(f"Page {selected_page} is identical between the two documents.")
                    else:
                        old_html, new_html = render_word_diff(old_text, new_text)

                        diff_col1, diff_col2 = st.columns(2)
                        with diff_col1:
                            st.markdown(f"**Old — Page {selected_page}**")
                            st.markdown(
                                f'<div style="border:1px solid #ddd;padding:10px;'
                                f'border-radius:6px;line-height:1.6">{old_html}</div>',
                                unsafe_allow_html=True,
                            )
                        with diff_col2:
                            st.markdown(f"**New — Page {selected_page}**")
                            st.markdown(
                                f'<div style="border:1px solid #ddd;padding:10px;'
                                f'border-radius:6px;line-height:1.6">{new_html}</div>',
                                unsafe_allow_html=True,
                            )