"""Mock implementation of the light panel for local development."""

from __future__ import annotations

from dataclasses import dataclass

from .base import LightPanel
from ..status import Status


@dataclass
class MockLightPanel(LightPanel):
  """A minimal in-memory implementation that records power state."""

  power_on: bool = False
  status: Status = Status.OFF

  def set_power(self, on: bool) -> None:
    self.power_on = on

  def set_status(self, status: Status) -> None:
    """Set the panel status and print a 17x7 colored grid of # for debugging."""
    self.status = status
    cols, rows = 17, 7
    prefix = f"\x1b[38;2;{status.color[0]};{status.color[1]};{status.color[2]}m"
    suffix = "\x1b[0m"

    line = prefix + ("#" * cols) + suffix
    for _ in range(rows):
      print(line)