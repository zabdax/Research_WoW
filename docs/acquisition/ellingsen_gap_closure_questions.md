# Follow-Up Questions for Simon Ellingsen — Gap-Closure Round

Draft date: 2026-08-25 · Status: DRAFT for human review before sending ·
Prepared from `research/data/ellingsen_gap_register.yaml` after exhausting the
supplied archive (nothing below is answerable from the received files).

Context for Simon: we have inventoried and hash-frozen the 5.8 GB material you
kindly supplied. It covers what appears to be 1998–99 correlator data, the
2010-08-16 session, and 2013/2014 field sessions. We are **not** asking for
new bulk data — only metadata, intent, and outcomes that you may remember or
may exist in old notes elsewhere. Where we ask about something you have said
you do not remember, even a "that's lost" answer is valuable and will be
recorded as such.

---

## Priority 1 — Observing intent (blocks any spatial interpretation)

1. Does the supplied ~5.8 GB represent the complete surviving Hobart material
   relevant to the Wow! follow-ups, or a selection?
2. For 2013–14: were Field 1 (≈RA 19:25:28, Dec −26°57) and Field 2 (≈RA
   19:28:17, Dec −26°57) intentionally different targets — e.g., the two Big
   Ear horn candidate positions?
3. Were those coordinates meant as J2000 values (our reading of the RPFITS
   `EPOCH='j2000'` cards), and did you derive them by precessing older B1950
   positions? (We notice they match the precessed images of your 1999 README
   grid points to <2 s of time.)
4. What was the intended target for the 2010-08-16 observation at ≈RA 19:23:03,
   Dec −26:43:24, including the ±1° Dec off-pairs (`wow_off1/off2`)?
5. Do any proposal/target-list/scheduling files or notebooks survive anywhere
   (yours, Mt Pleasant operations, or collaborators) recording intended
   coordinates for these campaigns?

## Priority 2 — Search procedure and outcomes (blocks any likelihood use)

6. Were explicit search results recorded for 2010 / 2013 / 2014 (even purely
   internal)?
7. Were there predefined detection thresholds or minimum S/N requirements?
8. Were candidates manually inspected? By whom?
9. Were repeat detections required for anything to count?
10. Were candidates rejected for RFI, baseline structure, persistence,
    polarization behavior, etc.?
11. Does any table/list/report of candidate events — **including rejected
    ones** — survive, with you, Bob Gray, Michael Jaekle, or others?
12. If Bob Gray retained analysis outputs for the newer campaigns, could you
    forward contact details or make an introduction?

## Priority 3 — Calibration semantics

13. In the 2013/2014 ASCII exports, what does the printed "Flux Unit: Jy"
    actually mean given the `wow_extract_fixtsys` path normalizes to a nominal
    Tsys = 500 K? Is it calibrated flux density, an internally normalized
    unit, or something else?
14. Are calibrator scans (e.g., Hydra A) and calibration constants available
    for 2013/2014, inside or outside the `.rpf` archives?
15. Is there any written SEFD/Tsys/cal record for those years analogous to the
    2010 README block (which we can reproduce internally)?

## Priority 4 — Correlator / raw formats

16. Is there documentation (or software) for the 1998–99 autocorrelator
    configuration — bandwidth, lag-to-channel conversion, windowing — needed to
    turn the `w*.fit.gz` ACF dumps into spectra?
17. Can the `.rpf` files be mapped to exact sessions beyond their filenames
    (we have already recovered their embedded source tables: e.g.,
    `wow_f2` at 19:28:17 −26:57)? Anything that adds scan-level times would help.
18. Is ASAP/RPFITS software still obtainable, or could converted copies of key
    `.rpf` archives be produced on your side if ever needed?

## Priority 5 — Timing and selection details

19. What were the dump integration times (we measure a uniform 5 s dump
    cadence in every session)?
20. Was the full recorded time searched, or were parts pre-filtered/excluded?
21. Were any sessions aborted, corrupted, or incomplete beyond what the logs
    show (2010 drive freeze 12:54–13:25 UT; VLBI handover 15:42 UT)?

---

*We appreciate that much of this is 10+ years past. "Unknown/lost" answers
will be logged verbatim as gap-closure results, not treated as failures.*
