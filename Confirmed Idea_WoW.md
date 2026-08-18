# **Combining Idea 1 \+ Idea 3: A Deep-Dive Methodology, Feasibility Check, and Execution Roadmap**

**Project working title:** *A Bayesian Multi-Hypothesis Assessment of the Wow\! Signal, Grounded in a Systematic Comparative Technosignature Census*

This document goes one level deeper than the first review: it identifies the actual published frameworks your methodology should be built on (not invented from scratch), shows precisely how the Bayesian model comparison (Idea 1\) and the comparative census (Idea 3\) can be structurally fused rather than just bundled together, stress-tests the feasibility, and lays out a phased plan for the two of you to execute it.

---

## **1\. The Key Insight: Why "Combining" Idea 1 \+ Idea 3 Is Stronger Than Doing Either Alone**

When I first proposed these as two separate ideas, I described Idea 3 (the census) as a lightweight desk-research byproduct of the review. Digging deeper into the literature changes that assessment: **there is a published formal link between the two that lets you build one integrated methodology instead of two adjacent projects.**

Sofia Sheikh's **"Nine Axes of Merit for Technosignature Searches"** (Sheikh 2020, *International Journal of Astrobiology*; arXiv:1908.02683) — a framework built at NASA's own 2018 Technosignatures Workshop — proposes nine standardized axes for scoring and comparing any candidate technosignature, one of which is explicitly called **"ambiguity."**

Separately, Lingam, Haqq-Misra, Wright, Huston, Frank & Kopparapu's **"Technosignatures: Frameworks for Their Assessment"** (2023, *The Astrophysical Journal*, 943:27) built a formal Bayesian posterior-probability framework for evaluating any technosignature candidate, in which the key quantity determining how much a detection should update your beliefs is an **ambiguity ratio, ξ**, defined as the probability of the observed data given a technological origin divided by the probability of the same data given a non-technological origin. The paper explicitly identifies this ξ term as mathematically equivalent to Sheikh's "ambiguity" axis.

**That's your synthesis.** Instead of running a census (Idea 3\) and a Bayesian comparison (Idea 1\) as two independent deliverables, you can:

1. Use Sheikh's nine axes to systematically score every Wow\!-like event in your census (Wow\! 1977, Méndez's 2024 "mini-Wow" events, BLC1, and any others you catalog).  
2. Convert each event's ambiguity-axis score into an explicit ξ estimate.  
3. Feed those ξ values directly into a Lingam-et-al.-style Bayesian posterior calculation as the evidentiary term for each competing hypothesis about the *original* Wow\! Signal.

This means your census isn't just a nice table sitting next to your Bayesian analysis — it's the empirical grounding that makes your priors and likelihoods defensible rather than arbitrary. That's a genuinely novel structural contribution: as far as this literature review found, nobody has explicitly chained Sheikh's taxonomy into Lingam et al.'s Bayesian formalism and applied the combination to the Wow\! Signal specifically.

---

## **2\. The Four Research-Backed Methodological Pillars**

Everything below rests on four published frameworks. Cite all four explicitly and early in your methods section — this is what will make reviewers treat your approach as "applying established formalism" rather than "inventing statistics for a blog post."

### **Pillar 1 — Lingam et al. (2023), *ApJ* 943:27, "Technosignatures: Frameworks for Their Assessment"**

Provides the core Bayesian machinery: a posterior-probability formula for any technosignature hypothesis that depends on (a) a prior probability of the relevant technology/phenomenon existing, and (b) the ambiguity ratio ξ (odds of the data given the candidate cause vs. given alternative causes). The paper also discusses the Youden index as a fallback metric when priors are too poorly constrained to specify with confidence — worth having in your back pocket for a robustness check. This is your master equation; you'll be instantiating it five times, once per hypothesis.

### **Pillar 2 — Sheikh (2020), *IJA*, "The Nine Axes of Merit for Technosignature Searches" (arXiv:1908.02683)**

