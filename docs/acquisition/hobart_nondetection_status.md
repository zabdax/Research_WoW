# Hobart Non-Detection Status Register

Date: 2026-08-25 · Scope: MASTER DIRECTIVE §12 ·
**Rule in force:** absence of detection records ≠ non-detection. Only an
explicit search outcome or a fully reconstructable search procedure may ever
support a non-detection statement.

| campaign | exposure | searched interval | candidate procedure | threshold | RFI handling | reported outcome | evidence | completeness | usable for likelihood? |
|---|---|---|---|---|---|---|---|---|---|
| 1998–99 correlator era | 122 ACF products; six documented 1999 sessions (+1998 DOY278–282 undocumented narrative) | session windows in top-level README (with documented incidents) | UNKNOWN (SAS σ-space plots imply a procedure; rules not archived) | MISSING | MISSING | UNVERIFIED — Gray & Ellingsen 2002 exists (DOI 10.1086/342646) but text unreadable locally; no outcome extracted | archive + bibliographic metadata | UNKNOWN (GAP-HOB-001) | **NO** |
| 2010-08-16 | 09:31:38–15:42:33 UT; drive-freeze gap 12:54–13:25; VLBI handover 15:42 | same, minus unverified-quality intervals | NONE ARCHIVED | MISSING | MISSING | NONE IN ARCHIVE | header index + logs | UNKNOWN | **NO** |
| 2013 tests (DOY189/192/198/199) | four sessions, Jul 8–18 | session spans via header index | NONE ARCHIVED | MISSING | MISSING | NONE IN ARCHIVE | header index | UNKNOWN | **NO** |
| 2013 fields (218/219/256/258) | Aug 6–Sep 15 spans | session spans via header index | NONE ARCHIVED | MISSING | MISSING | NONE IN ARCHIVE | header index | UNKNOWN | **NO** |
| 2014 fields (205/283) | Jul 24; Oct 10–11 spans | session spans via header index | NONE ARCHIVED | MISSING | MISSING | NONE IN ARCHIVE | header index | UNKNOWN | **NO** |

Standing consequences (enforced by tests):
1. Every "usable for likelihood" entry is NO; none may be flipped without
   GAP-HOB-005..009 closing through explicit evidence.
2. No P(no detection | H5) quantity, numerical or symbolic, has been derived
   from this archive, and none may be until the table above changes.
3. Data products (81,913 spectra) remain available for future noise/
   interference characterization — that is a different activity from claiming
   search outcomes.
