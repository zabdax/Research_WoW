#!/usr/bin/env python3
"""Deterministic text extraction for the frozen Gray & Ellingsen (2002) PDF.

MASTER DIRECTIVE (GE2002 OCR phase) sections 2, 3, 15.9.

- Verifies the frozen PDF SHA-256 before touching anything (refuses to run on
  mismatch).
- Extracts the text layer page-by-page with PyMuPDF (NO OCR needed if the
  text layer is intact; OCR fallback is a separate, not-yet-authorized step).
- Writes derived artifacts ONLY under
  research/sources/ellingsen_hobart/extracted/ge2002/ ; the source PDF is
  never modified.

Usage:  python scripts/ge2002_extract.py
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[1]
PDF = (
    REPO
    / "research" / "sources" / "ellingsen_hobart" / "original"
    / "drive-download-20260825T053211Z-1-001" / "wow_published.pdf"
)
OUT = REPO / "research" / "sources" / "ellingsen_hobart" / "extracted" / "ge2002"

# From research/sources/ellingsen_hobart/hashes/SHA256SUMS.txt (frozen 2026-08-25).
PINNED_SHA256 = "68c9a9c02a245df4dc0ae61b015856eea2e36f7c4e51f68c3673b73d5669e2b3"


def main() -> None:
    data = PDF.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != PINNED_SHA256:
        raise SystemExit(f"HASH MISMATCH: refusing to extract. {actual}")
    print(f"source hash verified: {actual}")

    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)

    pages_info = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        (OUT / f"page{i:02d}.txt").write_text(text, encoding="utf-8")
        pages_info.append({
            "pdf_page_index": i,
            "n_chars_text_layer": len(text),
            "n_images": len(page.get_images()),
            "paper_page_label": 966 + i,  # ApJ 578, pages 967-971
        })

    full = "\n".join(
        f"===== PDF PAGE {i + 1} (paper p.{966 + i + 1}) =====\n{p.get_text()}"
        for i, p in enumerate(doc)
    )
    (OUT / "fulltext.txt").write_text(full, encoding="utf-8")

    meta = {
        "artifact": "GE2002 text-layer extraction",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": "scripts/ge2002_extract.py",
        "source_pdf": str(PDF.relative_to(REPO)).replace("\\", "/"),
        "source_sha256": actual,
        "pdf_metadata": {k: v for k, v in doc.metadata.items() if v},
        "page_count": doc.page_count,
        "pages": pages_info,
        "ocr_required": all(p["n_chars_text_layer"] < 200 for p in pages_info),
        "method": "pymupdf get_text() (text layer; no OCR performed)",
        "source_modified": False,
    }
    (OUT / "extraction_manifest.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )
    print(f"pages extracted: {doc.page_count}")
    print(f"text-layer chars per page: {[p['n_chars_text_layer'] for p in pages_info]}")
    print(f"manifest: {OUT / 'extraction_manifest.json'}")


if __name__ == "__main__":
    main()
