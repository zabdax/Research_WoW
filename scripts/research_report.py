"""Generate machine-readable tables and limited exploratory figures for the revised program."""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import yaml

from research.data.loader import load_wow_observation
from research.geometry.big_ear import BeamCalibration, BigEarGeometryModel
from research.models.h3_feasibility import H3ReferenceConfiguration, feasibility_summary, h3_readiness
from research.models.readiness import MECHANISM_REGISTRY
from research.simulation.h5_assets import asset_report
from research.simulation.h5_restricted import RestrictedH5Config, run_restricted_check
from research.validation.data_gaps import GAPS

ROOT = Path(__file__).resolve().parents[1]


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((ROOT / "configs" / name).read_text(encoding="utf-8"))


def _write_markdown(report: dict, path: Path) -> None:
    event = report["observational_constraints"]
    rows = ["# Revised Research Status Tables", "", "## Observational constraints", "", "| Quantity | Value | Type | Source |", "|---|---:|---|---|"]
    for key, value in event.items():
        rows.append(f"| {key} | {value['value']} {value['unit']} | {value['kind']} | {value['source']} |")
    rows += ["", "## Model readiness", "", "| Model | Status |", "|---|---|"]
    for key, value in report["model_readiness"].items():
        rows.append(f"| {key} | {value['status']} |")
    rows += ["", "## H3 feasibility", "", "| Quantity | Value |", "|---|---:|"]
    for key, value in report["h3_feasibility"].items():
        rows.append(f"| {key} | {value:.6g} |")
    rows += ["", "## H5 upstream assets", "", "| Quantity | Value |", "|---|---|"]
    for key, value in report["h5_assets"].items():
        rows.append(f"| {key} | {value} |")
    rows += ["", "## Restricted H5 Monte Carlo check", "", "| Quantity | Value |", "|---|---|"]
    for key in ("big_ear_probability_mean", "between_seed_sd", "followup_poisson_penalty", "restricted_post_followup_estimate", "published_post_followup_map", "absolute_difference_from_published", "status"):
        rows.append(f"| {key} | {report['h5_restricted'][key]} |")
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def _figures(report: dict, output: Path) -> None:
    import matplotlib.pyplot as plt
    h3 = report["h3_feasibility"]
    distances = np.linspace(0.4, 5.0, 200)
    flux = 1e-3 * (0.4 / distances) ** 2
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.semilogy(distances, flux, label="Reference DSR configuration under inverse-square scaling")
    ax.axhline(250, color="crimson", linestyle="--", label="Wow! observed lower bound")
    ax.axvspan(2.0, 4.9, color="grey", alpha=0.2, label="Documented H3 kinematic range")
    ax.set(xlabel="Distance (kpc)", ylabel="Flux density (Jy)", title="H3 reference-flux feasibility constraint")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(output / "h3_flux_feasibility.png", dpi=180); plt.close(fig)


def main() -> None:
    output = ROOT / "results" / "research"
    output.mkdir(parents=True, exist_ok=True)
    obs = load_wow_observation().event
    config = _load_yaml("h3_reference_feasibility.yaml")
    h3_config = H3ReferenceConfiguration(**{key: config[key] for key in H3ReferenceConfiguration.__dataclass_fields__})
    report = {
        "created_utc": datetime.now(UTC).isoformat(),
        "interpretation": "Research infrastructure result. No revised five-way posterior is emitted.",
        "observational_constraints": {
            name: {"value": item.value, "unit": item.unit, "kind": item.kind, "source": item.provenance.source}
            for name, item in {"frequency": obs.frequency, "bandwidth": obs.bandwidth, "flux_density": obs.flux_density, "snr": obs.snr, "beam_crossing_duration": obs.beam_crossing_duration}.items()
        },
        "model_readiness": {"H1": MECHANISM_REGISTRY["H1"], "H3": h3_readiness(), "H4": MECHANISM_REGISTRY["H4"], "H5": {"status": "in_progress", "restriction": "asset parsing complete; emulator equivalence unresolved"}, "H2": {"status": "blocked", "restriction": "authoritative ephemeris and beam calibration required"}},
        "h3_feasibility": feasibility_summary(h3_config),
        "h5_assets": asset_report(),
        "h5_restricted": run_restricted_check(RestrictedH5Config(realisations_per_seed=2_000)),
        "data_gaps": GAPS,
    }
    (output / "research_status.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    _write_markdown(report, output / "research_tables.md")
    _figures(report, output)
    print(output / "research_status.json")


if __name__ == "__main__":
    main()
