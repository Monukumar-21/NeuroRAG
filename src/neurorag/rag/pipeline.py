"""Retrieval pipeline interfaces and placeholders."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class RetrievalResult:
    """Single retrieved chunk with ranking metadata."""

    chunk_id: str
    score: float
    content: str
    metadata: dict[str, Any]


class RAGPipeline:
    """Vector retrieval orchestrator implemented in Phase 4."""

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        raise NotImplementedError("RAGPipeline.retrieve is implemented in Phase 4.")
