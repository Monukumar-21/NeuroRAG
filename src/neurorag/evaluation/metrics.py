"""Simple evaluation metrics used by early RAG validation."""

from collections.abc import Iterable


def relevance_at_k(relevant_ids: set[str], retrieved_ids: Iterable[str], k: int) -> float:
    """Compute relevance@k as overlap ratio within the top-k retrieved IDs."""

    if k <= 0:
        return 0.0

    top_k = list(retrieved_ids)[:k]
    if not top_k:
        return 0.0

    hits = sum(1 for item_id in top_k if item_id in relevant_ids)
    return hits / k


def latency_ms(start_seconds: float, end_seconds: float) -> float:
    """Convert wall-clock timestamps to milliseconds."""

    return max((end_seconds - start_seconds) * 1000.0, 0.0)
