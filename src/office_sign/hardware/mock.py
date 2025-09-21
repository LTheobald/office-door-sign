"""Mock implementation of the light panel for local development."""

from __future__ import annotations

from dataclasses import dataclass

from .base import LightPanel


@dataclass
class MockLightPanel(LightPanel):
  """A minimal in-memory implementation that records power state."""

  power_on: bool = False

  def set_power(self, on: bool) -> None:
    self.power_on = on
