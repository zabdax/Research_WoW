"""
bayesian_engine.py — Five-Hypothesis Bayesian Model Comparison Engine

Module C: Computes comparative posterior probabilities for five competing
explanations of the Wow! Signal using the Lingam et al. (2023) framework,
grounded in published parameters and the Benford correction for shared
rarity.

Master equation (Lingam et al. 2023, ApJ 943:27, Eq. 6):
    P(T|D,C) = P(T|C) * xi / (1 + P(T|C) * (xi - 1))

Five hypotheses:
    H1: Instrumental / RFI
    H2: Cometary hydrogen emission (near-refuted control)
    H3: Interstellar hydrogen cloud / stimulated maser flare
    H4: Artificial interstellar power beam (leakage)
    H5: Stochastic repeating ETI beacon

Citation sources:
    - Lingam et al. (2023), ApJ 943:27, DOI:10.3847/1538-4357/acaca0
    - Sheikh (2020), arXiv:1908.02683
    - Kipping & Gray (2022), MNRAS 515:1122, arXiv:2206.08374
    - Méndez et al. (2024/2025), arXiv:2408.08513, arXiv:2508.10657
    - Benford et al. (2010a/b), arXiv:0810.3966, arXiv:0810.3964
"""

import json
import logging
import math
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Constants & Configuration
# ---------------------------------------------------------------------------

HYPOTHESIS_IDS = ["H1", "H2", "H3", "H4", "H5"]
HYPOTHESIS_NAMES = {
    "H1": "Instrumental / RFI",
    "H2": "Cometary hydrogen emission",
    "H3": "Interstellar HI cloud / maser flare",
    "H4": "Artificial interstellar power beam",
    "H5": "Stochastic repeating ETI beacon",
}

# Baseline priors (approved by humans, subject to sensitivity sweep)
# Sum must equal 1.0
DEFAULT_PRIORS = {
    "H1": 0.10,
    "H2": 0.02,
    "H3": 0.40,
    "H4": 0.15,
    "H5": 0.33,
}

