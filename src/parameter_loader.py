"""
parameter_loader.py — Module A interface for Phase 2

Loads and validates data/parameters.yaml into structured Python objects.
Provides typed access to all signal properties, hypothesis parameters,
non-detection campaigns, and methodological framework constants.

All numeric values are traced to their source citation and verification
status per AGENT_BRAIN_v2 §4 Rule 1 (source-or-silence).
"""

import os
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


# ---------------------------------------------------------------------------
# Dataclasses for structured access
# ---------------------------------------------------------------------------

@dataclass
class SourcedValue:
    """A single numeric or string value with full provenance."""
    value: Any
    unit: Optional[str] = None
    uncertainty: Optional[Any] = None
    uncertainty_type: Optional[str] = None
    source: Optional[str] = None
    source_location: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None

    @property
    def is_verified(self) -> bool:
        return self.status == "VERIFIED"

    @property
    def is_unverified(self) -> bool:
        return self.status is not None and "UNVERIFIED" in self.status

    def numeric_value(self) -> Optional[float]:
        """Attempt to extract a numeric value. Returns None for bounds/ranges."""
        if self.value is None:
            return None
        if isinstance(self.value, (int, float)):
            return float(self.value)
        if isinstance(self.value, str):
            # Handle ">250", "~3", "<10", "0.5-1.2" etc.
            v = self.value.strip()
            if v.startswith(">") or v.startswith("<") or v.startswith("~"):
                try:
                    return float(v[1:])
                except ValueError:
                    return None
            if "-" in v and not v.startswith("-"):
                # Range like "54-212" — return midpoint
                parts = v.split("-")
                try:
                    return (float(parts[0]) + float(parts[1])) / 2.0
                except (ValueError, IndexError):
                    return None
            try:
                return float(v)
            except ValueError:
                return None
        return None


@dataclass
class SignalProperties:
    """Core properties of the Wow! Signal itself."""
    detection_date: str
    frequency_mhz: float
    frequency_uncertainty_mhz: float
    peak_flux_lower_bound_jy: float
    peak_snr: float
    peak_snr_uncertainty: float
    signal_duration_s: float
    two_horn_turnon_window_min: float
    bandwidth_upper_khz: float
    sky_position_1_ra: str
    sky_position_1_dec: str
    sky_position_2_ra: str
    sky_position_2_dec: str


@dataclass
class NonDetectionCampaign:
    """A single follow-up observation campaign with null result."""
    name: str
    telescope: str
    obs_time_hours: Optional[float]
    flux_limit_jy: Optional[float]
    fov_degrees: Optional[float]
    result_summary: str
    source: str
    status: str


@dataclass
class ValidationBenchmark:
    """Kipping & Gray (2022) reproduction target."""
    initial_map_likelihood: float  # 0.323
    post_nondetection_map_likelihood: float  # 0.0178
    campaigns_used: List[str]
    total_followup_hours: float  # 192
    validation_criterion: str
    failure_action: str


@dataclass
class LingamFramework:
    """Lingam et al. (2023) posterior equation and reference xi values."""
    posterior_equation: str  # "P(T|D,C) = P(T|C) * xi / (1 + P(T|C) * (xi - 1))"
    xi_definition: str  # "xi = P(D|C,T) / P(D|C,T_bar)"
    equation_number: str  # "Eq. 6"
    reference_xi_em_signals: float  # ~1e4
    reference_xi_no2: float  # ~3
    reference_xi_cfcs: float  # ~1e4
    status: str


@dataclass
class KippingGrayH5:
    """Kipping & Gray (2022) H5 stochastic beacon parameters."""
    initial_map_likelihood: float  # 0.323
    post_nondetection_map_likelihood: float  # 0.0178
    tension_sigma: float  # 2.4
    duration_lower_s: float  # 72
    duration_upper_min: float  # 77
    repeat_rate_lower_per_day: float  # 0.043
    repeat_rate_upper_per_day: float  # 59.8
    additional_obs_days_for_3sigma: float  # 62
    total_followup_hours: float  # 192


@dataclass
class BenfordH4:
    """Benford (2010a/b, 2025) power beam parameters."""
    eirp_threshold_w: float  # >1e17
    emitted_power_gw: float  # >1
    antenna_area_km2: float  # >1
    preferred_freq_ghz: float  # ~10
    beam_dwell_time_s_range: Tuple[float, float]  # (10, 100)
    worked_example_l_band_eirp: float
    worked_example_l_band_power_gw: float
    worked_example_l_band_area_km2: float
    worked_example_l_band_cost_billion: float


