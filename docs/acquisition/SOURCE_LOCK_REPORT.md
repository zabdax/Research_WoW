# SOURCE LOCK REPORT — Arecibo Wow! Evidence Reconstruction (Phase 0)

**Generated:** 2026-08-22 (UTC), by ZCode agent session executing the MASTER DIRECTIVE (Phase 0 — Source Lock).
**Machine-readable freeze record:** `research/sources/mendez_arecibo/metadata/source_manifest.yaml`
**Checksum file:** `research/sources/mendez_arecibo/hashes/SHA256SUMS.txt`
**Public-source inventory:** `research/data/mendez_public_sources.yaml`
**Archive inventory:** `research/data/big_ear_archive_inventory.yaml`
**Integrity tests:** `tests/research/test_mendez_source_lock.py` (7 tests, all passing)

---

> ## ⛔ GATE — Phase A is BLOCKED until human sign-off
>
> Per the project's tightened rule for §0.15 of the MASTER DIRECTIVE:
>
> *"Phase A does not begin until a human has explicitly reviewed and signed off on SOURCE_LOCK_REPORT.md in writing. Agent completion of the report is not sufficient authorization to proceed."*
>
> **Status: AWAITING HUMAN SIGN-OFF.** No paper parameter extraction, no evidence-vector edits, no model updates have been performed. The signed authorization block is at the end of this report.

---

## 1. Sources successfully acquired (frozen)

