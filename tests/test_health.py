"""Smoke tests for backend health endpoint."""

from fastapi.testclient import TestClient

from neurorag.backend.main import create_app


def test_health_endpoint_returns_ready_payload() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "NeuroRAG"
