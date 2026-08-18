# AGENT BRAIN v2 — Domain Knowledge, Citation Ledger & Operating Protocol
## Wow! Signal Multi-Hypothesis Bayesian Assessment & Comparative Technosignature Census

> **VERSION NOTE:** This supersedes `AGENT_BRAIN.md` (v1). v1 was run through a comprehension-check session (see `implementation_plan_wow.md`) which independently verified most claims against primary sources, found several errors in v1, and flagged four items for human decision. All corrections and decisions are incorporated below, with a changelog at the end. **Use this file, not v1, going forward.**

**Read this file in full before doing any work.** Where anything here conflicts with your own training-data recollection, this file wins — and where this file flags something `UNVERIFIED`, treat it as unknown, not true.

---

## 1. Project Summary

Two independent undergraduate researchers are formally comparing five published explanations for the 1977 "Wow!" Signal using a Bayesian model-comparison framework, grounded in a systematic census of comparable technosignature events. Output: code, data, two manuscript drafts. See `PRD.md` for full requirements.

---

## 2. Domain Knowledge Base

### 2.1 Core facts about the signal itself
- Detected August 15, 1977, by the Big Ear radio telescope (Ohio State University).
- Named for Jerry Ehman's "Wow!" annotation on the printout sequence "6EQUJ5."
- Frequency at the neutral hydrogen line: **1420.726 ± 0.005 MHz** (Méndez et al. 2025 revised value — supersedes the older ~1420.4 MHz figure commonly cited pre-2025).
- Detected in only one of Big Ear's two feed horns (combined into a single data stream) — the "two-horn problem."
- Never repeated in any subsequent search across five decades.
- Jerry Ehman died in 2025.

### 2.2 The five hypotheses — corrected parameter table

| ID | Hypothesis | Verified parameters | Status |
|---|---|---|---|
| H1 | Instrumental / RFI | No confirmed 1977 local interference source; Méndez et al. (2025) judged instrumental/software error unlikely given the clean Gaussian rise/fall | `RE-CHECK exact wording in full PDF` |
| H2 | Cometary hydrogen emission (266P/Christensen, P/2008 Y2 Gibbs) | Positional mismatch (~3° dec, ~47 min RA) vs. Big Ear's ~3-min beam window; Paris & Davies (2017) report a candidate 1420.25 MHz signal from 266P/Christensen over 200 observations, Nov 2016–Feb 2017 (frequency is close to but not identical to Wow!'s 1420.726 MHz) | Treated as **near-refuted validation control** — see §2.4 |
| H3 | Interstellar hydrogen cloud / stimulated maser flare | Flux **exceeds 250 Jy** (verified lower bound, not "≈250 Jy" — correct this) at 1420.726 ± 0.005 MHz; two candidate positions (RA 19ʰ25ᵐ02ˢ±3ˢ or 19ʰ27ᵐ55ˢ±3ˢ, Dec −26°57′±20′ J2000); "mini-Wow" analogs in 2020 Arecibo data are ~2 orders of magnitude weaker, bandwidth 10 kHz | H3 core numbers VERIFIED (Méndez et al. 2025 abstract); mini-Wow detailed flux/position values still need the Méndez (2024) full PDF |
| H4 | Artificial interstellar power beam (leakage) | Worked example EIRP = **10¹⁷ W** (not 10¹⁸ — corrected) from Benford, Benford & Benford (2010a), with full cost-optimization equations available in the same paper and its companion (2010b) for independent re-derivation; bandwidth argument (<10 kHz, physics-forced by high-gain beaming) confirmed in Benford (2025) | VERIFIED via open-access 2010 papers — see Citation Ledger |
| H5 | Stochastic repeating ETI beacon | Initial MAP likelihood **32.3%** (not "~33%" — use exact figure); drops to **1.78%** after incorporating 192 hours of non-detection from **META + Hobart + ATA** (not VLA — VLA/Gray & Marvel is a separate, earlier campaign); tension level **2.4σ**; 2σ credible interval on duration: 72 s < T < 77 min; repeat rate: 0.043–59.8 day⁻¹; ~62 additional days of observation would be needed to reach 3σ | VERIFIED (Kipping & Gray 2022 abstract) |

