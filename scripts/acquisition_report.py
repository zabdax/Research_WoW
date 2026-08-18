"""Generate a reproducible evidence-acquisition status report."""
from __future__ import annotations

from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path

import yaml

from research.models.h2_horizons_sensitivity import geocentric_offset_report
from research.provenance.manifest import create_manifest

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    output = ROOT / "results" / "research"
    output.mkdir(parents=True, exist_ok=True)
    register_path = ROOT / "research" / "data" / "acquisition_register.yaml"
    register = yaml.safe_load(register_path.read_text(encoding="utf-8"))
    report = {
        "created_utc": datetime.now(UTC).isoformat(),
        "interpretation": "Acquisition-route report. Statuses identify evidence availability, not hypothesis probabilities.",
        "items": register["items"],
        "h2_geocentric_sensitivity": {
            "266P_Christensen": geocentric_offset_report(),
            "335P_Gibbs": geocentric_offset_report(ROOT / "research" / "data" / "processed" / "horizons_335p_1977_geocentric.json"),
        },
    }
    json_path = output / "acquisition_status.json"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    lines = ["# Evidence Acquisition Status", "", "| Input | Status | Next action |", "|---|---|---|"]
    for key, item in register["items"].items():
        lines.append(f"| {key} | {item['status']} | {item['next_action']} |")
    lines += ["", "## H2 public ephemeris sensitivity", ""]
    for name, h2 in report["h2_geocentric_sensitivity"].items():
        lines += [f"### {name}", "", f"- Source solution: `{h2['object_solution']}`; epoch: `{h2['epoch_utc']}`; frame: `{h2['frame']}`.", f"- Geocentric angular offset to candidate A: **{h2['offsets_deg']['candidate_a']:.3f}°**.", f"- Geocentric angular offset to candidate B: **{h2['offsets_deg']['candidate_b']:.3f}°**.", f"- Restriction: {h2['interpretation']}", ""]
    markdown_path = output / "acquisition_status.md"
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    create_manifest(output / "acquisition_manifest.json", [register_path, ROOT / "configs" / "acquisition" / "horizons_266p_1977.yaml", ROOT / "research" / "data" / "raw" / "horizons_266p_1977_geocentric.txt", ROOT / "research" / "data" / "processed" / "horizons_266p_1977_geocentric.json"], [json_path, markdown_path], seeds=[])
    print(json_path)

if __name__ == "__main__": main()
