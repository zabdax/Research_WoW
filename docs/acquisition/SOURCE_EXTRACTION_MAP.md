# SOURCE EXTRACTION MAP — Pre-Authorization Review Output

**Created:** 2026-08-22 (UTC), read-only pre-authorization review per MASTER DIRECTIVE Part 0.4–0.14.
**Source lock verified before mapping:** 7/7 integrity tests passing; no evidence/model files modified.
**Frozen sources of record:** Arecibo Wow! II = arXiv:2508.10657 **v1** (TeX: `research/sources/mendez_arecibo/extracted/awow2_2508.10657v1_eprint/awowii-v1.tex`, 487 lines — line numbers below refer to this frozen file). Wow! I = 2408.08513 **v2**. Ohio-SETI repo @ `28624a1`. Hotaling @ `0b491d4`.
**Status: NOT AUTHORIZED for Phase A.** This map records WHERE each quantity lives and HOW it will be extracted — final values are extracted only after explicit authorization.

Layer codes used throughout (never collapsed): **L1** = historical observation (1977), **L2** = modern reconstruction, **L3** = derived/model-dependent.

---

## 1. Arecibo II paper map

| Locator (frozen TeX) | Content | Role |
|---|---|---|
| Abstract (l.85–88) | Headline results (positions, >250 Jy, 1420.726±0.005 MHz) | L2 summary — wording differs slightly from Table 4 (see §11, conflict 6) |
| §1 Introduction (l.97–109) | History, two-horn problem, prior literature | context; horn E/W naming, 3-min interval |
| §2 The Ohio SETI Data (l.111–163) | N50CH record provenance: Abel photographs (75,000+ pages), formats (PNG/CR2→JPG), **1.24 TB / 69 GB**, 167 directories + `wow/` (wow-001…074), archive placement, SNR character encoding, IBM 1030 Assembler/FORTRAN IV code, LOBES | L1 archive description — **primary archival-input map** |
| **Table 1** `tab:august` (l.123–155) | All Aug 1977 observation runs: dates, declinations, page counts, start/end times; only 3 scans at Wow dec; final scan 48 h later re-covered Wow RA | L1 observing log — follow-up non-detection constraint |
| §3 Data Transcription (l.165–171) | OCR: Tesseract 4.0 neural net trained on frame **wow-053**; OpenCV pipeline; human verification; continuum computed; OSS object column added; Aug 13–17 1977 transcribed | transcription methodology (L1→digitized) |
| §4 Time (l.173–179) | EST vs EDT (10:16 PM EST = 11:16 PM EDT), 10 s integration + 2 s processing = 12 s cadence, sidereal clock offset (Ehman ±2 sidereal s), time corrected only for Wow via fit | temporal provenance |
| §5 Location (l.181–203) | Calibration with 5 OSS sources; Aug 16 1977 strip chart (Childers); **~27 s positional offset**; horn squint: Ehman 154.95 s vs **measured 128±3 s**; N50CH ±6 s time resolution; Gaussian fit → ±0.2 s statistical, ±3 s pointing; dec ±20′; 8′ RA beamwidth; duration & max source size derived | position/beam provenance |
| Figure 1 `fig:wowfit` (l.189–194) | Gaussian beam-profile fit; caption: SNR 30.1±0.4, RA 19h25m02±0.2 s, extent <1.9±0.1′ | central L2 measurement locator |
| Figure 2 `fig:wowmap` (l.198–203) | HI4PI map; earlier (gray) vs revised (yellow) Wow boxes | position comparison |
| §6 Flux Density (l.205–279) | Horn ON/OFF scheme; SNR algorithm (**Eq. 1** `eq:snr`, l.212–227, from Ehman 2010); Kraus 1994 continuum figure; \|S\| before 1977-10-22 → single-peak ambiguity; **no flux calibration in N50CH**; historical 54 (Ehman) / 212 (Childers) Jy; new calibration chain (Eqs. at l.266–276): σ_cnt = 9.4 Jy / 8.0±1.8 = 1.2±0.3 Jy; σ_channel = σ_cnt·√50 = 8.5±2.1 Jy; **S_Wow = SNR_Wow × σ_channel ≥ 256±63 Jy**; "lower limit value" reasoning (declination + noise-level uncertainties) | flux provenance — **censored L2 result** |
| **Table 2** `tab:calibrators` (l.241–254) | 5 calibration sources (OSS vs NVSS fluxes, J2000 coords) | calibration input |
| Figure 3 `fig:krausscont` (l.230–235) | 1994 Kraus→Sagan continuum analog record | L1 external document |
| Figure 4 `fig:continuum` (l.258–263) | Continuum SNR Aug 15 1977 with noise-tube signals | calibration input |
| §7 Frequency (l.281–322) | Prior estimates: Kraus 1994 = 1420.3556 MHz; Ehman 1997 = 1420.4556 MHz (LO1 = 1450.5056 MHz, +0.1 MHz error); **channel-order inversion discovery** (freq decreases with channel #); 2nd-LO software change 1977-12-13 (120.0→119.9 MHz); GSR-adjusted 2nd-LO printout; **Eqs. (l.316–321):** f_c = (f_2LO − f_2LOc) + 1420.4056 MHz; f_n = f_c + (25.5−n)×0.010 MHz; f_2LOc = 120.1 MHz (pre-Dec 1977); at Wow peak f_2LO = 120.185 MHz → f_c = 1420.491 → **channel 2 = 1420.726 MHz**; error = half of 10 kHz channel | frequency provenance — fully reconstructable |
| §8 Alternative Explanations (l.324–409) | Local RFI ((1/32)^6 ≈ 10⁻⁹ argument); second harmonic (Table 3 UHF TV); satellites (geo incl <15–20°, Molniya transit-time); solar (sunspots ~40, subflares only, burst types); internal artifacts (gain-step shape; **Eq. 2** `eq:max` EVT, l.403–406) | H1-relevant analysis (L2/L3) |
| **Table 3** `tab:ohio_uhf_1977` (l.349–370) | Ohio UHF TV stations Aug 1977 (channels 14/53/54: none active) | RFI evidence |
| §9 Results and Discussion (l.411–454) | 7.25′ position shift; IVC compatibility (25–90 km/s LSR); Gaia stars with comparable velocities; Wow2/Wow3 HI-cloud confirmation; no L-band missions | L2/L3 interpretation |
| **Table 4** `tab:wow` (l.417–444) | **THE central table** — Revised Properties: date/time (prev 22:16:01 → new 22:16:06 EST), frequency (1420.455→1420.726±0.005 MHz), duration (≥72→≥73.4±0.5 s), SNR (30.5±0.5→30.1±0.4), flux (54/212 Jy → ≥256±63 Jy), VHEL −84±1, VLSR −74±2 km/s, size ≤1.9±0.1′, J2000 + Galactic coords for both horns; previous values = Ehman 1998 | primary extraction target |
| §10 Conclusion (l.456–471) | Astrophysical-origin alignment; DSR reference to Wow! I | interpretive (L3) |
| l.92 (commented) | Draft abstract for a **third paper**: "detection of a weak transient broadband signal concurrently with the Wow event" | Paper III exists in preparation — monitor |
| l.425–433 (commented rows) | TeX-internal revisions: flux row "≥249 +77/−48 Jy" superseded by "≥256±63"; commented "Observation Frame GSR", "Bandwidth 10 kHz", **"Distance 1.5±1.4 kpc"** rows | author-internal version artifacts — see §11 conflict 7 |

## 2. Historical archival inputs (Layer-1 sources and their access status)

| Input | Citation (from `awowii-v1.bib`) | Access status |
|---|---|---|
| N50CH printout archive (75,000+ pages; 167 dirs + `wow/` wow-001…074; JPG 69 GB / original 1.24 TB) | §2, l.113–121; "available on the NAAPO website managed by Russ Childers" (l.117) | **Paper says publicly available on naapo.org; site UNREACHABLE at 2026-08-22 check → pending re-verification. Corrects Phase 0 inventory (visible amendment made).** |
| Wow printout page (the one frozen in Ohio-SETI as `oseti_19770815_220410.jpg`) | repo @ `28624a1` | FROZEN locally |
| IBM 1030 Assembler + FORTRAN IV N50CH code printouts (c. 1984); authors run it in an IBM 1030 emulator | §2, l.159 | Not located publicly — request/monitor |
| Ehman 30th report (methods: SNR Eq. 1, squint 154.95 s, LO details, 54 Jy estimate) | ehman2010big = bigear.org/Wow30th/wow30th.htm | CACHED (`data/sources_cache/ehman_30th.htm`, hash-recorded) |
| Ehman 20th report (previous values in Table 4: "calculated 1997–1998") | ehman1998big = bigear.org/**wow20th.htm** | **NOT yet cached — REQUIRED for historical comparison** |
| Ehman 2011 book chapter | DOI 10.1007/978-3-642-13196-7_4 (Springer, paywalled) | OPTIONAL |
| Kraus→Sagan 1994 letter (continuum figure + 1420.3556 MHz estimate) | wowkraus = **nrao.edu/archives/items/show/3684** (NRAO/AUI Archives) | Publicly listed — fetch in Phase A/C |
| Kraus 1979 Cosmic Search article | kraus1979we, Cosmic Search 1(3):31 | bigear.org CSMO archive (public) |
| Aug 16 1977 continuum strip chart (Childers; pointing/flux calibration input) | §5, l.185 | Not public — obtained by authors from Childers |
| Cole 1976 MSc thesis (noise tube: 5 K, 5 min per 2 h) | cole1976search, Ohio State Univ. | Not yet located — library route |
| Dixon 1970 OSS Master List (OBJECT column source) | TheMasterList, ApJS 20:1, DOI 10.1086/190216 | Public (ADS/CDS) |
| Ehman, Dixon & Kraus 1970 OSS survey (calibrator fluxes) | 1970AJ.....75..351E, AJ 75:351 | Public (ADS) |
| Dixon & Kraus 1968 (noise tube / OSS calibration heritage) | 1968AJ.....73..381D, AJ 73:381 | Public (ADS) |
| Dixon 1985 IAU 112 (Ohio SETI methods) | 1985IAUS..112..305D | Public (ADS) |
| Dixon 1977 (compact HI cloud detections pre-Wow) | 1977Icar...30..267D | Public (ADS) |

## 3. Ohio-SETI repository map (@ `28624a1`, dataset v0a 2024-10-14)

| Repo artifact | Paper quantity it underlies | Provenance class |
|---|---|---|
| `oseti_19770815_220410.jpg` (scan) | OCR input (§3); equivalent of one N50CH `wow/` frame | ORIGINAL_ARCHIVAL (scan surrogate) |
| `oseti_*.txt/.csv` (82 rows × 50 ch + RA/Dec/2LO/gal/EST) | printout layer: `RA_PRINT`, `DC_PRINT`, `FREQ_PRINT` (2nd LO), `ESTD_PRINT`, `SNR_PRINT` arrays | TRANSCRIBED_ARCHIVAL |
| `oseti_*.extended.pdf` (+ CNT, OBJECT) | continuum + OSS object columns (§3) | TRANSCRIBED_ARCHIVAL + derived fields |
| `oseti_*.sav` reanalysis arrays | `RA/DC_1950/2000` (corrected coords), `MJD/LST`, `CFREQ`, `SNR` (numeric), `FLUX`, `FREQ_CHAN(+VEL)`, `OBJECT` | CALIBRATED/RECONSTRUCTED — **v0a-era** |
| README SAV schema | TSYS=100 K, OFREQ=1420.4056 MHz, REFSYS=LSR, OBS_COORD | instrument metadata (verify against paper in Phase A) |

**⚠️ 54 Jy rule (Part 0.1):** README defines `FLUX` as "estimated flux density (Jy) [assuming max signal was 54 Jy]". Paper §6 (l.239) identifies **54 Jy as Ehman's legacy estimate** and 212 Jy as Childers', both superseded by the paper's own calibration chain (≥256±63 Jy). Therefore repo `FLUX` = **LEGACY_SUPERSEDED** for absolute flux. Repo `SNR` arrays remain valid (SNR is what N50CH actually recorded). Neither silently overwritten; both preserved with labels.

## 4. Hotaling transcription map (@ `0b491d4`, 2022-07-20)

- Manual transcription `Wow! Signal.csv` (82×50 + record columns); row-1 content verified identical to Ohio-SETI TXT/CSV (Phase 0).
- Role: independent TRANSCRIBED_ARCHIVAL witness enabling transcription-diff QC in Phase C (paper §3 used OCR + human validation; Hotaling used manual reading → two independent digitizations of the same page).
- Limitation: single page only; the paper's Aug 13–17 1977 transcription is not public in file form.

## 5. Flux/calibration provenance

```yaml
parameter: flux_density_S_Wow
paper: 2508.10657
paper_version: v1
section: "§6 Flux Density (l.205–279) + §9 (l.446) + Table 4 row (l.430)"
equation: "S_Wow = SNR_Wow × σ_channel ≥ 256±63 Jy (l.274–276); σ_channel = σ_cnt·√n (l.270–272); σ_cnt = 9.4 Jy / 8.0±1.8 (l.266–268)"
figure: "fig:wowfit (SNR input 30.1±0.4); fig:continuum (noise-tube SNR)"
table: "Table 2 (calibrator OSS/NVSS fluxes)"
underlying_data:
  repository: Ohio-SETI @ 28624a1
  file: "oseti_19770815_220410.txt/.csv (SNR rows), .sav (SNR array)"
  historical_source: "N50CH printout (noise-tube signal ~1 h after Wow); strip chart Aug 16 1977 (Childers); OSS/NVSS calibrators"
provenance_class: [TRANSCRIBED_ARCHIVAL → CALIBRATED → CENSORED_OR_BOUNDED]   # L2
censoring: "≥ lower bound — declination non-centring + noise-level uncertainty (l.279); prior noise-tube choice would give ~2× (l.279)"
planned_extraction_method: "read Table 4 row + §6 equations verbatim; recompute chain in Phase C"
independent_reproduction_possible: "YES from frozen repo SNR data + paper-stated calibration constants (9.4 Jy, 8.0±1.8); noise-tube SNR itself not in repo → partial"
current_access_status: frozen
known_conflict: "conflict 1 (54 Jy legacy), conflict 5 (project ≥250 Jy), conflict 6 (abstract 'exceeding 250' vs table '≥256±63' wording)"
scientific_importance: "CRITICAL — H3 energetics/feasibility, H4 engineering, censored-data handling project-wide"
---
parameter: noise_level_sigma_channel
section: "§6, l.265–272"
value_locator: "σ_cnt = 1.2±0.3 Jy; σ_channel = 8.5±2.1 Jy (n=50)"
provenance_class: CALIBRATED   # L2
independent_reproduction_possible: "YES (arithmetic chain)"
known_conflict: none
scientific_importance: "HIGH — dominates flux uncertainty"
---
parameter: SNR_Wow_peak
section: "§5 l.192 (fig:wowfit caption); §6 l.277; Table 4 l.428"
value_locator: "30.1±0.4 (Arecibo) vs 30.5±0.5 (previous, Ehman 1998)"
provenance_class: RECONSTRUCTED (Gaussian beam fit of transcribed SNR)   # L2
underlying_data: "repo SNR rows (channel 2, Wow rows)"
independent_reproduction_possible: "YES — Gaussian fit to frozen data"
known_conflict: "conflict 5 (project cites 30.5 from Wow I = previous value)"
scientific_importance: "HIGH"
```

## 6. Frequency provenance

```yaml
parameter: observed_frequency
paper: 2508.10657 v1
section: "§7 Frequency (l.281–322); Table 4 l.424"
equation: "f_c = (f_2LO − f_2LOc) + 1420.4056 MHz; f_n = f_c + (25.5−n)·0.010 MHz (l.316–321)"
value_locator: "channel 2 = 1420.726 MHz; uncertainty ±0.005 MHz = half the 10 kHz channel"
underlying_data:
  repository: Ohio-SETI @ 28624a1
  file: "oseti_*.txt/.csv '2ND LO FREQ' column (e.g. 120.162…) + .sav FREQ_PRINT/CFREQ/FREQ_CHAN"
  historical_source: "N50CH printout 2nd-LO values (GSR-referenced); Ehman 2010 methodology; LO1 = 1450.5056 MHz"
provenance_class: [TRANSCRIBED_ARCHIVAL → RECONSTRUCTED]   # L2; channel identification (n=2) is itself archival
planned_extraction_method: "read §7 + Table 4; recompute f_c/f_n from frozen 2LO column in Phase C"
independent_reproduction_possible: "YES — fully, from frozen repo data"
current_access_status: frozen
known_conflict: "conflict 5 (project frequency already matches table; verify uncertainty semantics = channel half-width)"
scientific_importance: "CRITICAL — drives velocity → HI candidate population (H3), RFI arguments (H1)"
---
parameter: frequency_reconstruction_corrections
section: "§7 (l.283–313)"
items: ["LO1 +0.1 MHz error history (Ehman 1997)", "channel-order inversion (freq ↓ with channel #)", "2LO software change 1977-12-13: f_2LOc 120.1 → 119.9 MHz (pre/post correction regimes)"]
provenance_class: RECONSTRUCTED (methodology validated on Wow2/Wow3 + galactic regions)
independent_reproduction_possible: "YES (apply equations to frozen 2LO data; validate on external HI4PI clouds)"
scientific_importance: "CRITICAL — without these corrections frequency is wrong by ~0.27 MHz"
```

## 7. Position provenance

```yaml
parameter: source_position_J2000 (both horns)
paper: 2508.10657 v1
section: "§5 Location (l.181–203); Table 4 l.435–440; abstract l.86"
figure: "fig:wowfit (positive-horn RA + statistical error); fig:wowmap (field comparison)"
value_locator: "positive horn 19:25:02±3 s / −26:57:18±20′; negative horn 19:27:55±3 s / −26:57:13±20′ (Table 4); Galactic coords also tabulated"
underlying_data:
  repository: Ohio-SETI @ 28624a1
  file: ".sav RA_2000/DC_2000 arrays (v0a-era corrected coords — cross-check only); printout times"
  historical_source: "Ehman 2010 (squint 154.95 s, negative-horn geometry); Aug 16 1977 strip chart (empirical squint 128±3 s); ~27 s clock/pointing offset"
provenance_class: [TRANSCRIBED_ARCHIVAL → RECONSTRUCTED]   # L2
corrections_chain: ["~27 s positional offset (clock)", "empirical squint 128±3 s replaces Ehman 154.95 s", "coordinates recomputed from printout time, printout values not overwritten"]
planned_extraction_method: "read Table 4 + §5; Phase C recompute via astropy from frozen EST/LST + documented corrections"
independent_reproduction_possible: "PARTIAL — corrections documented, but strip-chart calibration data (empirical squint) not public; repo .sav coords are v0a-era (possible mismatch — verify)"
current_access_status: frozen
known_conflict: "conflict 5 (project positions match abstract-level values; horn-labelled dec seconds −26:57:18/−26:57:13 are NEW detail); repo .sav v0a coords may differ from paper v1 coords"
scientific_importance: "CRITICAL — defines H3 search fields and H2 geometry tests"
---
parameter: positional_uncertainties
section: "§5 l.196"
value_locator: "RA: ±0.2 s statistical, ±3 s pointing (dominant), N50CH ±6 s time res; Dec: ±20′ (unchanged)"
provenance_class: RECONSTRUCTED
scientific_importance: "HIGH — defines spatial prior for H3 population integral"
---
parameter: horn_squint
section: "§5 l.187"
value_locator: "Ehman 154.95 s vs measured 128±3 s (at Wow declination)"
provenance_class: [SECONDARY (Ehman) vs CALIBRATED (empirical)]
known_conflict: "two squint values coexist — paper adopts empirical 128±3 s"
scientific_importance: "HIGH — horn separation geometry, two-horn timing, H2"
```

## 8. Velocity provenance

```yaml
parameter: radial_velocity_VHEL
paper: 2508.10657 v1
section: "Table 4 l.431; derivation context §7 + §9 l.448"
value_locator: "−84 ± 1 km/s"
underlying_data: "frequency 1420.726 MHz + standard heliocentric correction at Wow position/time"
provenance_class: DERIVED (L2 from L2 frequency)
independent_reproduction_possible: "YES — astropy radial-velocity transforms from frozen freq/position/time"
explicit_equation_in_paper: "NO — transformation equations not written out for the Wow values (method described for Wow2/Wow3 validation, l.299); STATUS = methodology-located, equations UNKNOWN"
scientific_importance: "CRITICAL for H3 (IVC membership 25–90 km/s LSR regime, l.450)"
---
parameter: LSR_velocity_VLSR
section: "Table 4 l.432; §9 l.448"
value_locator: "−74 ± 2 km/s"
provenance_class: DERIVED
assumptions: "solar peculiar motion convention not stated in paper — verify in Phase A/C (affects ±km/s level)"
independent_reproduction_possible: "YES (astropy), with convention ambiguity to document"
known_conflict: none recorded
scientific_importance: "CRITICAL for HI4PI cloud matching (H3)"
---
parameter: velocity_interpretation_IVC
section: "§9 l.450"
provenance_class: INTERPRETIVE (L3) — "compatible with intermediate-velocity clouds"
scientific_importance: "H3 framing; must not be encoded as measurement"
```

## 9. Temporal/beam provenance

```yaml
parameter: observation_datetime
section: "§4 l.175; Table 4 l.423"
value_locator: "1977 Aug 15 22:16:06 EST (= Aug 16 03:16:06 UTC); previous 22:16:01 EST"
underlying_data: "printout EST column (12 s cadence, 10 s integration + 2 s processing); sidereal-clock correction from Gaussian fit (time corrected only for Wow, l.179)"
provenance_class: [TRANSCRIBED_ARCHIVAL → RECONSTRUCTED]
independent_reproduction_possible: "YES from frozen EST column + fit"
known_conflict: "project has no datetime entry → NEW"
scientific_importance: "HIGH — geometry, velocity transforms, ephemeris queries"
---
parameter: apparent_duration
section: "Table 4 l.427; §5 l.196"
value_locator: "≥ 73.4 ± 0.5 s (previous: ≥ 72 s) — derived from Gaussian fit assuming 8′ RA beamwidth"
provenance_class: DERIVED + CENSORED_OR_BOUNDED (beam-geometry quantity — NOT intrinsic duration)
directive_guard: "72-s quarantine rule (A.6) preserved; paper's own '≥' censoring is consistent with it"
independent_reproduction_possible: "YES from fit width × beam"
scientific_importance: "MEDIUM (observational operator input, H2)"
---
parameter: beam_and_horn_geometry
section: "§1 l.101 (horns E/W, ~3 min); §5 l.196 (8′ RA beamwidth); §6 l.207–209 (ON/OFF scheme, 1415 MHz 8 MHz continuum receiver)"
value_locator: "beamwidth 8 arcmin RA; horn separation ~3 min (≈128–155 s squint-related — see §7); dec beam ≈ ±20′ scale"
provenance_class: [SECONDARY (Ehman) + CALIBRATED (paper)] — full 2-D beam response NOT published
independent_reproduction_possible: "PARTIAL — no beam map; Big Ear observation operator remains incomplete (H2 stays partially locked)"
scientific_importance: "CRITICAL for H2; source-size constraint"
---
parameter: source_angular_extent
section: "§5 l.196; fig:wowfit caption l.192; Table 4 l.434"
value_locator: "≤ 1.9 ± 0.1 arcmin (assumes 8′ beam)"
provenance_class: DERIVED + CENSORED_OR_BOUNDED
scientific_importance: "HIGH for H3 (cloud angular size prior)"
```

## 10. HI/DSR provenance (Layer 3)

```yaml
item: Wow2_and_Wow3_HI_cloud_signals
paper: 2508.10657 v1
section: "§7 l.285–313; figs wows/wowsprofile (l.287–311); §9 l.452"
content: "Jan 1978 narrowband signals, circled by Ohio SETI team; confirmed against HI4PI as compact HI clouds; used to validate channel-inversion correction (VLSR ≈ 0 alignment)"
provenance_class: [ORIGINAL_ARCHIVAL (printout marks) → RECONSTRUCTED (frequencies) → MODEL_DEPENDENT (HI association)]
access: "underlying Jan 1978 frames are in the N50CH archive (naapo.org, currently unreachable); paper's transcription not public"
scientific_importance: "HIGH — validation cornerstone of frequency reconstruction; analog population for H3 (mini-Wow context from Wow! I complements this)"
---
item: HI4PI_usage
section: "§7 l.299–313; fig:wowmap; §9 l.450"
method: "coordinate lookups + velocity-profile/brightness-temperature comparison (Aladin/HI4PI)"
provenance_class: DERIVED/MODEL_DEPENDENT (L3)
independent_reproduction_possible: "YES — public survey; deferred to H3 track per §0.9 discipline"
---
item: DSR_emission_hypothesis
section: "§10 l.460 (cites mendez2024arecibo = Wow! I, frozen)"
provenance_class: INTERPRETIVE (L3) — feasibility physics lives in Wow! I; population inference is OUR future work, explicitly ≠ P(D|H3)
---
item: commented_distance_row
section: "TeX l.433 (commented): 'Distance 1.5±1.4 kpc'"
note: "a distance estimate exists in the paper's revision history but was removed from the printed table — treat as UNVERIFIED/in-flux; do not use"
provenance_class: MODEL_DEPENDENT (superseded within v1)
```

## 11. Repository-version conflicts (unresolved, preserved)

1. **Flux calibration**: Ohio-SETI v0a `FLUX` (54 Jy Ehman-legacy assumption) vs paper ≥256±63 Jy — repo flux is LEGACY_SUPERSEDED; SNR arrays unaffected.
2. **README citation age**: "(2024) Arecibo Wow! II (in preparation)" vs frozen v1 (2025-08-14).
3. **PHL web Table 1**: self-declared outdated; never evidence.
4. **`awowi-v1.tex` inner filename** inside arXiv v2 tarball — documented, not "fixed".
5. **Existing project values pending reconciliation** (see §14): ≥250 Jy vs ≥256±63; SNR 30.5 vs 30.1±0.4; 72 s vs ≥73.4±0.5 s; no velocity entries.
6. **Paper-internal wording variance (new)**: abstract "exceeding 250 Jy" (l.86) vs Table 4 "≥256±63 Jy" (l.430) vs §9 "over 250 Jy" (l.446). Extraction rule: Table 4 + §6 equation are definitive; wording variance documented.
7. **TeX-internal revision rows (new)**: commented-out flux row "≥249 +77/−48 Jy" (l.429) and commented "Distance 1.5±1.4 kpc" (l.433) — author-internal evolution inside v1; do not use commented values as evidence.
8. **repo .sav coordinates (v0a-era) vs paper v1 positions** — cross-check required in Phase C; do not assume identity.

## 12. Missing Big Ear evidence (explicitly inaccessible today)

- N50CH full archive frames (Aug 13–17 1977 surrounding days; Jan 1978 Wow2/Wow3): paper says hosted on **naapo.org** (69 GB JPG) — site unreachable at 2026-08-22; re-verify before Phase C. *(This corrects the Phase 0 inventory claim that no printout archive was publicly hosted — amendment appended to `big_ear_archive_inventory.yaml`.)*
- The authors' own Aug 13–17 1977 transcription/OCR output files — not published (only the single Wow page via repo).
- Aug 16 1977 continuum strip chart (empirical squint + noise-tube calibration evidence) — private (Childers).
- IBM 1030 N50CH code + emulator runs — not public.
- PHL Big Ear Archive (documents, logs, engineering reports, Kraus/Dixon/Ehman papers) — public release August 2027.
- Original FITS — confirmed nonexistent (Méndez statement; README promised FITS "will be included", still absent).
- Full 2-D beam map/horn response — never published → Big Ear observation operator remains incomplete (H2).

## 13. Independent-reproduction opportunities (Phase C candidates, ranked)

| Rank | Target | Inputs available? | Expected tolerance |
|---|---|---|---|
| 1 | Frequency chain (f_c, f_n, 1420.726±0.005) | frozen repo 2LO column + paper equations | exact to channel grid |
| 2 | Flux arithmetic chain (σ_cnt→σ_channel→S≥256±63) | paper constants + repo SNR fit | exact arithmetic; SNR fit itself statistical |
| 3 | Gaussian beam fit (SNR 30.1±0.4, RA, extent ≤1.9′, duration ≥73.4 s) | frozen repo SNR rows | statistical (fit-implementation dependent) |
| 4 | VHEL/VLSR via astropy | frozen freq/position/time | km/s-level; document solar-motion convention |
| 5 | Transcription diff (Hotaling vs Ohio-SETI vs paper) | both frozen | exact |
| 6 | Position corrections (~27 s, squint 128±3 s) | paper constants + frozen times | partial — empirical squint data not public |
| 7 | RFI/EVT sanity checks ((1/32)^6 argument, Eq. 2) | paper-stated logic | independent recomputation |
| 8 | OCR reproduction from raw NAAPO frames | **blocked** — archive unreachable | n/a until re-verified |

## 14. Existing-project values requiring reconciliation (`research/data/wow_observation.yaml`)

| Project entry (current) | Arecibo II locator | Status |
|---|---|---|
| frequency 1420.726 MHz ±5 kHz (abstract) | Table 4 + §7 equations | CONFIRMED (upgrade locator from abstract → Table 4/equations; verify uncertainty semantics) |
| flux_density ≥250 Jy (abstract) | Table 4 "≥256±63" | CHANGED pending reconciliation (250 was abstract wording; 256±63 is the table+equation value; both censored) |
| snr 30.5±0.5 ("Méndez 2024 §II") | Table 4: 30.5±0.5 is the **previous (Ehman 1998)** value; new = 30.1±0.4 (fig:wowfit) | CHANGED — provenance now clear |
| bandwidth ≤10 kHz (Wow I) | §7: 10 kHz channel (also commented Table 4 row) | keep; re-verify against Wow! I v2 |
| beam_crossing_duration 72 s (Kipping) | Table 4: ≥73.4±0.5 s | CHANGED (both beam-geometry, censored; 72-s quarantine intact) |
| horn_turnon_window 180 s | §1: ~3 min horn interval (squint 128–155 s) | AMBIGUOUS — three related quantities (3 min interval, 180 s window, 128±3 s squint) must be kept distinct |
| sky_candidates RA/dec (abstract-level) | Table 4 horn-labelled rows incl. dec seconds (−26:57:18 / −26:57:13) + Galactic coords | CHANGED/NEW detail |
| (no datetime) | Table 4: 22:16:06 EST / 03:16:06 UTC | NEW |
| (no velocity) | VHEL −84±1, VLSR −74±2 | NEW |
| (no source size) | ≤1.9±0.1′ | NEW |

No project file was modified — reconciliation happens in Phase A/B after authorization.

## 15. Phase-A extraction sequence (proposed)

1. §2+§3: archive/transcription map completion (historical inputs table above → `mendez_paper_extraction_checklist.md` §C).
2. Table 4 verbatim → checklist §A rows (all locators already pinned above).
3. §6 Flux (equations + censoring semantics) → checklist §A flux rows.
4. §7 Frequency (corrections + equations) → checklist §A frequency rows.
5. §5 Location (corrections, uncertainties, horns) → checklist §A position rows.
6. §4 Time (EST/UTC, cadence) → checklist §A temporal rows.
7. §8 Alternatives → H1 source-backed components (RFI probability argument, harmonics table, satellites, solar, EVT).
8. §9 Wow2/Wow3 + HI4PI statements → checklist §D (L3, interpretive labels).
9. Build `research/data/mendez_evidence_vector.yaml` (Phase A.2) → `historical_vs_arecibo_parameters.csv` (A.4).
10. Freeze vector → Phase C reproduction per §13 ranking.

## 16. Scientific risks

1. **Flux censoring semantics**: "≥256±63" mixes a bound with a symmetric error — the paper's exact statistical meaning (bound on expectation? quantile?) is not formally defined (l.274–279 reasoning is verbal). Risk of referee attack; must be encoded as censored with documented ambiguity.
2. **Calibration constants not fully public**: noise-tube SNR 8.0±1.8 and S_ntube 9.4 Jy are paper-stated, not data-derived publicly; strip chart is private → flux chain reproducible only to paper-stated constants.
3. **Empirical squint 128±3 s** derives from a private strip chart; position correction chain partially unverifiable.
4. **v0a repo vs v1 paper coordinate drift** (conflict 8): if .sav corrected coords differ from Table 4, must not mix generations.
5. **NAAPO archive unreachability** blocks OCR-level independent verification (and the surrounding-days noise characterization) until access is re-established.
6. **Velocity convention ambiguity** (VLSR solar-motion convention unstated) — small but attackable.
7. **Paper III signal**: a concurrent broadband transient is teased in commented text (l.92); if published, it may revise the evidence base — version monitoring required.
8. **Duration/72-s**: any accidental slip into "the signal lasted 72/73.4 s" language would resurrect the quarantined interpretation.

---

**GATE: Phase A NOT started. No evidence, model, or manuscript files modified. Awaiting explicit authorization.**
