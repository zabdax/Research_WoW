# Arecibo Wow! II — Paper Extraction Checklist (Phase A) — COMPLETED

> **STATUS: COMPLETED 2026-08-23** under explicit Phase A authorization
> (see `docs/acquisition/SOURCE_LOCK_REPORT.md` authorization record).
> All extracted values live in the FROZEN `research/data/mendez_evidence_vector.yaml`
> (freeze manifest: `research/data/mendez_evidence_freeze_manifest.yaml`).
> Line references point to the frozen `awowii-v1.tex`.
> Phase C reproduction (frequency + flux arithmetic) completed; results in
> `research/data/processed/mendez_reproduction_results.json`.

**Frozen source of record:** arXiv:2508.10657 **v1**; repo planetaryhablab/Ohio-SETI @ `28624a1`.

## A. Observational parameters — EXTRACTED (vector keys in parentheses)
- [x] observation date/time + time system — `observation_datetime` (Table 4 l.423; §4 l.175-179; CSV row 61 = 22:16:10 sample)
- [x] time uncertainty — clock ±2 sidereal s; N50CH ±6 s (l.179, l.196)
- [x] signal apparent duration — `signal_apparent_duration` = ≥73.4±0.5 s, CENSORED (Table 4 l.427; §5 l.196)
- [x] frequency + uncertainty — `observed_frequency` = 1420.726±0.005 MHz (Table 4 l.424; equations l.316-322); REPRODUCED (AGREE)
- [x] channel number — 2 (l.322); data-located rows 58-63
- [x] local oscillator information — LO1 1450.5056 MHz (l.283); f_2LOc 120.1/119.9 regimes (l.322)
- [x] positive-horn RA — 19:25:02±3 s (Table 4 l.436)
- [x] negative-horn RA — 19:27:55±3 s (Table 4 l.437)
- [x] declination + uncertainty — −26:57:18 / −26:57:13, ±20′ (Table 4 l.436-437)
- [x] positional uncertainty — stat ±0.2 s; pointing ±3 s; squint 128±3 s vs Ehman 154.95 s; offset ~27 s (§5 l.187-196)
- [x] horn squint — 128±3 s empirical (PARTIAL_UNVERIFIABLE — private strip chart)
- [x] SNR — `snr_peak` = 30.1±0.4 (Table 4 l.428; fig:wowfit l.192); previous 30.5±0.5 identified as Ehman-1998 historical
- [x] flux density — `flux_density` = **≥256±63 Jy, lower_bound_censored** (Table 4 l.430; equations l.266-276); ARITHMETIC_REPRODUCTION_ONLY
- [x] flux uncertainty semantics — documented ambiguity preserved (beam-centered-equivalent; ~2× with prior noise tube; l.279)
- [x] source angular extent — ≤1.9±0.1′ upper bound (Table 4 l.434)
- [x] heliocentric velocity — −84±1 km/s (Table 4 l.431); DERIVED, methodology partially documented
- [x] LSR velocity — −74±2 km/s (Table 4 l.432); convention unstated — flagged

## B. Instrument / reconstruction parameters — EXTRACTED (`instrument_constants`)
- [x] beam dimensions (8′ RA assumption; ±20′ dec scale), cadence (12 s), integration (10 s), channels (50×10 kHz), receivers (SETI 500 kHz; continuum 8 MHz @1415 MHz), noise tube (5 K / 5 min / 2 h), SNR algorithm (Eq. 1 l.212-227), ON/OFF horn scheme (l.207-209), |S| pre-1977-10-22 single-peak ambiguity (l.237), repo README TSYS/OFREQ/REFSYS recorded with LSR-vs-GSR tension flagged

## C. Data provenance — EXTRACTED (`archive_provenance`)
- [x] N50CH record (Abel; 75,000+ pages; 1.24 TB/69 GB; 167 dirs + wow-001..074; hosting on NAAPO per paper §2 l.113-121 + human verification 2026-08-23; scope note applied)
- [x] OCR methodology (Tesseract 4.0 trained on wow-053; OpenCV; human verification; l.167-171)
- [x] transcription scope Aug 13-17 1977; continuum column history; OSS object column
- [x] Table 1 August 1977 runs; Wow run (74 pages, 13:20:05→09:13:24); 48-h-later same-RA scan recorded as follow-up constraint

## D. HI / physical interpretation — EXTRACTED, ALL TAGGED PAPER_ONLY / NOT_INDEPENDENTLY_REPRODUCIBLE (`hi_wow23`)
- [x] Wow2/Wow3 (Jan 1978), HI4PI cloud confirmation, channel-inversion validation via VLSR≈0, IVC context, Gaia stars statement, DSR hypothesis (interpretive; feasibility ≠ P(D|H3))

## E. Interpretive/model-dependent statements — EXTRACTED
- [x] §8 H1 components (`h1_alternative_explanations`): RFI (1/32)^6 argument (arithmetic verified), harmonics (Table 3), satellites, solar, internal artifacts/EVT — paper analysis, not our P(D|H1)

## Phase C reproduction — COMPLETED (authorized scope only)
- [x] Frequency chain: **AGREE** (Δ 0.0004 MHz; genuine independent verification incl. data-level 6EQUJ5 / 2LO 120.185 check)
- [x] Flux arithmetic: **MATCH within printed rounding** (255.41 via paper path); unrounded propagation 250.1±56 Jy (−2.3%, rounding-policy artifact) — documented, not tuned; mode ARITHMETIC_REPRODUCTION_ONLY
- [x] Report-only internal-consistency check: Table 4 positive-horn galactic b anomaly (+1.04°) — AMBIGUOUS, flagged
- [ ] NOT attempted (per authorization): squint/position corrections (private data), velocity transforms, beam fit, EVT, OCR

## New conflicts discovered (also in vector `conflict_resolutions`)
- conflict 9: Table 4 positive-horn galactic latitude internally inconsistent (AMBIGUOUS)
- conflict 10 (minor): noise-tube "7-sigma" text vs equation constant 8.0±1.8
- conflict 11 (minor): repo README REFSYS 'LSR' vs paper GSR tracking statement
