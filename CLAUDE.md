# LawnMowersWiki

## Agent skills

### Issue tracker

Issues are tracked as local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default canonical labels (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), recorded as a `Status:` line in each issue file. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` + `docs/adr/` at the vault root. See `docs/agents/domain.md`.

## Wiki

- Spec: `.scratch/wiki-bootstrap/spec.md`. Vocabulary: `GLOSSARY.md` (Problem, Cause, Procedure, Guide, Source, Trust tier, …). Decisions: `docs/adr/` (0001 symptom-keyed Problems, 0002 no RAG / relative markdown links, 0003 support agent is read-only).
- Layout: `raw/` holds immutable Sources (never edit). `wiki/` is the LLM-owned wiki: `index.md` (routing table, grouped by page type, Problems with aliases), `log.md` (append-only, entry header `## YYYY-MM-DD | operation | label`), and `problems/`, `causes/`, `procedures/`, `guides/`.
- Templates: `templates/` (one per page type, kept outside the wiki). Copy the template, keep every section in order, and cite Sources per section.
- Validator: `python tools/validate_wiki.py wiki raw` (PyYAML only; see `requirements.txt`). It must be clean before any commit that touches `wiki/`.
- Tests: `python -m unittest discover tests`. Fixtures live in `tests/fixtures/`.
