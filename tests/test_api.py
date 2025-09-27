"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from src.office_sign.api import create_app
from src.office_sign.hardware.mock import MockLightPanel


def test_health_check() -> None:
  client = TestClient(create_app(MockLightPanel()))
  response = client.get("/health")
  assert response.status_code == 200
  assert response.json() == {"status": "ok"}


def test_all_statuses() -> None:
  panel = MockLightPanel()
  client = TestClient(create_app(panel))

  status_client = client.post("/status/free")
  assert status_client .status_code == 200
  assert status_client .json() == {"status": "FREE"}
  assert panel.status.name is "FREE"
  assert panel.status.color is (0, 255, 0)

  status_client = client.post("/status/working")
  assert status_client .status_code == 200
  assert status_client .json() == {"status": "WORKING"}
  assert panel.status.name is "WORKING"
  assert panel.status.color is (255, 255, 0)

  status_client = client.post("/status/on_call")
  assert status_client .status_code == 200
  assert status_client .json() == {"status": "ON_CALL"}
  assert panel.status.name is "ON_CALL"
  assert panel.status.color is (255, 0, 0)

  status_client = client.post("/status/off")
  assert status_client .status_code == 200
  assert status_client .json() == {"status": "OFF"}
  assert panel.status.name is "OFF"
  assert panel.status.color is (0, 0, 0)

  status_client = client.post("/status/invalid")
  assert status_client .status_code == 404

