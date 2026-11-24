# 12: Fill cluster: uneven-cut

Child of [07: Fill pass](07-fill-pass.md). Cluster 4 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11

**Status:** resolved

**What to build:** the Problem `problems/uneven-cut.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

4. **uneven-cut**: 72 Sources.
   - Owns Causes: bad-blade-adapter-or-loose-blade, bad-tire, bent-deck-or-deck-shell, blade-installed-upside-down, debris-on-deck-or-pulleys, dull-or-bent-blade, incorrect-path-overlap, mowing-too-fast, unlevel-deck, wrong-cutting-height, wrong-engine-speed, wrong-tire-pressure
   - Owns Procedures: level-the-deck, measure-a-mower-blade, repair-a-flat-tire, replace-a-tire, sharpen-and-replace-the-blades
   - Shared (owned elsewhere): bent-crankshaft (mower-is-vibrating), bent-spindle-or-bad-spindle-bearing (mower-is-vibrating), worn-or-stretched-belt (mower-is-vibrating), worn-pulley-or-idler-bearing (mower-is-vibrating)

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. Shared pages owned by later clusters (13) do not exist yet: mention them as plain text, and the owning cluster turns them into links, adds the back-link and re-ranks this Problem's table.

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit b95eae0):**

- Created: problems/uneven-cut (78 Sources; push, self-propelled, riding, zero-turn; gas, battery); causes/bad-blade-adapter-or-loose-blade (31, incl. wrong-size/aftermarket blades), bad-tire (12), bent-deck-or-deck-shell (27), blade-installed-upside-down (34), debris-on-deck-or-pulleys (134), dull-or-bent-blade (123), incorrect-path-overlap (27), mowing-too-fast (66), unlevel-deck (32), wrong-cutting-height (10), wrong-engine-speed (46), wrong-tire-pressure (48); procedures/level-the-deck (20), measure-a-mower-blade (23), repair-a-flat-tire (4), replace-a-tire (4), sharpen-and-replace-the-blades (45).
- Updated: problems/engine-starts-then-dies (four plain-text rows linked; counts and order unchanged); index, log. 238 log lines.
- Dropped: no pages. A few Sources were not cited where their notes held only a pointer to another article.
- Conflicts flagged: blade replacement interval; file angle; sharpen vs replace a dull blade; deck front-to-rear rake; deck position while measuring. The "reverse threaded, also known as right-hand" claim is recorded as a Source contradiction, and no thread direction is stated.
- Plain text for later clusters on uneven-cut: bent spindle, worn belt, worn pulley, bent crankshaft, clogged deck chute (overlaps debris-on-deck-or-pulleys; decide merge), worn blade sail; Problems mower-is-vibrating, belt-keeps-coming-off, mower-pulls-to-one-side.
- Spot-check (15 random citations on debris-on-deck-or-pulleys, dull-or-bent-blade, uneven-cut): 0 errors.