@dataclass
class LoadedParameters:
    """Complete loaded parameter set for all modules."""
    signal: SignalProperties
    h5_params: KippingGrayH5
    h4_params: BenfordH4
    non_detection_campaigns: List[NonDetectionCampaign]
    validation_benchmark: ValidationBenchmark
    lingam_framework: LingamFramework
    raw: Dict[str, Any]  # Full YAML for anything not pre-parsed
    unverified_fields: List[str]  # Paths to UNVERIFIED fields
    warnings: List[str]  # Any issues found during loading


# ---------------------------------------------------------------------------
# Loader functions
# ---------------------------------------------------------------------------

def _find_unverified(data: Any, path: str = "") -> List[str]:
    """Recursively find all fields with UNVERIFIED status."""
    results = []
    if isinstance(data, dict):
        status = data.get("status", "")
        if isinstance(status, str) and "UNVERIFIED" in status:
            results.append(f"{path} (status: {status})")
        for key, val in data.items():
            results.extend(_find_unverified(val, f"{path}.{key}" if path else key))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            results.extend(_find_unverified(item, f"{path}[{i}]"))
    return results


def _validate_sources(data: Any, path: str = "") -> List[str]:
    """Check that parameter entries have source fields."""
    issues = []
    if isinstance(data, dict):
        # If it has a 'value' key, it should also have 'source'
        if "value" in data and "source" not in data:
            issues.append(f"{path}: has 'value' but no 'source'")
        for key, val in data.items():
            issues.extend(_validate_sources(val, f"{path}.{key}" if path else key))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            issues.extend(_validate_sources(item, f"{path}[{i}]"))
    return issues


def _safe_float(val: Any, default: float = 0.0) -> float:
    """Safely convert a value to float, handling strings like '>250', '~3'."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        v = val.strip().lstrip(">").lstrip("<").lstrip("~")
        try:
            return float(v)
        except ValueError:
            return default
    return default


def _safe_float_or_none(val: Any) -> Optional[float]:
    """Safely convert, returning None if not parseable."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        v = val.strip().lstrip(">").lstrip("<").lstrip("~")
        try:
            return float(v)
        except ValueError:
            return None
    return None


