# 23: Fill cluster: battery-keeps-dying

Child of [07: Fill pass](07-fill-pass.md). Cluster 15 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 22

**Status:** resolved

**What to build:** the Problem `problems/battery-keeps-dying.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

15. **battery-keeps-dying**: 12 Sources.
   - Owns Causes: bad-alternator, parasitic-battery-drain
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-battery (battery-mower-wont-start)

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (24) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 9bf71fc):**

- Created: problems/battery-keeps-dying (19 Sources; riding, zero-turn; gas); causes/bad-alternator (12), parasitic-battery-drain (7).
- Updated: causes weak-or-dead-battery, faulty-charging-system, loose-or-corroded-battery-cables, bad-wiring-or-ground; procedures test-the-battery, charge-the-battery; problems/engine-wont-crank (Related line); index, log (23 lines; the commit body's "20 Sources" undercounts).
- Dropped: no pages. The notes' riding-mower "bad-battery" is counted as weak-or-dead-battery; bad-battery (cluster 24) is left for battery-powered mowers and has no row here.
- Conflicts flagged: running voltage 13-14 V vs 13.2-13.9 V or higher (bad-alternator).
- Plain text for later clusters: Battery mower won't start.
- Spot-check (15 random citations on battery-keeps-dying, bad-alternator, parasitic-battery-drain): 0 errors.
