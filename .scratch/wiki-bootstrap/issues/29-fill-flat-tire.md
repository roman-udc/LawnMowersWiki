# 29: Fill cluster: flat-tire

Child of [07: Fill pass](07-fill-pass.md). Cluster 21 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 28

**Status:** resolved

**What to build:** the Problem `problems/flat-tire.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

21. **flat-tire**: 2 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 9f9bbc4):**

- Created: problems/flat-tire (4 Sources, all manufacturer; riding; gas).
- Updated: causes/bad-tire; index, log.
- Thin Problem kept, not folded: its notes name Bad tire (page exists); 4 of 4 (three Sources describe the damaged tire without a cause list).
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (5 random citations): 0 errors.
