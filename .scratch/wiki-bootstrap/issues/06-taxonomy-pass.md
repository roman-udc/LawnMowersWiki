# 06: Taxonomy pass (human approval gate)

**What to build:** Before hundreds of pages are written, the maintainer sees and approves the full structure of the wiki. All ~638 existing Sources are classified using the same rules as `/wiki-ingest`, and the result is a proposal document listing every Problem, Cause, Procedure and Guide the wiki will contain, with the Sources mapped to each.

**Blocked by:** 04

**Status:** resolved

- [x] Every Source in the raw folder is classified (Problem / Cause / Procedure / Guide / skip) with a Trust tier.
- [x] A proposal document (in this feature's scratch folder, not in the wiki) lists:
  - proposed Problems with aliases and sibling splits (e.g. won't crank / cranks but won't start / starts then dies)
  - proposed Causes with the Problems they produce
  - proposed Procedures with the Causes they fix
  - proposed Guides
  - mapped Sources for each entry
  - brand-specific Sources merged into each generic page (ADR-0001)
  - skipped Sources with reasons
- [x] The proposal groups pages into clusters (one Problem with its Causes and Procedures) for the fill pass, and flags pages shared between clusters.
- [x] Pages already created by tickets 01–04 are shown as existing, so the fill pass does not duplicate them.
- [x] **The maintainer has reviewed and approved the proposal. Any requested changes are applied and recorded in this ticket's Comments.** The ticket is not done until this approval exists.

## Comments

**2026-11-23, taxonomy pass.** Proposal: `.scratch/wiki-bootstrap/taxonomy-proposal.md`; per-Source classification: `.scratch/wiki-bootstrap/taxonomy-classification.jsonl`. 638 Sources classified (606 to ingest, 32 skipped): 26 Problems, 110 Causes, 44 Procedures, 16 Guides, 27 clusters. Classification was mostly heading-level; the fill pass must confirm each Cause/Procedure mapping by reading the Source in full.

**2026-11-23, maintainer approval.** Approved as is, no changes requested. Decisions recorded:
- Thin Problems (engine-backfires, mower-is-leaking-oil, loose-steering, mower-creeps-in-neutral, flat-tire, engine-hard-to-start-when-cold) are kept; the fill pass gives each its Causes from the full read, or folds it into a neighbour and records why in the log.
- battery-mower-wont-start stays a separate Problem (electric Causes share nothing with gas engines).
