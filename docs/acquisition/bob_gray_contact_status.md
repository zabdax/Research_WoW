# Bob Gray Contact Status

Status: PREPARED (internal) · Date 2026-08-29 · MASTER DIRECTIVE §19 ·
**No external search performed. No contact made. Nothing will be sent without
explicit human authorization.**

## Known identity (repo-local evidence only)

| Attribute | Value | Evidence class | Locator |
|---|---|---|---|
| Name as recorded | "Bob Gray" | DONOR_TESTIMONY (2026-08-29) + archive artifact | Donor response freeze (`research/data/ellingsen_simon_response.yaml`); `.gsf.gz` PostScript author metadata |
| Role | Performed processing and analysis of the 1998/99 Hobart Wow!-follow-up data | DONOR_TESTIMONY | Simon: "Bob Gray did all the processing and analysis of the data, I simply collected it." |
| Analysis products in archive | Four SAS 6.12/WinNT PROC GPLOT diagnostics, Sep 26–Oct 10 1998: `PLOT OF COUNT * SIGMA_RD`, `BUBBLE OF TIME * CHANNEL = SIGMA_P` (×2), `PLOT OF MAX_SIG * CHANNEL` | DOCUMENTED (file headers) | `docs/acquisition/ELLINGSEN_README_EXTRACTION.md` §4; `analysis/gsf_text_tokens.json` |
| Publication association | The archive's published-paper PDF (`wow_published.pdf`) metadata matches Gray & Ellingsen 2002, ApJ 578:967–971, DOI 10.1086/342646 (Crossref-verified page-range/DOI identity) | DOCUMENTED (metadata) / content UNVERIFIED (vectorized PDF, unreadable without OCR) | `ellingsen_gap_register.yaml` GAP-HOB-009/017; `hobart_literature_reconciliation.md` |

**Flagged inference (do not promote silently):** "Bob Gray" of the SAS plots
and donor testimony is very plausibly the "Gray" of Gray & Ellingsen (2002),
but the repo records only the surname from the Crossref-verified citation.
The given name and any honorific are NOT established in-repo. If confirmed,
the expansion of the name belongs to a human-authorized external search step.

## Public professional contact route

**UNKNOWN within this repository.** No email address, postal address,
institutional affiliation, or current status for Bob Gray exists anywhere in
the tracked repository. (The names appearing in control-software log
filenames — `bruce_*.log`, `ricky_*.log` — are system/operator artifacts and
MUST NOT be treated as identity evidence.)

### Update 2026-08-29 (Simon response round)

The project owner explicitly asked Simon whether he could provide an
introduction or contact information for Bob Gray (v3-Q6). Simon's verbatim
answer — "I don't have ready access to anything other than what I provided
yesterday" — establishes that **Simon is not a contact-route source**. No
introduction, address, or referral was provided. The donor additionally
recalled (Q2) that Bob "had a couple of other ideas that we tested" in the
2013/14 era, and that the setup-phase emails are not accessible to him —
reinforcing that Bob-side records are the only remaining route for the
analysis layer.

Additional Bob-side facts worth requesting (now in
`bob_gray_information_requirements.md` P2): which MPSLPP version was used
(manual v1.0 shows 20 slots; surviving source v1.8 shows 40) and whether the
missing subroutines/libraries or the MPSLPP Programming Manual survive.

## What remains to be determined (human-authorized steps only)

1. Whether an external web search for a public professional contact route is
   authorized (this was explicitly excluded from the current directive, §19).
2. If authorized: identify public, non-private routes only (e.g., publisher
   contact via the 2002 ApJ author affiliation, institutional/observatory
   directories). Private contact details must not be scraped, guessed, or used.
3. Human decision on sender identity, tone, and timing of the prepared draft
   (`bob_gray_email_draft.md`).
4. Whether the draft should also be reviewed by Simon Ellingsen before
   sending (he may know a current address or preferred approach; asking him
   is itself an external contact requiring authorization).

## Standing prohibitions

- Do not invent an address; do not scrape or guess private contact details.
- Do not send anything.
- Contact with any external party is a PRD §13 checkpoint requiring explicit
  human approval.
