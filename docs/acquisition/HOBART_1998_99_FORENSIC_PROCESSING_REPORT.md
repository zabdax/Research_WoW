# Hobart 1998/99 Forensic Processing Report (MPSLPP)

Status: **forensic; static analysis only; STOPPED before inference** ·
Date: 2026-08-29 · MASTER DIRECTIVE (2026-08-29) §27 ·
Companion: `research/data/ellingsen_fortran_inventory.yaml` (machine-readable),
`research/sources/ellingsen_hobart/analysis/fortran_dependency_map.json`,
`research/data/ellingsen_simon_response.yaml`.

## 1. Scope

Determine, by static analysis only, what the Simon-Ellingsen-supplied 1998/99
processing software and its partial documentation establish about the
historical data pipeline from correlator output to search/analysis product —
and where that pipeline is non-recoverable. No missing routine was
reconstructed; no search rule inferred; no calibration uncertainty invented;
no Bayesian quantity emitted (§32 stop conditions respected).

## 2. Newly supplied files

| File | Bytes | SHA-256 (first 16) | Donor description |
|---|---|---|---|
| `mpslpp.f` | 209,602 | `3274fe719b465825` | "the high-level fortran program" |
| `mpslpp.tex` | 20,311 | `09cd1e0217088800` | "some partial documentation" |

Received in workspace folder `reresearchdatarequestarchivalhobartfollowupobserv/`
(folder name as received from the owner). Simon's verbatim answer Q8 is the
provenance source for both.

## 3. Source preservation

Frozen read-only copies created under the existing archive architecture:

```text
research/sources/ellingsen_hobart/software/mpslpp.f
research/sources/ellingsen_hobart/documentation/mpslpp.tex
research/sources/ellingsen_hobart/hashes/SIMON_SOFTWARE_SHA256SUMS.txt
```

Originals untouched and hash-identical to the frozen copies (verified at
freeze time and re-verified by the test suite). Per repository policy the
copies are local-only; the hash manifest + inventories are the tracked
authoritative record. `scripts/ellingsen_fortran_inventory.py` regenerates all
derived artifacts deterministically and refuses to run on hash mismatch.

## 4. Fortran program inventory

- **Program name:** MPSLPP — Mt Pleasant Spectral Line Processing Package.
- **Source filename:** `mpslpp.f` (5,023 lines).
- **Language/version clues:** fixed-form Fortran 77-style (`integer*4`,
  `include`, RCS log); author **S P Ellingsen**, dated 19-JUL-1993,
  `version = 1.8`, `rel_date = '19-Jul-1995'`, RCS
  `$Id: mpslpp.f,v 1.8 1995/03/24 10:33:51 sellings Exp sellings $`.
- **Platforms (manual):** VMS ("physvax") and PC (Lahey Fortran + Phar Lap 386);
  SunOS port considered.
- **Main program:** `program mpslpp` (line 18).
- **Locally defined units:** exactly **two** — `mpslpp` and subroutine
  `extrtn` (line 4745). Everything else is called, not defined.
- **Called routines:** 71 distinct CALL targets.
- **COMMON blocks:** none found.
- **INCLUDE files:** `mpslpp.inc` (line 262), `headkey.inc` (263),
  `histkey.inc` (264), `mpslpp.def` (4781) — **none supplied**.
- **Declared EXTERNAL:** `extrtn`, `polynomial_curvefit`, `harmonic_curvefit`.
- **Key constants:** `maxlag = 1024` (lags), `maxspc = 40` (slots; manual
  v1.0 says 20), `maxifs = 2`, `cmax = 34` (menu commands), `maxord = 50`,
  `maxhis = 40`, `c = 2.99792458e5` km/s.
- **Command set (34):** LOAD, SPECSAVE, FLIST, FT, QUOTIENT, COPY, ADD, PLOT,
  PRINT, FIT, EDIT, SPAWN, SLIST, CLEAR, SETINFO, FITPOS, HISTORY, INTFLUX,
  RMS, PEAKS, GAUSFIT, GAUSCLR, GAUSSAV, MGF, GAUSIN, GAUSOUT, FTEST,
  VERSION, PEAKDB, OUTPLOT, MPSLHELP, EXIT, QUIT.

## 5. Documentation inventory

`mpslpp.tex` — "MPSLPP User Manual version 1.0", author line Simon Ellingsen,
LaTeX 2.09-era `\documentstyle[12pt,a4wide]{article}`. Documents: menu
operation; all commands (LOAD, SPECSAVE, FLIST, FT, QUOTIENT, COPY, FIT,
EDIT, SPAWN, SLIST, CLEAR, SETINFO, FITPOS, HISTORY, MPSLHELP, EXIT, QUIT);
menu parameters (ifile, ofile, ispec/rspec/ospec/ichan/ochan, automatic,
take, adjust, smoothing, ...). Key documented physics: correlator files store
observations **as autocorrelation functions**; with `automatic 'yes'` LOAD
Fourier-transforms and applies the **Van Vleck correction** (one-bit
sampling); **Hanning** smoothing may be applied **before** the transform;
quotient spectra via reference slots with Tsys `adjust` ∈ {None, Signal,
Baseline}; SPECSAVE stores data + header + processing **history** inside
`.fit`-format files. The manual references an **MPSLPP Programming Manual**
(not supplied).

