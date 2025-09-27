"""Domain services for controlling the light panel."""

from __future__ import annotations

from dataclasses import dataclass

from .hardware.base import LightPanel


@dataclass
class LightService:
  panel: LightPanel
