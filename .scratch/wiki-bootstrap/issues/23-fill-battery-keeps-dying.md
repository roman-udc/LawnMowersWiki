# 23: Fill cluster: battery-keeps-dying

Child of [07: Fill pass](07-fill-pass.md). Cluster 15 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 22

**Status:** ready-for-agent

**What to build:** the Problem `problems/battery-keeps-dying.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

15. **battery-keeps-dying**: 12 Sources.
   - Owns Causes: bad-alternator, parasitic-battery-drain
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-battery (battery-mower-wont-start)

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (24) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
