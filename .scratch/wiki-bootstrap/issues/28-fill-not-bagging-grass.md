# 28: Fill cluster: not-bagging-grass

Child of [07: Fill pass](07-fill-pass.md). Cluster 20 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 18, 27

**Status:** resolved

**What to build:** the Problem `problems/not-bagging-grass.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

20. **not-bagging-grass**: 3 Sources.
   - Owns Causes: bad-bagger-or-full-bag, clogged-blower-tubes-or-inlet, clogged-deck-chute, worn-blade-sail, worn-blower-fan-or-bearing
   - Owns Procedures: none
   - Shared (owned elsewhere): cutting-wet-or-tall-grass (engine-loses-power)

Blocking: this child waits for every earlier cluster that owns a page it shares (18) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 3824e65):**

- Created: problems/not-bagging-grass (title "Mower doesn't bag grass"; 3 Sources, all expert-blog); causes bad-bagger-or-full-bag (4), clogged-blower-tubes-or-inlet (3), clogged-deck-chute (63), worn-blade-sail (53), worn-blower-fan-or-bearing (3).
- Updated: causes blade-installed-upside-down, cutting-wet-or-tall-grass, worn-or-stretched-belt, wrong-engine-speed, debris-on-deck-or-pulleys (Scope paragraph), dull-or-bent-blade, mowing-too-fast; procedures/sharpen-and-replace-the-blades; problems uneven-cut, engine-starts-then-dies, engine-overheats, engine-runs-rough, engine-loses-power, engine-dies-when-hot, battery-mower-wont-start, mower-is-vibrating (plain rows linked); index, log.
- Clogged deck overlap: both pages kept with Scope paragraphs (packed clippings and chute vs top-of-deck, pulley and solid debris); earlier counts not merged.
- Mis-mapped note: cub-cadet-loses-power-bogs-down's blower-tubes note is engine air passages; the 1-of-N rows on engine-loses-power and engine-overheats stay unlinked with an explanation, for the maintainer.
- Candidate page for the maintainer: guides/grass-collection-system-types.
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (15 random citations): 0 errors.
