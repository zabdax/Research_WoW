"""Common interfaces for revised model-conditional inference.

No model may return a hand-assigned evidence scalar. A concrete model must
expose its parameters, provenance, and an observation likelihood.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Mapping, Protocol

from research.data.observation import ObservationBundle


class RandomGenerator(Protocol):
    """Minimal random interface used by posterior predictive models."""


@dataclass(frozen=True)
class ModelMetadata:
    identifier: str
    name: str
    mechanism: str
    readiness: str
    limitations: tuple[str, ...]


class HypothesisModel(ABC):
    metadata: ModelMetadata

    @abstractmethod
    def parameter_prior_description(self) -> Mapping[str, str]:
        """Return normalized-prior requirements and provenance constraints."""

    @abstractmethod
    def log_likelihood(self, observation: ObservationBundle, parameters: Mapping[str, float]) -> float:
        """Return log P(D | theta, H); bounds must be handled as censored data."""

    @abstractmethod
    def followup_log_likelihood(
        self, observation: ObservationBundle, parameters: Mapping[str, float]
    ) -> float:
        """Return campaign-specific follow-up likelihood, not a pooled scalar."""

    @abstractmethod
    def sample_predictive(self, rng: RandomGenerator, parameters: Mapping[str, float]) -> Mapping[str, float]:
        """Generate observable quantities for posterior predictive checks."""