## 6. Dependency map

73 dependencies mapped; classification per directive §12:

| Class | Count |
|---|---|
| FOUND | 0 |
| FOUND_PARTIAL | 0 |
| **REFERENCED_BUT_MISSING** | **73** |
| NOT_REFERENCED | 0 |
| UNKNOWN | 0 |

Library families identified from call signatures (all bodies missing):

| Family | Evidence | Role |
|---|---|---|
| CFITSIO (Fortran interface) | FTINIT, FTCRHD, FTPPH, FTBDEF, FTMAHD, FTPBNH, FTPKYS, FTMKYJ, FTPDAT, FTGCVD/VE/VJ/VS, FTCHKE, FTCLOS, FITSERR | reads/writes the correlator `.fit` files |
| SLALIB | SLA_CLDJ, SLA_GALEQ, SLA_PRECES | coordinate handling / precession |
| PGPLOT | PGASK, PGBBUF, PGEBUF, PGEND, PGPAGE | plotting |
| Dave McConnell menu software | MENU, OPENREAD, OPENWRITE, USER_WAIT, LIB$SPAWN, LOWCASE/UPCASE/NUMBER/THE/CLEAR_STRING | user interface (named in manual) |
| Numeric/analysis kernels | DOFFT, VANVLECK, HANNING, GAUSMOO, GAUFIT, SVDFIT, ANALYTICAL_FIT, GETRMS, INTFLUX, PEAKS, INDEXX, REVERSE | the "technical stuff" |
| Correlator I/O + display | READFIT, WRITEFIT, FITSERR, COPY_HEAD, CREATE_DET, DISPLAY, FITPOS, POSPLOT, LIST_FILES, ... | file in/out + display |

This **confirms the donor's statement** (Q8): the subroutines/libraries "are
where the technical stuff is located" — and none of them survive in the
supplied material.

## 7. Historical processing architecture (evidence-based)

```text
1998/99 correlator output            REPRODUCIBLE (122 .fit.gz in frozen archive)
        ↓
raw .fit.gz / ACF product            REPRODUCIBLE (1024-lag ACFs, COUNTS;
        ↓                             config metadata absent)
MPSLPP LOAD: readfit (CFITSIO)       DEPENDENCY_MISSING (kernel, line 603)
        ↓
Van Vleck one-bit correction         DOCUMENTED_ONLY (manual; kernel; 797/1246)
        ↓
optional Hanning smoothing           DOCUMENTED_ONLY (pre-FFT; kernel; 799/1248)
        ↓
DOFFT → power spectrum               DEPENDENCY_MISSING (kernel; 808/1256)
        ↓
QUOTIENT + Tsys adjust               DOCUMENTED_ONLY (None/Signal/Baseline)
        ↓
SPECSAVE → .fit + history ext.       DOCUMENTED_ONLY (format described)
        ↓
search/analysis product              UNKNOWN (no artifact/rule/record survives;
                                      attributed to Bob Gray per donor)
```

Reproducibility labels per §13. The 5 s dump timing is donor-supported, not
independently measured (GAP-HOB-014).

## 8. `.fit.gz` data interpretation

**CONTAIN (established, three independent lines of evidence):** 1024-lag
autocorrelation functions per polarization, FITS binary-table extensions with
unit COUNTS — (i) header audit (`analysis/data_fit_index.json`), (ii) MPSLPP
manual ("store the observations as autocorrelation functions"), (iii) source
parameter `maxlag = 1024` matching the archived dumps.

**NOT directly:** already-transformed spectra (LOAD's `automatic`/FT would be
pointless otherwise), power spectra, or calibrated flux (COUNTS units; no
calibration chain archived). **Multiple polarizations:** yes (2 linear).

**UNRESOLVED:** lag→channel mapping, bandwidth, window convention,
frequency/velocity reference, embedded normalization — file headers carry no
such metadata and the defining kernels are missing.

## 9. Mathematical transformations identified

Named and located, **not recoverable in executable form**: Van Vleck one-bit
correction (manual; call sites 797, 1246); Hanning pre-FFT smoothing (799,
1248); FFT lag→spectrum (DOFFT, 808, 1256); Gaussian smoothing (GAUSMOO,
2215); SVD polynomial/harmonic baseline fit (SVDFIT, 2264/2268); Gaussian
component fitting (GAUFIT, 3567/3589); 2-D Gaussian position fitting
(FITPOS/ANALYTICAL_FIT; manual §FITPOS). Only the manual's FIT defaults
(width=20, padding=5, linear=0.02) are recoverable; no window/lag conventions
are.

