# Evidential Input Acquisition Route

## Principle

An import is not evidence merely because it arrives from an API. Every record must pass identity, authority, epoch/frame, units, uncertainty-status, and inference-role checks. Missing uncertainty is recorded as missing.

## Current public acquisition result

The project has retrieved two NASA/JPL Horizons geocentric observer ephemerides for 1977-08-15:

- 266P/Christensen (selected 2008 solution `90001240;`)
- 335P/Gibbs = P/2008 Y2 (selected JPL#39 solution `90001326;`)

Both are suitable only for **geocentric geometry sensitivity**. Neither supplies covariance, neither establishes the relevant source object, neither models cometary brightness, and neither replaces a calibrated topocentric Big Ear beam response. They must not be used as confirmatory \(P(D|H_2)\).

## Remaining authoritative routes

- **Big Ear response and RFI:** archival technical/engineering/observing documentation; prepared request in `research/data/requests/big_ear_archive_request.md`.
- **Follow-up selection:** campaign logs/completeness records; prepared request in `research/data/requests/followup_data_request.md`.
- **H3/H4:** peer-reviewed physical/population models and declared prior families; software cannot infer these objectively from the current repository.

The machine-readable `research/data/acquisition_register.yaml` is the authoritative project ledger for status and validation requirements.