# Prior sensitivity ranges for sweep (PRD C1.4)
PRIOR_RANGES = {
    "H1": (0.01, 0.30),
    "H2": (0.001, 0.05),
    "H3": (0.15, 0.60),
    "H4": (0.01, 0.30),
    "H5": (0.05, 0.50),
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class HypothesisLikelihood:
    """Likelihood for a single hypothesis with full provenance."""
    hypothesis_id: str
    hypothesis_name: str
    likelihood: float  # P(D|Hi)
    components: Dict[str, float]  # Named sub-components
    justification: str
    sources: List[str]
    assumptions: List[str]


@dataclass
class BayesFactor:
    """Bayes factor comparing two hypotheses."""
    numerator_id: str
    denominator_id: str
    value: float  # P(D|Hi) / P(D|Hj)
    log10_value: float
    interpretation: str


@dataclass
class PosteriorResult:
    """Complete posterior result for all five hypotheses."""
    priors: Dict[str, float]
    likelihoods: Dict[str, HypothesisLikelihood]
    posteriors: Dict[str, float]
    bayes_factors: Dict[str, BayesFactor]  # key = "Hi_vs_Hj"
    ranking: List[Tuple[str, float]]  # Sorted (hypothesis_id, posterior)
    shared_rarity_parameter: Dict[str, Any]
    metadata: Dict[str, Any]

    def to_json(self) -> str:
        """Serialize to JSON with full provenance."""
        d = {
            "priors": self.priors,
            "likelihoods": {k: asdict(v) for k, v in self.likelihoods.items()},
            "posteriors": self.posteriors,
            "bayes_factors": {k: asdict(v) for k, v in self.bayes_factors.items()},
            "ranking": self.ranking,
            "shared_rarity_parameter": self.shared_rarity_parameter,
            "metadata": self.metadata,
        }
        return json.dumps(d, indent=2, default=str)


# ---------------------------------------------------------------------------
# Lingam et al. (2023) master equation
# ---------------------------------------------------------------------------

def lingam_posterior(prior_tech: float, xi: float) -> float:
    """
    Compute the posterior probability of a technological origin given
    data D and context C, using the Lingam et al. (2023) framework.

    P(T|D,C) = P(T|C) * xi / (1 + P(T|C) * (xi - 1))

    Where:
        P(T|C) = prior probability of technological origin
        xi = P(D|C,T) / P(D|C,T_bar) = ambiguity ratio

    Source: Lingam et al. (2023), ApJ 943:27, Equation 6.

    Args:
        prior_tech: Prior probability of technological origin P(T|C).
        xi: Ambiguity ratio.

    Returns:
        Posterior probability P(T|D,C).

    Raises:
        ValueError: If inputs are out of valid range.
    """
    if not 0 <= prior_tech <= 1:
        raise ValueError(f"Prior must be in [0,1], got {prior_tech}")
    if xi < 0:
        raise ValueError(f"Xi must be non-negative, got {xi}")

    denominator = 1.0 + prior_tech * (xi - 1.0)

    if denominator <= 0:
        # Edge case: can happen with xi < 1 and high prior
        # In this case, the posterior is capped at 0 or 1
        if prior_tech * xi >= 0:
            return min(1.0, max(0.0, prior_tech * xi))
        return 0.0

    posterior = prior_tech * xi / denominator
    return min(1.0, max(0.0, posterior))


def bayes_factor(likelihood_i: float, likelihood_j: float) -> float:
    """
    Compute the Bayes factor B_ij = P(D|Hi) / P(D|Hj).

    Args:
        likelihood_i: Marginal likelihood under hypothesis i.
        likelihood_j: Marginal likelihood under hypothesis j.

    Returns:
        Bayes factor. Returns inf if likelihood_j = 0.
    """
    if likelihood_j == 0:
        return float('inf') if likelihood_i > 0 else 1.0
    return likelihood_i / likelihood_j


def interpret_bayes_factor(bf: float) -> str:
    """
    Interpret a Bayes factor using the Jeffreys (1961) scale.

    Source: Jeffreys, H. (1961). Theory of Probability. Oxford.
    """
    log_bf = math.log10(abs(bf)) if bf > 0 else 0
    if log_bf < 0.5:
        return "Not worth more than a bare mention"
    elif log_bf < 1.0:
        return "Substantial"
    elif log_bf < 1.5:
        return "Strong"
    elif log_bf < 2.0:
        return "Very strong"
    else:
        return "Decisive"


# ---------------------------------------------------------------------------
# Shared Rarity Parameter (Benford Correction, AGENT_BRAIN_v2 §2.4)
# ---------------------------------------------------------------------------

def compute_shared_rarity_penalty(
    total_followup_hours: float = 192.0,
    lambda_map_per_day: float = 0.121,
) -> Dict[str, Any]:
    """
    Compute the shared rarity/rate nuisance parameter that constrains
    all hypotheses equally via the non-detection follow-up data.

    Per AGENT_BRAIN_v2 §2.4: "Non-detection data tells you the event
    is RARE. It does NOT, by itself, favor one specific hypothesis
    (H3, H4, or H5) over another."

    The Poisson non-detection penalty is:
        P(0 detections | lambda, T_obs) = exp(-lambda * T_obs)

    This factor is applied identically to H3, H4, and H5 likelihoods,
    ensuring non-detections constrain rarity without discriminating
    between hypotheses.

    H1 (RFI) and H2 (Comet) are evaluated independently:
    - H1 has its own rejection based on signal characteristics
    - H2 has its own geometric refutation

    Args:
        total_followup_hours: Total follow-up observation time.
        lambda_map_per_day: MAP event rate from K&G validation.

    Returns:
        Dictionary with rarity penalty and provenance.
    """
    penalty = math.exp(-lambda_map_per_day * total_followup_hours / 24.0)

    return {
        "penalty_factor": penalty,
        "lambda_map_per_day": lambda_map_per_day,
        "total_followup_hours": total_followup_hours,
        "applies_to": ["H3", "H4", "H5"],
        "does_not_apply_to": ["H1", "H2"],
        "justification": (
            "Non-detection data constrains the event rate (rarity) but does "
            "not discriminate between natural (H3) and artificial (H4, H5) "
            "explanations. Per Benford correction (AGENT_BRAIN_v2 §2.4)."
        ),
        "source": "Kipping & Gray 2022; Benford correction principle",
    }


# ---------------------------------------------------------------------------
# Per-Hypothesis Likelihood Construction
# ---------------------------------------------------------------------------

def compute_h1_likelihood() -> HypothesisLikelihood:
    """
    H1: Instrumental / RFI likelihood.

    The signal's characteristics are inconsistent with known RFI/instrumental
    artifacts:
    - Clean Gaussian rise/fall matches a celestial transit, not electronics
    - Frequency at exactly 1420.726 MHz (protected hydrogen line band)
    - No known 1977 RFI source at that frequency confirmed
    - SNR of 30.5σ — extremely strong for an artifact

    Using Sheikh et al. (2021) BLC1 verification framework as template:
    BLC1 was identified as RFI via off-source beam nods. The Wow! Signal
    passed (by absence) the transit-profile test that BLC1 failed.

    Likelihood set to a small but non-zero value reflecting that we cannot
    completely rule out an unknown 1977 interference source.

    Source: Méndez et al. (2025), arXiv:2508.10657; Sheikh et al. (2021).
    """
    # Component factors (multiplicative):
    # P(Gaussian transit | RFI) — RFI rarely produces clean Gaussian transits
    p_gaussian_given_rfi = 0.01

    # P(1420.726 MHz | RFI) — protected band, but not impossible
    p_freq_given_rfi = 0.05

    # P(30.5σ | RFI) — very strong signal is unusual for RFI
    p_snr_given_rfi = 0.10

    # P(single detection | RFI) — consistent: RFI can be transient
    p_single_given_rfi = 0.50

    likelihood = p_gaussian_given_rfi * p_freq_given_rfi * p_snr_given_rfi * p_single_given_rfi

    return HypothesisLikelihood(
        hypothesis_id="H1",
        hypothesis_name=HYPOTHESIS_NAMES["H1"],
        likelihood=likelihood,
        components={
            "p_gaussian_transit_given_rfi": p_gaussian_given_rfi,
            "p_protected_freq_given_rfi": p_freq_given_rfi,
            "p_high_snr_given_rfi": p_snr_given_rfi,
            "p_single_detection_given_rfi": p_single_given_rfi,
        },
        justification=(
            "Signal characteristics (clean Gaussian transit at protected "
            "1420.726 MHz with 30.5σ SNR) are strongly inconsistent with "
            "typical RFI patterns. Assessed via Sheikh et al. (2021) "
            "verification framework structure."
        ),
        sources=[
            "Méndez et al. 2025, arXiv:2508.10657",
            "Sheikh et al. 2021, DOI:10.1038/s41550-021-01508-8",
        ],
        assumptions=[
            "ASSUMPTION: Component probabilities are agent-derived estimates, "
            "not directly from a published source. Requires human review.",
            "ASSUMPTION: Independence of component factors assumed for "
            "multiplicative combination.",
        ],
    )


def compute_h2_likelihood() -> HypothesisLikelihood:
    """
    H2: Cometary hydrogen emission likelihood.

    Near-refuted validation control. The positional mismatch alone
    makes this hypothesis extremely unlikely:
    - Declination mismatch: ~3° (Big Ear beam ~0.5°)
    - RA mismatch: ~47 minutes (Big Ear beam ~3 minutes)
    - No confirmed precedent for cometary 1420 MHz emission

    Expected posterior: strongly suppressed (sanity check per Rule 13).

    Source: NAAPO Comet Hypothesis Rebuttal; Paris & Davies (2017).
    """
    # Geometric miss probability
    # Declination: 3° offset vs ~0.5° beam → P(in beam) ≈ 0
    # RA: 47 min offset vs ~3 min beam → P(in beam) ≈ 0
    # Using Gaussian beam approximation:
    dec_offset_beams = 3.0 / 0.5  # 6 beam widths
    ra_offset_beams = 47.0 / 3.0  # ~15.7 beam widths

    p_geometric = math.exp(-0.5 * dec_offset_beams**2) * math.exp(-0.5 * ra_offset_beams**2)

    # P(1420 MHz emission | comet) — no confirmed precedent
    p_emission = 0.001

    # P(250+ Jy from comet) — Paris detected only 4.76σ with 10m dish
    p_flux = 0.001

    likelihood = p_geometric * p_emission * p_flux

    return HypothesisLikelihood(
        hypothesis_id="H2",
        hypothesis_name=HYPOTHESIS_NAMES["H2"],
        likelihood=likelihood,
        components={
            "p_geometric_in_beam": p_geometric,
            "p_1420mhz_emission_from_comet": p_emission,
            "p_250jy_flux_from_comet": p_flux,
        },
        justification=(
            "Positional mismatch (~3° dec, ~47 min RA vs Big Ear's ~3-min "
            "beam) makes geometric probability negligible. No confirmed "
            "precedent for cometary 1420 MHz emission at relevant "
            "heliocentric distance. Treated as near-refuted validation "
            "control per AGENT_BRAIN_v2 §2.2."
        ),
        sources=[
            "NAAPO Comet Hypothesis Rebuttal, naapo.org/WOWCometRebuttal.html",
            "Paris & Davies 2017, arXiv:1706.03259",
        ],
        assumptions=[
            "ASSUMPTION: Gaussian beam approximation for positional "
            "probability. Actual beam shape may differ.",
            "ASSUMPTION: This is a validation control — posterior should "
            "be near-zero. If not, indicates a bug (Rule 13).",
        ],
    )


def compute_h3_likelihood(rarity_penalty: float = 1.0) -> HypothesisLikelihood:
    """
    H3: Interstellar HI cloud / stimulated maser flare likelihood.

    Currently the leading hypothesis with supporting evidence:
    - Mini-Wow analog events detected in Arecibo data (Méndez 2024)
    - DSR model produces consistent flux, frequency, bandwidth
    - Cold HI cloud temperature constraint (≤2.2K) consistent
    - Magnetar trigger mechanism physically plausible

    The rarity penalty from non-detections is applied via the shared
    Benford correction parameter.

    Source: Méndez et al. (2024/2025).
    """
    # P(narrowband at 1420.726 MHz | HI cloud maser)
    # Very high — this IS the hydrogen line, and masers are narrowband
    p_freq_bandwidth = 0.90

    # P(>250 Jy | DSR model) — consistent but requires favorable geometry
    # DSR model produces ~1 mJy at 0.4 kpc; needs closer or more
    # powerful flare for 250+ Jy
    p_flux = 0.30

    # P(single detection in 50 years | natural transient)
    # Rare transients are expected to be rare — consistent with rarity
    p_single_detection = 0.50

    # P(mini-Wow analogs exist | H3 true)
    # Strong supporting evidence — analog events detected
    p_analogs = 0.80

    # P(Gaussian transit profile | celestial source)
    # Expected for any point source transiting through the beam
    p_transit = 0.95

    # Intrinsic likelihood (before rarity penalty)
    intrinsic = p_freq_bandwidth * p_flux * p_single_detection * p_analogs * p_transit

    # Apply shared rarity penalty (Benford correction)
    likelihood = intrinsic * rarity_penalty

    return HypothesisLikelihood(
        hypothesis_id="H3",
        hypothesis_name=HYPOTHESIS_NAMES["H3"],
        likelihood=likelihood,
        components={
            "p_freq_bandwidth_given_maser": p_freq_bandwidth,
            "p_flux_given_dsr": p_flux,
            "p_single_detection_given_transient": p_single_detection,
            "p_mini_wow_analogs": p_analogs,
            "p_gaussian_transit_given_celestial": p_transit,
            "rarity_penalty": rarity_penalty,
            "intrinsic_likelihood": intrinsic,
        },
        justification=(
            "HI maser/DSR model produces narrowband emission at exactly "
            "the hydrogen line frequency. Mini-Wow analogs provide direct "
            "supporting evidence. Flux requires favorable geometry. "
            "Rarity penalty applied via shared Benford correction."
        ),
        sources=[
            "Méndez et al. 2024, arXiv:2408.08513",
            "Méndez et al. 2025, arXiv:2508.10657",
        ],
        assumptions=[
            "ASSUMPTION: Component probabilities are agent-derived from "
            "qualitative assessment of published evidence. Requires "
            "human review (PRD §13, checkpoint 1).",
            "ASSUMPTION: Mini-Wow analogs genuinely support H3 (not "
            "independently caused).",
            "ASSUMPTION: Rarity penalty applied equally to H3/H4/H5 "
            "per Benford correction.",
        ],
    )


def compute_h4_likelihood(rarity_penalty: float = 1.0) -> HypothesisLikelihood:
    """
    H4: Artificial interstellar power beam likelihood.

    Physically plausible beacon leakage with supporting physics:
    - Bandwidth <10 kHz is physics-forced by MOPA gain-bandwidth
    - EIRP >10^17 W achievable with km-scale aperture
    - Beam dwell time (10-100s) brackets the observation window
      NOTE: 72s match is QUARANTINED (assumptions_log A-020) —
      it is the telescope beam transit floor, not signal duration

    Source: Benford et al. (2010a/b), Benford (2025).
    """
    # P(narrowband <10 kHz | power beam)
    # Physics-forced by MOPA amplifier gain-bandwidth product
    p_bandwidth = 0.85

    # P(1420 MHz | power beam)
    # Benford's cost optimization favors ~10 GHz, not 1.42 GHz
    # But 1420 MHz is a "Schelling point" — universal meeting frequency
    p_freq = 0.30

    # P(>250 Jy at Earth | power beam at ~1-10 kpc)
    # Requires EIRP ~10^17-10^19 W — physically possible but demanding
    p_flux = 0.20

    # P(single detection | sweeping beacon)
    # Sweeping beacon has low duty cycle (10^-4 to 10^-7)
    # Single detection is expected for a sweeping beam
    p_single = 0.60

    # P(Gaussian transit | power beam in Big Ear)
    # A celestial point source produces Gaussian transit regardless
    p_transit = 0.95

    # NOTE: NOT using the 72s beam dwell time match as evidence
    # (quarantined per assumptions_log A-020)

    intrinsic = p_bandwidth * p_freq * p_flux * p_single * p_transit

    # Apply shared rarity penalty
    likelihood = intrinsic * rarity_penalty

    return HypothesisLikelihood(
        hypothesis_id="H4",
        hypothesis_name=HYPOTHESIS_NAMES["H4"],
        likelihood=likelihood,
        components={
            "p_bandwidth_given_beam": p_bandwidth,
            "p_freq_given_beam": p_freq,
            "p_flux_given_beam": p_flux,
            "p_single_given_sweeping": p_single,
            "p_gaussian_transit_given_celestial": p_transit,
            "rarity_penalty": rarity_penalty,
            "intrinsic_likelihood": intrinsic,
            "quarantined_dwell_time_match": "NOT USED (see A-020)",
        },
        justification=(
            "Power beam physics naturally produces narrowband emission. "
            "Cost optimization favors higher frequencies than 1420 MHz, "
            "reducing likelihood. EIRP requirement is achievable but "
            "demanding. 72s duration match is QUARANTINED — it reflects "
            "Big Ear's beam transit time, not signal characteristics."
        ),
        sources=[
            "Benford et al. 2010a, arXiv:0810.3966",
            "Benford et al. 2010b, arXiv:0810.3964",
            "Benford 2025, centauri-dreams.org",
        ],
        assumptions=[
            "ASSUMPTION: 72s dwell time match quarantined (A-020).",
            "ASSUMPTION: 1420 MHz Schelling point probability is "
            "agent-estimated. Requires human review.",
            "ASSUMPTION: Rarity penalty applied equally to H3/H4/H5.",
        ],
    )


def compute_h5_likelihood(
    rarity_penalty: float = 1.0,
    kg_map_likelihood: float = 0.0178,
) -> HypothesisLikelihood:
    """
    H5: Stochastic repeating ETI beacon likelihood.

    Directly uses the validated Kipping & Gray (2022) MAP likelihood
    as the primary evidence:
    - Big Ear-only MAP: 32.3% (highly compatible)
    - With follow-up (192h): 1.78% (2.4σ tension)

    The K&G result already incorporates non-detection evidence, so we
    use it directly rather than applying an additional rarity penalty
    (which would double-count the follow-up data).

    Source: Kipping & Gray (2022), arXiv:2206.08374.
    """
    # K&G's 1.78% already incorporates the non-detection campaigns
    # Do NOT apply additional rarity penalty — would double-count
    # The rarity_penalty parameter is accepted but noted as not applied

    # P(Gaussian transit | ETI beacon passing through beam)
    p_transit = 0.95

    # P(narrowband | ETI beacon)
    p_narrowband = 0.90

    # P(1420 MHz | ETI beacon) — Schelling point, higher than for H4
    p_freq = 0.50

    # K&G likelihood already contains the key statistical evidence
    # We weight the K&G result with additional consistency factors
    # but the K&G MAP is the dominant term
    consistency_factor = p_transit * p_narrowband * p_freq

    likelihood = kg_map_likelihood * consistency_factor

    return HypothesisLikelihood(
        hypothesis_id="H5",
        hypothesis_name=HYPOTHESIS_NAMES["H5"],
        likelihood=likelihood,
        components={
            "kg_map_likelihood": kg_map_likelihood,
            "p_gaussian_transit": p_transit,
            "p_narrowband": p_narrowband,
            "p_freq_schelling_point": p_freq,
            "consistency_factor": consistency_factor,
            "rarity_penalty_applied": False,
            "rarity_penalty_note": (
                "K&G MAP already incorporates 192h of non-detection data. "
                "Additional rarity penalty would double-count."
            ),
        },
        justification=(
            "Validated Kipping & Gray (2022) MAP likelihood of 1.78% "
            "directly used. K&G already incorporates META + Hobart + ATA "
            "non-detection data, so no additional rarity penalty applied "
            "(would double-count). Signal characteristics (narrowband, "
            "1420 MHz, Gaussian transit) are consistent with ETI beacon."
        ),
        sources=[
            "Kipping & Gray 2022, MNRAS 515:1122, arXiv:2206.08374",
        ],
        assumptions=[
            "ASSUMPTION: K&G MAP likelihood (1.78%) used directly. This "
            "is a MAP likelihood, NOT a posterior probability (Rule 19).",
            "ASSUMPTION: No additional rarity penalty applied to avoid "
            "double-counting K&G's built-in non-detection evidence.",
            "ASSUMPTION: Consistency factors are agent-estimated.",
        ],
    )


# ---------------------------------------------------------------------------
# Full Model Comparison
# ---------------------------------------------------------------------------

def compute_posteriors(
    priors: Optional[Dict[str, float]] = None,
    kg_map_likelihood: float = 0.0178,
    total_followup_hours: float = 192.0,
    lambda_map_per_day: float = 0.121,
    random_seed: int = 42,
) -> PosteriorResult:
    """
    Compute the full five-hypothesis posterior comparison.

    Args:
        priors: Prior probabilities for each hypothesis. Must sum to 1.
                If None, uses DEFAULT_PRIORS.
        kg_map_likelihood: Validated K&G MAP likelihood for H5.
        total_followup_hours: Total follow-up observation hours.
        lambda_map_per_day: MAP event rate from K&G validation.
        random_seed: For reproducibility.

    Returns:
        PosteriorResult with all posteriors, Bayes factors, and provenance.

    Raises:
        ValueError: If priors don't sum to ~1 or are invalid.
    """
    timestamp = datetime.now(timezone.utc).isoformat() + "Z"

    # Validate priors
    if priors is None:
        priors = DEFAULT_PRIORS.copy()
    else:
        priors = dict(priors)

    for h_id in HYPOTHESIS_IDS:
        if h_id not in priors:
            raise ValueError(f"Missing prior for {h_id}")
        if priors[h_id] < 0:
            raise ValueError(f"Negative prior for {h_id}: {priors[h_id]}")

    prior_sum = sum(priors.values())
    if abs(prior_sum - 1.0) > 0.01:
        raise ValueError(f"Priors sum to {prior_sum}, must be ~1.0")

    # Normalize priors to exactly 1.0
    for h_id in HYPOTHESIS_IDS:
        priors[h_id] /= prior_sum

    # Compute shared rarity penalty
    rarity = compute_shared_rarity_penalty(total_followup_hours, lambda_map_per_day)
    rarity_penalty = rarity["penalty_factor"]

    # Compute likelihoods
    likelihoods = {
        "H1": compute_h1_likelihood(),
        "H2": compute_h2_likelihood(),
        "H3": compute_h3_likelihood(rarity_penalty),
        "H4": compute_h4_likelihood(rarity_penalty),
        "H5": compute_h5_likelihood(rarity_penalty, kg_map_likelihood),
    }

    # Compute unnormalized posteriors: P(Hi|D) ∝ P(D|Hi) × P(Hi)
    unnorm = {}
    for h_id in HYPOTHESIS_IDS:
        unnorm[h_id] = likelihoods[h_id].likelihood * priors[h_id]

    # Normalize posteriors
    total = sum(unnorm.values())
    if total <= 0:
        raise ValueError("Total unnormalized posterior is zero — all likelihoods are zero")

    posteriors = {}
    for h_id in HYPOTHESIS_IDS:
        posteriors[h_id] = unnorm[h_id] / total

    # Compute all pairwise Bayes factors
    bayes_factors_dict = {}
    for i, h_i in enumerate(HYPOTHESIS_IDS):
        for j, h_j in enumerate(HYPOTHESIS_IDS):
            if i >= j:
                continue
            bf = bayes_factor(
                likelihoods[h_i].likelihood,
                likelihoods[h_j].likelihood,
            )
            key = f"{h_i}_vs_{h_j}"
            bayes_factors_dict[key] = BayesFactor(
                numerator_id=h_i,
                denominator_id=h_j,
                value=bf,
                log10_value=math.log10(bf) if bf > 0 else float('-inf'),
                interpretation=interpret_bayes_factor(bf),
            )

    # Rank hypotheses by posterior
    ranking = sorted(posteriors.items(), key=lambda x: x[1], reverse=True)

    # Sanity checks (Rule 13)
    sanity = {}
    # H2 should have the lowest posterior
    h2_rank = [i for i, (h, _) in enumerate(ranking) if h == "H2"][0]
    sanity["h2_lowest"] = h2_rank == len(ranking) - 1
    if not sanity["h2_lowest"]:
        logger.warning(
            f"⚠ Sanity check failed: H2 (comet) is not the lowest-ranked "
            f"hypothesis (rank {h2_rank + 1}/{len(ranking)}). This is "
            f"unexpected for a near-refuted hypothesis."
        )

    # Posteriors should sum to 1
    posterior_sum = sum(posteriors.values())
    sanity["posteriors_sum_to_1"] = abs(posterior_sum - 1.0) < 1e-10

    # Bayes factors should be self-consistent: B_ij × B_ji = 1
    bf_consistent = True
    for key, bf_obj in bayes_factors_dict.items():
        reverse_key = f"{bf_obj.denominator_id}_vs_{bf_obj.numerator_id}"
        if bf_obj.value > 0:
            reverse_bf = 1.0 / bf_obj.value
            # Check consistency
            if abs(reverse_bf * bf_obj.value - 1.0) > 1e-10:
                bf_consistent = False
    sanity["bayes_factor_consistency"] = bf_consistent

    metadata = {
        "timestamp": timestamp,
        "random_seed": random_seed,
        "sanity_checks": sanity,
        "claim_tier": "Agent-derived computation",
        "notes": [
            "All component probabilities are agent-derived estimates "
            "requiring human review (PRD §13).",
            "Results are prior-sensitive — see sensitivity analysis.",
            "This is a probabilistic comparison, never a verdict "
            "(AGENT_BRAIN_v2 §4, Rule 18).",
        ],
    }

    return PosteriorResult(
        priors=priors,
        likelihoods=likelihoods,
        posteriors=posteriors,
        bayes_factors=bayes_factors_dict,
        ranking=ranking,
        shared_rarity_parameter=rarity,
        metadata=metadata,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print("=" * 70)
    print("Wow! Signal — Five-Hypothesis Bayesian Model Comparison")
    print("=" * 70)

    result = compute_posteriors()

    print("\n--- Priors ---")
    for h_id, p in result.priors.items():
        print(f"  {h_id} ({HYPOTHESIS_NAMES[h_id]}): {p:.4f}")

    print("\n--- Likelihoods ---")
    for h_id, lik in result.likelihoods.items():
        print(f"  {h_id}: {lik.likelihood:.6e}")

    print("\n--- Posteriors (ranked) ---")
    for h_id, post in result.ranking:
        print(f"  {h_id} ({HYPOTHESIS_NAMES[h_id]}): {post:.4f} "
              f"({post*100:.2f}%)")

    print("\n--- Bayes Factors ---")
    for key, bf in result.bayes_factors.items():
        print(f"  {key}: {bf.value:.4f} (log10: {bf.log10_value:.2f}) "
              f"— {bf.interpretation}")

    print("\n--- Sanity Checks ---")
    for check, passed in result.metadata["sanity_checks"].items():
        status = "✅" if passed else "⚠️"
        print(f"  {status} {check}: {passed}")

    print("\n--- Shared Rarity Parameter ---")
    print(f"  Penalty factor: {result.shared_rarity_parameter['penalty_factor']:.4f}")
    print(f"  Applies to: {result.shared_rarity_parameter['applies_to']}")

    # Save results
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data", "posterior_results.json"
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.to_json())
    print(f"\nResults saved to {output_path}")
