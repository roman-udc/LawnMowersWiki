# 26: Fill cluster: engine-only-runs-with-choke-on

Child of [07: Fill pass](07-fill-pass.md). Cluster 18 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 15, 25

**Status:** resolved

**What to build:** the Problem `problems/engine-only-runs-with-choke-on.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

18. **engine-only-runs-with-choke-on**: 6 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-carburetor-gasket-or-needle-and-seat (mower-is-leaking-gas)

Blocking: this child waits for every earlier cluster that owns a page it shares (15) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 3d040a9):**

- Created: problems/engine-only-runs-with-choke-on (7 Sources, all expert-blog; push, self-propelled, riding, zero-turn; gas).
- Updated: causes old-fuel, dirty-carburetor, clogged-fuel-line, clogged-fuel-filter, bad-fuel-pump, plugged-fuel-cap-vent, bad-carburetor-gasket-or-needle-and-seat, cracked-fuel-line; problems/engine-starts-then-dies (Related line linked); index, log.
- Dropped: no pages.
- Conflicts flagged: none.
- Spot-check (5 random citations on engine-only-runs-with-choke-on): 0 errors.
