# 19: Fill cluster: engine-runs-rough

Child of [07: Fill pass](07-fill-pass.md). Cluster 11 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 12, 18

**Status:** resolved

**What to build:** the Problem `problems/engine-runs-rough.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

11. **engine-runs-rough**: 35 Sources.
   - Owns Causes: water-in-fuel
   - Owns Procedures: none
   - Shared (owned elsewhere): mowing-too-fast (uneven-cut), wrong-engine-speed (uneven-cut)

Blocking: this child waits for every earlier cluster that owns a page it shares (12) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit aa52de6):**

- Created: problems/engine-runs-rough (34 Sources; push, self-propelled, riding, zero-turn; gas); causes/water-in-fuel (12).
- Updated: causes dirty-carburetor, fouled-spark-plug, old-fuel, clogged-fuel-filter, clogged-fuel-line, mowing-too-fast, plugged-fuel-cap-vent, wrong-engine-speed, dull-or-bent-blade, clogged-air-filter, debris-on-deck-or-pulleys, wrong-choke-setting, low-compression, sheared-flywheel-key, bad-fuel-pump, bad-gas-cap-seal, bad-safety-switch, dirty-cooling-fins, overfilled-oil; procedures/replace-the-fuel-filter (fixes Water in fuel); problems engine-cranks-but-wont-start, engine-starts-then-dies, mower-is-smoking (Water in fuel rows linked), engine-loses-power (Related line); index, log (41 lines).
- Dropped: no pages. Overfilled oil added to the table as 1 of 34 from the too-much-oil article (no causes-named line, but its note says overfill fouls the plug and the engine runs rough).
- Conflicts flagged: none.
- Plain text for later clusters: Clogged deck chute (row); Engine overheats.
- Spot-check (15 random citations on engine-runs-rough, water-in-fuel, wrong-engine-speed): 0 errors.