Provides the structured, citable taxonomy for the census: observational capability, search cost, ancillary benefits, detectability, duration, **ambiguity**, extrapolation, inevitability, and richness of information. You don't need to use all nine for every purpose, but scoring your catalog of events on at least detectability, duration, and ambiguity gives you both a defensible census structure and the direct ξ inputs Pillar 1 needs.

### **Pillar 3 — Kipping & Gray (2022), *MNRAS*, "Could the 'Wow' signal have originated from a stochastic repeating beacon?" (arXiv:2206.08374)**

Your closest direct precedent and a built-in validation check. They found Big Ear had roughly a 33% chance of detecting a stochastic artificial beacon on one look, dropping to about 1.8% once every subsequent non-detection campaign (VLA, Hobart, ATA) is folded in as sequential Bayesian evidence. **Use this as a unit test for your own pipeline**: if your generalized multi-hypothesis model, restricted to just the "stochastic ETI beacon" hypothesis and the same non-detection dataset, doesn't reproduce numbers in the same ballpark as their 1.8%, you have a bug or a prior-specification problem before you trust any of your other four hypotheses' results.

### **Pillar 4 — Sheikh et al. (2021), *Nature Astronomy*, "Analysis of the Breakthrough Listen signal of interest blc1 with a technosignature verification framework"**

Provides the structured evidence-checklist approach (instrumentation checks, off-source comparison, known-RFI cross-referencing) that you'll adapt to build the likelihood term for your RFI/instrumental hypothesis specifically — this is the paper that turned "was blc1 real?" into a formal, repeatable procedure, and yours is functionally the same kind of question asked of an event 42 years older with far worse original data provenance.

---

## **3\. The Five Hypotheses to Compare (and the published numbers behind each)**

| Hypothesis | Core published parameters you'll use | Key source(s) |
| ----- | ----- | ----- |
| **H1 — Instrumental/RFI** | No confirmed local interference source identified at 1420 MHz in 1977 records; Big Ear's clean double-horn transit signature is hard to reproduce via RFI, but total ambiguity is nonzero given single-detection provenance | Ehman (2010); Méndez et al. (2025) instrumental-error assessment |
| **H2 — Cometary hydrogen emission** | Declination off by \~3°, right ascension off by \~47 min from Big Ear's 3-minute beam window; no confirmed precedent for 1420 MHz cometary emission at the relevant heliocentric distance | Paris & Davies (2017); NAAPO rebuttal; Fitzsimmons (in Astronomy Now, 2017\) |
| **H3 — Interstellar hydrogen cloud / stimulated maser flare** | Revised flux ≈250 Jy; frequency 1420.726 MHz; two candidate sky positions (19h25m02s / 19h27m55s, dec –26°57′); supporting "mini-Wow" analog events found in 2020 Arecibo data | Méndez et al. (2024, 2025), arXiv:2408.08513, arXiv:2508.10657 |
| **H4 — Artificial interstellar power beam (leakage)** | EIRP order 10¹⁸ W typical for a 1,000 ly beacon; narrow bandwidth is a *physics-forced consequence* of high-gain amplifiers needed for beaming, not a free choice — this is the crux of Benford's argument | Benford (2021), *JBIS* 74:196–200; Benford (2025), *JBIS* "Beaming and Bandwidth" note |
| **H5 — Stochastic repeating ETI beacon** | \~33% single-look detection probability at Big Ear; drops to \~1.8% once all subsequent non-detections are incorporated | Kipping & Gray (2022) |

**Important methodological correction to build in from the start:** Benford himself has explicitly pointed out a reasoning trap worth avoiding — repeated non-detections in follow-up searches only tell you the *event is rare*, they do **not** by themselves favor one specific hypothesis (power beam, hydrogen cloud, or otherwise) over another, since rarity is consistent with all of them. Practically, this means your non-detection data (Gray & Marvel 2001, Gray & Ellingsen 2002, Harp et al. 2020, Perez et al. 2022\) should update a **shared rarity/rate nuisance parameter common to all hypotheses**, not be used as direct discriminating evidence between H3, H4, and H5. Getting this right is exactly the kind of thing that separates a paper reviewers respect from one they pick apart — flag it explicitly in your methods section as something you deliberately guarded against.

