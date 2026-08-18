"""NASA/JPL Horizons retrieval and strict observer-ephemeris parsing."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlencode
from urllib.request import urlopen

import yaml

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class HorizonsRecord:
    epoch_utc: str
    right_ascension: str
    declination: str
    frame: str
    solution_command: str
    observer_center: str
    uncertainty_status: str
    source_url: str
    raw_sha256: str


def build_url(config: dict[str, object]) -> str:
    parameters = {
        "format": "text", "COMMAND": f"'{config['command']}'", "CENTER": f"'{config['center']}'",
        "MAKE_EPHEM": "'YES'", "EPHEM_TYPE": f"'{config['ephem_type']}'",
        "START_TIME": f"'{config['start_time']}'", "STOP_TIME": f"'{config['stop_time']}'",
        "STEP_SIZE": f"'{config['step_size']}'", "QUANTITIES": f"'{config['quantities']}'",
        "CSV_FORMAT": "'YES'",
    }
    return f"{config['endpoint']}?{urlencode(parameters)}"


def retrieve(config_path: str | Path, raw_path: str | Path) -> dict[str, object]:
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    url = build_url(config)
    with urlopen(url, timeout=60) as response:
        raw = response.read()
    destination = Path(raw_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    manifest = {"provider": config["provider"], "url": url, "retrieved_utc": datetime.now(UTC).isoformat(), "sha256": hashlib.sha256(raw).hexdigest(), "config": config}
    destination.with_suffix(destination.suffix + ".manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def parse_observer_ephemeris(raw_path: str | Path, source_url: str, solution_command: str, observer_center: str) -> list[HorizonsRecord]:
    raw = Path(raw_path).read_bytes()
    text = raw.decode("utf-8")
    if "$$SOE" not in text or "$$EOE" not in text:
        raise ValueError("Horizons response lacks a complete SOE/EOE ephemeris block.")
    if "R.A._(ICRF)" not in text or "DEC__(ICRF)" not in text:
        raise ValueError("Expected ICRF RA/Dec columns are absent.")
    block = text.split("$$SOE", 1)[1].split("$$EOE", 1)[0]
    records: list[HorizonsRecord] = []
    pattern = re.compile(r"^\s*(\d{4}-[A-Za-z]{3}-\d{2}\s+\d{2}:\d{2}),.*?(\d{2}\s+\d{2}\s+\d{2}\.\d+),\s*([+-]\d{2}\s+\d{2}\s+\d{2}\.\d+),", re.MULTILINE)
    digest = hashlib.sha256(raw).hexdigest()
    for epoch, ra, dec in pattern.findall(block):
        records.append(HorizonsRecord(epoch, ra.replace(" ", "h", 1).replace(" ", "m", 1) + "s", dec.replace(" ", "d", 1).replace(" ", "m", 1) + "s", "ICRF", solution_command, observer_center, "not_provided_in_response", source_url, digest))
    if not records:
        raise ValueError("No RA/Dec records parsed from Horizons SOE block.")
    return records


def write_processed(records: list[HorizonsRecord], destination: str | Path) -> None:
    output = {"schema_version": "0.1.0", "authority": "NASA/JPL Horizons API", "interpretation": "Geocentric geometry sensitivity only; uncertainty/covariance absent from retrieved response.", "records": [asdict(record) for record in records]}
    Path(destination).write_text(json.dumps(output, indent=2), encoding="utf-8")
