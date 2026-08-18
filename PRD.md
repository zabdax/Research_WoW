# Product Requirements Document (PRD)
## Wow! Signal Multi-Hypothesis Bayesian Assessment & Comparative Technosignature Census

**Document status:** Active — hand this to your executing agent alongside `AGENT_BRAIN.md`
**Owners (final authority on all judgment calls):** Patali + research teammate
**Executor role:** An agentic AI implements this PRD but does NOT have sign-off authority on scientific judgment calls (priors, ambiguity scores, claims of novelty/significance) — see Section 13.

---

## 1. Mission Statement

Build, validate, and publish a reproducible, quantitative, multi-hypothesis assessment of the Wow! Signal by (a) formally comparing five competing explanations in a single Bayesian framework, and (b) grounding that comparison in a systematic, published-taxonomy-based census of comparable technosignature events. The output is a portfolio of research artifacts (code, dataset, and manuscripts), not just a document.

---

## 2. Objectives (Measurable)

| ID | Objective | Measurable outcome |
|---|---|---|
| O1 | Multi-hypothesis Bayesian comparison | A posterior-odds / Bayes-factor table across 5 named hypotheses, each with a credible interval |
| O2 | Comparative technosignature census | A structured dataset scoring ≥3 Wow!-like events on Sheikh's (2020) axes, with each ambiguity score converted to an explicit ξ value |
| O3 | Robustness | A sensitivity analysis showing how O1's conclusions shift across a documented range of prior assumptions |
| O4 | Validation | A passing reproduction of Kipping & Gray's (2022) single-hypothesis result as an internal pipeline check |
| O5 | Reproducibility package | A public Git repository + Zenodo archive with DOI, containing all code, data, and a README sufficient for an independent third party to rerun the analysis |
| O6 | Publication-ready manuscripts | A complete RNAAS note draft (≤1,500 words, one table) and a complete full-length manuscript draft (literature review + methods + results + discussion) targeting International Journal of Astrobiology |

---

## 3. Scope

**In scope:**
- Computational synthesis and statistical modeling using only already-published data (parameters, uncertainty ranges, non-detection statistics).
- Building and validating the Bayesian comparison pipeline.
- Building and scoring the census dataset.
- Drafting manuscript sections from the analysis outputs.
- Literature retrieval and citation verification for every factual claim used.

**Explicitly out of scope (do not attempt):**
- Any new telescope observation, data collection, or proposal for telescope time.
- Any claim of a confirmed detection, confirmed origin, or definitive resolution of the Wow! Signal's cause. The project's output is a *probabilistic comparison*, never a verdict.
- Submitting anything to a journal or preprint server without explicit human approval (see Section 13).
- Contacting any external researcher, journal, or third party on the team's behalf without explicit human approval.

---

## 4. Users & Stakeholders

- **Primary stakeholders / domain owners:** Patali and research teammate. They hold final authority over priors, ambiguity scores, interpretive claims, and anything that leaves the repository (submissions, emails, public posts).
- **Executor:** an agentic AI (e.g., operating inside a coding environment). Treated as a highly capable but non-authoritative implementer — see the Operating Protocol in `AGENT_BRAIN.md` for the hard limits on what it may decide unilaterally.

---

## 5. Functional Requirements, by Module

### Module A — Knowledge Base Construction
- A1.1: Parse every source in the Citation Ledger (`AGENT_BRAIN.md` §3) and extract every numeric parameter needed for Modules B and C into a single structured file (e.g. `data/parameters.yaml` or `.json`), with each value tagged with its source citation key and the exact location (page/section/equation number) it came from.
- A1.2: Any parameter the agent cannot locate in the primary source text itself (as opposed to a summary or secondary citation) must be flagged `UNVERIFIED` and surfaced to the humans rather than estimated or silently omitted.
- **Acceptance criteria:** every field in `parameters.yaml` has a non-empty `source` field; zero fields are populated from the agent's general knowledge without a citation.

