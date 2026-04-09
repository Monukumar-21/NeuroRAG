"""Database session helpers for Neon PostgreSQL."""

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from neurorag.config import get_settings


def create_engine_from_settings() -> Engine:
    """Create SQLAlchemy engine from validated runtime settings."""

    settings = get_settings()
    if not settings.neon_database_url:
        raise RuntimeError(
            "NEON_DATABASE_URL is not configured. Set it in .env before enabling database features."
        )

    return create_engine(
        settings.neon_database_url,
        pool_pre_ping=True,
        pool_recycle=1800,
    )


def check_database_connection(engine: Engine | None = None) -> None:
    """Verify database reachability with a lightweight query."""

    owns_engine = engine is None
    active_engine = engine or create_engine_from_settings()

    try:
        with active_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise RuntimeError(
            "Database connectivity check failed. Verify NEON_DATABASE_URL and network access."
        ) from exc
    finally:
        if owns_engine:
            active_engine.dispose()


def create_session_factory() -> sessionmaker:
    """Build a session factory for request-scoped DB sessions."""

    engine = create_engine_from_settings()
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
