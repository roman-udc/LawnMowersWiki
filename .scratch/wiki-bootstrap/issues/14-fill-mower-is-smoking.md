# 14: Fill cluster: mower-is-smoking

Child of [07: Fill pass](07-fill-pass.md). Cluster 6 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 11, 13

**Status:** resolved

**What to build:** the Problem `problems/mower-is-smoking.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

6. **mower-is-smoking**: 58 Sources.
   - Owns Causes: bad-head-gasket, bad-valve-train, oil-in-air-filter-or-tipped-mower, rich-fuel-mixture, spilled-oil-on-engine, worn-piston-rings-or-valve-guides
   - Owns Procedures: check-compression
   - Shared (owned elsewhere): overfilled-oil (engine-starts-then-dies), wrong-oil-or-low-oil (engine-starts-then-dies)

Blocking: this child waits for every earlier cluster that owns a page it shares (11) and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit f9d6b11):**

- Created: problems/mower-is-smoking (64 Sources, all expert-blog; push, self-propelled, riding, zero-turn; gas); causes/bad-head-gasket (43), bad-valve-train (35), oil-in-air-filter-or-tipped-mower (2), rich-fuel-mixture (9), spilled-oil-on-engine (14), worn-piston-rings-or-valve-guides (47); procedures/check-compression (7).
- Updated: causes/overfilled-oil, wrong-oil-or-low-oil, clogged-air-filter, wrong-choke-setting (smoking mentions linked, Sources added); causes/low-compression (links Check compression); procedures/clean-or-replace-the-air-filter, clean-the-carburetor (back-links); index, log (71 lines).
- Dropped: no pages. Two water/rain articles mapped to oil-in-air-filter-or-tipped-mower are not cited (water, not oil).
- Gasket wording: most Sources say "engine gasket"; bad-head-gasket keeps that wording and says they don't specify which gasket. No Source describes valve guides.
- Conflicts flagged: none new.
- Plain text for later clusters: Water in fuel; Problems Engine overheats, Engine quits when hot, Engine loses power.
- Spot-check (15 random citations on mower-is-smoking, worn-piston-rings-or-valve-guides, bad-head-gasket): 1 error (overreaching Related problems line), fixed before commit.
