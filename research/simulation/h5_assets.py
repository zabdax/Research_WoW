"""Parse and audit bundled upstream Kipping--Gray replication assets."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM = ROOT / "data" / "kipping_master_dl" / "wow-main"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_fortran_days(path: Path | None = None) -> list[float]:
    source = (path or UPSTREAM / "wow.f90").read_text(encoding="utf-8")
    match = re.search(r"days\s*=\s*\(/(.*?)/\)", source, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        raise ValueError("Could not locate Fortran days array.")
    values = re.findall(r"[-+]?\d+(?:\.\d+)?", match.group(1))
    days = [float(value) for value in values]
    if len(days) != 90:
        raise ValueError(f"Expected 90 observation dates, found {len(days)}.")
    return days


def parse_output_grid(path: Path | None = None) -> dict[str, float | int]:
    rows = []
    for line in (path or UPSTREAM / "output_grid.dat").read_text(encoding="utf-8").splitlines():
        if line.startswith("Column") or not line.strip():
            continue
        rows.append([float(x) for x in line.split()])
    if not rows:
        raise ValueError("No grid rows parsed.")
    best = max(rows, key=lambda row: row[2])
    return {"rows": len(rows), "max_log10_likelihood_floor": best[2], "log10_duration_days": best[0], "log10_lambda_per_day": best[1]}


def asset_report() -> dict[str, object]:
    fortran = UPSTREAM / "wow.f90"
    grid = UPSTREAM / "output_grid.dat"
    days = parse_fortran_days(fortran)
    grid_summary = parse_output_grid(grid)
    declared_grid_points = 150 * 160
    return {
        "source_repository_readme": str(UPSTREAM / "README.md"),
        "fortran_path": str(fortran),
        "fortran_sha256": sha256(fortran),
        "output_grid_path": str(grid),
        "output_grid_sha256": sha256(grid),
        "observation_days": len(days),
        "first_day": days[0],
        "last_day": days[-1],
        "baseline_days_from_dates": days[-1] - days[0],
        "grid": grid_summary,
        "declared_fortran_grid_points": declared_grid_points,
        "grid_row_count_matches_declared_loops": grid_summary["rows"] == declared_grid_points,
        "status": "assets_parsed; bundled grid/declared-loop discrepancy and independent emulator equivalence remain unresolved",
    }
