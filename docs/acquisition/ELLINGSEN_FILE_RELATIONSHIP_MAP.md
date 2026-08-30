# Ellingsen/Hobart Archive — File Relationship Map

Status: forensic · Date: 2026-08-25 · All relationships below are established
from README statements, embedded headers, timestamps inside file content, or
verified byte-identity — never from filename similarity alone.

## 1. Provenance chain (conceptual)

```
campaign (1998–99 | 2010 | 2013/14)
   │
   ├── observing session (per DOY / per .rpf archive)
   │       ├── acquisition control  → bruce_*.log, ricky_*.log
   │       ├── raw correlator data  → *.rpf (RPFITS)   [2010, 2013/14]
   │       │                          wYYDOYNNN.fit.gz (ACF FITS) [1998–99]
   │       ├── calibration          → bruce_10228.fit + ricky_10228.log + 2010obs/README
   │       ├── pointing metadata    → positions/telescope_pos_*.txt, dump headers
   │       └── processing           → wow.py (ASAP) → fileN-scanM-polP.txt dumps
   │                                        → tar-bundled by donor (wow_*.tar.gz)
   └── statistical output (1998 era) → *.gsf.gz (SAS/GRAPH PostScript plots)
publication                            → wow_published.pdf
```

## 2. Established edges (with evidence)

### 1998–99 correlator era
- `data/w98278xx–w98282xx.fit.gz`, `data/w99076xx–w9910004.fit.gz` — sequence
  defined by filenames (`wYYDOYNNN`); each file self-identifies via
  `DATE/ORIGIN='UTAS'/INSTRUME='CORRELATOR'`. **No header links** to sessions;
  session narratives come only from the top-level README (1999 portion only).
- `pl-distr.gsf.gz`, `sp-pl1.gsf.gz`, `sp-pl1c.gsf.gz`, `sp-plt5.gsf.gz` —
  SAS PROC GPLOT outputs dated 1998-09-26/10-06/10-07/10-10, i.e.
  contemporaneous with the 1998 DOY 278+ spectra; plot variables
  (SIGMA_RD, SIGMA_P vs TIME×CHANNEL, MAX_SIG vs CHANNEL) are search-space
  statistics. Edge to specific .fit.gz files: **NOT ESTABLISHED** (no
  identifiers embedded).
- `wow_published.pdf` — PDF metadata page range "967..971" matches ApJ
  578:967–971; content identity INFERRED (Gray & Ellingsen 2002), unverified.

### 2010 campaign (2010obs/)
- `c102280930.rpf`, `c102281100.rpf`, `c102281325.rpf`
  (in part -002) ⇢ **documented mapping** in 2010obs/README:
  `wow_extract('c102280930.rpf') → "file1"`,
  `('c102281100.rpf','file2')`, `('c102281325.rpf','file3')`.
- `wow.py` ⇢ all `file{1,2,3}-scanM-pol{1,2}.txt`: script writes exactly this
  name pattern from those three inputs (DOCUMENTED). The integer after
  "scan" is the ASAP cycle counter `c`, which increments globally within one
  call — it is **not** guaranteed to be the correlator scan ID (INFERRED from
  code; authoritative per-file time/position come from the dump headers).
- `bruce_10228.fit` ⇢ `ricky_10228.log`: log's first line names the FITS file;
  its eight Source/CAL and SEFD/CAL pairs match the README table exactly and
  the TSYS columns of the FITS rows (verified numerically).
- `bruce_10228.log` ⇢ same JD 2455424 (=2010-08-16); documents the NGC6334 /
  Hydra A / 3C348 command sequence preceding program data.
- loose `file*-scan*-pol*.txt` (6,500 files, parts -001/-002) =
  `spectra.tar.gz` members (part -002): name sets identical 6500↔6500,
  sampled hashes identical ⇒ **exact duplicate packaging** (keep both per
  no-delete rule).
- Dump header `Position: J2000 19:23:03.0 -26.43.24.0` ⇢ on-position;
  `Name: wow_off1/wow_off2` ⇢ −25:43:24 / −27:43:24 (±1° Dec offsets).

### 2013/14 campaigns (2013obs/)
- `c<YY><DDD><HHMM>.rpf` naming ⇢ UT start of each raw archive (INFERRED from
  pattern consistency across 29 files; matches bruce log JDs on doy 189/192/205).
- `wow_<field>_<year>doy<DDD>.tar.gz` ⇢ member names embed the same tag
  (`2013DOY192-scan…`, `./2013DOY218FILE1-scan…`) ⇒ tarball↔member link is
  DOCUMENTED by construction (donor packing command in 2013obs/README).
- Member `FILE1/FILE2` suffixes ⇢ field1/field2 pointings; dump headers give
  Name wow_f1 / wow_f2 with Position 19:25:28 / 19:28:17 (both labelled J2000,
  Dec −26:57) — cross-checked against live-pages extracts (antenna tracked
  19:28:17 on one 2013 day, 19:25:28 on 2014-10-10).
- `bruce_13189.log` / `bruce_13192.log` / `bruce_14205.log` ⇢ JD day numbers
  match DOY 189/192/205 sessions; they document control sessions, not the full
  integrations (rpf coverage exceeds log spans).
- `positions/telescope_pos_YYYY_DOY.txt` ⇢ SQL recipe documented in
  2013obs/README; internal time-of-day only. Filename-vs-SQL-filter day
  labeling ambiguous (see limitations).
- `Mt Pleasant 2013 Observing PLAN (draft 2013-07-22).xls` — OLE2/BIFF
  workbook, not parsed in this pass (no reader in environment); role:
  planning documentation.
- `zenith`-named dumps appear inside test/field tarballs at Dec-shifted
  position strings (−27:57/−28:57/−36:57): association zenith-park records,
  INFERRED; exact purpose UNKNOWN.

## 3. Unresolved relationship questions
1. Which .rpf archives correspond to which 2013/14 tarball sessions (no
   explicit mapping received; would require reading RPFITS contents with an
   RPFITS-aware tool, which is unavailable here)?
2. Whether the four 1998 .gsf plots reference the surviving w98* files or
   additional (unsupplied) data.
3. Where the outputs of any 2010–2014 candidate searches are (none included).
4. Whether `yf0` (always 0) is a placeholder for a flagged/fitted channel set.
