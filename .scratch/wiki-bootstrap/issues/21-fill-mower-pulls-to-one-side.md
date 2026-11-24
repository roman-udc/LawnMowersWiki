# 21: Fill cluster: mower-pulls-to-one-side

Child of [07: Fill pass](07-fill-pass.md). Cluster 13 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 16, 20

**Status:** resolved

**What to build:** the Problem `problems/mower-pulls-to-one-side.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

13. **mower-pulls-to-one-side**: 29 Sources.
   - Owns Causes: bad-drive-control-linkage-or-damper, brake-hung-up, loose-or-seized-wheel-bearing, unbalanced-load
   - Owns Procedures: adjust-the-neutral-control, adjust-the-tracking
   - Shared (owned elsewhere): air-in-hydraulic-system (mower-wont-move), bad-hydrostatic-transmission (mower-wont-move), worn-drive-belt (mower-wont-move)

Blocking: this child waits for every earlier cluster that owns a page it shares (16) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit b703086):**

- Created: problems/mower-pulls-to-one-side (29 Sources; push, self-propelled, riding, zero-turn; gas); causes/bad-drive-control-linkage-or-damper (28), brake-hung-up (6), loose-or-seized-wheel-bearing (1), unbalanced-load (4); procedures/adjust-the-tracking (23), adjust-the-neutral-control (1).
- Updated: causes wrong-tire-pressure, bad-tire, unlevel-deck, worn-drive-belt, bad-hydrostatic-transmission, air-in-hydraulic-system, low-hydraulic-oil (Problem added, plain mentions linked); problems mower-wont-move (Brake hung up row linked), mower-is-vibrating (Bad drive control linkage or damper row linked), uneven-cut (Related line); index, log (33 lines).
- Dropped: no pages. Tracking adjustment folded into bad-drive-control-linkage-or-damper / adjust-the-tracking; attachment imbalance into unbalanced-load.
- Conflicts flagged: none. Not cited: Kubota roundup's garbled tire-pressure solution cell.
- Plain text for later clusters: Loose steering linkage, Bad belt tensioner spring (rows); Problems Loose steering, Mower creeps in neutral.
- Spot-check (15 random citations on mower-pulls-to-one-side, bad-drive-control-linkage-or-damper, adjust-the-tracking): 1 error, fixed.
