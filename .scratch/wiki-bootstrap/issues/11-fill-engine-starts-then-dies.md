# 11: Fill cluster: engine-starts-then-dies

Child of [07: Fill pass](07-fill-pass.md). Cluster 3 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09, 10

**Status:** resolved

**What to build:** the Problem `problems/engine-starts-then-dies.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

3. **engine-starts-then-dies**: 95 Sources.
   - Owns Causes: dirty-cooling-fins, dirty-fuel-tank, overfilled-oil, wrong-choke-setting **(exists)**, wrong-fuel, wrong-oil-or-low-oil
   - Owns Procedures: change-the-engine-oil, clean-the-cooling-fins, clean-the-gas-tank, drain-excess-oil
   - Shared (owned elsewhere): bad-fuel-pump (engine-cranks-but-wont-start), bad-ignition-coil (engine-cranks-but-wont-start), clogged-air-filter (engine-cranks-but-wont-start), clogged-fuel-filter (engine-cranks-but-wont-start), clogged-fuel-line (engine-cranks-but-wont-start), debris-on-deck-or-pulleys (uneven-cut), dirty-carburetor (engine-cranks-but-wont-start), dull-or-bent-blade (uneven-cut), empty-fuel-tank (engine-cranks-but-wont-start), faulty-charging-system (engine-wont-crank), fouled-spark-plug (engine-cranks-but-wont-start), old-fuel (engine-cranks-but-wont-start), plugged-fuel-cap-vent (engine-cranks-but-wont-start), water-in-fuel (engine-runs-rough)

Blocking: this child waits for every earlier cluster that owns a page it shares (09, 10) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (12, 19) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-23 (fill pass, commit 1bc9c59):**

- Created: problems/engine-starts-then-dies (82 Sources with notes; gas and battery); causes/dirty-cooling-fins, dirty-fuel-tank, overfilled-oil, wrong-fuel, wrong-oil-or-low-oil; procedures/change-the-engine-oil, clean-the-cooling-fins, clean-the-gas-tank, drain-excess-oil.
- Updated: causes/wrong-choke-setting (75 Sources); 16 existing Causes now link this Problem with Sources from its notes; problems/engine-cranks-but-wont-start (Wrong fuel and Overfilled oil rows linked, Dirty fuel tank row added, 121 Sources, related link) and engine-wont-crank (Overfilled oil row linked); index, log.
- Dropped: none. dirty-fuel-tank belongs to engine-cranks-but-wont-start only (its one Source names no other Problem).
- Conflicts flagged: drain-to-full vs below max (overfilled-oil); topping up low oil (wrong-oil-or-low-oil); oil change and break-in intervals (change-the-engine-oil); compressed air on fins; water in tank cleaning.
- Plain text for later clusters: debris-on-deck-or-pulleys, clogged-deck-chute (overlaps debris; decide merge), dull-or-bent-blade, mowing-too-fast, wrong-engine-speed, bad-gas-cap-seal, bad-cooling-shroud, water-in-fuel, battery-mower Causes; Problems engine-dies-when-hot, engine-overheats, engine-loses-power, engine-only-runs-with-choke-on, mower-is-smoking.
- Spot-check (15 random citations on engine-starts-then-dies, overfilled-oil, wrong-oil-or-low-oil): 0 errors.
