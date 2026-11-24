# 16: Fill cluster: mower-wont-move

Child of [07: Fill pass](07-fill-pass.md). Cluster 8 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 13, 15

**Status:** resolved

**What to build:** the Problem `problems/mower-wont-move.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

8. **mower-wont-move**: 42 Sources.
   - Owns Causes: air-in-hydraulic-system, bad-hydrostatic-transmission, bypass-valve-open, hot-hydraulic-fluid, low-hydraulic-oil, missing-axle-key, missing-idler-arm-spring, worn-drive-belt
   - Owns Procedures: change-the-hydraulic-oil, purge-the-hydraulic-system
   - Shared (owned elsewhere): bad-belt-tensioner-spring (belt-keeps-coming-off), worn-pulley-or-idler-bearing (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares (13) and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (22) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 41d0651):**

- Created: problems/mower-wont-move (43 Sources; riding, zero-turn; gas); causes/worn-drive-belt (26), bypass-valve-open (41), low-hydraulic-oil (28), missing-idler-arm-spring (26), hot-hydraulic-fluid (22), air-in-hydraulic-system (25), missing-axle-key (11), bad-hydrostatic-transmission (17); procedures/change-the-hydraulic-oil (20), purge-the-hydraulic-system (21).
- Updated: causes/worn-pulley-or-idler-bearing, dirty-carburetor, bad-safety-switch, worn-or-stretched-belt; problems/mower-is-vibrating (idler spring row linked; worn-drive-belt row folded into the deck belt row); procedures/replace-a-tire; index, log (58 lines).
- Dropped: no pages. Deck/blade-belt notes are not cited on worn-drive-belt.
- Conflicts flagged: drive belt life (yearly vs 3-4 years); purge throttle (half vs high).
- Plain text for later clusters: Bad belt tensioner spring, Brake hung up; Problems Mower pulls to one side, Zero-turn weak on one side, Mower won't drive straight, Engine quits when hot.
- Spot-check (15 random citations): 0 errors.
