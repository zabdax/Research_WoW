# H5 Reproducibility Acceptance Criterion

Because exact numerical reproducibility of the K&G (2022) stochastic emulator depends on 
undocumented choices (e.g. Monte Carlo runtime sampling, grid interpolation details, 
or discrepancy between published source `wow.f90` (150-by-160 loops) and the bundled 
`output_grid.dat` (160-by-160 loops)), the project defines the following acceptance criterion:

**Either:**
1. Independently reproduce the published MAP (1.78%) within a quantitatively justified 
   tolerance (e.g., 0.1-0.2 percentage points) using an exact simulation of the 
   90 observation dates with recorded Monte Carlo uncertainty. 
**Or:**
2. Document the irreducible baseline discrepancy (e.g., the 0.36 point gap found between 
   the independent 1.42% simulation and the 1.78% target) and retain H5 permanently in 
   a *comparison-only* mode. It will not be treated as an exact replication.
