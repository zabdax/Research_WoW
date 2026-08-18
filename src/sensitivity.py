"""
sensitivity.py — Prior Sensitivity Analysis

Module C/D: Sweeps the prior space to test the robustness of the
posterior rankings. Explores the ranges defined in PRD C1.4 and
outputs ranges rather than single point estimates (Rule 14).
"""

import json
import logging
import os
from typing import Any, Dict, List, Tuple

import numpy as np

from src.bayesian_engine import (
    DEFAULT_PRIORS,
    HYPOTHESIS_IDS,
    HYPOTHESIS_NAMES,
    PRIOR_RANGES,
    compute_posteriors,
)

logger = logging.getLogger(__name__)


def run_sensitivity_sweep(steps: int = 10) -> Dict[str, Any]:
    """
    Run a grid sweep across all prior ranges to compute posterior bounds.

    Because priors must sum to 1, we can't just vary them all independently.
    We'll vary one at a time across its full range, and scale the others
    proportionally to keep the sum at 1.0.

    Args:
        steps: Number of points to evaluate for each prior's range.

    Returns:
        Dictionary containing the posterior bounds for each hypothesis.
    """
    posterior_bounds = {h_id: {"min": 1.0, "max": 0.0} for h_id in HYPOTHESIS_IDS}
    all_rankings = []
    
    # Baseline result for reference
    baseline = compute_posteriors(DEFAULT_PRIORS)
    baseline_rank1 = baseline.ranking[0][0]

    # For each hypothesis, sweep its prior across its range
    for target_h, (p_min, p_max) in PRIOR_RANGES.items():
        sweep_values = np.linspace(p_min, p_max, steps)
        
        for p_val in sweep_values:
            # Create a new prior dict
            test_priors = {}
            
            # The remaining probability mass to distribute
            remaining_mass = 1.0 - p_val
            
            # Sum of default priors for the *other* hypotheses
            other_default_sum = sum(DEFAULT_PRIORS[h] for h in HYPOTHESIS_IDS if h != target_h)
            
            # Distribute remaining mass proportionally to other defaults
            for h_id in HYPOTHESIS_IDS:
                if h_id == target_h:
                    test_priors[h_id] = float(p_val)
                else:
                    if other_default_sum > 0:
                        test_priors[h_id] = float(DEFAULT_PRIORS[h_id] * (remaining_mass / other_default_sum))
                    else:
                        # Fallback if somehow others sum to 0 (shouldn't happen with our defaults)
                        test_priors[h_id] = remaining_mass / 4.0
            
            # Compute posteriors with this configuration
            result = compute_posteriors(test_priors)
            
            # Update bounds
            for h_id, post_val in result.posteriors.items():
                if post_val < posterior_bounds[h_id]["min"]:
                    posterior_bounds[h_id]["min"] = float(post_val)
                if post_val > posterior_bounds[h_id]["max"]:
                    posterior_bounds[h_id]["max"] = float(post_val)
                    
            # Record the top-ranked hypothesis for stability analysis
            all_rankings.append(result.ranking[0][0])
            
    # Analyze ranking stability
    rank1_counts = {}
    for r in all_rankings:
        rank1_counts[r] = rank1_counts.get(r, 0) + 1
        
    stability = {
        "total_sweeps": len(all_rankings),
        "baseline_top_rank": baseline_rank1,
        "top_rank_distribution": rank1_counts,
        "is_stable": len(rank1_counts) == 1  # True if the top rank never changes
    }
    
    output = {
        "baseline_priors": DEFAULT_PRIORS,
        "prior_ranges_tested": PRIOR_RANGES,
        "posterior_bounds": posterior_bounds,
        "ranking_stability": stability
    }
    
    return output

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("=" * 70)
    print("Running Prior Sensitivity Analysis")
    print("=" * 70)
    
    results = run_sensitivity_sweep(steps=20)
    
    print("\n--- Posterior Bounds (across all prior sweeps) ---")
    for h_id in HYPOTHESIS_IDS:
        bounds = results['posterior_bounds'][h_id]
        print(f"  {h_id} ({HYPOTHESIS_NAMES[h_id]}): "
              f"{bounds['min']:.4f} – {bounds['max']:.4f} "
              f"({bounds['min']*100:.1f}% – {bounds['max']*100:.1f}%)")
              
    print("\n--- Ranking Stability ---")
    stab = results['ranking_stability']
    print(f"  Baseline Top Rank: {stab['baseline_top_rank']}")
    print(f"  Is Stable (Top rank never changes): {stab['is_stable']}")
    print("  Top Rank Distribution across sweep:")
    for h_id, count in stab['top_rank_distribution'].items():
        pct = (count / stab['total_sweeps']) * 100
        print(f"    {h_id}: {count}/{stab['total_sweeps']} sweeps ({pct:.1f}%)")
        
    # Save results
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data", "sensitivity_results.json"
    )
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nSensitivity results saved to {output_path}")
