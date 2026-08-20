# A Generative Bayesian Assessment Framework for the 1977 Wow! Signal

**Authors:** [Undergraduate Researchers]
**Target:** Research Notes of the AAS (RNAAS)

### Introduction
The Wow! Signal has remained unclassified since its detection in 1977. Historically, efforts to categorize its origin operate under heuristic, binary classifications (terrestrial/instrumental interference vs. artificial extraterrestrial communication). Recent literature has advanced specific, testable physical models ranging from interstellar power beams (Benford et al. 2010), to stochastic ETI beacons (Kipping & Gray 2022), to natural interstellar hydrogen (HI) maser flares (Méndez et al. 2024; 2025). 

We report on the development of a unified, generative Bayesian model-comparison framework (Lingam et al. 2023) designed to evaluate five contemporary hypotheses simultaneously. Because historical multi-observatory data requires strict calibration, this communication does not yet issue a unified five-way posterior. Instead, we constrain three critical parameters using reproducible physical models built within our open-source computational pipeline.

### Methodology
To produce robust likelihoods, we abandon heuristic qualitative scoring. Instead, we divide our analysis strictly between observationally constrained measurements and model-dependent priors. The five hypotheses tracked are H1 (RFI), H2 (Comet control), H3 (HI maser), H4 (Power beam), and H5 (Stochastic beacon). 

### 1. H2 Geometry vs Horizons Ephemeris
Paris & Davies (2017) hypothesized that hydrogen emission from passing comets (e.g. 266P/Christensen) induced the signal. Through exact geometrical modeling projecting the NASA/JPL Horizons 2008 geocentric solution of 266P into the Big Ear altitude/azimuth frame, we confirm a significant positional mismatch (~3° Declination, ~47 min Right Ascension). Unless severe, unmeasured coordinate covariance is extracted from a topocentric 1977 ephemeris, calculating P(Detection | H2) approaches zero, successfully functioning as a negative control for our system.

### 2. H3 Flux Normalization constraint
The H3 framework relies heavily on archival 'mini-wow' analogues identified in 2020. Our pipeline establishes an empirical H3 prior by uncoupling the foreground cloud count catalog (e.g., HI4PI) from the theoretical interaction rate of triggering mechanisms. Crucially, any physical model yielding an H3 likelihood must be driven by an un-censored flux measurement. The pipeline explicitly maintains the historical signal flux as an >250 Jy lower bound and tests candidate models for specific required intrinsic enhancements (between 10^6 and 10^7 baseline brightness improvements) without generating a heuristic event-rate prior prematurely.

### 3. H5 Stochastic Emulator Bounds
Kipping & Gray (2022) leveraged 192 hours of follow-up campaigns to generate a stochastic likelihood model for H5. We engineered a NumPy-vectorized strict implementation emulator derived from the parameters recorded in their bundled code. Extracting exactly 90 observation dates reflecting the 2,673 simulated days, we achieve a baseline MAP likelihood of 1.42%. When directly evaluating this behavior, exact reproduction of the published 1.78% MAP is subjected to minor, irreducible baseline discrepancy due to a hardcoded boundary artifact (150x160 bounds in the published source against 160x160 extracted bundles). In our strict framework, this locks the current H5 MAP simulation as an 'exploratory' comparison tool rather than an exact substitution for an analytical integral.

### Conclusion and Platform Availability
Robust triage of anomalous technosignatures strictly requires an analytical framework prohibiting arbitrary prior manipulation. A strict framework reveals multiple areas—including Big Ear archival receiver validation and transmitter alignment constraints—that blocked rigorous verification for this signal. The codebase constructed (incorporating models, strict observational schemas, Monte Carlo emulators, and Python replication tests) provides a reproducible bedrock for processing subsequent transients using strict Bayesian conditions. It is publicly maintained.

### References
*   Benford, J., Benford, G., & Benford, D. (2010). *Astrobiology*, 10(5), 475-490.
*   Kipping, D., & Gray, R. (2022). *MNRAS*, 515(1), 1122-1129.
*   Lingam, M., et al. (2023). *ApJ*, 943, 27.
*   Méndez, A., et al. (2024). *arXiv preprint*, 2408.08513.
*   Méndez, A., et al. (2025). *arXiv preprint*, 2508.10657.
*   Paris, A., & Davies, E. (2017). *J. Washington Academy of Sciences*, 101.
