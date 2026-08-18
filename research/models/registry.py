"""Readiness registry preventing incomplete physical models from producing posteriors."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelReadiness:
    hypothesis: str
    status: str
    blocker: str


READINESS = (
    ModelReadiness("H1", "blocked", "Requires adversarial, provenance-backed RFI mechanism mixture."),
    ModelReadiness("H2", "blocked", "Requires independent ephemeris and Big Ear beam-intersection reconstruction."),
    ModelReadiness("H3", "blocked", "Requires normalized physical flux, geometry, trigger, and event-rate model."),
    ModelReadiness("H4", "blocked", "Requires transmitter-population and alignment model distinct from engineering feasibility."),
    ModelReadiness("H5", "in_progress", "Requires independently validated restricted Kipping--Gray emulator with uncertainty."),
)


def ready_for_comparison() -> bool:
    return all(item.status == "ready" for item in READINESS)
