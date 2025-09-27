"""Base abstraction for the functionality I want to expose on the Unicorn Hat Mini"""

from __future__ import annotations

from enum import Enum
from typing import Protocol


class LightPanel(Protocol):
    """Interface describing the capabilities required by the service."""

    @property
    def status(self) -> Status:
        """Return the current status of the panel."""

    @status.setter
    def status(self, value: Status) -> None:
        """Set the panel to display the provided status."""


class Status(Enum):
    """Enum representing my status to reflect on the door sign."""

    OFF = (0, 0, 0)  # Black / Off
    FREE = (0, 255, 0)  # Green
    WORKING = (255, 255, 0)  # Yellow
    ON_CALL = (255, 0, 0)  # Red

    @property
    def color(self):
        """Return the RGB color tuple associated with this status."""
        return self.value


class PanelUnavailableError(RuntimeError):
    """Raised when the configured panel cannot be created."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
