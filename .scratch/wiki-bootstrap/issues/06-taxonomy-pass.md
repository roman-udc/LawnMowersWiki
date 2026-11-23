# 06: Taxonomy pass (human approval gate)

**What to build:** Before hundreds of pages are written, the maintainer sees and approves the full structure of the wiki. All ~638 existing Sources are classified using the same rules as `/wiki-ingest`, and the result is a proposal document listing every Problem, Cause, Procedure and Guide the wiki will contain, with the Sources mapped to each.

**Blocked by:** 04

**Status:** ready-for-agent

- [ ] Every Source in the raw folder is classified (Problem / Cause / Procedure / Guide / skip) with a Trust tier.
- [ ] A proposal document (in this feature's scratch folder, not in the wiki) lists:
  - proposed Problems with aliases and sibling splits (e.g. won't crank / cranks but won't start / starts then dies)
  - proposed Causes with the Problems they produce
  - proposed Procedures with the Causes they fix
  - proposed Guides
  - mapped Sources for each entry
  - brand-specific Sources merged into each generic page (ADR-0001)
  - skipped Sources with reasons
- [ ] The proposal groups pages into clusters (one Problem with its Causes and Procedures) for the fill pass, and flags pages shared between clusters.
- [ ] Pages already created by tickets 01–04 are shown as existing, so the fill pass does not duplicate them.
- [ ] **The maintainer has reviewed and approved the proposal. Any requested changes are applied and recorded in this ticket's Comments.** The ticket is not done until this approval exists.
