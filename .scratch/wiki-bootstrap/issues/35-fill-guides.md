# 35: Fill cluster: Guides cluster

Child of [07: Fill pass](07-fill-pass.md). Cluster 27 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 34

**Status:** ready-for-agent

**What to build:** every Guide from the taxonomy, plus Procedures with no owning Cause (replace-the-seat), written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

27. **Guides cluster**: all 16 Guides, plus Procedures with no owning Cause (replace-the-seat) and Causes with no Problem (none).

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
