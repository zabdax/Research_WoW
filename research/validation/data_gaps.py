"""Machine-readable outstanding-input report for confirmatory inference."""
from __future__ import annotations

import json

GAPS = {
    "BigEarGeometry": ["archival beam map/calibration", "receiver configuration", "dual-horn pointing/orientation"],
    "H1": ["1977 RFI environment", "receiver/signal-chain documentation", "raw-recording diagnostics"],
    "H2": ["authoritative 1977 comet ephemerides", "ephemeris uncertainty/covariance", "confirmed beam calibration"],
    "H3": ["trigger fluence model", "cloud population and geometry priors", "event-rate distribution", "independent confirmation of proposed analogue mechanism"],
    "H4": ["transmitter population prior", "alignment and sweep distribution", "occurrence/revisit model"],
    "H5": ["independent restricted emulator equivalence", "convergence and uncertainty report"],
    "FollowUp": ["timestamp-level observing windows", "campaign completeness surfaces", "META primary campaign metadata"],
}


def main() -> None:
    print(json.dumps({"confirmatory_comparison_enabled": False, "gaps": GAPS}, indent=2))


if __name__ == "__main__":
    main()
