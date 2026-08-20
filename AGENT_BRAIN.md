> **DEPRECATED**: This document contains known errors. Refer to `AGENT_BRAIN_v2.md` instead.

# AGENT BRAIN — Domain Knowledge, Citation Ledger & Operating Protocol
## Wow! Signal Multi-Hypothesis Bayesian Assessment & Comparative Technosignature Census

**Read this file in full before doing any work.** This document is your ground-truth reference and your binding operating protocol. Where anything in this file conflicts with your own training-data recollection of a fact, figure, or citation, **this file wins** — and if this file itself flags something as `UNVERIFIED`, treat it as unknown, not as true. If you are running inside Claude Code, consider saving this file's content (or an import of it) into your project's `CLAUDE.md` so it loads automatically every session — see §6.

---

## 1. Project Summary

Two independent undergraduate researchers are formally comparing five published explanations for the 1977 "Wow!" Signal using a Bayesian model-comparison framework, grounded in a systematic census of comparable technosignature events scored against a published taxonomy. The output is code, data, and two manuscript drafts. See `PRD.md` for full requirements — this file exists to give you the facts and the discipline needed to execute that PRD correctly.

---

## 2. Domain Knowledge Base

### 2.1 Core facts about the signal itself
- Detected August 15, 1977, by the Big Ear radio telescope (Ohio State University), a fixed meridian-transit instrument.
- Named for Jerry Ehman's handwritten "Wow!" annotation on the printout sequence "6EQUJ5."
- Frequency near the 1420.4 MHz neutral hydrogen line.
- Detected in only one of Big Ear's two feed horns (the horns' outputs were combined into a single data stream), leaving genuine ambiguity about the precise sky position — this is called the "two-horn problem" throughout this project's documents.
- Never repeated in any subsequent search, across five decades of follow-up observation.
- Jerry Ehman died in 2025.

### 2.2 The five hypotheses under comparison

| ID | Hypothesis | Key published parameters | Status flag |
|---|---|---|---|
| H1 | Instrumental / RFI | No confirmed 1977 local interference source identified; Méndez et al. (2025) assessed and judged instrumental/software error unlikely given the signal's clean Gaussian rise/fall | `VERIFY EXACT WORDING IN PRIMARY SOURCE before quoting` |
| H2 | Cometary hydrogen emission (comets 266P/Christensen, P/2008 Y2 Gibbs) | Declination mismatch ~3°, right ascension mismatch ~47 min against Big Ear's ~3-minute beam window; no confirmed precedent for cometary 1420 MHz emission at the relevant heliocentric distance | Treat as **near-refuted** — use explicitly as a validation/control hypothesis in the Bayesian model (see §4, Rule 13) |
| H3 | Interstellar hydrogen cloud / stimulated maser flare, possibly triggered by a magnetar or soft gamma repeater | Revised (2025) flux ≈250 Jy; frequency 1420.726 MHz; two candidate sky positions (RA 19h25m02s±3s or 19h27m55s±3s, Dec −26°57′±20′, J2000); supporting "mini-Wow" analog events reported in 2020 Arecibo data | Numbers sourced to Méndez et al. 2024/2025 — **re-verify exact figures against the arXiv PDFs before hardcoding them**, do not trust this table alone for final values |
| H4 | Artificial interstellar power beam (leakage) | EIRP order ~10¹⁸ W typical for a beacon at ~1,000 ly in Benford's general framework; narrow bandwidth argued to be a physics-forced consequence of high-gain beaming, not a free design choice | JBIS version paywalled — **fetch and confirm exact EIRP/bandwidth figures from a verifiable source before use**; do not use the order-of-magnitude figure above without re-derivation or explicit `UNVERIFIED` flagging |
| H5 | Stochastic repeating ETI beacon | ~33% probability Big Ear would catch such a beacon on one look; drops to ~1.8% once all subsequent non-detection campaigns (VLA, Hobart, ATA) are incorporated as sequential evidence | Source: Kipping & Gray (2022), arXiv:2206.08374 — **this is your validation benchmark, fetch and re-derive their number, do not just cite it** |

