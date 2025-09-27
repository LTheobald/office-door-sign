from __future__ import annotations

import json

import pytest

from office_sign.openapi import export_openapi_schema


def test_export_openapi_schema_generates_json_file(tmp_path):
  output_path = tmp_path / "schema.json"

  result = export_openapi_schema(output_path)

  assert result == output_path
  data = json.loads(output_path.read_text())
  assert data["info"]["title"] == "Office Door Sign"
  assert "/light/status" in data["paths"]


def test_export_openapi_schema_generates_yaml_file(tmp_path):
  yaml = pytest.importorskip("yaml")
  output_path = tmp_path / "schema.yaml"

  result = export_openapi_schema(output_path)

  assert result == output_path
  data = yaml.safe_load(output_path.read_text())
  assert data["info"]["title"] == "Office Door Sign"
  assert "/light/status" in data["paths"]
