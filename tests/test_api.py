"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from office_sign.api import create_app
from office_sign.hardware.mock import MockLightPanel


def test_health_check() -> None:
  client = TestClient(create_app(MockLightPanel()))
  response = client.get("/health")
  assert response.status_code == 200
  assert response.json() == {"status": "ok"}


def test_turn_light_on_and_off() -> None:
  panel = MockLightPanel()
  client = TestClient(create_app(panel))

  turn_on = client.post("/light/on")
  assert turn_on.status_code == 200
  assert turn_on.json() == {"power_on": True}
  assert panel.power_on is True

  turn_off = client.post("/light/off")
  assert turn_off.status_code == 200
  assert turn_off.json() == {"power_on": False}
  assert panel.power_on is False

  status = client.get("/light/status")
  assert status.status_code == 200
  assert status.json() == {"power_on": False}
