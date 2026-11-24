# 09: Fill cluster: engine-cranks-but-wont-start

Child of [07: Fill pass](07-fill-pass.md). Cluster 1 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** none

**Status:** resolved

**What to build:** the Problem `problems/engine-cranks-but-wont-start.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

1. **engine-cranks-but-wont-start** **(exists)**: 137 Sources.
   - Owns Causes: air-in-fuel-system, bad-fuel-pump **(exists)**, bad-glow-plugs, bad-ignition-coil **(exists)**, bad-recoil-starter, clogged-air-filter **(exists)**, clogged-fuel-filter **(exists)**, clogged-fuel-line **(exists)**, dirty-carburetor **(exists)**, disconnected-fuel-solenoid **(exists)**, empty-fuel-tank, fouled-spark-plug **(exists)**, fuel-valve-off, incorrect-starting-procedure, low-compression **(exists)**, old-fuel **(exists)**, plugged-fuel-cap-vent **(exists)**, sheared-flywheel-key **(exists)**, vapor-lock, wet-electrical-components
   - Owns Procedures: clean-or-replace-the-air-filter, clean-the-carburetor, rebuild-the-carburetor, replace-the-carburetor, replace-the-flywheel-key, replace-the-fuel-filter, replace-the-fuel-line, replace-the-ignition-coil, replace-the-spark-plug **(exists)**, start-a-mower-with-old-gas, start-a-zero-turn-mower, test-the-ignition-coil, tune-up
   - Shared (owned elsewhere): bad-ignition-switch (engine-wont-crank), bad-safety-switch (engine-wont-crank), bad-shutoff-valve (mower-is-leaking-gas), bad-starter-motor (engine-wont-crank), bad-starter-solenoid (engine-wont-crank), blown-fuse (engine-wont-crank), faulty-charging-system (engine-wont-crank), loose-or-corroded-battery-cables (engine-wont-crank), weak-or-dead-battery (engine-wont-crank), wrong-choke-setting (engine-starts-then-dies), wrong-fuel (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (10, 11, 15) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-23 (fill pass, commit 157665d):**

- Created: causes/air-in-fuel-system, bad-glow-plugs, bad-recoil-starter, empty-fuel-tank, fuel-valve-off, incorrect-starting-procedure, wet-electrical-components; procedures/clean-or-replace-the-air-filter, clean-the-carburetor, rebuild-the-carburetor, replace-the-carburetor, replace-the-flywheel-key, replace-the-fuel-filter, replace-the-fuel-line, replace-the-ignition-coil, start-a-mower-with-old-gas, start-a-zero-turn-mower, test-the-ignition-coil, tune-up.
- Updated: problems/engine-cranks-but-wont-start (120 Sources, power_sources gas + diesel, table re-ranked, new aliases), the 12 existing Causes in the cluster, procedures/replace-the-spark-plug, index, log.
- Dropped: causes/vapor-lock (no supporting notes).
- Conflicts flagged: starter fluid vs carburetor cleaner (Problem); foam-filter oiling and filter intervals; clean vs replace a lightly dirty plug; fuel age, stabilizer mixing, "minimum 10% ethanol" typo, diesel shelf life; clean vs replace gas cap; safety-bar order; reusing carb gaskets; coil repair difficulty; zero-turn cold-start throttle; tune-up interval.
- Plain text for later clusters on the Problem: bad-safety-switch, weak-or-dead-battery, bad-ignition-switch, loose-or-corroded-battery-cables, bad-starter-solenoid, faulty-charging-system, blown-fuse, wrong-fuel, overfilled-oil, bad-gas-cap-seal, water-in-fuel.
- Spot-check (25 random citations on 5 Causes): 1 misplaced citation fixed (4%). The flagged old-fuel S14 and fouled-spark-plug S9 citations are supported by their raw Sources and were kept.