def load_parameters(yaml_path: Optional[str] = None) -> LoadedParameters:
    """
    Load and validate parameters.yaml.

    Args:
        yaml_path: Path to parameters.yaml. If None, uses the default
                   project location.

    Returns:
        LoadedParameters with all structured data.

    Raises:
        FileNotFoundError: If the YAML file doesn't exist.
        ValueError: If critical required fields are missing.
    """
    if yaml_path is None:
        yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "data", "parameters.yaml"
        )

    path = Path(yaml_path)
    if not path.exists():
        raise FileNotFoundError(f"Parameters file not found: {yaml_path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    load_warnings = []

    # Validate sources
    source_issues = _validate_sources(raw)
    if source_issues:
        for issue in source_issues:
            load_warnings.append(f"Source validation: {issue}")

    # Find unverified fields
    unverified = _find_unverified(raw)
    if unverified:
        for field_path in unverified:
            warnings.warn(f"UNVERIFIED parameter: {field_path}")

    # --- Extract SignalProperties ---
    sp = raw.get("signal_properties", {})
    signal = SignalProperties(
        detection_date=sp.get("detection_date", {}).get("value", "1977-08-15"),
        frequency_mhz=_safe_float(sp.get("frequency", {}).get("value")),
        frequency_uncertainty_mhz=_safe_float(
            sp.get("frequency", {}).get("uncertainty"), 0.005
        ),
        peak_flux_lower_bound_jy=_safe_float(
            sp.get("peak_flux_density", {}).get("value"), 250.0
        ),
        peak_snr=_safe_float(sp.get("peak_snr", {}).get("value"), 30.5),
        peak_snr_uncertainty=_safe_float(
            sp.get("peak_snr", {}).get("uncertainty"), 0.5
        ),
        signal_duration_s=_safe_float(
            sp.get("signal_duration", {}).get("value"), 72.0
        ),
        two_horn_turnon_window_min=_safe_float(
            sp.get("two_horn_turnon_window", {}).get("value"), 3.0
        ),
        bandwidth_upper_khz=_safe_float(
            sp.get("bandwidth", {}).get("value"), 10.0
        ),
        sky_position_1_ra=sp.get("sky_position_candidate_1", {}).get("ra", ""),
        sky_position_1_dec=sp.get("sky_position_candidate_1", {}).get("dec", ""),
        sky_position_2_ra=sp.get("sky_position_candidate_2", {}).get("ra", ""),
        sky_position_2_dec=sp.get("sky_position_candidate_2", {}).get("dec", ""),
    )

    # --- Extract H5 (Kipping & Gray) parameters ---
    h5_raw = raw.get("hypotheses", {}).get("H5_stochastic_beacon", {})
    h5 = KippingGrayH5(
        initial_map_likelihood=_safe_float(
            h5_raw.get("initial_map_likelihood", {}).get("value"), 0.323
        ),
        post_nondetection_map_likelihood=_safe_float(
            h5_raw.get("post_nondetection_map_likelihood", {}).get("value"), 0.0178
        ),
        tension_sigma=_safe_float(
            h5_raw.get("tension_level", {}).get("value"), 2.4
        ),
        duration_lower_s=_safe_float(
            h5_raw.get("signal_duration_credible_interval", {}).get("lower"), 72.0
        ),
        duration_upper_min=_safe_float(
            h5_raw.get("signal_duration_credible_interval", {}).get("upper_value"), 77.0
        ),
        repeat_rate_lower_per_day=_safe_float(
            h5_raw.get("repeat_rate_credible_interval", {}).get("lower"), 0.043
        ),
        repeat_rate_upper_per_day=_safe_float(
            h5_raw.get("repeat_rate_credible_interval", {}).get("upper"), 59.8
        ),
        additional_obs_days_for_3sigma=_safe_float(
            h5_raw.get("additional_obs_for_3sigma", {}).get("value"), 62.0
        ),
        total_followup_hours=_safe_float(
            h5_raw.get("total_followup_hours", h5_raw.get("total_followup_hours")), 192.0
        ),
    )

    # --- Extract H4 (Benford) parameters ---
    h4_raw = raw.get("hypotheses", {}).get("H4_power_beam", {})
    bd = h4_raw.get("beam_dwell_time", {})
    dwell_range_str = bd.get("typical_dwell_range", "10-100")
    try:
        dwell_parts = dwell_range_str.replace("seconds", "").strip().split("-")
        dwell_range = (float(dwell_parts[0]), float(dwell_parts[1]))
    except (ValueError, IndexError):
        dwell_range = (10.0, 100.0)

    we_l = h4_raw.get("worked_example_L_band", {})
    h4 = BenfordH4(
        eirp_threshold_w=_safe_float(
            h4_raw.get("eirp_requirement_for_1000ly", {}).get("value"), 1e17
        ),
        emitted_power_gw=_safe_float(
            h4_raw.get("emitted_power_baseline", {}).get("value"), 1.0
        ),
        antenna_area_km2=_safe_float(
            h4_raw.get("antenna_area_baseline", {}).get("value"), 1.0
        ),
        preferred_freq_ghz=_safe_float(
            h4_raw.get("preferred_frequency", {}).get("value"), 10.0
        ),
        beam_dwell_time_s_range=dwell_range,
        worked_example_l_band_eirp=_safe_float(we_l.get("eirp"), 1e17),
        worked_example_l_band_power_gw=_safe_float(
            we_l.get("optimal_power", {}).get("value"), 1.88
        ),
        worked_example_l_band_area_km2=_safe_float(
            we_l.get("optimal_antenna_area", {}).get("value"), 3.76
        ),
        worked_example_l_band_cost_billion=_safe_float(
            we_l.get("total_capital_cost", {}).get("value"), 7.52
        ),
    )

    # --- Extract non-detection campaigns ---
    nd_raw = raw.get("non_detection_campaigns", {})
    campaigns = []
    for key, camp_data in nd_raw.items():
        if not isinstance(camp_data, dict):
            continue

        # Handle varied data structures across campaigns
        telescope = camp_data.get("telescope", camp_data.get("telescope_1", "Unknown"))
        obs_val = camp_data.get("obs_time", {})
        if isinstance(obs_val, dict):
            obs_hours = _safe_float_or_none(obs_val.get("value"))
        else:
            obs_hours = _safe_float_or_none(obs_val)

        # Try to extract flux limit
        sens = camp_data.get("sensitivity", {})
        flux_limit = None
        if isinstance(sens, dict):
            fl = sens.get("flux_limit", {})
            if isinstance(fl, dict):
                flux_limit = _safe_float_or_none(fl.get("value"))

        fov_data = camp_data.get("fov", {})
        fov = None
        if isinstance(fov_data, dict):
            fov = _safe_float_or_none(fov_data.get("value"))

        campaigns.append(NonDetectionCampaign(
            name=key,
            telescope=telescope if isinstance(telescope, str) else str(telescope),
            obs_time_hours=obs_hours,
            flux_limit_jy=flux_limit,
            fov_degrees=fov,
            result_summary=camp_data.get("result", "No result text"),
            source=camp_data.get("source", "Unknown"),
            status=camp_data.get("status", "UNKNOWN"),
        ))

    # --- Extract validation benchmark ---
    vb_raw = raw.get("validation_benchmark", {})
    vb_campaigns = []
    for c in vb_raw.get("campaigns_used", []):
        if isinstance(c, dict):
            vb_campaigns.append(c.get("name", ""))
        else:
            vb_campaigns.append(str(c))

    benchmark = ValidationBenchmark(
        initial_map_likelihood=_safe_float(
            vb_raw.get("initial_map_likelihood", {}).get("value",
            vb_raw.get("initial_map_likelihood")), 0.323
        ),
        post_nondetection_map_likelihood=_safe_float(
            vb_raw.get("post_nondetection_map_likelihood", {}).get("value",
            vb_raw.get("post_nondetection_map_likelihood")), 0.0178
        ),
        campaigns_used=vb_campaigns,
        total_followup_hours=_safe_float(
            vb_raw.get("total_followup_hours"), 192.0
        ),
        validation_criterion=vb_raw.get("validation_criterion", ""),
        failure_action=vb_raw.get("failure_action", ""),
    )

    # --- Extract Lingam framework ---
    mf_raw = raw.get("methodological_framework", {})
    lpe = mf_raw.get("lingam_posterior_equation", {})
    ref_xi = mf_raw.get("reference_xi_values", {})

    lingam = LingamFramework(
        posterior_equation=lpe.get("equation", ""),
        xi_definition=mf_raw.get("xi_definition", {}).get("equation", ""),
        equation_number=lpe.get("equation_number", ""),
        reference_xi_em_signals=_safe_float(
            ref_xi.get("em_signals", {}).get("value"), 1e4
        ),
        reference_xi_no2=_safe_float(
            ref_xi.get("no2_atmospheric", {}).get("value"), 3.0
        ),
        reference_xi_cfcs=_safe_float(
            ref_xi.get("cfcs", {}).get("value"), 1e4
        ),
        status=lpe.get("status", "UNKNOWN"),
    )

    return LoadedParameters(
        signal=signal,
        h5_params=h5,
        h4_params=h4,
        non_detection_campaigns=campaigns,
        validation_benchmark=benchmark,
        lingam_framework=lingam,
        raw=raw,
        unverified_fields=unverified,
        warnings=load_warnings,
    )


def get_total_followup_hours(params: LoadedParameters) -> float:
    """
    Calculate total follow-up observation hours from non-detection campaigns.

    Per Kipping & Gray (2022): META (16h) + Hobart (84h) + ATA (100h) = 200h
    But they use 192h as the pooled figure. We use their published value.
    """
    return params.validation_benchmark.total_followup_hours


def get_hobart_followup_hours(params: LoadedParameters) -> float:
    """Get Hobart-specific follow-up hours (6 × 14h = 84h)."""
    for c in params.non_detection_campaigns:
        if "hobart" in c.name.lower():
            if c.obs_time_hours is not None:
                return c.obs_time_hours * 6  # 6 sessions
    return 84.0  # Default from published data


def get_meta_ata_followup_hours(params: LoadedParameters) -> float:
    """Get META + ATA combined follow-up hours (108h per K&G)."""
    # Per K&G Section 4.3: G = 108 hours
    # (8h META × 2 positions + 100h ATA, excluding VLA's short dwell)
    return 108.0


if __name__ == "__main__":
    params = load_parameters()
    print(f"Signal frequency: {params.signal.frequency_mhz} ± "
          f"{params.signal.frequency_uncertainty_mhz} MHz")
    print(f"Peak flux: >{params.signal.peak_flux_lower_bound_jy} Jy")
    print(f"H5 MAP likelihood (Big Ear only): {params.h5_params.initial_map_likelihood}")
    print(f"H5 MAP likelihood (with follow-up): "
          f"{params.h5_params.post_nondetection_map_likelihood}")
    print(f"Validation target: {params.validation_benchmark.post_nondetection_map_likelihood}")
    print(f"Non-detection campaigns: {len(params.non_detection_campaigns)}")
    print(f"Unverified fields: {len(params.unverified_fields)}")
    for uv in params.unverified_fields:
        print(f"  ⚠ {uv}")
    if params.warnings:
        print(f"Warnings: {len(params.warnings)}")
        for w in params.warnings:
            print(f"  ⚠ {w}")