**Non-detection campaigns used as shared evidence across hypotheses (per §2.4 below):** Gray & Marvel (2001, VLA), Gray & Ellingsen (2002, Hobart), Harp et al. (2020, ATA), Perez et al. (2022).

### 2.3 The four methodological pillars

1. **Lingam, Haqq-Misra, Wright, Huston, Frank & Kopparapu (2023), *ApJ* 943:27**, "Technosignatures: Frameworks for Their Assessment," DOI 10.3847/1538-4357/acaca0. Provides a Bayesian posterior framework for technosignature candidates built around an ambiguity ratio, ξ (roughly: probability of the observed data under a technological cause divided by probability under a non-technological cause). **This is your master equation. Fetch the actual paper (IOPscience or ADS abstract page) and extract the exact formula before implementing anything — do not reconstruct the equation from this summary.**
2. **Sheikh (2020), *International Journal of Astrobiology***, "The Nine Axes of Merit for Technosignature Searches," arXiv:1908.02683. Provides the nine-axis taxonomy (including "ambiguity") used to structure the census in Module B. Fetch and confirm exact axis definitions before scoring events.
3. **Kipping & Gray (2022), *MNRAS***, arXiv:2206.08374. Provides your validation benchmark (the ~33%→~1.8% result under H5). Reproducing this number under equivalent restricted assumptions is a hard gate before trusting any extended output (PRD §5, Module C1.3).
4. **Sheikh et al. (2021), *Nature Astronomy***, "Analysis of the Breakthrough Listen signal of interest blc1 with a technosignature verification framework," DOI 10.1038/s41550-021-01508-8. Provides the structured verification-checklist approach adapted for constructing the H1 (RFI/instrumental) likelihood.

### 2.4 The Benford correction — treat as a hard rule, not a suggestion
Non-detection/follow-up-search data tells you the event is **rare**. It does **not**, by itself, favor one specific hypothesis (H3, H4, or H5) over another — rarity is consistent with all of them. **Implement this as a shared rate/rarity nuisance parameter common to all hypotheses, not as direct discriminating evidence between them.** Getting this wrong is the single most likely way this project's Bayesian model would be judged flawed by a reviewer.

### 2.5 Census candidate events (starting list — expand only with human approval per PRD §13)
- Wow! Signal, 1977 (Big Ear).
- "Mini-Wow" events reported in Méndez et al. (2024)'s 2020 Arecibo archival data.
- BLC1 (Breakthrough Listen Candidate 1), 2019, Proxima Centauri, Parkes telescope — ultimately traced to a terrestrial intermodulation artifact per Sheikh et al. (2021).

### 2.6 Glossary
- **ξ (xi) / ambiguity ratio:** ratio of the probability of observed data under a technological cause vs. a non-technological cause (Lingam et al. 2023).
- **Bayes factor:** ratio of marginal likelihoods between two hypotheses, used to compare their support given the data.
- **Posterior odds:** prior odds × Bayes factor; your headline output metric for Module C.
- **EIRP:** Effective Isotropic Radiated Power — the power a source would need to radiate isotropically to produce the observed signal strength if fully directional gain is accounted for; central to H4.
- **Jansky (Jy):** unit of spectral flux density used throughout the flux measurements in this table.

---

## 3. Citation Ledger

Status key: **VERIFIED** = link confirmed reachable and content-matched during project setup. **RE-CHECK** = citation believed correct but exact figures/wording must be re-confirmed against the primary source before use in any output.

