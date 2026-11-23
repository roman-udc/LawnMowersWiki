# 07: Fill pass

**What to build:** The wiki contains every page from the approved taxonomy, built from all mapped Sources. The support agent can then handle the full range of Problems found in the current Sources.

**Blocked by:** 06

**Status:** ready-for-agent

- [ ] First step: this ticket splits itself into one child ticket per cluster from the approved taxonomy (following the issue-tracker conventions, numbered after the existing tickets). Each child is blocked by any cluster that owns a page it shares.
- [ ] Each cluster: the Problem, its Causes and its Procedures are written or updated from all mapped Sources, following the `/wiki-ingest` rules (citations, Trust tier ranking, conflict callouts, Brand notes, OEM part number caveats). The index and log are updated, the validator passes, and the cluster gets its own commit.
- [ ] Guides from the taxonomy are written, either as their own cluster or together with the cluster they most relate to.
- [ ] Skipped Sources are recorded in the log, so every Source in the raw folder has a log entry and the validator's log-coverage rule passes on the whole wiki.
