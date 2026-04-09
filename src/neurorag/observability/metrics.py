"""Latency and performance instrumentation helpers."""

from contextlib import contextmanager
from time import perf_counter
from typing import Iterator

from neurorag.observability.logging import get_logger

logger = get_logger(__name__)


@contextmanager
def timed_block(metric_name: str) -> Iterator[None]:
    """Log elapsed time for a named execution block."""

    start = perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (perf_counter() - start) * 1000.0
        logger.info("metric.timing", metric=metric_name, elapsed_ms=round(elapsed_ms, 2))
