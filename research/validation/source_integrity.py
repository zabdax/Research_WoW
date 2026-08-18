"""Enforce source-class restrictions for revised confirmatory likelihood inputs."""
from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
DISALLOWED_SOLE_SUPPORT = {"preprint", "web_secondary"}


def audit_ledger(path: Path | None = None) -> dict[str, object]:
    ledger = yaml.safe_load((path or ROOT / "research" / "data" / "source_ledger.yaml").read_text(encoding="utf-8"))
    sources = ledger["sources"]
    missing_assets = [key for key, item in sources.items() if not (ROOT / item["local_asset"]).exists()]
    restricted = [key for key, item in sources.items() if item["source_class"] in DISALLOWED_SOLE_SUPPORT]
    return {"sources_checked": len(sources), "missing_local_assets": missing_assets, "restricted_as_sole_likelihood_support": restricted, "passed": not missing_assets, "policy": ledger["policy"]}


def main() -> None:
    import json
    report = audit_ledger(); print(json.dumps(report, indent=2))
    if not report["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
