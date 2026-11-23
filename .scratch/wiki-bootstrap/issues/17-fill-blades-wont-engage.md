# 17: Fill cluster: blades-wont-engage

Child of [07: Fill pass](07-fill-pass.md). Cluster 9 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 10, 13, 16

**Status:** ready-for-agent

**What to build:** the Problem `problems/blades-wont-engage.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

9. **blades-wont-engage**: 41 Sources.
   - Owns Causes: bad-clutch-cable-or-linkage, bad-pto-switch
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-belt-tensioner-spring (belt-keeps-coming-off), bad-pto-clutch (mower-is-vibrating), bad-safety-switch (engine-wont-crank), belt-guard-or-keeper-missing (belt-keeps-coming-off), blown-fuse (engine-wont-crank), weak-or-dead-battery (engine-wont-crank), worn-or-stretched-belt (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares (10, 13) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (22) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
