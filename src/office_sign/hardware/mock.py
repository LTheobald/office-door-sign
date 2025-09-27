"""Mock implementation of the light panel for local development."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from .base import LightPanel, Status

logger = logging.getLogger(__name__)


@dataclass
class MockLightPanel(LightPanel):
  """A minimal in-memory implementation that records power state."""
  _status: Status = Status.OFF

  @property
  def status(self) -> Status:
    """Return the current panel status."""
    logger.info("Current MOCK panel status: {self.status}")
    return self._status
    return self._status

  @status.setter
  def status(self, value: Status) -> None:
    """Update the panel status and show debug output."""
    logger.info("Setting status to %s", value.name)
    self._status = value
    self._print_debug()

  def _print_debug(self) -> None:
    """Print a 17x7 grid of # in the color of the status."""
    cols, rows = 17, 7
    prefix = f"\x1b[38;2;{self._status.color[0]};{self._status.color[1]};{self._status.color[2]}m"
    suffix = "\x1b[0m"

    line = prefix + ("#" * cols) + suffix
    for _ in range(rows):
      logger.info(line)
