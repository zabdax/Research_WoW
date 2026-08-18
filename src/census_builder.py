import pandas as pd

# ---------------------------------------------------------
# Rubrics for Sheikh Axes (Extension as per PRD B1.2)
# ---------------------------------------------------------
def score_detectability(snr):
    """
    Ordinal 1-5 rubric for Detectability based on Signal-to-Noise Ratio (SNR).
    1: SNR < 5 (Barely detectable)
    2: 5 <= SNR < 15 (Weakly detectable)
    3: 15 <= SNR < 25 (Moderately detectable)
    4: 25 <= SNR < 50 (Highly detectable)
    5: SNR >= 50 (Extremely detectable)
    """
    if snr < 5: return 1
    elif snr < 15: return 2
    elif snr < 25: return 3
    elif snr < 50: return 4
    else: return 5

def score_duration(duration_seconds):
    """
    Ordinal 1-5 rubric for Duration.
    Duration here refers strictly to intrinsic signal presence/persistence, 
    NOT the length of the total observing campaign.
    1: < 1 second (Extremely transient)
    2: 1s to 300s (5 min) (Short transient)
    3: 300s to 3600s (1 hr) (Moderate duration)
    4: 3600s to 86400s (1 day) (Extended duration)
    5: > 86400s (Persistent)
    """
    if duration_seconds < 1: return 1
    elif duration_seconds <= 300: return 2
    elif duration_seconds <= 3600: return 3
    elif duration_seconds <= 86400: return 4
    else: return 5

def compute_ambiguity_xi(is_narrowband, has_modulation, resolved_by_spatial_rfi=False, resolved_by_natural_model=False):
    """
    Computes the Lingam et al. (2023) xi factor for the Ambiguity axis.
    xi = P(Data | Tech) / P(Data | Natural)
    
    Rather than hardcoding 1e-4, we explicitly derive the total xi by 
    multiplying the intrinsic xi by subsequent verification evidence xi.
    """
    # 1. Intrinsic Evidence (D_int)
    xi_intrinsic = 1.0
    if is_narrowband:
        xi_intrinsic = 10000.0  # Lingam et al. baseline for unresolved EM signals
    if has_modulation:
        xi_intrinsic *= 100.0
        
    # 2. Post-hoc Verification Evidence (D_verif)
    xi_verification = 1.0
    
    # If the signal persists in off-target beam nod pointings, P(D_spatial | Extraterrestrial) ~ 0
    # and P(D_spatial | RFI) ~ 1. Thus xi_verification = 10^-8
    if resolved_by_spatial_rfi:
        xi_verification = 1e-8
        
    # If the signal is explicitly fit by a verified natural physical model (like DSR),
    # P(D_model | Tech) is very small relative to P(D_model | Natural). Thus xi_verification = 1e-8.
    if resolved_by_natural_model:
        xi_verification = 1e-8

    return xi_intrinsic * xi_verification

# ---------------------------------------------------------
# Candidate Events Data
# ---------------------------------------------------------
events = [
    {
        "id": "wow_1977",
        "name": "Wow! Signal",
        "year": 1977,
        "snr": 30.5,
        "duration_s": 72.0,  # 72s is telescope beam transit time floor, representing the intrinsic presence limit
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": False,
        "resolved_by_natural_model": False,
        "notes": "Intrinsic properties only. 72s is beam transit floor."
    },
    {
        "id": "mini_wow_a",
        "name": "Mendez Mini-Wow Event A",
        "year": 2020,
        "snr": 5.0, # Baseline estimate, reported fluxes are 2 Jy vs noise
        "duration_s": 120.0, # Intrinsic persistence over scan
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": False,
        "resolved_by_natural_model": True,
        "notes": "Mendez et al. 2024 DSR natural candidate A."
    },
    {
        "id": "mini_wow_b",
        "name": "Mendez Mini-Wow Event B",
        "year": 2020,
        "snr": 5.0, 
        "duration_s": 120.0,
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": False,
        "resolved_by_natural_model": True,
        "notes": "Mendez et al. 2024 DSR natural candidate B."
    },
    {
        "id": "mini_wow_c",
        "name": "Mendez Mini-Wow Event C",
        "year": 2020,
        "snr": 5.0, 
        "duration_s": 120.0,
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": False,
        "resolved_by_natural_model": True,
        "notes": "Mendez et al. 2024 DSR natural candidate C."
    },
    {
        "id": "mini_wow_d",
        "name": "Mendez Mini-Wow Event D",
        "year": 2020,
        "snr": 5.0, 
        "duration_s": 120.0,
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": False,
        "resolved_by_natural_model": True,
        "notes": "Mendez et al. 2024 DSR natural candidate D."
    },
    {
        "id": "blc1_2019",
        "name": "BLC1",
        "year": 2019,
        "snr": 15.0, 
        "duration_s": 18000.0, # Intrinsic presence: persisted over ~5 hours of scans
        "is_narrowband": True,
        "has_modulation": False,
        "resolved_by_spatial_rfi": True,
        "resolved_by_natural_model": False,
        "notes": "Confirmed terrestrial intermodulation via off-source spatial verification."
    }
]

# Calculate scores
for e in events:
    e["detectability_score"] = score_detectability(e["snr"])
    e["duration_score"] = score_duration(e["duration_s"])
    e["ambiguity_xi"] = compute_ambiguity_xi(
        e["is_narrowband"], 
        e["has_modulation"], 
        e["resolved_by_spatial_rfi"], 
        e["resolved_by_natural_model"]
    )

df = pd.DataFrame(events)
df.to_csv(r"f:\Research_WoW!\data\census.csv", index=False)
print("Census data exported to census.csv")
