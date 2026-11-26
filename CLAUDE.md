# LawnMowersWiki

## Development-only files (not in Git)

`.scratch/`, `docs/` and `tests/` are ignored by Git. They exist only on the developer's machine, so they will be missing from a fresh clone. When they are absent, skip anything below that depends on them.

- Issue tracker: local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.
- Triage labels: the default canonical labels (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), recorded as a `Status:` line in each issue file. See `docs/agents/triage-labels.md`.
- Domain docs: single context, with `GLOSSARY.md` at the vault root (tracked) and ADRs in `docs/adr/`. See `docs/agents/domain.md`.
- Spec: `.scratch/wiki-bootstrap/spec.md`. ADRs: 0001 symptom-keyed Problems, 0002 no RAG / relative markdown links, 0003 support agent is read-only.
- Tests: `python -m unittest discover tests`. Fixtures live in `tests/fixtures/`.

## Wiki

- Overview for the maintainer: `README.md`. Vocabulary: `GLOSSARY.md` (Problem, Cause, Procedure, Guide, Source, Trust tier, …).
- Layout: `raw/` holds immutable Sources (never edit). Expert notes from the specialist go in `raw/Expert/in-house/` with `type: expert-note` and trust tier `expert`. `wiki/` is the LLM-owned wiki: `index.md` (routing table, grouped by page type, Problems with aliases), `log.md` (append-only, entry header `## YYYY-MM-DD | operation | label`), and `problems/`, `causes/`, `procedures/`, `guides/`.
- Templates: `templates/` (one per page type, kept outside the wiki). Copy the template, keep every section in order, and cite Sources per section.
- Ingest: run the project skill `/wiki-ingest` (`.claude/skills/wiki-ingest/SKILL.md`) to fold new Sources into the wiki. It commits `wiki/` together with the batch's `raw/` files. Don't edit wiki pages from Sources by hand outside it.
- Lint: run the project skill `/wiki-lint` (`.claude/skills/wiki-lint/SKILL.md`) for a health report in `reports/lint/`.
- Validator: `python tools/validate_wiki.py wiki raw` (PyYAML only; see `requirements.txt`). It must be clean before any commit that touches `wiki/`. Until the bootstrap ingest has logged every Source, batch ingests run it with `--allow-unlogged` (the `unlogged` rule flags every raw file missing from the log).
- Work is committed straight to `main`.
