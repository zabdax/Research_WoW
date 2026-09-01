#!/usr/bin/env python3
"""Generate SHA-256 manifest for the GE2002 derived authoritative artifacts.

Directive: GE2002 phase section 15.8. Re-runnable; overwrites the manifest
with current hashes (hashes change only if the artifacts change).
"""

import hashlib
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "research" / "sources" / "ellingsen_hobart" / "hashes" / "GE2002_DERIVED_SHA256SUMS.txt"

FILES = [
    "research/data/ge2002_extraction.yaml",
    "research/data/ge2002_search_outcome.yaml",
    "docs/acquisition/GE2002_OCR_REPORT.md",
    "docs/acquisition/GE2002_HOBART_RECONCILIATION.md",
    "docs/acquisition/GE2002_GAP_AMENDMENT.md",
    "docs/acquisition/bob_gray_remaining_requirements.md",
]


def main() -> None:
    lines = []
    for rel in FILES:
        p = REPO / rel
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(lines)} entries)")


if __name__ == "__main__":
    main()
