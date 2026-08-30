# Wow! Signal Bayesian Triage Research Program

[![Research Framework](https://img.shields.io/badge/Framework-Bayesian_Triaging-blue.svg)](https://arxiv.org/abs/2301.07275)
[![Status](https://img.shields.io/badge/Project_Status-Active_Reconstruction-brightgreen.svg)]()
[![Model Comparison](https://img.shields.io/badge/Hypotheses_Evaluated-5-orange.svg)]()

## Overview

This repository hosts a **multi-hypothesis Bayesian assessment and comparative technosignature census** of the famous August 15, 1977 "Wow!" Signal detected by the Big Ear radio observatory.

The Wow! Signal remains one of the most compelling narrowband radio transients ever recorded. Over the decades, multiple hypotheses have been proposed to explain it. Rather than endorsing a single explanation, this undergraduate research effort formalizes five distinct published hypotheses and compares them within a unified mathematical framework. By employing the Bayesian posterior framework for technosignatures established by Lingam et al. (2023), and the nine-axis taxonomy for searches by Sheikh (2020), this project produces a quantitative, model-driven comparison.

## The Five Hypotheses Evaluated

We formally test the following theoretical explanations to calculate their Bayes factors and posterior odds:

1. **H1: Instrumental / RFI Error:** Local interference, software errors, or unresolved hardware artifacts.
2. **H2: Cometary Hydrogen Emission:** Originating from cometary halo emissions (e.g., 266P/Christensen or P/2008 Y2 Gibbs). *Treated as a near-refuted validation control due to known positional/declination mismatches with the Big Ear beam.*
3. **H3: Interstellar Hydrogen Cloud / Maser Flare:** A stimulated non-thermal maser flare in an interstellar H1 cloud, potentially triggered by a magnetar, as proposed by Méndez et al. (2025).
4. **H4: Artificial Interstellar Power Beam (Leakage):** Interstellar beacon leakage driven by high-gain beaming (Benford et al. 2010), exhibiting narrow bandwidth as a consequence of fundamental beam physics.
5. **H5: Stochastic Repeating ETI Beacon:** An uncoordinated, repeating extraterrestrial beacon modeled via Kipping & Gray (2022)'s survival analysis baseline.

## Methodology

The pipeline relies on four methodological pillars:
- **Lingam et al. (2023):** Provides the posterior framework utilizing the *ambiguity ratio* ($\xi$), representing the probability of observed data under a technological vs. non-technological cause.
- **Sheikh (2020):** Translates ambiguity, duration, and observability into structured census checkpoints.
- **Kipping & Gray (2022):** Used as an internal validation pipeline to reliably reconstruct their single-hypothesis findings.
- **Sheikh et al. (2021) "BLC1":** Adapting the verification checklist logic used on Breakthrough Listen Candidate 1 to evaluate H1 systematically.

## Project Structure

This repository separates the original exploratory models from the rigorous, provenance-aware current framework:

- `research/` — **Revised research framework (Active)**: Defensible Bayesian pipeline admitting formalized likelihood models. No final hypothesis ranking is endorsed until physical, observational, and follow-up priors successfully pass independent verification gates. 
- `legacy/` — **Legacy Phase 2 Prototype (Preserved)**: Original heuristic-driven explorations frozen under the Git tag `phase2-prototype-audit`. Retained intentionally for reproducibility and comparative analysis against the newer Bayesian models.
- `src/` & `tests/` — Core calculation engines for Bayesian updates and parameter extraction, tested via `pytest`.
- `manuscripts/` — Artifacts and drafts targeting RNAAS notes and publication-ready journals.

## How to Run the Validations

### 1. Validate the Revised Structured Inputs
Run the active framework's source verification audit:
```bash
python -m research.validation.source_audit
```

### 2. Run the Legacy Preserved Baseline
If you need to reproduce the original Phase 2 pipeline without modifying final results:
```bash
python -m pytest tests/
python -m scripts.legacy_report
```

## Core Principles & Disclaimers

- Do **not** treat a normalized heuristic score as a rigorous Bayes factor or posterior evidence.
- The absence of subsequent signal detections (non-detections across VLA, Hobart, ATA) represents a generalized event rarity rather than direct discriminating evidence between specific rare hypotheses (e.g., H3 vs. H4).
- Do not present preprints as peer-reviewed confirmation.
- **No result in this repository is a definitive attribution of the Wow! Signal.** The purpose is statistical triage, model validation, and ambiguity admission under strict scientific skepticism.

> *Note: This work is conducted by independent high-school researchers (Zubayer and teammates) as an ongoing comparative technosignature assessment.*