### Module B — Comparative Census Engine
- B1.1: Build a dataset (`census.csv` or equivalent) with one row per catalogued event (minimum: Wow! 1977, Méndez 2024 mini-Wow events, BLC1 2019; agent should actively search for additional legitimate candidates and propose them to the humans for inclusion, not add them unilaterally).
- B1.2: Score each event on at minimum the ambiguity, detectability, and duration axes from Sheikh (2020), with a written justification per score. **[RESOLVED, see AGENT_BRAIN.md v2 §2.3]** Sheikh's axes are qualitative by design and not intended for per-event numeric scoring. Use ξ (Lingam et al. 2023) as the quantitative proxy specifically for the ambiguity axis; for detectability and duration, use a documented custom ordinal rubric (1–5, explicit per-point criteria), stated in manuscript text as an original extension of Sheikh's framework, not as something her paper itself endorses.
- B1.3: Convert each ambiguity score into an explicit ξ estimate per the methodology in `AGENT_BRAIN.md` §2.3, showing the conversion logic, not just the output number.
- **Acceptance criteria:** every score has an accompanying justification string; the ξ conversion logic is a documented, reviewable function, not a hardcoded lookup table.

### Module C — Bayesian Model Comparison Engine
- C1.1: Implement the five-hypothesis posterior/Bayes-factor calculation per the framework in `AGENT_BRAIN.md` §2.2, using Module A's parameters and Module B's ξ values as inputs.
- C1.2: Implement the shared rarity/rate nuisance parameter explicitly (per the Benford correction, `AGENT_BRAIN.md` §2.4) — non-detection data must update this shared parameter, not directly discriminate between H3/H4/H5.
- C1.3: Implement and pass the Kipping & Gray (2022) validation check (Module D) before producing or reporting any 5-hypothesis result.
- C1.4: Implement the prior-sensitivity sweep — vary each hypothesis's prior across a documented, justified range and report how posterior odds shift.
- **Acceptance criteria:** C1.3's validation check must pass (output within the same order of magnitude as Kipping & Gray's reported ~1.8% figure under equivalent restricted assumptions) before Module C's outputs are used anywhere downstream. If it does not pass, work stops and the discrepancy is reported to the humans — do not proceed and do not adjust the validation target to make it pass.

### Module D — Validation & Testing
- D1.1: Unit tests for every computational component (parameter loader, ξ converter, posterior calculator, sensitivity sweep) using toy/synthetic inputs with known expected outputs.
- D1.2: The Kipping & Gray reproduction test (see C1.3) as an integration test.
- D1.3: A changelog or test report generated on every run, timestamped, logging inputs/seed/outputs.
- **Acceptance criteria:** test suite passes; no computational module is used in reporting until its tests pass.

### Module E — Reporting & Manuscript Drafting
- E1.1: Auto-generate the posterior-odds table and sensitivity-analysis figure from Module C's outputs (no manually re-typed numbers — figures/tables must be generated directly from the data files).
- E1.2: Draft the RNAAS note (≤1,500 words, one table/figure) as a standalone document.
- E1.3: Draft the full manuscript (literature review, methods citing all four pillars explicitly, results, sensitivity analysis, limitations, discussion, references) as a standalone document.
- E1.4: All manuscript prose must paraphrase source material — no verbatim reproduction of sentences from any cited paper (see `AGENT_BRAIN.md` §4, Rule 12).
- **Acceptance criteria:** every number appearing in manuscript prose or tables traces back to a specific file/function in the repository — no number is typed directly into manuscript text without a traceable computational or literature source.

### Module F — Reproducibility Packaging
- F1.1: Repository structure per `AGENT_BRAIN.md` §5.
- F1.2: README sufficient for an independent third party to install dependencies and rerun the full pipeline from raw parameters to final tables/figures.
- F1.3: Prepare (but do not submit) a Zenodo archive package.
- **Acceptance criteria:** a clean clone of the repository, following only the README, reproduces Module C's headline result.

---

## 6. Non-Functional Requirements

- **Reproducibility:** every result must be regenerable from versioned code + versioned data with a fixed random seed.
- **Traceability:** every factual claim or number in any output document must be traceable to either (a) a specific citation in the ledger, or (b) a specific computation in the repository. No exceptions.
- **Transparency:** all assumptions, priors, and judgment calls must be logged in a visible, human-readable assumptions log — nothing "invisible" baked into code without documentation.
- **Correctness over speed:** the agent should prioritize getting the validation gate (C1.3/D1.2) right over moving quickly through later phases.