---

## **4\. Feasibility Check**

### **Data availability — ✅ Fully feasible**

Every number in the table above is already published in peer-reviewed papers or arXiv preprints. You need zero telescope time, zero data-download bandwidth, and no institutional data-use agreements. This is a desk-based computational statistics project from day one.

### **Computational requirements — ✅ Fully feasible**

A Bayesian model comparison across five hypotheses with a handful of parameters each runs comfortably on a laptop. Recommended stack: Python, `PyMC` or `emcee` for posterior sampling (or even a simpler closed-form / grid-based Bayes factor calculation if you want to avoid MCMC entirely — worth trying the simple version first and only reaching for MCMC if the model gets more complex than expected), `pandas`/`matplotlib` for the census dataset and figures. No GPU, no cluster, no paid compute needed.

### **Skill fit — ✅ Strong match**

This sits squarely in your team's existing strengths: Bayesian/statistical modeling in Python is methodologically close to work you've already done (e.g., the Latin Hypercube uncertainty analysis on [STRATA](https://github.com/zabdax/STRATA)), and building a structured, scoring-based dataset (the census) is a lighter lift than the transit-detection pipeline work on [Project Astraeus.](https://github.com/zabdax/project-astraeus)

### **Realistic honest risks (and how to defuse each)**

1. **Prior subjectivity.** Bayesian priors for hypotheses like "probability an ETI beacon exists at all" are inherently somewhat subjective, and a skeptical reviewer will push on this hardest. *Mitigation:* don't pick single point-value priors. Run a **sensitivity analysis** — show how your posterior odds change across a reasonable range of prior assumptions (e.g., an order-of-magnitude sweep), and report which conclusions are robust across that whole range versus which ones are prior-dependent. This is standard practice in exactly this literature (Kipping's own papers do this) and turns a weakness into a demonstrated strength.  
2. **Small-N problem in the census.** You'll realistically have somewhere between 3 and \~10 genuinely comparable "Wow\!-like" events to catalog (the original signal, Méndez's mini-Wows, BLC1, maybe one or two borderline others). That's too small for a statistical distribution claim. *Mitigation:* frame the census explicitly as a **proof-of-concept demonstration of the Sheikh-axes-to-Lingam-ξ pipeline**, not as a large-sample statistical survey. That's an honest framing that's still a genuine methodological contribution — you're showing the pipeline works and giving the field a template, not claiming a population-level result.  
3. **H2 (comet) is already essentially dead.** Since the comet hypothesis is about as refuted as a SETI hypothesis gets, including it might look like padding. *Mitigation:* reframe it as your **built-in validation/control hypothesis** — a good multi-hypothesis Bayesian framework should assign it a strongly suppressed posterior probability. If your model doesn't do that, something's wrong with your setup; if it does, that's a clean sanity check you can show reviewers directly. This is good methodological practice, not padding, and you should say so explicitly in the paper.  
4. **Reviewers may see the whole exercise as "just re-packaging existing numbers."** *Mitigation:* this is exactly why Pillars 1–4 matter — you are not inventing a bespoke statistical scheme, you're the first to formally chain two specific, separately-published, peer-reviewed frameworks (Sheikh 2020 \+ Lingam et al. 2023\) and apply the combination to a specific, currently-contested case. Say that explicitly, early, in your introduction.

**Overall feasibility verdict: high.** This is a genuinely achievable project for a two-person remote team with no institutional backing, on a timeline measured in weeks rather than months, using only free tools and already-published data.

---

## **5\. Phased Execution Roadmap**

### **Phase 0 — Foundational immersion (≈1 week)**

