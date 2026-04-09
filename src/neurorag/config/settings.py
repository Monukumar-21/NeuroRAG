"""Application settings loaded from environment variables."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed settings with validation for startup safety."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        populate_by_name=True,
        extra="ignore",
    )

    app_name: str = Field(default="NeuroRAG", alias="APP_NAME")
    app_version: str = Field(default="0.1.0", alias="APP_VERSION")
    environment: Literal["development", "staging", "production", "test"] = Field(
        default="development",
        alias="ENVIRONMENT",
    )
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    streamlit_port: int = Field(default=8501, alias="STREAMLIT_PORT")

    ollama_base_url: str = Field(default="http://localhost:11434", alias="OLLAMA_BASE_URL")
    ollama_chat_model: str = Field(default="llama3", alias="OLLAMA_CHAT_MODEL")
    ollama_embed_model: str = Field(default="nomic-embed-text", alias="OLLAMA_EMBED_MODEL")

    neon_database_url: str | None = Field(default=None, alias="NEON_DATABASE_URL")
    require_database: bool = Field(default=False, alias="REQUIRE_DATABASE")

    enable_hitl: bool = Field(default=False, alias="ENABLE_HITL")
    request_timeout_seconds: int = Field(default=60, alias="REQUEST_TIMEOUT_SECONDS")

    def validate_for_startup(self, require_database: bool | None = None) -> None:
        """Fail fast with actionable messages when required settings are missing."""

        db_required = self.require_database if require_database is None else require_database
        errors: list[str] = []

        required_non_empty = {
            "OLLAMA_BASE_URL": self.ollama_base_url,
            "OLLAMA_CHAT_MODEL": self.ollama_chat_model,
            "OLLAMA_EMBED_MODEL": self.ollama_embed_model,
        }

        for key, value in required_non_empty.items():
            if not value or not value.strip():
                errors.append(f"{key} must be set and non-empty.")

        if db_required and not self.neon_database_url:
            errors.append("NEON_DATABASE_URL is required when REQUIRE_DATABASE=true.")

        if errors:
            joined_errors = " ".join(errors)
            raise ValueError(f"Invalid configuration: {joined_errors}")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings instance to avoid repeated environment parsing."""

    return Settings()
