"""Create reproducibility manifests for generated research artifacts."""
from __future__ import annotations

from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def create_manifest(output_path: Path, inputs: list[Path], outputs: list[Path], seeds: list[int] | None = None) -> dict[str, object]:
    manifest = {"created_utc": datetime.now(UTC).isoformat(), "git_commit": git_commit(), "python": sys.version, "platform": platform.platform(), "inputs": {_display_path(path): sha256(path) for path in inputs if path.exists()}, "outputs": {_display_path(path): sha256(path) for path in outputs if path.exists()}, "seeds": seeds or []}
    output_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest
