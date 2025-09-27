"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from office_sign.api import create_app
from office_sign.hardware.mock import MockLightPanel


def test_health_check() -> None:
    client = TestClient(create_app(MockLightPanel()))
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_all_statuses() -> None:
    panel = MockLightPanel()
    client = TestClient(create_app(panel))

    status_client = client.get("/status/free")
    assert status_client.status_code == 200
    assert status_client.json() == {"status": "FREE"}
    assert panel.status.name == "FREE"
    assert panel.status.color == (0, 255, 0)

    status_client = client.get("/status/working")
    assert status_client.status_code == 200
    assert status_client.json() == {"status": "WORKING"}
    assert panel.status.name == "WORKING"
    assert panel.status.color == (255, 255, 0)

    status_client = client.get("/status/on_call")
    assert status_client.status_code == 200
    assert status_client.json() == {"status": "ON_CALL"}
    assert panel.status.name == "ON_CALL"
    assert panel.status.color == (255, 0, 0)

    status_client = client.get("/status/off")
    assert status_client.status_code == 200
    assert status_client.json() == {"status": "OFF"}
    assert panel.status.name == "OFF"
    assert panel.status.color == (0, 0, 0)

    status_client = client.get("/status/invalid")
    assert status_client.status_code == 404
