# 15: Fill cluster: mower-is-leaking-gas

Child of [07: Fill pass](07-fill-pass.md). Cluster 7 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 09, 14

**Status:** resolved

**What to build:** the Problem `problems/mower-is-leaking-gas.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

7. **mower-is-leaking-gas**: 55 Sources.
   - Owns Causes: bad-carburetor-gasket-or-needle-and-seat, bad-gas-cap-seal, bad-shutoff-valve, cracked-fuel-filter, cracked-fuel-line, cracked-fuel-tank, cracked-primer-bulb, overfilled-fuel-tank
   - Owns Procedures: none
   - Shared (owned elsewhere): bad-fuel-pump (engine-cranks-but-wont-start)

Blocking: this child waits for every earlier cluster that owns a page it shares (09) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit cb5b01c):**

- Created: problems/mower-is-leaking-gas (56 Sources; push, self-propelled, riding, zero-turn; gas); causes/bad-carburetor-gasket-or-needle-and-seat (36), bad-gas-cap-seal (38), bad-shutoff-valve (28), cracked-fuel-filter (23), cracked-fuel-line (37, incl. kinked/punctured lines), cracked-fuel-tank (33), cracked-primer-bulb (11), overfilled-fuel-tank (1).
- Updated: causes/bad-fuel-pump, dirty-carburetor, clogged-fuel-filter, old-fuel; problems/engine-cranks-but-wont-start, engine-starts-then-dies (Bad gas cap seal rows linked, order unchanged); procedures rebuild-the-carburetor, replace-the-carburetor, clean-the-carburetor, replace-the-fuel-filter, replace-the-fuel-line (back-links); index, log (70 lines).
- Dropped: no pages.
- Conflicts flagged: metal-tank rust hole, epoxy patch vs replace (cracked-fuel-tank).
- Open question: gas-cap rows on the two non-leak Problems describe the cap vent; consider re-pointing to plugged-fuel-cap-vent.
- Plain text for later clusters: Engine only runs with the choke on.
- Spot-check (15 random citations on mower-is-leaking-gas, bad-carburetor-gasket-or-needle-and-seat, bad-gas-cap-seal): 0 errors.
