"""Streamlit UI entrypoint for NeuroRAG."""

import streamlit as st

from neurorag.config import get_settings


def main() -> None:
    """Render a minimal but production-oriented operator UI shell."""

    settings = get_settings()

    st.set_page_config(
        page_title="NeuroRAG",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("NeuroRAG Control Panel")
    st.caption("Phase 1 scaffold: ingestion and multi-agent views are placeholders.")

    with st.sidebar:
        st.subheader("Runtime")
        st.write(f"Environment: {settings.environment}")
        st.write(f"Backend: http://{settings.api_host}:{settings.api_port}")
        st.write(f"Ollama: {settings.ollama_base_url}")
        st.write(f"Chat model: {settings.ollama_chat_model}")
        st.write(f"Embed model: {settings.ollama_embed_model}")

    ingestion_tab, query_tab, output_tab = st.tabs([
        "Document Ingestion",
        "Query",
        "Agent Outputs",
    ])

    with ingestion_tab:
        st.subheader("Upload Documents")
        st.file_uploader(
            "Upload PDF, DOCX, or TXT",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True,
            disabled=True,
            help="Enabled in Phase 7 when /upload is implemented.",
        )
        st.info("Upload pipeline will connect to Docling ingestion service.")

    with query_tab:
        st.subheader("Ask a Question")
        st.text_area(
            "Query",
            placeholder="Example: What are the top compliance risks mentioned in the policy set?",
            height=140,
            disabled=True,
            help="Enabled in Phase 7 when /query is implemented.",
        )
        st.button("Run Multi-Agent Pipeline", disabled=True)

    with output_tab:
        st.subheader("Retrieved Chunks")
        st.code("No retrieval output yet.")
        st.subheader("Agent Outputs")
        st.code("Retriever: pending\nAnalyst: pending\nRisk: pending\nSynthesizer: pending")
        st.subheader("Final Answer")
        st.success("Final answer will appear here once orchestration is live.")


if __name__ == "__main__":
    main()
