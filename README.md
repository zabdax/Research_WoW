# Wow! Signal — Multi-Hypothesis Bayesian Assessment

This repository contains the data, code, and manuscript drafts for a quantitative, Bayesian comparison of five competing explanations for the 1977 "Wow!" Signal, grounded by a systematic census of comparable technosignature events.

## Directory Structure

* `/data/` - Contains the master knowledge base (`parameters.yaml`) and the comparative event census (`census.csv`).
* `/src/` - Python source code for the Bayesian inference engine, Bayes factor calculations, and sensitivity analysis.
* `/tests/` - Unit tests, including the validation gate reproducing Kipping & Gray (2022) MAP likelihoods.
* `/figures/` - Generated plots and visualizations for the manuscripts.
* `/logs/` - Project execution logs, assumption tracking, and status reports.
* `/manuscripts/` - LaTeX source and compiled PDFs for the RNAAS note and the full *International Journal of Astrobiology* paper.

## Hypotheses Evaluated
1. **H1:** Instrumental / RFI
2. **H2:** Cometary hydrogen emission (Control)
3. **H3:** Interstellar hydrogen cloud / stimulated maser flare
4. **H4:** Artificial interstellar power beam (leakage)
5. **H5:** Stochastic repeating ETI beacon
