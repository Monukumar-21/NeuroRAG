"""Runtime startup checks for database readiness behavior."""

from fastapi.testclient import TestClient

from neurorag.config.settings import get_settings


def test_startup_runs_database_check_when_required(monkeypatch) -> None:
    monkeypatch.setenv(
        "NEON_DATABASE_URL",
        "postgresql+psycopg://user:pass@localhost/testdb?sslmode=disable",
    )
    monkeypatch.setenv("REQUIRE_DATABASE", "true")
    get_settings.cache_clear()

    calls = {"count": 0}

    def fake_check_database_connection() -> None:
        calls["count"] += 1

    monkeypatch.setattr("neurorag.backend.main.check_database_connection", fake_check_database_connection)

    from neurorag.backend.main import create_app

    with TestClient(create_app()) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert calls["count"] == 1

    get_settings.cache_clear()


def test_startup_skips_database_check_when_not_required(monkeypatch) -> None:
    monkeypatch.delenv("NEON_DATABASE_URL", raising=False)
    monkeypatch.setenv("REQUIRE_DATABASE", "false")
    get_settings.cache_clear()

    calls = {"count": 0}

    def fake_check_database_connection() -> None:
        calls["count"] += 1

    monkeypatch.setattr("neurorag.backend.main.check_database_connection", fake_check_database_connection)

    from neurorag.backend.main import create_app

    with TestClient(create_app()) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert calls["count"] == 0

    get_settings.cache_clear()
