# 12: Fill cluster: uneven-cut

Child of [07: Fill pass](07-fill-pass.md). Cluster 4 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11

**Status:** ready-for-agent

**What to build:** the Problem `problems/uneven-cut.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

4. **uneven-cut**: 72 Sources.
   - Owns Causes: bad-blade-adapter-or-loose-blade, bad-tire, bent-deck-or-deck-shell, blade-installed-upside-down, debris-on-deck-or-pulleys, dull-or-bent-blade, incorrect-path-overlap, mowing-too-fast, unlevel-deck, wrong-cutting-height, wrong-engine-speed, wrong-tire-pressure
   - Owns Procedures: level-the-deck, measure-a-mower-blade, repair-a-flat-tire, replace-a-tire, sharpen-and-replace-the-blades
   - Shared (owned elsewhere): bent-crankshaft (mower-is-vibrating), bent-spindle-or-bad-spindle-bearing (mower-is-vibrating), worn-or-stretched-belt (mower-is-vibrating), worn-pulley-or-idler-bearing (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (13) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
