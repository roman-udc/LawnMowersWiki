# 30: Fill cluster: engine-hard-to-start-when-cold

Child of [07: Fill pass](07-fill-pass.md). Cluster 22 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 29

**Status:** resolved

**What to build:** the Problem `problems/engine-hard-to-start-when-cold.md` with every Cause and Procedure this cluster owns, written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

22. **engine-hard-to-start-when-cold**: 1 Sources.
   - Owns Causes: none
   - Owns Procedures: none
   - Shared (owned elsewhere): none

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24 (fill pass, commit 0749e86):**

- Created: problems/engine-hard-to-start-when-cold (3 Sources, all expert-blog; all mower types; gas, diesel).
- Updated: 15 Causes (bad-fuel-pump, bad-glow-plugs, bad-safety-switch, bad-starter-solenoid, clogged-air-filter, clogged-fuel-filter, clogged-fuel-line, dirty-carburetor, faulty-charging-system, fouled-spark-plug, loose-or-corroded-battery-cables, old-fuel, weak-or-dead-battery, wrong-choke-setting, wrong-oil-or-low-oil); index, log.
- Thin Problem kept, not folded: the notes name 14 Causes with pages plus glow plugs. All rows are 1 of 3 (alphabetical).
- Dropped: no pages. Conflicts flagged: none.
- Spot-check (5 random citations): 0 errors.