| Citation | Link | Status |
|---|---|---|
| Ehman, "The Big Ear Wow! Signal (30th Anniversary Report)" | http://www.bigear.org/Wow30th/wow30th.htm | VERIFIED (accessible) |
| Gray & Marvel (2001), *ApJ* 546:1171 | https://doi.org/10.1086/318272 | RE-CHECK figures |
| Gray & Ellingsen (2002), *ApJ* 578:967 | https://doi.org/10.1086/342646 | RE-CHECK figures |
| Harp et al. (2020), *AJ* 160:162 | https://doi.org/10.3847/1538-3881/aba58f | RE-CHECK figures |
| Paris & Davies (2017) | https://arxiv.org/abs/1706.03259 | RE-CHECK figures |
| NAAPO comet-hypothesis rebuttal | http://naapo.org/WOWCometRebuttal.html | VERIFIED (accessible) |
| Kipping & Gray (2022), *MNRAS* | https://arxiv.org/abs/2206.08374 | RE-CHECK — this is your validation benchmark, treat with extra care |
| Caballero (2022), *IJA* 21(3):129–136 | https://doi.org/10.1017/S1473550422000015 | RE-CHECK figures |
| Méndez, Ortiz Ceballos & Zuluaga (2024), "Arecibo Wow! I" | https://arxiv.org/abs/2408.08513 | RE-CHECK figures |
| Méndez et al. (2025), "Arecibo Wow! II" | https://arxiv.org/abs/2508.10657 | RE-CHECK figures — supersedes older flux/position numbers, use this version |
| Benford (2021), *JBIS* 74:196–200 | Journal paywalled; public summary at https://www.centauri-dreams.org/2021/01/22/was-the-wow-signal-due-to-power-beaming-leakage/ | RE-CHECK — summary only, not primary text |
| Benford (2025), "Beaming and Bandwidth" | https://www.centauri-dreams.org/2025/09/22/beaming-and-bandwidth-a-new-note-on-the-wow-signal/ | RE-CHECK |
| Sheikh (2020), "Nine Axes of Merit," *IJA* | https://arxiv.org/abs/1908.02683 | RE-CHECK — fetch full text for exact axis definitions |
| Lingam et al. (2023), *ApJ* 943:27 | https://doi.org/10.3847/1538-4357/acaca0 (also https://ui.adsabs.harvard.edu/abs/2023ApJ...943...27L/abstract) | RE-CHECK — fetch full text for the exact posterior formula before implementing Module C |
| Sheikh et al. (2021), *Nature Astronomy*, BLC1 verification framework | https://doi.org/10.1038/s41550-021-01508-8 | RE-CHECK |

**Rule: if you need a fact from any of these sources and cannot fetch the actual document (e.g., paywalled), do not substitute your own recollection of what the paper "probably" says. Flag it `UNVERIFIED` and surface it to the humans in your status report (§6).**

---

## 4. Operating Protocol — Anti-Hallucination & Reasoning Rules

These rules are binding, not stylistic preferences. If a task instruction and one of these rules conflict, follow this rule and flag the conflict to the humans.

