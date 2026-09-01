# Gray & Ellingsen (2002) OCR — Preparation Artifact

> **SUPERSEDED (same phase):** the extraction was subsequently authorized and
> executed WITHOUT OCR — the PDF's text layer proved fully readable via
> PyMuPDF. See `GE2002_OCR_REPORT.md` and
> `research/data/ge2002_extraction.yaml`. This document is retained only as
> the record of the preparation/authorization step; its tooling plan was not
> needed.

Status: **SUPERSEDED — SEE GE2002_OCR_REPORT.md** · Prepared 2026-08-29
phase directive §6 · Nothing was OCR'd under this plan.

## 1. Target identity (provenance verified)

| Attribute | Value | Evidence class | Locator |
|---|---|---|---|
| File | `research/sources/ellingsen_hobart/original/drive-download-20260825T053211Z-1-001/wow_published.pdf` | DOCUMENTARY | frozen archive |
| Size | 520 KB | MEASURED | file system |
| SHA-256 | `68c9a9c02a245df4dc0ae61b015856eea2e36f7c4e51f68c3673b73d5669e2b3` | HASH_VERIFIED | matches `hashes/SHA256SUMS.txt` line 1558 (frozen 2026-08-25) |
| Bibliographic identity | Gray & Ellingsen 2002, "A Search for Periodic Emissions at the Wow Locale", ApJ 578:967–971, DOI 10.1086/342646 | DOCUMENTARY (Crossref-verified 2026-08-25) | `hobart_literature_reconciliation.md` |
| Text-layer state | all text vectorized outlines; 28/37 content streams decompress with zero readable text | DOCUMENTED (prior forensic pass) | `hobart_literature_reconciliation.md` |

## 2. Purpose (narrowly defined)

Establish exactly what the published 1998/99 work reports and what it does
NOT report — specifically: search procedure, sensitivity, candidates,
non-detections/outcome statements, calibration, and observing setup. This
directly bears on GAP-HOB-009 (search outcomes) and GAP-HOB-017
(campaign-to-publication relationship).

## 3. Tooling assessment (as of preparation)

| Requirement | Available? | Note |
|---|---|---|
| PDF text-layer extractor (pypdf/pdfminer/PyMuPDF) | NO | not installed in `.venv`; prior pass already showed no usable text layer |
| PDF rasterizer (PyMuPDF / pdf2image + poppler) | NO | not installed |
| OCR engine (tesseract) | NO | not on PATH; requires system-level install |
| Image handling (Pillow) | YES | v12.3.0 |

Proposed execution route (requires authorization + installs):
1. `pip install pymupdf` (or `pypdf` for a text-layer re-probe first);
2. rasterize pages at ≥300 dpi;
3. install tesseract (system package) + `pytesseract`;
4. OCR page-by-page; keep per-page PNG + TXT artifacts under
   `research/sources/ellingsen_hobart/extracted/ge2002_ocr/` (local-only,
   hash-manifested);
5. produce a tracked extraction summary `docs/acquisition/GE2002_EXTRACTION.md`.

## 4. Extraction protocol (to be executed only after authorization)

- Work page-by-page; record page number, extractor version, and per-page
  confidence; keep raw OCR output immutable and derive summaries separately.
- Label every extracted item with exactly one evidence class:
  `DIRECTLY_STATED` · `TABLE_VALUE` · `FIGURE_VALUE` · `OCR_CONFIRMED` ·
  `OCR_AMBIGUOUS` · `NOT_STATED` · `INFERRED`.
- OCR_AMBIGUOUS items must record the ambiguous string and the candidate
  readings; numbers in tables/figures must be double-checked against the
  page image before any `TABLE_VALUE`/`FIGURE_VALUE` label is assigned.
- `INFERRED` items stay outside the authoritative evidence layer.
- Target sections: abstract; observing setup (telescope/backend/bandwidth/
  channels/integration); calibration; sensitivity statements; search
  procedure; candidate handling; outcome statements; conclusions.

## 5. Scope boundaries (hard)

- Do NOT infer missing methodology from results.
- Do NOT reconstruct missing software kernels.
- Do NOT convert qualitative statements into quantitative parameters without
  explicit source support.
- Do NOT calculate any likelihood, detection efficiency, or rate.
- Do NOT treat absence of a statement as proof that something did not occur
  (`NOT_STATED` ≠ "did not happen").
- Do NOT modify `mendez_evidence_vector.yaml`, the gap register statuses, or
  `confirmatory_comparison_enabled` on the basis of extraction alone; any
  consequential updates go through a separate human-reviewed amendment.

## 6. Authorization gate

The project already defines this gate: gap register GAP-HOB-009 notes
"G&E2002 OCR pending authorization" and `hobart_literature_reconciliation.md`
lists it as the recommended next action requiring sign-off.

**STOP — execution requires explicit written human authorization** naming
this document. Until then: no installs, no rasterization, no OCR.
