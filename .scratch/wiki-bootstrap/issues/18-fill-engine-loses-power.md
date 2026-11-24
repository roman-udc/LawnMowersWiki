# 18: Fill cluster: engine-loses-power

Child of [07: Fill pass](07-fill-pass.md). Cluster 10 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11, 12, 17

**Status:** resolved

**What to build:** the Problem `problems/engine-loses-power.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

10. **engine-loses-power**: 36 Sources.
   - Owns Causes: bad-governor, cutting-wet-or-tall-grass
   - Owns Procedures: none
   - Shared (owned elsewhere): dirty-cooling-fins (engine-starts-then-dies), mowing-too-fast (uneven-cut), overfilled-oil (engine-starts-then-dies), wrong-oil-or-low-oil (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares (11, 12) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit a9d4cae):**

- Created: problems/engine-loses-power (25 Sources; push, self-propelled, riding, zero-turn; gas); causes/bad-governor (1), cutting-wet-or-tall-grass (31).
- Updated: causes dirty-carburetor, old-fuel, clogged-fuel-line, clogged-fuel-filter, clogged-air-filter, dull-or-bent-blade, mowing-too-fast, dirty-cooling-fins, overfilled-oil, wrong-oil-or-low-oil, fouled-spark-plug, debris-on-deck-or-pulleys, bad-fuel-pump, plugged-fuel-cap-vent, wrong-engine-speed, bad-ignition-coil, bent-spindle-or-bad-spindle-bearing, low-compression, worn-or-stretched-belt, bad-gas-cap-seal (Problem added, plain mentions linked); problems/engine-starts-then-dies (Cutting wet or tall grass row and Related line linked); index, log (43 lines).
- Dropped: no pages. Not counted: weak hydrostatic transmission notes (Ariens, common-lawn-mower-problems-fixed, Snapper, Husqvarna zero-turn; they belong to mower-wont-move) and Simplicity "Loses Power and Dies" (starts-then-dies).
- Conflicts flagged: none.
- Plain text for later clusters: Clogged deck chute, Bad cooling shroud, Clogged blower tubes or inlet (rows); Problems Engine overheats, Engine runs rough, Mower doesn't bag grass.
- Spot-check (15 random citations on engine-loses-power, cutting-wet-or-tall-grass, bad-governor): 0 errors.
- New helper: .scratch/wiki-bootstrap/helpers/linkprob.py adds a Problem to shared Cause pages (links a matching plain bullet or adds one, appends "Sources for <Problem>").
