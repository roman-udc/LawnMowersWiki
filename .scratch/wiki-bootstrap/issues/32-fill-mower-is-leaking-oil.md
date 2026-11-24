# 32: Fill cluster: mower-is-leaking-oil

Child of [07: Fill pass](07-fill-pass.md). Cluster 24 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 31

**Status:** resolved

**What to build:** the Problem `problems/mower-is-leaking-oil.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

24. **mower-is-leaking-oil**: 1 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit cc343af):**

- Created: problems/mower-is-leaking-oil (7 Sources: 1 manufacturer, 6 expert-blog; push, riding, zero-turn; gas).
- Updated: causes bad-head-gasket, overfilled-oil; index, log.
- Thin Problem kept, not folded: notes name Overfilled oil and Bad head gasket. The gasket leak onto the muffler from the Bad Boy, Exmark, Honda and John Deere smoking articles is here, linked to bad-head-gasket with their 'engine gasket' wording.
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (5 random citations): 0 errors.
