# 27: Fill cluster: mower-is-noisy

Child of [07: Fill pass](07-fill-pass.md). Cluster 19 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 26

**Status:** resolved

**What to build:** the Problem `problems/mower-is-noisy.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

19. **mower-is-noisy**: 5 Sources.
   - Owns Causes: clogged-muffler-or-spark-arrestor
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit b0f021b):**

- Created: problems/mower-is-noisy (5 Sources: 1 manufacturer, 4 expert-blog; push, riding, zero-turn; gas); causes/clogged-muffler-or-spark-arrestor (2).
- Updated: causes worn-pulley-or-idler-bearing, bent-spindle-or-bad-spindle-bearing, worn-or-stretched-belt, dull-or-bent-blade, wrong-oil-or-low-oil, bad-belt-tensioner-spring, debris-wrapped-around-blade-spindle, bad-blade-adapter-or-loose-blade, clogged-air-filter, belt-guard-or-keeper-missing, debris-on-deck-or-pulleys, engine-mount-loose, wrong-belt; index, log.
- Folded: damaged muffler (cracked, broken baffles) and loose muffler into clogged-muffler-or-spark-arrestor; no Source describes a clogging, and the page says so. Not counted: Sears 'failing starter' (no detail).
- Dropped: no pages.
- Conflicts flagged: none.
- Spot-check (10 random citations on mower-is-noisy and clogged-muffler-or-spark-arrestor): 0 errors.
