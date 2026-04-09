"""State contract for LangGraph execution."""

from typing import Any, TypedDict


class GraphState(TypedDict, total=False):
    """Versioned state object carried through agent nodes."""

    state_version: int
    query: str
    retrieved_chunks: list[dict[str, Any]]
    analyst_output: str
    risk_output: str
    synthesized_output: str
    metrics: dict[str, float]
