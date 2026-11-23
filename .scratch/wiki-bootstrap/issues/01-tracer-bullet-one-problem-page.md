# 01: Tracer bullet: one Problem page end to end

**What to build:** The thinnest complete path through the wiki system. The repository is set up and one real Problem page exists, built from the Problem template, cited from its Sources, listed in the index, recorded in the log, checked by the validator and committed. Afterwards, the maintainer can open the wiki in Obsidian and see one well-formed Problem page, and the validator reports it clean. See the spec (`../spec.md`), GLOSSARY.md and ADRs 0001–0003.

**Blocked by:** None (can start immediately)

**Status:** resolved

- [x] The project is a git repository. Obsidian ignore filters keep Sources, templates, docs and scratch out of view, and the wiki stays visible.
- [x] A wiki skeleton exists with an index (grouped by page type) and an append-only log using the greppable `date | operation | label` entry header.
- [x] A Problem template exists outside the wiki, with the frontmatter keys and section order defined in the spec (Summary → Diagnostic questions → Quick triage → Possible causes → Brand notes → Tips & life hacks → Parts commonly needed → Safety → When to send to a technician → Related problems → Sources).
- [x] A deterministic Python validator (PyYAML only) takes a wiki root and a raw root, prints violations and exits non-zero when any are found. Rules in this ticket:
  - Problem frontmatter keys and controlled-vocabulary values (mower_types, power_sources)
  - required sections present and in order
  - source_count equals the number of distinct Sources listed
  - every page is in the index, and every index entry points to an existing page
- [x] Fixture tests: one valid baseline fixture passes clean, and each rule above has at least one failing fixture that triggers exactly that violation. The tests check only the validator's output and exit status.
- [x] One real Problem page (e.g. "Engine cranks but won't start") is written from the relevant Sources. It has aliases, Diagnostic questions in answer → Cause table form, Brand notes and per-section citations. Cause links may point to pages ticket 02 will create, because link integrity is not checked yet.
- [x] The page has an index line (with aliases) and the log records the Sources used.
- [x] Project instructions (CLAUDE.md) point to the glossary, the ADRs, the templates and the validator.
- [x] The validator passes on the real wiki, and everything is committed.
