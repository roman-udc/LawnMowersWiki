# 20: Fill cluster: engine-overheats

Child of [07: Fill pass](07-fill-pass.md). Cluster 12 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11, 19

**Status:** resolved

**What to build:** the Problem `problems/engine-overheats.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

12. **engine-overheats**: 30 Sources.
   - Owns Causes: bad-cooling-shroud, bad-engine-cooling-fan
   - Owns Procedures: none
   - Shared (owned elsewhere): dirty-cooling-fins (engine-starts-then-dies), wrong-oil-or-low-oil (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares (11) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 26ab778):**

- Created: problems/engine-overheats (37 Sources; push, self-propelled, riding, zero-turn; gas, battery); causes/bad-cooling-shroud (23), bad-engine-cooling-fan (1).
- Updated: causes wrong-oil-or-low-oil, clogged-air-filter, dirty-cooling-fins, dull-or-bent-blade, cutting-wet-or-tall-grass, debris-on-deck-or-pulleys, mowing-too-fast, overfilled-oil, bad-head-gasket, old-fuel, worn-or-stretched-belt; problems engine-loses-power and engine-starts-then-dies (Bad cooling shroud rows linked, order unchanged; Related lines), mower-is-smoking (Related line); index, log (41 lines).
- Dropped: no pages. Not cited: scrambled low-oil and cooling-fins rows in the Ferris, Cub Cadet zero-turn, Hustler, John Deere zero-turn, Kubota zero-turn and Husqvarna zero-turn tables (Sources still counted for naming the Causes).
- Conflicts flagged: none.
- Candidate page for the maintainer: Clogged motor vents (electric mowers; Source electric-lawn-mowers-dangers-and-safety-guide).
- Plain text for later clusters: Clogged deck chute, Clogged blower tubes or inlet, Clogged motor vents (rows); Engine quits when hot.
- Spot-check (15 random citations on engine-overheats, bad-cooling-shroud, bad-engine-cooling-fan): 0 errors.
