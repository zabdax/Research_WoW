"""Validate provenance completeness and status for revised structured inputs."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_PROVENANCE = ("source", "locator", "status")
VALID_STATUS = {"VERIFIED", "PARTIAL", "UNVERIFIED", "UNVERIFIED-PRIMARY"}


def _walk(value: Any, path: str = "") -> list[tuple[str, dict[str, Any]]]:
    records: list[tuple[str, dict[str, Any]]] = []
    if isinstance(value, dict):
        if "value" in value or ("right_ascension" in value and "declination" in value) or "identifier" in value:
            records.append((path, value))
        for key, child in value.items():
            records.extend(_walk(child, f"{path}.{key}" if path else key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            records.extend(_walk(child, f"{path}[{index}]"))
    return records


def audit(path: str | Path) -> dict[str, Any]:
    input_path = Path(path)
    raw = yaml.safe_load(input_path.read_text(encoding="utf-8"))
    missing: list[str] = []
    unverified: list[str] = []
    invalid_status: list[str] = []
    for location, record in _walk(raw):
        for key in REQUIRED_PROVENANCE:
            if not record.get(key):
                missing.append(f"{location}: missing {key}")
        status = record.get("status")
        if status and status not in VALID_STATUS:
            invalid_status.append(f"{location}: unknown status {status}")
        if status and status != "VERIFIED":
            unverified.append(f"{location}: {status}")
    return {
        "path": str(input_path),
        "records_checked": len(_walk(raw)),
        "missing_provenance": missing,
        "non_verified_records": unverified,
        "invalid_status": invalid_status,
        "passed": not missing and not invalid_status,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default=str(ROOT / "research" / "data" / "wow_observation.yaml"),
    )
    args = parser.parse_args()
    report = audit(args.input)
    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
