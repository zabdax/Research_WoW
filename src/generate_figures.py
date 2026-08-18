"""
generate_figures.py — Generates publication-ready plots for the manuscripts.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

from bayesian_engine import compute_posteriors, HYPOTHESIS_IDS, HYPOTHESIS_NAMES

# Ensure figures directory exists
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# Set global plot style for academic papers
plt.style.use('seaborn-v0_8-paper')
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
})

def plot_sensitivity_sweep():
    """Plot posterior probabilities vs H3 prior variation."""
    h3_priors = np.linspace(0.05, 0.95, 50)
    
    posteriors_h3 = []
    posteriors_h4 = []
    posteriors_h5 = []
    
    # Baseline priors (summing to 1 for the remaining 60%)
    # H1=10%, H2=2%, H4=15%, H5=33% -> ratios: 10/60, 2/60, 15/60, 33/60
    base_ratios = {
        "H1": 10/60,
        "H2": 2/60,
        "H4": 15/60,
        "H5": 33/60
    }
    
    for h3_p in h3_priors:
        remaining_mass = 1.0 - h3_p
        test_priors = {"H3": h3_p}
        for k, v in base_ratios.items():
            test_priors[k] = v * remaining_mass
            
        result = compute_posteriors(priors=test_priors)
        posteriors_h3.append(result.posteriors["H3"] * 100)
        posteriors_h4.append(result.posteriors["H4"] * 100)
        posteriors_h5.append(result.posteriors["H5"] * 100)
        
    plt.figure(figsize=(9, 6))
    plt.plot(h3_priors * 100, posteriors_h3, label="H3: HI Maser (Natural)", linewidth=3, color='#2ca02c')
    plt.plot(h3_priors * 100, posteriors_h5, label="H5: Stochastic Beacon (ETI)", linewidth=3, color='#1f77b4')
    plt.plot(h3_priors * 100, posteriors_h4, label="H4: Power Beam (ETI)", linewidth=3, color='#ff7f0e')
    
    # Add vertical line for our baseline 40% prior
    plt.axvline(x=40.0, color='gray', linestyle='--', alpha=0.7, label="Baseline H3 Prior (40%)")
    
    plt.title("Posterior Sensitivity to H3 Prior Probability")
    plt.xlabel("Assumed Prior Probability of H3 (HI Maser) [%]")
    plt.ylabel("Computed Posterior Probability [%]")
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    out_path = os.path.join(FIGURES_DIR, "fig1_sensitivity_sweep.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {out_path}")

def plot_validation_pillars():
    """Plot the 3-pillar validation results against the K&G Target."""
    # Data from Phase 2
    labels = ['K&G Target', 'Level 1\n(Analytical)', 'Level 2\n(Rep. Monte Carlo)', 'Level 2\n(Exact Monte Carlo)']
    values = [1.78, 1.78, 1.7818, 2.50]
    colors = ['#7f7f7f', '#2ca02c', '#2ca02c', '#1f77b4']
    
    plt.figure(figsize=(9, 6))
    bars = plt.bar(labels, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Add exact value labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f"{yval:.2f}%", ha='center', va='bottom', fontweight='bold')
        
    # Draw horizontal target line
    plt.axhline(y=1.78, color='red', linestyle='--', alpha=0.7, label='Target MAP (1.78%)')
    
    plt.title("3-Pillar Validation of the Likelihood Emulator")
    plt.ylabel("Computed Final MAP Likelihood [%]")
    plt.ylim(0, 3.0)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # Add some descriptive text
    plt.text(2.9, 2.0, "*Exact MC variance expected\ndue to 20x20 coarse grid\nand pure stochasticity.", 
             fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
             
    plt.tight_layout()
    out_path = os.path.join(FIGURES_DIR, "fig2_validation_pillars.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {out_path}")

if __name__ == "__main__":
    print("Generating manuscript figures...")
    plot_sensitivity_sweep()
    plot_validation_pillars()
    print("Done.")
