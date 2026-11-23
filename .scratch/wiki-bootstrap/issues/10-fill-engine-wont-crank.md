# 10: Fill cluster: engine-wont-crank

Child of [07: Fill pass](07-fill-pass.md). Cluster 2 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09

**Status:** ready-for-agent

**What to build:** the Problem `problems/engine-wont-crank.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

2. **engine-wont-crank**: 136 Sources.
   - Owns Causes: bad-ignition-switch, bad-safety-switch, bad-starter-motor, bad-starter-solenoid, bad-wiring-or-ground, blown-fuse, faulty-charging-system, hydrolocked-engine, loose-or-corroded-battery-cables, seized-engine, weak-or-dead-battery
   - Owns Procedures: charge-the-battery, jump-start-the-battery, read-a-wiring-schematic, replace-the-ignition-switch, replace-the-seat-switch, replace-the-starter-motor, replace-the-starter-solenoid, reset-the-ignition-code, test-and-replace-a-fuse, test-the-battery, test-the-starter-solenoid
   - Shared (owned elsewhere): bad-fuel-pump (engine-cranks-but-wont-start), bad-ignition-coil (engine-cranks-but-wont-start), bad-recoil-starter (engine-cranks-but-wont-start), clogged-air-filter (engine-cranks-but-wont-start), clogged-fuel-filter (engine-cranks-but-wont-start), clogged-fuel-line (engine-cranks-but-wont-start), dirty-carburetor (engine-cranks-but-wont-start), empty-fuel-tank (engine-cranks-but-wont-start), fouled-spark-plug (engine-cranks-but-wont-start), incorrect-starting-procedure (engine-cranks-but-wont-start), low-compression (engine-cranks-but-wont-start), old-fuel (engine-cranks-but-wont-start), plugged-fuel-cap-vent (engine-cranks-but-wont-start), sheared-flywheel-key (engine-cranks-but-wont-start), wet-electrical-components (engine-cranks-but-wont-start), wrong-choke-setting (engine-starts-then-dies), wrong-fuel (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares (09) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (11) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
