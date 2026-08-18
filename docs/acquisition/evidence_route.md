# Evidential Input Acquisition Route

## Principle

An import is not evidence merely because it arrives from an API. Every record must pass identity, authority, epoch/frame, units, uncertainty-status, and inference-role checks. Missing uncertainty is recorded as missing.

## Current public acquisition result

The project has retrieved a NASA/JPL Horizons geocentric observer ephemeris for the selected 2008 orbit solution of 266P/Christensen for 1977-08-15. It is suitable for a **geocentric geometry sensitivity calculation only**. It does not supply covariance, does not establish the relevant source object, does not model cometary brightness, and cannot replace a calibrated topocentric Big Ear beam response.

## Remaining authoritative routes

- **Big Ear response and RFI:** archival technical/engineering/observing documentation; prepared request in `research/data/requests/big_ear_archive_request.md`.
- **Follow-up selection:** campaign logs/completeness records; prepared request in `research/data/requests/followup_data_request.md`.
- **H3/H4:** peer-reviewed physical/population models and declared prior families; software cannot infer these objectively from the current repository.

The machine-readable `research/data/acquisition_register.yaml` is the authoritative project ledger for status and validation requirements.