All artifacts live under `research/sources/mendez_arecibo/` (papers/, repositories/, extracted/, metadata/, hashes/). Bulk artifacts are local provenance copies (gitignored, mirroring the project's `data/sources_cache/` policy); manifests and hashes are git-tracked and authoritative.

### Primary paper (REQUIRED)

| Artifact | Version pinned | SHA-256 (first 16) | Notes |
|---|---|---|---|
| `papers/awow2_2508.10657v1.pdf` | **v1** (2025-08-14) | `ba87bc0b98518164` | 10 pages; byte-identical to earlier cache `data/sources_cache/mendez_2025.pdf` |
| `papers/awow2_2508.10657v1_eprint.tar.gz` | v1 | `d15a9d3dd5d4e4a3` | LaTeX source (top-level `awowii-v1.tex`), unpacked read-only under `extracted/` |
| `papers/awow2_2508.10657v1.html` | v1 | `2313853ec0e8fd63` | arXiv experimental HTML full text |

Title: **"Arecibo Wow! II: Revised Properties of the Wow! Signal from Archival Ohio SETI Data"** — Méndez, Ortiz Ceballos, Zuluaga, Palencia-Torres, Smith, Cardona Rodríguez, Socas-Navarro, Kipping, Hubbard-James, Le, Rincón-Torres. arXiv:2508.10657. DOI 10.48550/arXiv.2508.10657. License CC BY 4.0.

### Companion/supporting papers

| Artifact | Version pinned | SHA-256 (first 16) | Classification |
|---|---|---|---|
| `papers/awow1_2408.08513v2.pdf` | **v2** (2024-09-11) | `6c8cbc60c4323594` | USEFUL (mini-Wow analogs, instrument/SNR context; byte-identical to cache `mendez_2024.pdf`) |
| `papers/awow1_2408.08513v2_eprint.tar.gz` | v2 | `37c92e7f8b6d51fc` | USEFUL |
| `papers/ohio_seti_last_decades_2606.11102v1.pdf` | v1 (2026-06-09) | `4a8bd27a2876f054` | OPTIONAL ("The Ohio SETI Program — The Last Decades", Méndez/Dixon/Childers) |

### Code/data repositories (full clones, exact state preserved incl. `.git`)

| Repository | Commit (HEAD) | Branch | Cloned (UTC) | Tree | Classification |
|---|---|---|---|---|---|
| `planetaryhablab/Ohio-SETI` | `28624a1eaf955ced940db347684cee61c8e4fd61` | main | 2026-08-22T06:11:17Z | clean | REQUIRED |
| `MichaelHotaling/The-Wow-Signal` | `0b491d40d03337722254f70eb5f945ad8e181e1c` | main | 2026-08-22T06:47Z | clean | USEFUL |

No tags, no releases exist in either repository (GitHub API records frozen under `metadata/github_api_*.json`).

### Pre-existing cache cross-check (no re-download needed)
- `data/sources_cache/mendez_2025.pdf` ≡ frozen Wow! II **v1** PDF (hash-identical) — the 2026-08-18 cache was already v1.
- `data/sources_cache/mendez_2024.pdf` ≡ frozen Wow! I **v2** PDF (hash-identical).
- `data/sources_cache/awowi-v1.{tex,bib,bbl}` are the *inner filenames* of the arXiv **v2** tarball (author naming quirk), not arXiv version v1 — ambiguity resolved and recorded.

## 2. Sources not yet acquired (and why)

| Source | Status | Reason / plan |
|---|---|---|
| PHL **Big Ear Archive** full collection (logs, engineering reports, Kraus/Dixon/Ehman papers, printouts 1963–1998) | **NOT PUBLIC — scheduled release August 2027** (phl.upr.edu/wow/bigear, checked 2026-08-22) | Nothing to acquire yet; recheck near release; blocks independent inspection of surrounding Aug 1977 records |
| August 13–17, 1977 Big Ear printout scans beyond the Wow! row block | Not found publicly hosted anywhere | bigear.org hosts none; Ohio-SETI contains only the Wow! block |
| January 1978 "Wow2"/"Wow3" narrowband-signal records (cited in Wow! II figures) | Not in Ohio-SETI repo | To locate in Phase A (may be internal/unpublished) |
| 1994 Kraus→Sagan letter with continuum analog record (Wow! II figure input) | Not in public repo | Archival private correspondence; request or note as unavailable |
| HI4PI survey data | IDENTIFIED, deferred | H3-track acquisition (Phase E) once slice geometry/selection function is specified scientifically |
| NOAA NGDC 1977 sunspot/flare tables; ATNF/VLA calibrator lists; OCR tools (tesseract/OpenCV/IDL libs) | IDENTIFIED in paper source | Acquire on demand in Phase A/C as reproduction needs them (§0.9 discipline) |
| bigear.org pages beyond Wow30th (wow.htm, CSMO issues, survey menus) | MAPPED, not fetched | Optional historical context; fetch per-page with hashes when needed |
| naapo.org root | **UNREACHABLE at check time** (http/https timeouts 2026-08-22) | Cached rebuttal page exists from 2026-08-18; retry before Phase C |

## 3. Exact versions/commits — including the mandated arXiv & ApJ checks

### Arecibo Wow! II (arXiv:2508.10657) — the authoritative paper for this audit
- **arXiv version check (checked 2026-08-22, ~06:20 UTC):** only **v1** exists (submitted 2025-08-14T13:58:48Z). **No v2 or later found.** Method: arXiv abs page + arXiv API record (`metadata/arxiv_api_2508.10657.xml`).
- **ApJ status check (checked 2026-08-22):** **No evidence of ApJ acceptance or publication.** arXiv Comments field verbatim: *"To be submitted to ApJ after incorporating feedback"*; no journal-ref assigned. PHL project page (content "as of August 2026") still states *"The research will be submitted to the Astrophysical Journal."* Web search found no published ApJ version. Caveat recorded: an attempted Semantic Scholar API cross-check was rate-limited (HTTP 429); arXiv+PHL+search triangulation stands without it.
- **Consequence:** the evidence base is a **preprint v1**; `source_ledger.yaml` policy already forbids a preprint as sole confirmatory likelihood support. Any future v2/ApJ version triggers a **new source version**, not an in-place update.

### Arecibo Wow! I (arXiv:2408.08513)
- Versions: v1 (2024-08-16), **v2 (2024-09-11, latest)**; v2 frozen. Comments: *"22 pages, 8 figures, submitted to ApJ"*; no journal-ref as of check date; no ApJ acceptance found.

### Repositories
- Ohio-SETI: commit `28624a1eaf955ced940db347684cee61c8e4fd61` (branch main, clean). **Dataset version: v0a (2024-10-14)** — predates the Wow! II paper by ~10 months; no data-file changes since (README-only edits, last 2025-07-30).
- The-Wow-Signal (Hotaling): commit `0b491d40d03337722254f70eb5f945ad8e181e1c` (2022-07-20).

## 4. File hashes

Full list: `research/sources/mendez_arecibo/hashes/SHA256SUMS.txt` (19 artifacts, generated 2026-08-22T06:52:37Z). Per-source hashes are embedded in `metadata/source_manifest.yaml`; the Ohio-SETI per-file hashes are:

| File | SHA-256 (first 16) |
|---|---|
| `README.md` | `0bc93c2e3c21ebcb` |
| `oseti_19770815_220410.csv` | `84d623a489159ffc` |
| `oseti_19770815_220410.extended.pdf` | `50a6cc8a876fd87e` |
| `oseti_19770815_220410.jpg` | `3ca862b4cca91ce7` |
| `oseti_19770815_220410.sav` | `122cca196f7bf89a` |
| `oseti_19770815_220410.txt` | `52d0ec66dd6c5d96` |

`tests/research/test_mendez_source_lock.py` recomputes and verifies all of these on every test run — an upstream change to any local artifact will fail CI rather than pass silently.

## 5. Repository structure

### planetaryhablab/Ohio-SETI @ 28624a1 (6 files, ~1.5 MB)
```
README.md                        # dataset documentation, IDL SAV schema, v0a (2024-10-14)
oseti_19770815_220410.jpg        # scan of the original Wow! printout (1.3 MB)
oseti_19770815_220410.txt        # transcribed data, no header (82 rows)
oseti_19770815_220410.csv        # transcribed data, with header (50 channels + RA/Dec/2nd-LO/gal/EST)
oseti_19770815_220410.extended.pdf  # transcription + CNT and OBJECT (Ohio Sky Survey) fields
oseti_19770815_220410.sav        # IDL reanalysis arrays (corrected B1950/J2000 coords, MJD/LST,
                                 #   CFREQ, numeric SNR, FLUX, FREQ_CHAN(+VEL), OBJECT)
```
**Data-generation history (from git log — critical for preliminary-vs-final discipline):**
- 2024-10-08: initial upload `oseti.sav` + `wow.jpg` — **SUPERSEDED generation**, deleted 2024-10-14 (recoverable from git history if ever needed);
- 2024-10-14 (`db5c6e2`, "New data format."): the current five `oseti_19770815_220410.*` files; README version **v0a**;
- 2024-10-14 → 2025-07-30: README-only edits. **The public dataset has not changed since 10 months before the paper appeared.**
- README also promises "FITS format will also be included" — **no FITS file exists yet**.
- Transcription provenance acknowledged in README: upstream manual transcription by MichaelHotaling (cloned, verified: row-1 content identical to Ohio-SETI TXT/CSV).

### MichaelHotaling/The-Wow-Signal @ 0b491d4
```
README.md            # "Dataset Transcription from the August 15th, 1977 Big Ear Radio Transmission"
Wow! Signal.csv      # 82 rows × 50 channels + record columns (2022-07-20)
```

## 6. Relevant paper sections/tables/figures (structure only — values deferred to Phase A)

From frozen `awowii-v1.tex` (487 lines; AASTeX v7):

**Sections:** Introduction · **The Ohio SETI Data** · **Data Transcription** · **Time** · **Location** · **Flux Density** · **Frequency** · Alternative Explanations (Local RFI / Second Harmonic / Satellites and Space Probes / Solar Activity / Internal Artifacts) · Results and Discussion · Conclusion.

**Tables:** 4 `deluxetable` environments (parameter tables — exact contents to be enumerated with locators in Phase A).

**Figures (by caption):** Gaussian beam-profile fit of the Wow! signal (peak SNR stated in caption); HI4PI galactic H I column-density map with candidate Wow! positions; **continuum analog record from a 1994 Kraus→Sagan letter**; continuum SNR from the 50-channel output of 1977-08-15; Jan 1978 "Wow2"/"Wow3" narrowband signals; HI4PI velocity profiles/brightness-temperature maps for Wow2/Wow3.

**External resources cited in the TeX** (recorded for the Phase A source map): tesseract OCR, OpenCV, IDLAstro, Markwardt IDL library, Astropy, Aladin, HI4PI, ATNF calibrators, NRAO VLA calibrator list, NOAA NGDC 1977 sunspot + Hα flare tables, naapo.org, naic.edu.

## 7. Relevant repository files (roles in the provenance chain)

| File | Provenance layer (directive §3 categories) |
|---|---|
| `oseti_19770815_220410.jpg` | closest public surrogate of ORIGINAL_ARCHIVAL (scan of physical printout) |
| Hotaling `Wow! Signal.csv` | TRANSCRIBED_ARCHIVAL (manual, 2022) |
| `oseti_*.txt` / `oseti_*.csv` | TRANSCRIBED_ARCHIVAL (2024 reformat of transcription) |
| `oseti_*.extended.pdf` | TRANSCRIBED_ARCHIVAL + derived CNT/OBJECT fields |
| `oseti_*.sav` | CALIBRATED / RECONSTRUCTED (v0a-era assumptions — see §10 conflicts) |

## 8. Relevant historical archive files

Per `research/data/big_ear_archive_inventory.yaml` (mapped 2026-08-22, no bulk downloads): the only public historical artifacts are the six Ohio-SETI files and the Hotaling CSV (all frozen), plus the project's earlier cached Ehman 30th-anniversary report (`data/sources_cache/ehman_30th.htm`, hash recorded) and NAAPO comet-rebuttal page. **The full Big Ear Archive is not public until August 2027.**

## 9. Missing evidence (honest inventory)

1. **Surrounding August 13–17, 1977 records** — not public; needed for noise/null characterization; blocked until 2027 release (or author-provided access, which Méndez has stated does not exist beyond what is online).
2. **January 1978 Wow2/Wow3 records** and the **1994 Kraus→Sagan continuum letter** — cited by the paper, not in the public repo.
3. **Beam maps / two-horn engineering calibration for 1977** — still `archival/human-contact-required` per `research/data/acquisition_register.yaml`; the paper's Location/Flux sections may partially address this (Phase A will determine how much).
4. **FITS version of the dataset** — promised in README, absent.
5. **Topocentric/covariance ephemeris products** — unchanged from existing register limitations.
6. **Published (peer-reviewed) version of the papers** — both remain preprints.

## 10. Conflicting versions / ambiguities (documented, NOT silently resolved)

| # | Conflict | Status |
|---|---|---|
| 1 | **Flux calibration generations**: Ohio-SETI README (v0a) defines SAV `FLUX` as *"estimated flux density (Jy) [assuming max signal was 54 Jy]"*, while the directive cites the paper's lower-bound constraint ≈ **≥256 ± 63 Jy** (to be located precisely in Phase A) and the current project file uses **≥250 Jy** (abstract-level). | AMBIGUOUS until Phase A extracts the paper's exact flux semantics; **repository FLUX must not be substituted for paper flux** |
| 2 | README citation block: *"Arecibo Wow! II (2024) (in preparation)"* vs. actual arXiv v1 (2025-08-14) | README is v0a-era metadata; arXiv record wins |
| 3 | PHL `/wow/data` flags its own Table 1 *"(This table is outdated)"* and Gaussian-fit parameters *"still under refinement"* vs. frozen paper v1 | Web values are NOT evidence; paper v1 is the frozen authority |
| 4 | `awowi-v1.tex` inner filename inside the **v2** tarball | Naming quirk recorded; version identity comes from the arXiv tarball, not inner filenames |
| 5 | Project's `wow_observation.yaml` (SNR 30.5 from Wow! I §II; freq/positions from Wow! II abstract) vs. full-paper values (e.g., figure caption states peak SNR 30.1±0.4) | Reconciliation is Phase B work — **no project values were modified in Phase 0** |
| 6 | A "Paper III" is listed on the PHL page (August 2025, no URL); `2606.11102` (June 2026) is titled "The Ohio SETI Program — The Last Decades", not "Arecibo Wow! III" | Unresolved; monitor arXiv |

## 11. Preliminary provenance map (to be finalized in Phase A/B)

```
1977-08-15 physical Big Ear printout (OSURO; N50CH records)
        │
        ├─ scan: oseti_19770815_220410.jpg  (Ohio-SETI repo, 2024)          [scan layer]
        │
        ├─ manual transcription: Hotaling "Wow! Signal.csv" (2022)          [transcription layer]
        │       └─ reformatted: oseti_*.txt / .csv / .extended.pdf (2024)   [same layer + fields]
        │
        ├─ reanalysis arrays: oseti_*.sav (2024, v0a assumptions)           [calibrated/reconstructed layer]
        │
        └─ paper pipeline (arXiv:2508.10657 v1, 2025): OCR (tesseract/OpenCV)
           + coordinate/time reconstruction + frequency reconstruction
           + Gaussian-beam SNR fit + flux calibration                        [reconstruction layer]
                │
                ├── published tables/figures (4 tables, 6 figures)           [derived quantities]
                │
                └── external inputs: HI4PI, ephemerides/almanac, calibrator
                    lists, NOAA solar tables, 1994 Kraus letter, Jan-1978
                    Wow2/Wow3 records                                        [external catalogue layer]
                            │
                            ▼
        OUR route: Phase A extraction → Phase B evidence vector +
        historical comparison → Phase C independent reproduction
        (paper chain reproductions from the frozen repo files)
```

## 12. Recommended extraction order (Phase A, after sign-off)

1. §The Ohio SETI Data + §Data Transcription → enumerate archival inputs, OCR/transcription methodology, validation (directive §0.5 A–B).
2. §Time → observation date/time, timing uncertainty, duration interpretation (72 s quarantine rule stays in force).
3. §Location → horn RAs, declination, squint, pointing, coordinate frames/epochs, positional uncertainties.
4. §Flux Density → SNR, calibration constants, flux lower bound **with exact statistical semantics** (censoring rule).
5. §Frequency → channel, LO treatment, frequency reconstruction, reference frame.
6. §Alternative Explanations → paper's RFI/satellite/solar/artifact analyses (source-backed H1 components only).
7. §Results and Discussion + 4 tables → derived quantities with table/equation locators.
8. Then: `mendez_evidence_vector.yaml` (Phase B) → `historical_vs_arecibo_parameters.csv` → reproduction plan/module (Phase C).
Checklist scaffold: `docs/acquisition/mendez_paper_extraction_checklist.md` (all items PENDING, gated).

---

## Repository hygiene notes

- **No commits were made.** New/changed tracked files: `.gitignore` (added ignore rules for the frozen bulk artifacts, mirroring the `data/sources_cache/` policy), `research/data/mendez_public_sources.yaml`, `research/data/big_ear_archive_inventory.yaml`, `research/sources/mendez_arecibo/metadata/*`, `research/sources/mendez_arecibo/hashes/SHA256SUMS.txt`, `tests/research/test_mendez_source_lock.py`, this report, and the checklist. The pre-existing uncommitted edit to `manuscripts/rnaas_note.md` was left untouched.
- The two cloned repositories are kept in place with `.git` intact (exact-state preservation) and are gitignored — same convention as `data/kipping_wow_repo/`, never treated as submodules.
- `research/data/acquisition_register.yaml`, `docs/model_assumptions.md`, `docs/referee_attack_map.md` were **not** modified: per the directive's execution order those updates belong to Phase D, after extraction/reproduction.

---

## ✍️ HUMAN AUTHORIZATION — required before Phase A

I have reviewed this SOURCE_LOCK_REPORT.md (sections 1–12), the freeze manifest, and the conflict list in §10. I authorize Phase A (full-paper scientific extraction) to begin against exactly the frozen sources listed herein.

- Reviewed by: Zubayer Hasan Shaad
- Date (UTC): 22/8/2026
- Signature/statement: Shaad

Notes/conditions (optional): flag conflict #1 (flux calibration source) as the single highest-priority item for Phase A to resolve first, and flag Wow2/Wow3 as paper-sourced-only pending the 2027 archive release.

(Without this block completed in writing, Phase A must not start; the gate flag in `metadata/source_manifest.yaml` stays BLOCKED.)

---

### AUTHORIZATION RECORD (appended 2026-08-23 — visible addition; signed block above preserved verbatim)

Phase A was additionally and explicitly authorized in writing on **2026-08-23** via the "PHASE A — EXPLICIT AUTHORIZATION" directive. Scope and conditions:

1. **Part 1 (completed 2026-08-23):** NAAPO scope-note amendments appended to `research/data/big_ear_archive_inventory.yaml` and `research/data/mendez_public_sources.yaml`; NAAPO availability independently re-verified by the human (`argus.naapo.org/~rchilders/N50CH_data/scans/png/folder.wow/` + continuum strip-chart archive, both reachable; agent spot-check: server alive, directory listing 404, filenames unconfirmed → HUMAN_VERIFIED / AGENT_PARTIAL).
2. Extraction follows `SOURCE_EXTRACTION_MAP.md` §15 order; §9 HI/Wow2/Wow3 values tagged `SOURCE_VERIFICATION = PAPER_ONLY, NOT_INDEPENDENTLY_REPRODUCIBLE`.
3. Build + freeze `research/data/mendez_evidence_vector.yaml` and `research/data/historical_vs_arecibo_parameters.csv`; then Phase C reproduction limited to the **frequency chain** (genuine independent verification) and **flux arithmetic** (`ARITHMETIC_REPRODUCTION_ONLY` — paper-stated constants 9.4 Jy, 8.0±1.8).
4. Standing rules reaffirmed: flux stays censored; Table 4/equations authoritative over abstract; commented-out TeX values (≥249 +77/−48 Jy; 1.5±1.4 kpc) permanently excluded; no silent reconciliation; no five-way posterior; H2 ≤ partially unlocked; H3 modeling only after vector freeze; no orphan numbers.
5. **STOP condition:** after vector + CSV freeze and Phase C (frequency + flux), stop and report; no H1/H4/H5/H3-population/Bayesian work.

**Signer's conditions from the signed block above (binding on Phase A):** (a) conflict #1 (flux-calibration source) is the highest-priority item and is resolved first; (b) Wow2/Wow3 are flagged paper-sourced-only pending the August 2027 archive release.
