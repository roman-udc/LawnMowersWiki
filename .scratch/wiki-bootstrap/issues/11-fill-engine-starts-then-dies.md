# 11: Fill cluster: engine-starts-then-dies

Child of [07: Fill pass](07-fill-pass.md). Cluster 3 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09, 10

**Status:** ready-for-agent

**What to build:** the Problem `problems/engine-starts-then-dies.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

3. **engine-starts-then-dies**: 95 Sources.
   - Owns Causes: dirty-cooling-fins, dirty-fuel-tank, overfilled-oil, wrong-choke-setting **(exists)**, wrong-fuel, wrong-oil-or-low-oil
   - Owns Procedures: change-the-engine-oil, clean-the-cooling-fins, clean-the-gas-tank, drain-excess-oil
   - Shared (owned elsewhere): bad-fuel-pump (engine-cranks-but-wont-start), bad-ignition-coil (engine-cranks-but-wont-start), clogged-air-filter (engine-cranks-but-wont-start), clogged-fuel-filter (engine-cranks-but-wont-start), clogged-fuel-line (engine-cranks-but-wont-start), debris-on-deck-or-pulleys (uneven-cut), dirty-carburetor (engine-cranks-but-wont-start), dull-or-bent-blade (uneven-cut), empty-fuel-tank (engine-cranks-but-wont-start), faulty-charging-system (engine-wont-crank), fouled-spark-plug (engine-cranks-but-wont-start), old-fuel (engine-cranks-but-wont-start), plugged-fuel-cap-vent (engine-cranks-but-wont-start), water-in-fuel (engine-runs-rough)

Blocking: this child waits for every earlier cluster that owns a page it shares (09, 10) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (12, 19) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
