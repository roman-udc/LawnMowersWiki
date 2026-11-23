# 27: Fill cluster: mower-is-noisy

Child of [07: Fill pass](07-fill-pass.md). Cluster 19 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 26

**Status:** ready-for-agent

**What to build:** the Problem `problems/mower-is-noisy.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

19. **mower-is-noisy**: 5 Sources.
   - Owns Causes: clogged-muffler-or-spark-arrestor
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
