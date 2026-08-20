# A Five-Hypothesis Bayesian Assessment of the 1977 Wow! Signal

**Authors:** [Undergraduate Researchers]
**Target:** Research Notes of the AAS (RNAAS)

### Introduction
For nearly five decades, the 72-second, 1420.726 MHz narrowband radio transient known as the Wow! Signal has remained unclassified. Historically, the debate surrounding its origin has been partitioned into a binary classification of terrestrial interference versus extraterrestrial intelligence. However, recent literature has advanced specific, testable mechanistic models. These range from artificial interstellar power beams (Benford et al. 2010) and stochastic repeating beacons (Kipping & Gray 2022) to natural explanations such as stimulated interstellar hydrogen (HI) maser flares (Méndez et al. 2024; 2025). Rather than analyzing these proposals in isolation, we implement a unified Bayesian framework to simultaneously evaluate five competing hypotheses. Our computational pipeline assigns the highest posterior probability to the natural HI maser flare model under a wide array of prior assumptions.

### Methodology: The Bayesian Framework
We adapt the Bayesian model for technosignature assessment introduced by Lingam et al. (2023), integrating qualitative axes from the Sheikh (2020) taxonomy to inform our ambiguity parameters. Our framework tests five mutually exclusive hypotheses:
- **H1:** Instrumental artifact or local radio frequency interference (RFI).
- **H2:** Cometary hydrogen emission (utilized as a near-refuted negative control).
- **H3:** Interstellar HI cloud maser flare.
- **H4:** Artificial interstellar power beam leakage.
- **H5:** Stochastic repeating ETI beacon.

We established a set of baseline prior probabilities (H1: 0.10, H2: 0.02, H3: 0.40, H4: 0.15, H5: 0.33) and subjected them to a rigorous 100-step sensitivity sweep to ensure ranking stability.

### The Benford Correction: A Shared Rarity Parameter
A critical innovation in our pipeline is the treatment of historical non-detection follow-up campaigns, which total 192 pooled hours (e.g., META, Hobart, ATA). Previous analyses have occasionally leveraged these non-detections exclusively against artificial hypotheses. We introduce the "Benford Correction," which treats continuous non-detection as a constraint on spatial and temporal *event rarity* that applies equally to any hypothesized transient source in that region of the sky, whether natural (H3) or artificial (H4, H5). 

Using the maximum a posteriori (MAP) event rate of 0.121 events per day derived from stochastic modeling, we calculate a shared Poisson non-detection penalty of $e^{-192h \times (0.121/24)} \approx 0.380$. This scalar is applied identically to the intrinsic likelihoods of H3, H4, and H5.

### Simulation and Validation
To ensure mathematical rigor before applying our five-hypothesis comparison, we independently replicated the complex stochastic beacon likelihoods published by Kipping & Gray (2022). We constructed a custom, NumPy-vectorized Monte Carlo likelihood emulator. By extracting the exact array of 90 historical observation dates from the original 2022 Fortran source code (spanning a 2,673-day baseline), our independent emulator achieved a Final MAP likelihood of 2.50%. This yields a 1.41 ratio against the published 1.78% target, easily passing the order-of-magnitude threshold required for stochastic grid validation.

### Results and Conclusion
When processing the five hypotheses through the validated Bayesian engine, the natural HI maser flare (H3) emerges as the dominant model. Under our baseline priors, H3 achieves a posterior probability of 75.3%, followed by the stochastic repeating beacon (H5) at 16.5%. 

To test the fragility of this conclusion, we swept the prior allocations across extreme bounds (e.g., varying the H3 prior from 15% to 60% while proportionally scaling the others). Across 100 distinct permutations, H3 maintained the top rank 100% of the time, never dropping below a 49.7% posterior probability. H1 (RFI) and H2 (Comet) are effectively suppressed to near-zero, driven by the signal's clean celestial transit profile and severe geometric coordinate mismatches, respectively. 

While this Bayesian framework provides a probabilistic comparison rather than a definitive origin classification, the analysis robustly assigns the highest posterior probability to the Méndez (2025) HI maser flare hypothesis.

### Table 1: Bayesian Posteriors and Sensitivity Bounds
| Hypothesis | Baseline Prior | Intrinsic Likelihood | Baseline Posterior | Sensitivity Sweep Bounds (Min – Max) |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (RFI)** | 10.0% | $5.0 \times 10^{-5}$ | 0.00% | 0.0% – 0.0% |
| **H2 (Comet)** | 2.0% | $\sim 0$ | 0.00% | 0.0% – 0.0% |
| **H3 (HI Maser)** | 40.0% | $4.3 \times 10^{-2}$ | 75.3% | 49.7% – 89.4% |
| **H4 (Power Beam)** | 15.0% | $1.2 \times 10^{-2}$ | 8.2% | 0.5% – 20.0% |
| **H5 (Stochastic Beacon)** | 33.0% | $1.1 \times 10^{-2}$ | 16.5% | 1.5% – 30.3% |

### References
*   Benford, J., Benford, G., & Benford, D. (2010). Messaging with cost-optimized interstellar beacons. *Astrobiology, 10*(5), 475-490.
*   Kipping, D., & Gray, R. (2022). Could the 'Wow' signal have originated from a stochastic repeating beacon? *Monthly Notices of the Royal Astronomical Society, 515*(1), 1122-1129.
*   Lingam, M., et al. (2023). A Bayesian Framework for the Evaluation of Technosignatures. *The Astrophysical Journal, 943*, 27.
*   Méndez, A., et al. (2024). Arecibo Wow! I: An Astrophysical Explanation for the Wow! Signal. *arXiv preprint arXiv:2408.08513*.
*   Méndez, A., et al. (2025). Arecibo Wow! II: Further Constraints on the Origin of the Wow! Signal. *arXiv preprint arXiv:2508.10657*.
*   Paris, A., & Davies, E. (2017). Hydrogen clouds from comets 266/P Christensen and P/2008 Y2 (Gibbs) are candidates for the source of the 1977 “WOW” Signal. *Journal of the Washington Academy of Sciences, 101*.
*   Sheikh, S. Z. (2020). The Nine Axes of Merit for Technosignature Searches. *International Journal of Astrobiology, 19*(3), 241-255.
