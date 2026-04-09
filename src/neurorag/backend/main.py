"""FastAPI application entrypoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from neurorag.backend.routes.health import router as health_router
from neurorag.config import get_settings
from neurorag.observability.logging import configure_logging, get_logger

settings = get_settings()
configure_logging(settings.log_level)
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run startup and shutdown hooks with validated configuration."""

    runtime_settings = get_settings()
    runtime_settings.validate_for_startup()
    logger.info(
        "api.startup",
        environment=runtime_settings.environment,
        version=runtime_settings.app_version,
    )

    yield

    logger.info("api.shutdown")


def create_app() -> FastAPI:
    """Build and configure the FastAPI application instance."""

    runtime_settings = get_settings()
    app = FastAPI(
        title=runtime_settings.app_name,
        version=runtime_settings.app_version,
        description=(
            "NeuroRAG backend for document ingestion, multi-agent reasoning, "
            "and retrieval workflows."
        ),
        lifespan=lifespan,
    )
    app.include_router(health_router)
    return app


app = create_app()
