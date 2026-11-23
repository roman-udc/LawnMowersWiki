# 22: Fill cluster: belt-keeps-coming-off

Child of [07: Fill pass](07-fill-pass.md). Cluster 14 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 12, 13, 21

**Status:** ready-for-agent

**What to build:** the Problem `problems/belt-keeps-coming-off.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

14. **belt-keeps-coming-off**: 24 Sources.
   - Owns Causes: bad-belt-tensioner-spring, belt-guard-or-keeper-missing, oil-or-rust-on-belt, wrong-belt
   - Owns Procedures: replace-the-deck-belt
   - Shared (owned elsewhere): bent-spindle-or-bad-spindle-bearing (mower-is-vibrating), debris-on-deck-or-pulleys (uneven-cut), worn-or-stretched-belt (mower-is-vibrating), worn-pulley-or-idler-bearing (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares (12, 13) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [ ] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [ ] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [ ] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [ ] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.
