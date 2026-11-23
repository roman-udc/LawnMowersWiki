# 08: First full lint and cleanup

**What to build:** After the bootstrap, the maintainer has a wiki that passes the validator and has had its first content review. Its remaining problems are either fixed or recorded as tickets.

**Blocked by:** 05, 07

**Status:** ready-for-agent

- [ ] `/wiki-lint` has been run on the full wiki.
- [ ] Every structural violation is fixed, and the validator passes clean.
- [ ] Each content suspicion is either fixed or recorded as a new ticket in the issue tracker, with `needs-triage`.
- [ ] The index is checked for size and split per page type if it has passed a few hundred lines.
- [ ] The lint run and fixes are recorded in the log and committed.
