# 07: Fill pass

**What to build:** The wiki contains every page from the approved taxonomy, built from all mapped Sources. The support agent can then handle the full range of Problems found in the current Sources.

**Blocked by:** 06

**Status:** resolved

- [x] First step: this ticket splits itself into one child ticket per cluster from the approved taxonomy (following the issue-tracker conventions, numbered after the existing tickets). Each child is blocked by any cluster that owns a page it shares.
- [x] Each cluster: the Problem, its Causes and its Procedures are written or updated from all mapped Sources, following the `/wiki-ingest` rules (citations, Trust tier ranking, conflict callouts, Brand notes, OEM part number caveats). The index and log are updated, the validator passes, and the cluster gets its own commit.
- [x] Guides from the taxonomy are written, either as their own cluster or together with the cluster they most relate to.
- [x] Skipped Sources are recorded in the log, so every Source in the raw folder has a log entry and the validator's log-coverage rule passes on the whole wiki.

## Comments

**2026-11-24, fill pass complete.** Split into child tickets 09–35, all resolved, one commit per cluster. Every Source was read once into per-Source notes (`.scratch/wiki-bootstrap/notes/`), and the pages were built from them. The wiki has 26 Problems, 109 Causes, 43 Procedures and 16 Guides. `python tools/validate_wiki.py wiki raw` is clean with no flag (every raw Source has a log line), and the tests pass. Finalizers spot-checked citations on the largest pages of each cluster: 4 errors in about 400, all fixed.

**Open maintainer decisions** (also in the final log Note):
1. **Dropped pages (approved but no supporting Sources):** causes/vapor-lock (ticket 09) and procedures/replace-the-pto-clutch (ticket 13).
2. **Decision 5 overridden without approval.** At the skip review, the cluster 35 agent un-skipped four Sources and ingested their repair and safety facts only:
   - a-guide-to-choosing-a-cordless-lawn-mower, which Decision 5 kept skipped
   - should-i-get-an-electric-riding-mower
   - best-zero-turn-mower-tires-for-hills
   - choosing-between-a-residential-commercial-zero-turn-mower

   Revert or confirm.
3. **Corded electric mowers** have no `power_sources` value.
4. **bad-battery overlaps weak-or-dead-battery.**
5. **Gas-cap rows:** the "Bad gas cap seal" rows on cranks-but-won't-start and starts-then-dies are really about the vent.
6. **Valve guides:** no Source supports "valve guides" in causes/worn-piston-rings-or-valve-guides. Rename it or keep it.
7. **Clogged blower tubes:** the rows on engine-loses-power and engine-overheats are really engine air passages.
8. **Candidate Guide:** grass-collection-system-types.

**Review findings for ticket 08 (lint):**
- **Very large pages:** the citation lines on the big Cause pages are huge (old-fuel is about 114 KB, and one line runs to 16,000 characters). Consider capping citations per section.
- **Inferred values:** difficulty values with no Source are listed in each log Note.
- **Log dates out of order:** the run crossed midnight, so some log entry dates are out of order. The log is append-only, so they were left as written.
- **Ranking skew:** battery and switch Causes rank high on cranks-but-won't-start, because generic "won't start" Sources feed both crank siblings (Decision 1).
- **Unflagged conflict:** the solenoid test needs at least 12.3 V, while the battery pages treat 12.7 V as a full charge.
