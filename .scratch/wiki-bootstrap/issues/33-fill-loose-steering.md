# 33: Fill cluster: loose-steering

Child of [07: Fill pass](07-fill-pass.md). Cluster 25 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 32

**Status:** resolved

**What to build:** the Problem `problems/loose-steering.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

25. **loose-steering**: 1 Sources.
   - Owns Causes: bad-front-axle, loose-steering-linkage
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit a225d8f):**

- Created: problems/loose-steering (7 Sources: 1 manufacturer, 6 expert-blog; riding; gas); causes/loose-steering-linkage (14), bad-front-axle (1).
- Updated: problems mower-pulls-to-one-side (row 12 of 29 linked; Related line), mower-is-vibrating (row linked); index, log.
- Thin Problem kept, not folded. Steering, tie-rod and front-axle content folded into the two Causes; no Procedure created. The wheel spindle (mis-mapped to the deck-spindle page) is on bad-front-axle.
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (15 random citations): 0 errors.
