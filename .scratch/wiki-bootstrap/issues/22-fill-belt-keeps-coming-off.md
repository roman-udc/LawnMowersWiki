# 22: Fill cluster: belt-keeps-coming-off

Child of [07: Fill pass](07-fill-pass.md). Cluster 14 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 12, 13, 21

**Status:** resolved

**What to build:** the Problem `problems/belt-keeps-coming-off.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

14. **belt-keeps-coming-off**: 24 Sources.
   - Owns Causes: bad-belt-tensioner-spring, belt-guard-or-keeper-missing, oil-or-rust-on-belt, wrong-belt
   - Owns Procedures: replace-the-deck-belt
   - Shared (owned elsewhere): bent-spindle-or-bad-spindle-bearing (mower-is-vibrating), debris-on-deck-or-pulleys (uneven-cut), worn-or-stretched-belt (mower-is-vibrating), worn-pulley-or-idler-bearing (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares (12, 13) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 50f1568):**

- Created: problems/belt-keeps-coming-off (26 Sources; push, riding, zero-turn; gas); causes/bad-belt-tensioner-spring (75), belt-guard-or-keeper-missing (31), oil-or-rust-on-belt (22), wrong-belt (9); procedures/replace-the-deck-belt (13).
- Updated: causes worn-or-stretched-belt (links Replace the deck belt), worn-pulley-or-idler-bearing, bent-spindle-or-bad-spindle-bearing, debris-on-deck-or-pulleys; problems blades-wont-engage, mower-is-vibrating, mower-wont-move, mower-pulls-to-one-side (tensioner and keeper rows linked, counts unchanged), uneven-cut; procedures/replace-the-idler-pulley; index, log (85 lines).
- Dropped: no pages. Shredded-belt content split between worn-or-stretched-belt (count), belt-guard-or-keeper-missing (bracket fix) and wrong-belt (routing/part check).
- Conflicts flagged: belt prices ($60-250 vs $20-200 vs $80-250). Not cited: V-belt ".22 inches high" typo.
- Plain text for later clusters: none.
- Spot-check (15 random citations on bad-belt-tensioner-spring, belt-guard-or-keeper-missing, belt-keeps-coming-off): 1 error, fixed.
