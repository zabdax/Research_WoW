# Simon Questionnaire Change Log (v1 → v2)

Legend — Action ∈ {RETAINED-narrowed, MERGED, REMOVED-locally-answered,
REPHRASED, NEW}. Evidence key: XLS = donor-supplied plan workbook
(`extracted/HOBART_XLS_PLAN_TEXT.txt`); WIDE-SU = `rpfits_su_widescan.json`;
CARDS = `rpfits_card_inventory.json`.

| v1 # | Old question | Action | Reason | v2 result |
|---|---|---|---|---|
| Q1 | Complete archive or selection? | RETAINED-narrowed | still donor-only knowledge (GAP-001) | v2 Q7 (P3) |
| Q2 | Field1 vs Field2 intentionally different targets? | REMOVED-locally-answered | XLS 'Wow Details' documents East/West beam locales deliberately | stated as finding in email intro |
| Q3 | B1950-vs-J2000 interpretation correct? | REMOVED-locally-answered | XLS gives explicit B1950↔J2000 pairs for both locales | same |
| Q4 | Intended target of 2010 position? | RETAINED (unchanged core) | not answered anywhere locally (GAP-004) | v2 Q2 (P0) |
| Q5 | Proposal/target-list/notebook records? | REPHRASED→narrowed | XLS IS such a record for 2013; asking generically wasted effort | folded into v2 Q1/Q11 context |
| Q6 | Explicit search results recorded? | MERGED | same information sink as Q7–Q12 | v2 Q3 (P0) |
| Q7 | Predefined detection thresholds? | MERGED | ″ | v2 Q4 (P1) |
| Q8 | Manual candidate inspection? | MERGED | ″ | v2 Q3/Q4 |
| Q9 | Minimum S/N requirement? | MERGED | ″ | v2 Q4 |
| Q10 | Repeat detections required? | RETAINED | distinct selection ingredient (R8) | v2 Q5 (P1) |
| Q11 | Rejection criteria (RFI etc.)? | RETAINED-narrowed | plan lists intended criteria; executed ones unknown | v2 Q4/Q5 |
| Q12 | Surviving candidate tables incl. rejected? | MERGED | duplicates Q6 scope | v2 Q3 |
| Q13 | 2013 flux-cal documentation? | MERGED | calibration cluster | v2 Q6 (P2) |
| Q14 | 2014 flux-cal documentation? | MERGED | ″ | v2 Q6 |
| Q15 | What does "Flux Unit: Jy" mean? | RETAINED-narrowed | code path known (fixtsys); his semantic confirmation still needed | v2 Q6 |
| Q16 | Calibrated vs normalized unit? | MERGED | same as Q15 | v2 Q6 |
| Q17 | Calibrator scans/constants available? | REPHRASED | WIDE-SU proved NO calibrators in any supplied .rpf → question narrowed to external records + Tsys constants | v2 Q6 tail |
| Q18 | 1998–99 correlator documentation/software? | RETAINED | GAP-012 unchanged | v2 Q8 (P3) |
| Q20 | rpf→session mapping possible? | REMOVED-locally-answered | CARDS give OBS dates + SU pointings for all 27 files (GAP-013 RESOLVED) | finding noted in email |
| Q21 (v1 #20) | Dump integration times? | RETAINED-narrowed | XLS specifies planned Tint=5 s; executed confirmation remains | v2 Q10 (P3) |
| Q22 (v1 #23) | All dumps searched / pre-filter? | MERGED | subsumed by outcomes cluster | v2 Q3/Q4 |
| — | (none) | NEW | channel-count discrepancy discovered locally (4096 raw vs 2048 exported) | v2 Q9 (P3) |
| — | (none) | NEW | publication status of 2010–2014 efforts (GAP-017 tail) | v2 Q11 (P3) |

Net effect: 21 broad questions → **11 targeted questions** (P0×3, P1×2,
P2×1, P3×5), with two former questions replaced by statements of locally
established findings.
