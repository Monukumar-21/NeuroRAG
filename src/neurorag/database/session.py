"""Database session helpers for Neon PostgreSQL."""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from neurorag.config import get_settings


def create_engine_from_settings() -> Engine:
    """Create SQLAlchemy engine from validated runtime settings."""

    settings = get_settings()
    if not settings.neon_database_url:
        raise RuntimeError(
            "NEON_DATABASE_URL is not configured. Set it in .env before enabling database features."
        )

    return create_engine(settings.neon_database_url, pool_pre_ping=True)


def create_session_factory() -> sessionmaker:
    """Build a session factory for request-scoped DB sessions."""

    engine = create_engine_from_settings()
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)
