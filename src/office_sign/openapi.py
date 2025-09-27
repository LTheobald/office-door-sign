"""Utilities for exporting the FastAPI OpenAPI schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
  import yaml
except ImportError:  # pragma: no cover - optional dependency
  yaml = None

from .api import create_app


def _dump_schema(schema: dict[str, Any], destination: Path) -> str:
  suffix = destination.suffix.lower()
  if suffix in {".yaml", ".yml"}:
    if yaml is None:
      raise RuntimeError(
          "PyYAML is required to export YAML. Install it or use a .json output path.")
    return yaml.safe_dump(schema, sort_keys=False)
  return json.dumps(schema, indent=2)


def export_openapi_schema(output_path: str | Path = "openapi.json") -> Path:
  """Generate the OpenAPI schema and persist it to ``output_path``."""

  path = Path(output_path)
  app = create_app()
  schema: dict[str, Any] = app.openapi()
  path.parent.mkdir(parents=True, exist_ok=True)
  serialized = _dump_schema(schema, path)
  path.write_text(serialized, encoding="utf-8")
  return path


def _build_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description="Export the Office Door Sign OpenAPI schema")
  parser.add_argument(
      "--output",
      "-o",
      default="openapi.json",
      help="Path to write the generated schema (default: openapi.json)")
  return parser


def main(argv: list[str] | None = None) -> Path:
  """Parse CLI arguments and export the OpenAPI schema."""

  parser = _build_parser()
  args = parser.parse_args(argv)
  output = export_openapi_schema(args.output)
  print(f"OpenAPI schema written to {output}")
  return output


if __name__ == "__main__":
  main()
