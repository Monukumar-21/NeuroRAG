"""Health and readiness routes."""

from fastapi import APIRouter

from neurorag.common.schemas import HealthResponse
from neurorag.config import get_settings

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Return process health metadata for monitoring and smoke checks."""

    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )
