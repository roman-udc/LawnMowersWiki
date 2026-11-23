# 04: /wiki-ingest skill and log coverage

**What to build:** The maintainer drops Sources into the raw folder, runs `/wiki-ingest`, and the knowledge is folded into the wiki without further input. The skill finds new Sources by comparing the raw folder with the log, classifies each Source (Problem / Cause / Procedure / Guide / skip), assigns a Trust tier, updates existing pages or creates new ones from the templates, flags conflicts, updates the index, appends to the log, repeats the validator until it passes, and commits.

**Blocked by:** 02, 03

**Status:** ready-for-agent

- [ ] New validator rule, with failing fixtures: any Source in the raw folder that has no log entry is reported.
- [ ] The ingest skill is a project skill and encodes all of the following:
  - finds new Sources by comparing the raw folder with the log (no separate manifest)
  - never modifies Sources
  - assigns the Trust tier from the Source's domain or type (searspartsdirect.com → manufacturer, poweredoutdoors.com → expert-blog, forum domains → forum)
  - skip policy: buying guides, lawn-care advice and repair-shop listings are skipped and logged with a reason
  - ingests non-conforming Sources anyway and notes them in the log
  - prefers updating existing pages, and creates a page only when nothing fits; Problem granularity follows ADR-0001
  - cites per section and keeps source_count up to date
  - ranks "how common" by Source count weighted by Trust tier
  - adds "⚠ Conflicting advice" callouts naming both sides and their Sources
  - marks single-report forum tips as such
  - updates the index with aliases
  - writes the log entry listing each raw path with its outcome
  - repeats the validator until it passes
  - makes one commit per ingest
- [ ] Verified on a real batch of about 5–10 Sources that touch the tracer Problem cluster, plus at least one Source that should be skipped. The resulting log entry, page updates and commit are correct.
- [ ] The project instructions point to the skill.
