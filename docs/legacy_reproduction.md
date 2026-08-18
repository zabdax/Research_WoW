# Legacy Reproduction Protocol

The Phase 2 prototype is retained for auditability, not as the revised scientific model.

```bash
py -m pytest
py -m scripts.legacy_report
```

The report records:

- the current code-derived five-way normalized score output;
- the stored `data/posterior_results.json` output, if available;
- legacy manuscript headline values extracted as declared targets;
- the Level 1 Kipping--Gray algebra check;
- the configured prior sensitivity result.

A mismatch is a finding. The report must not modify source code, round values to agree, or replace manuscript numbers. New research results belong in `research/` and `research/results/`, never in the legacy input/output paths.
