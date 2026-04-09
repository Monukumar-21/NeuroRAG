"""Docling-based document parsing placeholders."""


class DoclingIngestionPipeline:
    """Parses and chunks documents before embedding."""

    def parse_and_chunk(self, file_path: str) -> list[dict[str, str]]:
        raise NotImplementedError(
            "Docling parsing and structure-aware chunking are implemented in Phase 3."
        )
