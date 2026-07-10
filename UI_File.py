import os
import tempfile
from pathlib import Path

import streamlit as st
from openai import OpenAI

from Comparator import run_design_tool

# Extractor.py builds its OpenAI client at IMPORT time
# (client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])), so importing it
# with no key set would crash the app before the sidebar can even render.
# Seed a placeholder so import succeeds; the sidebar below swaps in the
# real client once the user enters a key.
os.environ.setdefault("OPENAI_API_KEY", "placeholder-set-key-in-sidebar")
import Extractor

st.set_page_config(page_title="Specification Version Comparator", layout="wide")
st.title("Specification Version Comparator")

st.header("Input")

input_mode = st.radio(
    "What are you uploading?",
    ["PDF specs (run extractor first)", "Already-extracted document.json files"],
    horizontal=True,
)
is_pdf_mode = input_mode.startswith("PDF")
file_type = ["pdf"] if is_pdf_mode else ["json"]

old_file = st.file_uploader(f"Old {'PDF' if is_pdf_mode else 'document.json'}", type=file_type)
new_file = st.file_uploader(f"New {'PDF' if is_pdf_mode else 'document.json'}", type=file_type)

uploaded_files = st.file_uploader(
    "Select Files",
    type=["py", "cpp", "h", "hpp", "txt"],
    accept_multiple_files=True
)

if is_pdf_mode:
    with st.sidebar:
        st.subheader("Extractor settings")
        api_key_input = st.text_input(
            "OpenAI API key",
            type="password",
            value=os.environ.get("OPENAI_API_KEY", ""),
            help="Only needed for PDF mode — the extractor calls the OpenAI vision API for each figure/image.",
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

generate = st.button("Generate")

st.header("Output")


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


if generate:
    if not old_file:
        st.error(f"Please upload the old {'PDF' if is_pdf_mode else 'document.json'} file.")
    elif not new_file:
        st.error(f"Please upload the new {'PDF' if is_pdf_mode else 'document.json'} file.")
    elif is_pdf_mode and os.environ.get("OPENAI_API_KEY", "").startswith("placeholder"):
        st.error("Enter your OpenAI API key in the sidebar to run PDF extraction.")
    else:
        try:
            with tempfile.TemporaryDirectory() as tmp_dir:
                if is_pdf_mode:
                    with st.spinner("Extracting old PDF (this calls the vision model per figure)..."):
                        old_json_path = run_extractor_on_pdf(old_file, "old")
                    with st.spinner("Extracting new PDF (this calls the vision model per figure)..."):
                        new_json_path = run_extractor_on_pdf(new_file, "new")
                else:
                    old_json_path = Path(tmp_dir) / "old_document.json"
                    new_json_path = Path(tmp_dir) / "new_document.json"
                    Path(old_json_path).write_bytes(old_file.getvalue())
                    Path(new_json_path).write_bytes(new_file.getvalue())

                with st.spinner("Comparing documents..."):
                    result_log, result_md_path = run_design_tool(
                        str(old_json_path),
                        str(new_json_path),
                    )

                # run_design_tool writes into comparison_output/ on disk,
                # which persists after tmp_dir is cleaned up.
                csv_path = Path("comparison_output/version_differences.csv")
                json_path = Path("comparison_output/version_differences.json")
                md_path = Path(result_md_path)

                csv_bytes = csv_path.read_bytes() if csv_path.exists() else None
                json_bytes = json_path.read_bytes() if json_path.exists() else None
                md_text = md_path.read_text(encoding="utf-8") if md_path.exists() else None

        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()

        st.subheader("Results Log")
        st.text_area("Log", value=result_log, height=300)

        st.subheader("Download Reports")
        col1, col2, col3 = st.columns(3)

        with col1:
            if csv_bytes:
                st.download_button(
                    label="Download CSV",
                    data=csv_bytes,
                    file_name=csv_path.name,
                    mime="text/csv",
                )

        with col2:
            if json_bytes:
                st.download_button(
                    label="Download JSON",
                    data=json_bytes,
                    file_name=json_path.name,
                    mime="application/json",
                )

        with col3:
            if md_text:
                st.download_button(
                    label="Download Markdown",
                    data=md_text,
                    file_name=md_path.name,
                    mime="text/markdown",
                )

        if md_text:
            st.subheader("Markdown Report Preview")
            st.markdown(md_text)