Both of you read the four pillar papers closely (Section 2), plus Arecibo Wow\! I & II, Kipping & Gray (2022), and Benford's two notes (2021, 2025). Deliverable: a shared annotated bibliography document (this can literally extend the reference list from the first review document) with, for each hypothesis, the specific numbers you'll need in Phase 2 already extracted into a spreadsheet.

*Suggested split:* one of you owns the "natural explanation" papers (comet, hydrogen cloud, RFI/verification framework) and one owns the "artificial explanation" papers (power beam, stochastic beacon, Sheikh/Lingam frameworks) — then swap and cross-check each other's extracted numbers before moving on. Two independent reads of the same source catching the same numbers is cheap insurance against transcription errors that would otherwise sit silently in your priors.

### **Phase 1 — Build the census first (≈1.5–2 weeks)**

Do this before Phase 2, since it produces inputs Phase 2 needs.

1. Finalize your event list (start with: Wow\! 1977, Méndez's 2024 mini-Wow detections, BLC1 2019; actively search for any other borderline "signal of interest" events documented in the SETI literature to strengthen the N).  
2. Score each event on at minimum three of Sheikh's nine axes — **ambiguity**, detectability, and duration — with a written justification for each score (this justification text becomes your methods section prose almost directly).  
3. Convert each ambiguity score into an explicit ξ estimate (a ratio, not just a qualitative label) — this is the step that requires the most care and the most explicit documentation of your reasoning, since it's the bridge into Phase 2\.

**Deliverable:** a structured dataset (CSV or small SQLite table is fine) plus a comparison figure — a radar/spider chart across the axes per event works well and is highly reusable in slides or a poster later.

### **Phase 2 — Build the Bayesian model comparison (≈2–3 weeks)**

1. Implement Lingam et al.'s posterior framework for each of the five hypotheses in Section 3, using the ξ values from Phase 1 wherever they apply and the published parameter ranges (flux, position, EIRP, detection probabilities) as your likelihood inputs elsewhere.  
2. Explicitly build in the shared rarity/rate nuisance parameter discussed in Section 3 rather than letting non-detection data directly discriminate between hypotheses.  
3. Run the Kipping & Gray validation check (Pillar 3\) as your first sanity test before trusting the full five-hypothesis output.  
4. Run the prior-sensitivity sweep (Section 4, risk \#1).

**Deliverable:** a table of posterior odds / Bayes factors across all five hypotheses, plus the sensitivity-analysis figure showing robustness (or lack thereof) across your prior range.

### **Phase 3 — Synthesis and write-up (≈1.5–2 weeks)**

Pull Phase 1 and Phase 2 together into the paper: literature review (you already have this from the first document) → methods (Pillars 1–4, explicitly) → census results → Bayesian results → discussion (be honest about the small-N limitation and the prior-sensitivity findings) → conclusion. Push code and the census dataset to a public GitHub repo, ideally archived on Zenodo for a DOI — you've done exactly this before with STRATA, so this part of the workflow should feel familiar.

### **Phase 4 — Target and submit**

Given the methodology is a genuine quantitative contribution rather than a pure narrative review, **Research Notes of the AAS (RNAAS)** is worth strong consideration for a fast, focused submission of the Bayesian comparison result alone, with the fuller review-plus-census version going to **International Journal of Astrobiology** (which has direct precedent here via Caballero 2022\) or arXiv first regardless of eventual journal target.

**Total realistic timeline: roughly 6–8 weeks of consistent part-time work for two people**, assuming Phase 0 overlaps with the tail end of finishing the literature review from the first document rather than starting cold.

---

## **6\. Immediate Next Step**

The highest-leverage next move is Phase 1, step 3 — nailing down exactly how you'll convert a qualitative "ambiguity" score into a quantitative ξ ratio, since every other number in the project chains off that decision. If you want, I can work through that conversion methodology with you in detail next — it's the one piece of this pipeline that doesn't come pre-packaged from the literature and needs your own careful derivation.