---

## 7. Technical Stack

- **Language:** Python 3.
- **Statistical modeling:** `PyMC` or `emcee` for posterior sampling if needed; prefer a simpler closed-form/grid-based Bayes factor calculation first, and only escalate to MCMC if model complexity genuinely requires it.
- **Data handling:** `pandas`.
- **Visualization:** `matplotlib` (posterior-odds bar chart, sensitivity plot, census radar/spider chart).
- **Testing:** `pytest`.
- **Version control:** Git, with meaningful commit messages per logical change (not one giant commit).

---

## 8. Data Sources

All sources are public and free — see `AGENT_BRAIN.md` §3 for the full, verified citation ledger with links. No proposal, paywall access, or institutional agreement is required for this project as scoped.

---

## 9. Milestones & Timeline

| Phase | Content | Target duration | Gate to proceed |
|---|---|---|---|
| 0 | Knowledge base construction (Module A) | ~1 week | All parameters sourced and human-reviewed |
| 1 | Census (Module B) | ~1.5–2 weeks | Ambiguity scores human-approved (Section 13) |
| 2 | Bayesian engine + validation (Modules C, D) | ~2–3 weeks | Kipping & Gray validation test passes |
| 3 | Reporting (Module E) | ~1.5–2 weeks | Every manuscript number traces to source |
| 4 | Packaging + human final review (Module F) | ~few days | Human sign-off before any submission |

Total: ~6–8 weeks, consistent with the feasibility estimate already validated in the project's prior planning documents.

---

## 10. Risk Register

| Risk | Likelihood | Mitigation | Owner |
|---|---|---|---|
| Prior subjectivity undermines credibility | Medium | Mandatory sensitivity sweep (C1.4); document justification for every prior | Humans approve priors; agent implements |
| Small-N census looks like overreach | Medium | Explicitly frame census as proof-of-concept in all manuscript language, not a population-level claim | Agent drafts framing; humans approve |
| Agent hallucinates a citation, number, or quote | High if unmitigated | Hard rules in `AGENT_BRAIN.md` §4; nothing enters outputs without a traced source | Agent (enforced), humans spot-check |
| Agent silently "fixes" a failed validation test by loosening the target | High if unmitigated | Explicit rule: validation failure must stop work and be reported, never quietly resolved (Module C1.3) | Agent (enforced), humans review test logs |
| Scope creep (agent starts drafting claims of certainty about the Wow! Signal's origin) | Medium | Explicit "never a verdict" language in Section 3 and reinforced in `AGENT_BRAIN.md` | Humans review all outward-facing language |

---

## 11. Acceptance Testing / QA Plan

Before any phase is considered complete, the humans review:
1. The assumptions log for that phase.
2. The test report (pass/fail, with failure explanations if any).
3. A sample of at least 3 numeric claims traced backward from output to source, checked manually.

---

## 12. Definition of Done (Project-Level)

The project is "done" when all six objectives in Section 2 are met, the Module F acceptance criterion (clean-clone reproducibility) passes, and both manuscript drafts have been reviewed and approved by both human researchers — not when the agent believes the work is complete.

---

## 13. Human-in-the-Loop Checkpoints (Non-Negotiable)

The agent must pause and request explicit human input — not proceed on its own best guess — at each of these points:
1. Before finalizing any prior probability used in Module C.
2. Before finalizing any ambiguity/axis score in Module B.
3. Before adding or removing any event from the census dataset.
4. Before any claim of novelty, significance, or interpretation enters manuscript text (as opposed to a reported number or a paraphrased literature fact).
5. Before any external action: submission, preprint posting, email, or public repository visibility change.
6. Whenever the validation gate (C1.3) fails.

---

## 14. Related Documents

This PRD is designed to be used alongside:
- `AGENT_BRAIN.md` — domain knowledge base and the operating protocol / anti-hallucination rules referenced throughout this PRD.
- The three prior planning documents already produced for this project (literature review, combined-approach deep dive, publication strategy) — the agent should treat these as background context but `AGENT_BRAIN.md` as the authoritative, structured reference for facts and figures.
