# 24: Fill cluster: battery-mower-wont-start

Child of [07: Fill pass](07-fill-pass.md). Cluster 16 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09, 10, 13, 23

**Status:** resolved

**What to build:** the Problem `problems/battery-mower-wont-start.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

16. **battery-mower-wont-start**: 12 Sources.
   - Owns Causes: bad-battery, bad-charger, bad-motor, battery-not-seated, clogged-motor-vents, overheated-battery, safety-key-missing
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-wiring-or-ground (engine-wont-crank), debris-wrapped-around-blade-spindle (mower-is-vibrating), wet-electrical-components (engine-cranks-but-wont-start)

Blocking: this child waits for every earlier cluster that owns a page it shares (09, 10, 13) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit e5680f8):**

- Created: problems/battery-mower-wont-start (13 Sources; push, self-propelled, riding, zero-turn; battery); causes/bad-battery (6), bad-charger (11), bad-motor (13), battery-not-seated (11), clogged-motor-vents (3), overheated-battery (12), safety-key-missing (4).
- Updated: causes weak-or-dead-battery, bad-wiring-or-ground, incorrect-starting-procedure, debris-on-deck-or-pulleys, wet-electrical-components, bad-safety-switch, cutting-wet-or-tall-grass, mowing-too-fast, debris-wrapped-around-blade-spindle; problems engine-starts-then-dies, engine-overheats, mower-is-vibrating (rows linked, counts unchanged), engine-wont-crank, battery-keeps-dying (Related lines; attributed "one hour" run-time claim); index, log (15 lines).
- Dropped: no pages. Not counted: the car-battery jump-start article (12-volt gas batteries). Handle-out-of-position folded into safety-key-missing.
- Maintainer decisions: corded mowers need a power_sources value (corded content is on the Problem's Brand notes); bad-battery overlaps weak-or-dead-battery (bad-battery scoped to battery-mower packs).
- Conflicts flagged: none.
- Plain text left: Bad bagger or full bag, Clogged deck chute.
- Spot-check (15 random citations on battery-mower-wont-start, bad-motor, overheated-battery): 0 errors.
