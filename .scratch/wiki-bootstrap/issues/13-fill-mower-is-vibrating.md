# 13: Fill cluster: mower-is-vibrating

Child of [07: Fill pass](07-fill-pass.md). Cluster 5 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09, 12

**Status:** ready-for-agent

**What to build:** the Problem `problems/mower-is-vibrating.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

5. **mower-is-vibrating**: 62 Sources.
   - Owns Causes: bad-pto-clutch, bent-crankshaft, bent-spindle-or-bad-spindle-bearing, debris-wrapped-around-blade-spindle, engine-mount-loose, worn-or-stretched-belt, worn-pulley-or-idler-bearing
   - Owns Procedures: replace-the-idler-pulley, replace-the-pto-clutch, replace-the-spindle-assembly, test-the-pto-clutch
   - Shared (owned elsewhere): bad-belt-tensioner-spring (belt-keeps-coming-off), bad-blade-adapter-or-loose-blade (uneven-cut), debris-on-deck-or-pulleys (uneven-cut), dull-or-bent-blade (uneven-cut), sheared-flywheel-key (engine-cranks-but-wont-start)

Blocking: this child waits for every earlier cluster that owns a page it shares (09, 12) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (22) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
