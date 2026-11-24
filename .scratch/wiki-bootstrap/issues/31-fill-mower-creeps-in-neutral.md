# 31: Fill cluster: mower-creeps-in-neutral

Child of [07: Fill pass](07-fill-pass.md). Cluster 23 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 30

**Status:** resolved

**What to build:** the Problem `problems/mower-creeps-in-neutral.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

23. **mower-creeps-in-neutral**: 1 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit b4e121d):**

- Created: problems/mower-creeps-in-neutral (1 Source, manufacturer; riding, zero-turn; gas).
- Updated: causes/bad-drive-control-linkage-or-damper (mention linked); problems/mower-pulls-to-one-side (Related line); index, log.
- Thin Problem kept, not folded: its Source names Bad drive control linkage or damper (page exists), fixed by Adjust the neutral control.
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (5 random citations): 0 errors.
