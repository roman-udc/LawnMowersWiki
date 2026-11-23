# 28: Fill cluster: not-bagging-grass

Child of [07: Fill pass](07-fill-pass.md). Cluster 20 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 18, 27

**Status:** ready-for-agent

**What to build:** the Problem `problems/not-bagging-grass.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

20. **not-bagging-grass**: 3 Sources.
   - Owns Causes: bad-bagger-or-full-bag, clogged-blower-tubes-or-inlet, clogged-deck-chute, worn-blade-sail, worn-blower-fan-or-bearing
   - Owns Procedures: none
   - Shared (owned elsewhere): cutting-wet-or-tall-grass (engine-loses-power)

Blocking: this child waits for every earlier cluster that owns a page it shares (18) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