## 10. Missing software / dependencies

Per the frozen dependency map (73/73 `REFERENCED_BUT_MISSING`):

- Kernels: `readfit`, `writefit`, `vanvleck`, `dofft`, `hanning`, `gausmoo`,
  `gaufit`, `svdfit`, `analytical_fit`, `getrms`, `intflux`, `peaks`, ...
- INCLUDE files: `mpslpp.inc` (slot/header data structures), `headkey.inc`
  (FITS header keyword map), `histkey.inc` (history keyword map),
  `mpslpp.def` (menu parameter definitions).
- Libraries: CFITSIO Fortran interface, SLALIB, PGPLOT, Dave McConnell's
  menu software.
- Documents: MPSLPP Programming Manual (referenced twice in the user manual).
- Donor status (Q8): "I can't quickly find any of the
  subroutines/librariries which are where the technical stuff is located."

No missing routine has been reconstructed or guessed (§12, §32.1).

## 11. Reproducibility assessment

| Reconstruction | Status | Basis |
|---|---|---|
| Data-product layer (`.fit.gz` files as archived) | REPRODUCIBLE (held) | frozen archive + inventories |
| ACF → power-spectrum conversion | PARTIALLY_REPRODUCIBLE at best; currently DEPENDENCY_MISSING | architecture + Van Vleck/Hanning/FFT semantics documented; kernels + conventions missing |
| Instrumental interpretation of converted spectra | DOCUMENTED_ONLY | bandwidth/frame/lag mapping unresolved (GAP-HOB-012) |
| Absolute calibration (1998/99) | UNKNOWN | no calibration chain archived or documented |
| Historical search selection function | NOT ESTABLISHED | threshold/RFI/candidate rules attributed to Bob Gray; not recovered |
| Historical search outcome | NOT ESTABLISHED | no candidate/outcome record survives donor-side (Q6) |

## 12. Calibration implications

The surviving software documents a quotient/Tsys-adjust workflow
(None/Signal/Baseline) but no absolute-flux chain for 1998/99; COUNTS-unit
ACFs and absent calibrator documentation leave the 1998/99 era without an
absolute scale. The 2013/14 "Jy" scale remains
`PROVISIONAL / DONOR-LIMITED` (donor-stated ≈50% qualitative accuracy —
**not** a Gaussian σ; GAP-HOB-010/011). Nothing here promotes any
evidence layer, and the Arecibo/Méndez flux evidence vector is untouched.

## 13. Search-layer implications

`raw-data processing ≠ candidate search`. Even a complete software
reconstruction would not recover: detection threshold, S/N criterion, RFI
rejection, baseline criteria, candidate inspection, persistence/repeat
criteria, candidate rejection, search completeness, or the outcome list.
That layer is attributed to Bob Gray by the donor and is the subject of
`bob_gray_information_requirements.md` (P0/P1). **No non-detection is
inferred.**

## 14. Scientific limitations

1. The 1998/99 `.fit.gz` files cannot currently be converted to spectra with
   historically validated conventions (kernel + config missing).
2. Even if converted, absolute calibration would remain unavailable.
3. The historical search/analysis record is not in the surviving
   donor-held material; its recoverability depends on Bob Gray.
4. The manual is v1.0 (20 slots) while the source is v1.8 (40 slots) —
   version skew exists; the executed campaign version is unknown (Bob Gray
   P2 question).
5. Donor recollections (correlator generations, "other ideas") are context,
   not observational fact.

## 15. Recommended next action

1. Human review of this report and the status matrix.
2. (Authorized contact only) Bob Gray round using
   `bob_gray_information_requirements.md` — P0 search outcome first; P2
   software version/missing routines second.
3. If kernels or the Programming Manual are recovered: extend this static
   inventory, never guess; validate any reconstruction against the archived
   `.gsf.gz` diagnostics only as a cross-check of *format*, not of science.
4. Meanwhile: no H5 work; GAP-HOB-012 remains TECHNICALLY_OPEN.

---

### Reproducibility artifacts produced this phase

| Artifact | Producer |
|---|---|
| `analysis/fortran_dependency_map.json` | `scripts/ellingsen_fortran_inventory.py` |
| `research/data/ellingsen_fortran_inventory.yaml` | `scripts/ellingsen_fortran_inventory.py` |
| `hashes/SIMON_SOFTWARE_SHA256SUMS.txt` | freeze step (re-verified by script + tests) |
| `research/data/ellingsen_simon_response.yaml` | donor-response freeze |
| `tests/research/test_simon_response_and_fortran.py` | verification suite |

Originals under `original/` and in the donor-supplied folder remain
byte-for-byte unchanged (verified by the test suite).



