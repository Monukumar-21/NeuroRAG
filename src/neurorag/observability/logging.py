"""Structured logging helpers for API and orchestration flows."""

import logging
import sys

import structlog


def configure_logging(log_level: str = "INFO") -> None:
    """Configure standard and structured logging once at process startup."""

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(message)s",
        stream=sys.stdout,
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str):
    """Return a namespaced structured logger."""

    return structlog.get_logger(name)
