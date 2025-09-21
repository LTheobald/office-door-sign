"""FastAPI application factory for the office door light service."""

from __future__ import annotations

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from .hardware.base import LightPanel
from .hardware.mock import MockLightPanel
from .service import LightService


class LightStatus(BaseModel):
  power_on: bool


def create_app(panel: LightPanel | None = None) -> FastAPI:
  """Create a FastAPI application configured with the provided panel."""

  light_panel = panel or MockLightPanel()
  service = LightService(light_panel)
  app = FastAPI(title="Office Door Sign", version="0.1.0")

  def get_service() -> LightService:
    return service

  @app.get("/health")
  def health() -> dict[str, str]:
    return {"status": "ok"}

  @app.get("/light/status", response_model=LightStatus)
  def read_status(light_service: LightService = Depends(get_service)) -> LightStatus:
    return LightStatus(power_on=light_service.status())

  @app.post("/light/on", response_model=LightStatus)
  def turn_on(light_service: LightService = Depends(get_service)) -> LightStatus:
    light_service.turn_on()
    return LightStatus(power_on=True)

  @app.post("/light/off", response_model=LightStatus)
  def turn_off(light_service: LightService = Depends(get_service)) -> LightStatus:
    light_service.turn_off()
    return LightStatus(power_on=False)

  return app
