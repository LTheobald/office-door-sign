"""Domain services for controlling the light panel."""

from __future__ import annotations

from dataclasses import dataclass

from .hardware.base import LightPanel


@dataclass
class LightService:
  panel: LightPanel
  power_on: bool = False

  def turn_on(self) -> None:
    self.panel.set_power(True)
    self.power_on = True

  def turn_off(self) -> None:
    self.panel.set_power(False)
    self.power_on = False

  def status(self) -> bool:
    return self.power_on
