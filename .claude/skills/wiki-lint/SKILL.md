---
name: wiki-lint
description: Health check for the lawn mower wiki. Runs the structural validator, then reviews page content for missing pages, unflagged conflicts, superseded claims, overlapping Problems and thin pages. Writes a report that separates must-fix violations from suspicions, logs the run, and edits no wiki page unless asked. Use when the maintainer runs /wiki-lint or asks how healthy the wiki is.
argument-hint: "[optional: page paths or a glob to limit the content review]"
---

# /wiki-lint

Report on the wiki's health. **Read-only for wiki pages:** propose fixes, never apply them unless the maintainer asks in this session. Only three things get written: the report, one log entry, and one commit.

Read `GLOSSARY.md` and `docs/adr/` once if you haven't this session. Use the vocabulary (Problem, Cause, Procedure, Guide, Source, Trust tier) exactly as defined there.

## 1. Structural check (validator)

```bash
python tools/validate_wiki.py wiki raw
```

Every line is a structural violation: `<page>: [<rule>] <message>`. These **must be fixed**. Group them by rule in the report.

`[unlogged]` lines are a special case. While the bootstrap ingest is unfinished (raw/ still holds Sources that no ingest has looked at), there will be hundreds of them. Don't list them all. Report the count and say whether it went down since the last lint entry in `wiki/log.md`. List them one by one only once fewer than about 30 are left.

The validator doesn't check for **orphan pages**: pages that no other page links to (the index doesn't count). Check that yourself and report orphans as structural.

## 2. Content review

Read every page under `wiki/problems/`, `wiki/causes/`, `wiki/procedures/` and `wiki/guides/`, plus `wiki/index.md` and the Notes in `wiki/log.md`. If the maintainer passed paths, review only those, but still run step 1 on the whole wiki. Open a raw Source only to check a specific suspicion, such as its `published` date or what it actually says. Report each finding under one of these headings:

1. **Missing pages.** A Cause, Procedure, Problem or Guide named in the text (plain text, a "No Procedure page covers this yet" line, a "page not written yet" link, a log Note) that has no page. Count how many pages mention it. Inline step lists inside a Cause's Fix section are Procedure candidates.
2. **Unflagged conflicts.** Two pages, or two sections of one page, that give different advice with no `⚠ Conflicting advice` callout where the reader would see it. A callout that exists on one page but not on another page repeating the same advice counts. Malformed callouts count too, for example Sources cited as bare `S1` without links.
3. **Superseded claims.** A claim backed only by an older Source when a newer Source (compare `published` in the raw frontmatter) says something different. Note the dates and Trust tiers. A newer Source of a lower tier doesn't automatically win. Say so and leave the call to the maintainer.
4. **Overlapping Problems.** Problems whose symptoms or Causes overlap enough that they should be merged, or a Problem covering sub-symptoms that point to clearly different Causes and should be split (ADR-0001). Include planned Problems the text already refers to when their boundaries are unclear.
5. **Thin pages.** Pages whose `## Sources` lists only one Source. Also flag "near-thin" pages, where one Source carries nearly every section, and Possible-causes rows that rest on a single Source.

For each finding, give the page(s) with relative paths, what's wrong in one or two sentences, and a **proposed fix**. Write "none found" under any empty heading. Don't invent findings to fill a heading.

## 3. Write the report

Write the report to `reports/lint/YYYY-MM-DD.md` (add `-2`, `-3`, … if one already exists for today):

```markdown
# Wiki lint YYYY-MM-DD

Scope: <whole wiki | paths>. Pages reviewed: <n>. Validator: <n> violations (<n> unlogged).

## Structural violations (must fix)
### <rule>
- <page>: <message> → <proposed fix>
### Orphan pages
...

## Content suspicions (needs review)
### Missing pages
### Unflagged conflicts
### Superseded claims
### Overlapping Problems
### Thin pages

## Suggested next steps
<short ordered list: what to fix first>
```

The report lives outside `wiki/` on purpose. It is a snapshot, not a wiki page, so it isn't indexed or validated.

## 4. Log the run

Append one entry to `wiki/log.md`:

```markdown
## YYYY-MM-DD | lint | <scope label>

Report: reports/lint/YYYY-MM-DD.md. Structural: <n> violations (<n> unlogged, <n> other), <n> orphans. Content: <n> missing pages (<n> Problems, <n> Causes, <n> Procedures, <n> Guides), <n> unflagged conflicts, <n> superseded claims, <n> overlap suspicions, <n> thin pages (<n> near-thin).
```

Never start a line in a lint entry with `- raw/`. The validator reads those lines as ingest records.

## 5. Commit

Run the validator again (`--allow-unlogged` while bootstrap is unfinished) and make sure the log entry broke nothing. Then:

```bash
git add reports/lint wiki/log.md
git commit -m "Lint: <scope label>" -m "<one-line summary of the counts>"
```

Tell the maintainer the counts, the top few findings and the report path. Offer to apply specific fixes. Fixes that change page content from Sources go through `/wiki-ingest` or the fill pass, not through lint.
