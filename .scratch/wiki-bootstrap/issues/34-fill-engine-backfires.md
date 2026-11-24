# 34: Fill cluster: engine-backfires

Child of [07: Fill pass](07-fill-pass.md). Cluster 26 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 33

**Status:** resolved

**What to build:** the Problem `problems/engine-backfires.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

26. **engine-backfires**: 1 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 506c7fa):**

- Created: problems/engine-backfires (6 Sources: 1 manufacturer, 5 expert-blog; push, riding, zero-turn; gas).
- Updated: causes/dirty-carburetor (mention linked); index, log.
- Thin Problem kept, not folded: notes name Dirty carburetor (5 of 6). The Sears shutdown backfire names no part; it's in the Summary, triage and tips.
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (5 random citations): 0 errors.
