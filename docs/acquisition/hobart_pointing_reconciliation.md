# Hobart Pointing Reconciliation (Pure Geometry — No Weighting, No Intent Claims)

Date: 2026-08-25 · Scope: MASTER DIRECTIVE §8 · Inputs:
`analysis/pointing_geometry.json`, `research/data/ellingsen_coordinate_provenance.yaml`,
`analysis/rpfits_source_table_index.json`.

**What this document is:** angular separations between every Hobart commanded
pointing and the project-canonical Wow! horn locales, plus documented
epoch relationships. **What it is not:** a beam weighting, a likelihood, or a
decision about what Simon "meant" — that intent remains OPEN
(GAP-HOB-002/003/004).

## 1. Reference positions (frozen)

| Locale | J2000 | Uncertainty | Source |
|---|---|---|---|
| Positive horn | 19:25:02 −26:57:18 | ±3 s RA; ±20′ Dec | Arecibo II Table 4 (paper states J2000) |
| Negative horn | 19:27:55 −26:57:13 | ±3 s RA; ±20′ Dec | Arecibo II Table 4 |

## 2. Commanded Hobart pointings vs locales

Commands verified three ways: dump headers, RPFITS SU tables (all 27 files;
`EPOCH='j2000'` system card in every file), live-pages DB extracts.

| Pointing | vs Positive horn | vs Negative horn |
|---|---|---|
| field1 19:25:28 −26:57 | **5.80′** (ΔRA +5.79′) | 32.76′ |
| field2 19:28:17 −26:57 | 43.46′ | **4.91′** (ΔRA +4.90′) |
| 2010 ON 19:23:03 −26:43:24 | 29.96′ (ΔRA −26.57′, ΔDec +13.9′) | 66.59′ |
| 2010 off-north (−25:43:24) | 78.56′ | 98.63′ |
| 2010 off-south (−27:43:24) | 53.14′ | 79.61′ |

Beam context: measured 1-D FWHM 33.8′–36.8′ (2010 calibrator). **No 2-D beam
model exists**; a centered-Gaussian response at these offsets is NOT asserted
anywhere in this project.

Geometric facts only (no intent interpretation):
- The field pair jointly brackets both horn locales within ~5–6′ of each.
- The 2010 ON position lies ≈30′ (≈0.85×FWHM) from the positive-horn locale,
  with its ±1° Dec off-pairs further out.
- Session→locale assignment is not recorded anywhere in the archive.

## 3. Epoch relationships (documented/derived, not interpreted)

- Every `.rpf` carries `EPOCH='j2000'`; live-pages column is `coord_ra2000`.
  Commands were processed as J2000 by the observatory chain (DOCUMENTED).
- The 1999 README grid (B1950, DOCUMENTED) precesses to:

| 1999 point (B1950) | → J2000 (derived, FK4→ICRS incl. E-terms) | vs PosH / NegH |
|---|---|---|
| A 19:22:22 −27:18 | 19:25:27.9 −27:12:01 | 15.81′ / 35.93′ |
| B 19:25:12 −27:18 | 19:28:17.8 −27:11:50 | 45.93′ / 15.46′ |
| C 19:22:22 −26:48 | 19:25:27.2 −26:42:01 | 16.28′ / 36.30′ |
| D 19:25:12 −26:48 | 19:28:17.1 −26:41:50 | 46.19′ / 16.16′ |

- Derived coincidence: field1's commanded RA equals A's precessed RA and
  field2's equals B's, each to <2 s of time. This is consistent with (but does
  not prove) deliberate epoch-corrected re-observation of the 1999 grid.
- Hypothetical transforms recorded for completeness ONLY (intent hypotheses,
  not evidence): if the field strings had been B1950 values fed through
  precession, their "intended" images would be 19:28:33 (10.7′ from NegH) and
  19:31:22 respectively — while the antenna would still have physically
  pointed where the DB/SU tables say it pointed.

## 4. Status against the directive rules

- No spatial weights assigned anywhere (rule §0 upheld).
- Which locale each session "targeted" is UNRESOLVED and must come from donor/
  project records or be explicitly waived by the human gate.
- The geometric coverage facts above hold regardless of how that question is
  eventually answered, because actual antenna positions are triple-confirmed.
