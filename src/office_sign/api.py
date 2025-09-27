"""FastAPI application factory for the office door light service."""
from __future__ import annotations
import logging

from fastapi import Depends, FastAPI

from .hardware.base import LightPanel, Status
from .hardware.mock import MockLightPanel

# Configure basic logging
logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a logger instance
logger = logging.getLogger(__name__)

def create_app(panel: LightPanel | None = None) -> FastAPI:
  """Create a FastAPI application configured with the provided panel."""

  light_panel = panel or MockLightPanel()
  logger.info("Light panel initialized: %s", type(light_panel).__name__)
  app = FastAPI(title="Office Door Sign", version="0.1.0")

  @app.on_event("startup")
  def _on_startup() -> None:
    logger.info("API startup complete. Active panel: %s", type(light_panel).__name__)

  def get_panel() -> LightPanel:
    return light_panel

  @app.get("/health")
  def health() -> dict[str, str]:
    logger.info("Health check endpoint called.")
    return {"status": "ok"}

  @app.get("/status")
  def read_status(panel: LightPanel = Depends(get_panel)) -> dict[str, str]:
    logger.info("Reading status endpoint called.")
    return {"status": panel.status.name}

  @app.get("/status/free")
  def set_free(panel: LightPanel = Depends(get_panel)) -> dict[str, str]:
    logger.info("Setting free endpoint called.")
    panel.status = Status.FREE
    return {"status": panel.status.name}

  @app.get("/status/on_call")
  def set_on_call(panel: LightPanel = Depends(get_panel)) -> dict[str, str]:
    panel.status = Status.ON_CALL
    return {"status": panel.status.name}

  @app.get("/status/working")
  def set_working(panel: LightPanel = Depends(get_panel)) -> dict[str, str]:
    panel.status = Status.WORKING
    return {"status": panel.status.name}

  @app.get("/status/off")
  def set_off(panel: LightPanel = Depends(get_panel)) -> dict[str, str]:
    panel.status = Status.OFF
    return {"status": panel.status.name}

  return app