**Non-detection campaigns (shared evidence, §2.4):**
- Gray & Marvel (2001, VLA) — ~1 hr, flux limit ~20 mJy, rules out continuous source brightening by factor <~100.
- Gray & Ellingsen (2002, Hobart 26m) — ~14 hr, flux limit ~18 Jy, rules out periodic repetition ≤14 hr at ≥18 Jy.
- Harp et al. (2020, ATA) — ~100 hr, 10.2 MHz bandwidth, rms ~1.25 Jy, 99% of repetition rates 0–40 hr would have been detected.
- **META** (Horowitz et al. 1986) + Hobart + ATA, 192 hr pooled — this is the specific dataset behind Kipping & Gray's 1.78% figure.
- **Perez et al. (2022)** — first *targeted* search (not blind field survey), GBT + ATA simultaneous, 580 s overlap, May 21 2022, target: 2MASS 19281982-2640123 (Caballero 2022's candidate Sun-like star, ~1,800 ly, Sagittarius). No technosignature candidates detected.

### 2.3 The four methodological pillars — corrected

1. **Lingam et al. (2023), *ApJ* 943:27.** Master equation **confirmed from full text** (Eq. 6):
 $$P(T \mid D, C) = \frac{P(T \mid C) \cdot \xi}{1 + P(T \mid C)(\xi - 1)}$$
 Ambiguity ratio (Eq. 5): $\xi = \dfrac{P(D \mid C, T)}{P(D \mid C, \bar{T})}$
 Worked examples from the paper: EM signals ξ~10⁴, NO₂ atmospheric signature ξ~3, CFCs ξ~10⁴, physical artifacts ξ~10⁴. High ξ is necessary but not sufficient — posterior still depends on the prior P(T|C). **This is a closed-form expression — no MCMC required for the base calculation**, confirming the PRD's preference for a simple closed-form approach first.

2. **Sheikh (2020), arXiv:1908.02683.** Nine axes confirmed, in order: Observing Capability, Cost, Ancillary Benefits, Detectability, Duration, **Ambiguity**, Extrapolation, Inevitability, Information. **Critical, verified caveat directly from the paper:** the axes are explicitly qualitative and designed for comparing *search strategies*, and the paper states outright that they "cannot be used as a quantitative measure" in their original form.
 **RESOLVED METHODOLOGY (human decision, supersedes v1's open question):** use ξ (Pillar 1) as the quantitative proxy specifically for the ambiguity axis. For detectability and duration, build and document your own transparent ordinal rubric (e.g. 1–5 scale with explicit per-point criteria), stated plainly in the methods section as *your extension* of Sheikh's framework for cross-event numeric comparison — not something Sheikh's paper itself claims to support. This resolution is final; do not revisit without flagging a specific new problem with it.

3. **Kipping & Gray (2022), arXiv:2206.08374 / MNRAS 515(1):1122–1129.** Your validation benchmark — see §2.2 H5 for the exact, verified figures. Note the paper also cites Kipping (2021) as a prior general framework for one-off event analysis, explicitly noted as insufficient alone because Big Ear's data is sparse and irregularly sampled — Kipping & Gray built a dedicated emulator for this reason. Worth reading if your own model needs to handle irregular sampling.

4. **Sheikh et al. (2021), *Nature Astronomy*.** BLC1 verification framework, 10 steps, fully confirmed. BLC1 parameters: ~982 MHz, Parkes 64m, UWL receiver 0.704–4.032 GHz, observed 2019-04-29 to 2019-05-04, 26h9m total, drift rate median 0.021 Hz/s. Final determination: an electronically drifting intermodulation product of local, time-varying terrestrial interferers — i.e., confirmed RFI, not a technosignature. Useful direct analog for structuring your H1 likelihood.

### 2.4 The Benford correction — hard rule, unchanged from v1
Non-detection data updates a shared rarity/rate nuisance parameter common to all hypotheses. It does not, by itself, discriminate between H3/H4/H5. Implement accordingly.

### 2.5 Census candidate events
- Wow! Signal, 1977.
- "Mini-Wow" events, Méndez et al. (2024), 2020 Arecibo data (bandwidth 10 kHz, ~2 orders of magnitude weaker than Wow!; full flux/position values still pending full-PDF fetch).
- BLC1, 2019, confirmed RFI (Sheikh et al. 2021) — useful as a second validation-style control event (expect near-zero ambiguity/ξ once resolved as RFI).

### 2.6 Glossary
(unchanged from v1 — see below if needed)
- **ξ (xi):** ratio of P(data | technological cause) to P(data | non-technological cause).
- **Bayes factor:** ratio of marginal likelihoods comparing two hypotheses.
- **Posterior odds:** prior odds × Bayes factor.
- **EIRP:** Effective Isotropic Radiated Power.
- **Jansky (Jy):** unit of spectral flux density.
- **MAP:** Maximum a posteriori (the peak/mode of a posterior distribution) — relevant to the Kipping & Gray 32.3%/1.78% figures, which are MAP likelihoods, not full posterior probabilities. Keep this distinction precise when building your own validation check.

---

## 3. Citation Ledger — corrected and expanded

Status key: **VERIFIED** = confirmed reachable and content-matched (by this project's own comprehension-check session or this update). **RE-CHECK** = believed correct, needs re-confirmation against full primary text before use.

| Citation | Link | Status |
|---|---|---|
| Ehman, "Big Ear Wow! Signal (30th Anniversary Report)" | http://www.bigear.org/Wow30th/wow30th.htm | VERIFIED |
| Gray & Marvel (2001), *ApJ* 546:1171 | https://doi.org/10.1086/318272 | VERIFIED (params confirmed) |
| Gray & Ellingsen (2002), *ApJ* 578:967 | https://doi.org/10.1086/342646 | VERIFIED (params confirmed) |
| Harp et al. (2020), *AJ* 160:162 | https://doi.org/10.3847/1538-3881/aba58f | VERIFIED (params confirmed) |
| **Horowitz et al. (1986), *Icarus* 67:525** — Project META, primary reference | (no free online copy located yet — library/DOI lookup needed) | RE-CHECK — needed for full validation-gate reproduction |
| **Perez et al. (2022), *RNAAS* 6(9):197** | https://doi.org/10.3847/2515-5172/ac9408 (open access) | VERIFIED — newly added, resolves v1 gap |
| Paris & Davies (2017) | https://arxiv.org/abs/1706.03259 | VERIFIED — parameters extracted |
| NAAPO comet-hypothesis rebuttal | http://naapo.org/WOWCometRebuttal.html | VERIFIED |
| Kipping & Gray (2022), *MNRAS* 515(1):1122–1129 | https://arxiv.org/abs/2206.08374 ; https://doi.org/10.1093/mnras/stac1807 | VERIFIED — validation benchmark, exact figures in §2.2 |
| Caballero (2022), *IJA* 21(3):129–136 | https://doi.org/10.1017/S1473550422000015 | VERIFIED — stellar parameters cross-referenced via Perez 2022 |
| Méndez et al. (2024), "Arecibo Wow! I" | https://arxiv.org/abs/2408.08513 | VERIFIED |
| Méndez et al. (2025), "Arecibo Wow! II" | https://arxiv.org/abs/2508.10657 | VERIFIED — use this version's numbers, supersedes 2024 |
| **Benford, Benford & Benford (2010a), "Searching for Cost-Optimized Interstellar Beacons," *Astrobiology* 10(5):491–498** | https://arxiv.org/abs/0810.3966 (open) | VERIFIED — **replaces** the paywalled 2021 JBIS note as H4's primary quantitative source |
| **Benford, Benford & Benford (2010b), "Messaging with Cost-Optimized Interstellar Beacons," *Astrobiology* 10(5):475–490** | https://arxiv.org/abs/0810.3964 (open) | VERIFIED — companion paper, full cost/EIRP/aperture equations |
| Benford (2021), *JBIS* 74:196–200 | Paywalled; blog summary at centauri-dreams.org/2021/01/22 | DEPRECATED as primary H4 source — use 2010a/b above instead; keep as historical context only |
| Benford (2025), "Beaming and Bandwidth" | https://www.centauri-dreams.org/2025/09/22/beaming-and-bandwidth-a-new-note-on-the-wow-signal/ | VERIFIED (bandwidth argument only, no new EIRP figure) |
| Sheikh (2020), arXiv:1908.02683 | https://arxiv.org/abs/1908.02683 | VERIFIED (full text) — see §2.3 caveat |
| Lingam et al. (2023), *ApJ* 943:27 | https://doi.org/10.3847/1538-4357/acaca0 | VERIFIED (full text, master equation confirmed) |
| Sheikh et al. (2021), *Nature Astronomy* | https://doi.org/10.1038/s41550-021-01508-8 | VERIFIED |

---

## 4. Operating Protocol — Anti-Hallucination & Reasoning Rules

Unchanged from v1 (18 rules) — reproduced in full in `AGENT_BRAIN.md` v1 if needed, and remain fully binding. Two additions based on what the comprehension-check session actually demonstrated was needed:

19. **Distinguish MAP likelihoods from posterior probabilities, precisely.** Kipping & Gray's 32.3%/1.78% are MAP likelihoods under a specific model, not full Bayesian posteriors. Do not conflate the two when building or describing your own validation check — this is exactly the kind of precise-sounding-but-wrong error rule 14 (confidence calibration) exists to catch.
20. **When a prior document (this one included) is found to contain an error, correct it visibly and note the correction's provenance** (which session/fetch found it), rather than just silently updating a number. This file's own version note at the top is the model to follow.

---

## 5. Repository / File Structure Convention
(unchanged from v1)

---

## 6. Communication Protocol Back to the Humans
(unchanged from v1)

---

## Changelog (v1 → v2)

| Item | v1 | v2 | Why |
|---|---|---|---|
| H5 non-detection campaigns | Implied VLA | META + Hobart + ATA | Verified against Kipping & Gray abstract; VLA is a separate campaign |
| H5 initial likelihood | "~33%" | 32.3% | Exact figure from source |
| H3 flux | "≈250 Jy" | "exceeds 250 Jy" | Paper states a lower bound, not an approximation |
| H3 frequency | "1420.726 MHz" | "1420.726 ± 0.005 MHz" | Added omitted uncertainty |
| H4 EIRP | "~10¹⁸ W," paywalled/unverifiable JBIS source | "10¹⁷ W" worked example, open-access 2010 Benford papers | Original figure unverifiable; found a better, open, more usable source |
| Perez et al. (2022) | Referenced, missing from ledger | Full citation + DOI added | Located via search |
| META primary source | Not identified | Horowitz et al. (1986), *Icarus* 67:525 | Located via search |
| Sheikh axis scoring | Open question | Resolved: ξ for ambiguity axis, custom documented rubric for others | Human decision, see §2.3 |
