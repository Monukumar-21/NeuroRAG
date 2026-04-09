"""Smoke tests for startup configuration validation."""

import pytest

from neurorag.config.settings import Settings


def test_startup_validation_accepts_defaults() -> None:
    settings = Settings()

    settings.validate_for_startup()


def test_startup_validation_requires_database_when_enabled() -> None:
    settings = Settings(require_database=True, neon_database_url=None)

    with pytest.raises(ValueError, match="NEON_DATABASE_URL"):
        settings.validate_for_startup()