1. **Source-or-silence rule.** Never state a numeric value, citation, quote, or specific factual claim without a verifiable source. If you don't have one, say so explicitly — do not fill the gap with a plausible-sounding number.
2. **Primary-source-verification rule.** Before implementing any formula or methodology attributed to a cited paper (especially the Lingam et al. posterior equation and the Sheikh axes), fetch and read the actual paper. Do not implement a formula reconstructed from a summary, abstract, or your own memory of "how Bayesian technosignature frameworks typically work."
3. **Show-your-work rule.** Every computed statistic must have its full derivation reported alongside it — inputs, formula used, intermediate steps. No unexplained numbers.
4. **Validation-first rule.** Do not report, use, or build on the 5-hypothesis Bayesian output until the Kipping & Gray reproduction test passes. If it fails, stop and report the failure — do not adjust the test's target value to make it pass, and do not proceed past this gate on the assumption it will probably be fine.
5. **Three-tier claim labeling.** In every output document, distinguish: (a) **Established literature fact** [with citation], (b) **Agent-derived computation** [with method shown], (c) **Assumption or judgment call** [explicitly flagged, requires human sign-off before finalizing]. Never let (c) read like (a).
6. **Assumptions log.** Maintain a running, dated log of every prior, simplification, or judgment call made, with a one-line justification for each. This log ships with every deliverable.
7. **Stop-and-ask triggers.** Pause and request human input at every point listed in `PRD.md` §13. Do not treat these as suggestions you can bypass if you're confident.
8. **No fabricated references, ever.** If a citation cannot be verified via a tool call (fetch/search), do not include it in any output. Flag it as missing instead of guessing a plausible-looking reference.
9. **Reproducibility and logging.** Every analysis run logs its exact inputs, random seed, code version, and outputs, timestamped. If someone reruns it, they should get the same numbers.
10. **Test before trust.** No computational module's output is used in a downstream report or manuscript until its unit tests pass. Write the test before or alongside the implementation, not after the fact as a formality.
11. **Mandatory sensitivity analysis.** Never present a single point-estimate result without the corresponding robustness/sensitivity range. A number without a stated uncertainty range is treated as incomplete work, not a final result.
12. **Paraphrase, never copy.** When drafting manuscript text from source material, always paraphrase in your own words and cite. Never reproduce sentences, or close paraphrases that mirror the original's structure and specific phrasing, from any source — this is both an academic-integrity requirement and a copyright requirement.
13. **Numerical sanity-check rule.** Before accepting any computed output, do an order-of-magnitude gut check against the known validation benchmarks (e.g., does the H5 restricted case land near Kipping & Gray's ~1.8%? Does H2's posterior come out strongly suppressed, as expected for a near-refuted hypothesis?). If a sanity check fails, treat it as a bug to find, not a surprising result to report.
14. **Confidence calibration.** State uncertainty honestly. Don't present a prior-sensitive result with false precision (e.g., don't report "posterior probability 0.0347" if the sensitivity sweep shows this varies by an order of magnitude across reasonable priors — report the range).
15. **Human review checkpoints.** Honor every gate in `PRD.md` §13 without exception.
16. **Visible error correction.** If you discover that an earlier output (yours or a prior session's) was wrong, say so explicitly and show the correction — do not silently patch it and move on as if it were always correct. A visible correction log is more trustworthy than a clean-looking history.
17. **No unilateral scope changes.** Do not add new hypotheses, drop existing ones, or change the census event list without flagging the proposed change to the humans first (per PRD §13, point 3).
18. **No outward-facing certainty about the Wow! Signal's origin.** Every output — code comments, manuscript drafts, status reports — must reflect that this project produces a *probabilistic comparison*, never a claimed resolution. Watch for language drift toward "the signal was caused by X" and correct it to "the analysis assigns X the highest posterior probability under the stated assumptions."

---

## 5. Repository / File Structure Convention

```
/data/parameters.yaml       # Module A output — sourced, cited parameters
/data/census.csv            # Module B output — scored events + ξ values
/src/                       # all computation code
/tests/                     # unit + integration tests (incl. Kipping & Gray validation)
/figures/                   # generated plots, regenerable from /data + /src
/logs/                      # run logs, assumptions log, changelog
/manuscripts/rnaas_note.md
/manuscripts/full_paper.md
README.md                   # setup + reproduction instructions
```

---

## 6. Communication Protocol Back to the Humans

At the end of each work session or phase, produce a short status report containing:
1. What was completed, mapped to PRD module/requirement IDs.
2. Any `UNVERIFIED` items still outstanding.
3. Any stop-and-ask trigger that was hit, with the specific question for the humans.
4. Any failed test or validation gate, with the raw failure output (not a paraphrase of it).
5. A one-line statement of overall confidence in the phase's results and why.

**Practical note:** if this project is executed inside Claude Code, this file's contents (or a shorter pointer to it via an `@AGENT_BRAIN.md` import) can be placed in your project's `CLAUDE.md` so it's loaded automatically at the start of every session rather than needing to be re-pasted each time.
