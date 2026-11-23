# 05: /wiki-lint skill

**What to build:** The maintainer runs `/wiki-lint` and gets a health report for the wiki. The report covers the structural violations the validator finds, plus content-level problems found by LLM review.

**Blocked by:** 04

**Status:** resolved

- [x] The lint skill is a project skill. It runs the validator first and reports its violations.
- [x] It then reviews content and reports:
  - Causes or Procedures mentioned in text that have no page
  - contradictory claims across pages with no conflict callout
  - claims that newer Sources have superseded
  - Problems that may overlap and should be merged or split
  - thin pages backed by a single Source
- [x] The report separates structural violations (which must be fixed) from content suspicions (which need review). It proposes fixes but makes no edits unless asked.
- [x] Each lint run is recorded in the log.
- [x] The project instructions point to the skill.
- [x] Run once on the current wiki, with the result committed.
