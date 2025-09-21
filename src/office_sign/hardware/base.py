"""Abstract definitions for light panel hardware integrations."""

from __future__ import annotations

from typing import Protocol


class LightPanel(Protocol):
  """Interface describing the capabilities required by the service."""

  def set_power(self, on: bool) -> None:
    """Turn the panel on or off."""


class PanelUnavailableError(RuntimeError):
  """Raised when the configured panel cannot be created."""

  def __init__(self, message: str) -> None:
    super().__init__(message)
