# 25: Fill cluster: engine-dies-when-hot

Child of [07: Fill pass](07-fill-pass.md). Cluster 17 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11, 24

**Status:** resolved

**What to build:** the Problem `problems/engine-dies-when-hot.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

17. **engine-dies-when-hot**: 12 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): dirty-cooling-fins (engine-starts-then-dies), overfilled-oil (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares (11) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 38423d0):**

- Created: problems/engine-dies-when-hot (14 Sources, all expert-blog; push, self-propelled, riding, zero-turn; gas).
- Updated: causes bad-ignition-coil, dirty-cooling-fins, overfilled-oil, clogged-air-filter, dirty-carburetor, old-fuel, wrong-oil-or-low-oil, plugged-fuel-cap-vent, debris-on-deck-or-pulleys, dull-or-bent-blade, fouled-spark-plug, worn-piston-rings-or-valve-guides, low-compression; problems engine-starts-then-dies, engine-overheats, mower-wont-move (plain mentions linked); index, log.
- Dropped: no pages. Not cited: common-lawn-mower-problems-fixed (doesn't cover the symptom).
- Conflicts flagged: none.
- Plain text left: Clogged deck chute (cluster 28).
- Spot-check (5 random citations on engine-dies-when-hot): 0 errors.
