"""Read-only harvest of ASAP ASCII spectrum headers across the Ellingsen/Hobart
archive, including headers inside donor tarballs (streamed in memory; nothing
is extracted to disk).

Outputs (analysis products, never touching original/):
    research/sources/ellingsen_hobart/analysis/spectrum_header_index.csv
    research/sources/ellingsen_hobart/analysis/tarball_census.json

Each spectrum dump carries a self-describing header block written by ASAP,
e.g. Name / Position (J2000 string) / Time / Flux Unit / Pol Type / Abcissa /
WCS (frame, center Hz, channels, resolution kHz) / Rest Freq. This tool parses
those blocks verbatim without interpreting them scientifically.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import tarfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE = REPO_ROOT / "research" / "sources" / "ellingsen_hobart"
ORIGINAL = BASE / "original"

HEADER_KEYS = [
    "Name", "Position", "Time", "Flux Unit", "Pol Type", "Abcissa",
    "Beam No", "IF No", "WCS", "Rest Freq.", "Row_Flagged",
]


def parse_header_block(text: str) -> dict:
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^#\s*([A-Za-z_ .]+?):\s*(.*?)\s*$", line)
        if not m:
            m2 = re.match(r"^#\s{0,3}(\w[\w .]*?)\s:\s(.*)$", line)
            if not m2:
                continue
            m = m2
        key, val = m.group(1).strip(), m.group(2).strip()
        if key in HEADER_KEYS and key not in out:
            out[key] = val
    return out


def iter_loose():
    for p in sorted(ORIGINAL.rglob("*.txt")):
        rel = p.relative_to(BASE).as_posix()
        if "/positions/" in rel:
            continue
        try:
            text = p.read_text(errors="replace")[:2000]
        except OSError as exc:
            yield rel, "", {"error": str(exc)}
            continue
        yield rel, "", parse_header_block(text)


def iter_tarballs():
    for p in sorted(ORIGINAL.rglob("*.tar.gz")):
        rel = p.relative_to(BASE).as_posix()
        with tarfile.open(p, "r:gz") as tf:
            n = 0
            for member in tf:
                if not member.isfile() or not member.name.lower().endswith(".txt"):
                    continue
                n += 1
                fh = tf.extractfile(member)
                if fh is None:
                    continue
                text = fh.read(2000).decode("utf-8", errors="replace")
                yield f"{rel}::{member.name}", rel, parse_header_block(text)
            yield f"__census__{rel}", rel, {"__entries__": str(n)}


def main() -> int:
    rows = []
    census = {}
    for origin, tarball, hdr in iter_loose():
        rows.append({"origin": origin, "container": "", **hdr})
    for origin, tarball, hdr in iter_tarballs():
        if origin.startswith("__census__"):
            census[tarball] = int(hdr.get("__entries__", 0))
            continue
        rows.append({"origin": origin, "container": tarball, **hdr})

    fields = ["origin", "container"] + HEADER_KEYS + ["error"]
    out_path = BASE / "analysis" / "spectrum_header_index.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    census_path = BASE / "analysis" / "tarball_census.json"
    json.dump(census, open(census_path, "w"), indent=1)

    print(f"[header-index] loose+member rows: {len(rows)}")
    print(f"[header-index] tarball census: {json.dumps(census, indent=1)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
