"""Adapter for the Pimoroni Unicorn HAT Mini hardware."""

from __future__ import annotations

from typing import Any

from .base import LightPanel, PanelUnavailableError

try:
  from unicornhatmini import UnicornHATMini
except ImportError:  # pragma: no cover - optional hardware dependency
  UnicornHATMini = None  # type: ignore[assignment]


class UnicornHatMiniPanel(LightPanel):
  """Controls the Unicorn HAT Mini panel."""

  def __init__(self, brightness: float = 0.2) -> None:
    if UnicornHATMini is None:
      raise PanelUnavailableError(
          "Unicorn HAT Mini library is not installed. Install `unicornhatmini`.")
    self._hat = UnicornHATMini()
    self._hat.set_brightness(brightness)

  def set_power(self, on: bool) -> None:
    if on:
      self._hat.set_all(255, 255, 255)
    else:
      self._hat.clear()
    self._hat.show()

  @property
  def raw(self) -> Any:
    """Expose the underlying Unicorn HAT Mini instance for advanced use cases."""

    return self._hat
