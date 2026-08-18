"""Generate an audit report for the preserved Phase 2 prototype."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from src.bayesian_engine import compute_posteriors
from src.kg_validation import run_level1_validation
from src.sensitivity import run_sensitivity_sweep

ROOT = Path(__file__).resolve().parents[1]

LEGACY_MANUSCRIPT_TARGET = {
    "H3": 0.753,
    "H5": 0.165,
    "H4": 0.082,
    "source": "manuscripts/full_paper.md and manuscripts/rnaas_note.md",
}


def _result_to_dict(result: Any) -> dict[str, Any]:
    return json.loads(result.to_json())


def main() -> None:
    output_dir = ROOT / "results" / "legacy"
    output_dir.mkdir(parents=True, exist_ok=True)

    current = _result_to_dict(compute_posteriors())
    stored_path = ROOT / "data" / "posterior_results.json"
    stored = json.loads(stored_path.read_text(encoding="utf-8")) if stored_path.exists() else None
    validation = asdict(run_level1_validation())
    sensitivity = run_sensitivity_sweep(steps=20)

    report = {
        "report_type": "legacy_phase2_audit",
        "created_utc": datetime.now(UTC).isoformat(),
        "interpretation": (
            "Exploratory legacy output only. Scalar component values are not "
            "validated marginal likelihoods and must not be presented as "
            "confirmatory posterior inference."
        ),
        "current_code_output": current,
        "stored_output": stored,
        "manuscript_declared_targets": LEGACY_MANUSCRIPT_TARGET,
        "manuscript_minus_current": {
            key: LEGACY_MANUSCRIPT_TARGET[key] - current["posteriors"][key]
            for key in ("H3", "H5", "H4")
        },
        "kipping_gray_level1": validation,
        "sensitivity": sensitivity,
    }

    destination = output_dir / "legacy_audit_report.json"
    destination.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
