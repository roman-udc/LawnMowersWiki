# 08: First full lint and cleanup

**What to build:** After the bootstrap, the maintainer has a wiki that passes the validator and has had its first content review. Its remaining problems are either fixed or recorded as tickets.

**Blocked by:** 05, 07

**Status:** resolved

- [x] `/wiki-lint` has been run on the full wiki.
- [x] Every structural violation is fixed, and the validator passes clean.
- [x] Each content suspicion is either fixed or recorded as a new ticket in the issue tracker, with `needs-triage`.
- [x] The index is checked for size and split per page type if it has passed a few hundred lines.
- [x] The lint run and fixes are recorded in the log and committed.

## Comments

2026-11-24: Lint run, report at `reports/lint/2026-11-24.md`. Validator clean, no orphans, index 209 lines (no split). Content suspicions filed as needs-triage tickets 36–40.
