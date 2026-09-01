# Bob Gray — Evidence Summary Briefing (internal background for the contact)

Status: PREPARED (internal; for the human-led contact phase) · **DO NOT
SEND** · Companion: `bob_gray_email_draft.md`,
`bob_gray_remaining_requirements.md`, `bob_gray_do_not_ask_again.md`.

## 1. What we already hold

- The complete **donor-held** Mt Pleasant Hobart follow-up archive
  (Prof. Simon Ellingsen): 1998/99 one-bit autocorrelator products
  (122 `.fit.gz`, 1024-lag ACFs), the 2010 Jaekle RPFITS + 6,500 calibrated
  spectra, the 2013/14 RPFITS + 75,413 processed spectra, observing-plan
  workbook, logs, and READMEs — all SHA-256 frozen and inventoried.
- The high-level 1998/99 processing program (**MPSLPP** v1.8 source) and its
  partial user manual, as supplied by Simon.
- The published **Gray & Ellingsen (2002, ApJ 578:967–971)** paper, fully
  text-extracted from the frozen PDF.

## 2. What we have independently established

- Session↔file↔pointing mapping for every archived observation; measured
  5.0 s dump cadence (2013/14) and 33.8′–36.8′ beam FWHM (2010); the 2010
  calibration chain reproduced from archived artifacts alone.
- The 2013/14 fields correspond to the two documented Big Ear beam locales
  (deliberate B1950→J2000 conversions; plan workbook + Simon).
- The G&E 2002 paper's session list, DOYs, and instrument description match
  the archived 1998/99 material exactly.

## 3. What the published record (G&E 2002) establishes

The 1998/99 search: 6 × ~14 hr tracking runs at the two B1950 Wow locales
(±15′ coverage fields), 2.5 MHz band, 512 channels/polarization, 30 s
integrations, 5.9σ (P_e=0.05) single-channel thresholds (15.7–18 Jy),
Virgo A calibration, documented RFI screening and H i removal — and a
**published non-detection**, constraining periodic re-emission to periods
>14 hr (detection probability >0.90 up to ~20 hr at the nominal positions).

## 4. What remains genuinely missing

1. Any record of the **2010/2013/14 analysis layer**: thresholds, candidate
   rules, RFI handling, repeat criteria, outcomes — nothing survives in the
   donor-held material, and the 2002 paper predates those campaigns.
2. **1998/99 candidate-level data**: the paper describes two features; no
   complete candidate list was published or archived.
3. The **executed implementation** behind the published description:
   software version, exact parameters, and the processing
   subroutines/libraries (which Simon could not locate and which are
   referenced-but-missing from the supplied source).

## 5. Why these matter

Our project is recovering and independently auditing the observational,
instrumental, and **search-selection** evidence needed to determine whether
a quantitatively defensible statistical treatment of the Wow! follow-up
campaigns is possible. The published non-detection is a historical result;
turning it (or the later campaigns' records) into a defensible selection
function requires knowing what was actually executed and what the candidate
population actually was — not assuming either.

## 6. What material from Bob would be useful

Essential (P0): any surviving 2010/2013/14 search records (thresholds,
candidate lists incl. rejected items, outcomes — or confirmation that none
exist); 1998/99 candidate-level files; the executed processing
configuration.
High-value (P1): analysis scripts, calibration constants, RFI channel
masks/lists, missing MPSLPP subroutines/INCLUDE files or the Programming
Manual, Figure 3 source data.
Context (P2/P3): correspondence, notebooks, later re-analyses.

"Nothing survives" / "lost" is a genuinely useful, recordable answer. We do
not ask him to reconstruct decades-old work from memory, and we do not
assume any unpublished material is owed to us.
