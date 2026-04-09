"""Pydantic schemas shared across backend and frontend surfaces."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Standard health payload for service readiness checks."""

    status: str
    service: str
    version: str
    environment: str
