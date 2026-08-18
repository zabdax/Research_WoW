# Revised Source and Evidence Status

## Evidence-class convention

`VERIFIED` means the numerical claim was checked against the locally cached cited material and has a locator. It does **not** mean independent replication, physical validation, or peer-reviewed status.

Every revised analysis record must separately state:

1. bibliographic status: peer-reviewed, preprint, technical report, web archive, or secondary source;
2. extraction status: `VERIFIED`, `PARTIAL`, `UNVERIFIED`, or `UNVERIFIED-PRIMARY`;
3. inference role: direct observation, physical-model parameter, model prior, or exploratory context.

## Current high-impact source limitations

- Méndez et al. (2024) and Méndez et al. (2025) are retained as arXiv preprints in the source cache. Their proposal is a hypothesis source, not independent confirmation of H3.
- The H3 reference flux configuration documented in the legacy ledger is approximately 1 mJy at 0.4 kpc, while the Wow! flux is recorded as a lower bound of 250 Jy. A revised H3 model must explicitly derive/marginalize that gap.
- Kipping & Gray (2022) constrains the H5 stochastic-repeater model. Its inferred rate cannot be transferred to H3/H4 without model-specific derivation.
- META campaign details remain `UNVERIFIED-PRIMARY` in the legacy ledger.
- Web/blog material can provide discovery context but cannot be sole support for an evidential likelihood term.

## Gate

The source-audit command validates required provenance fields for revised structured inputs. It is a necessary but insufficient check: high-impact records also require manual source review and model-role review before confirmatory use.
