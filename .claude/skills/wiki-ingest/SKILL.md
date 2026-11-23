---
name: wiki-ingest
description: Fold new Sources from raw/ into the lawn mower wiki. Finds Sources not yet in wiki/log.md, classifies each one, updates or creates pages from templates/, updates the index and log, runs the validator until it is clean, and makes one commit. Use when the maintainer runs /wiki-ingest or says they dropped new Sources into raw/.
argument-hint: "[optional: raw paths or a glob to limit this run to a batch]"
---

# /wiki-ingest

Fold every new Source into the wiki without asking the maintainer anything. Read `GLOSSARY.md` and `docs/adr/` once if you haven't this session. The vocabulary (Problem, Cause, Procedure, Guide, Source, Trust tier, Brand note, Part type) is used exactly as defined there.

## Hard rules

- **Never modify anything under `raw/`.** Don't rename, reformat or fix Sources, even broken ones.
- The log (`wiki/log.md`) is the only record of what has been ingested. There is no manifest. Append to it; never rewrite earlier entries.
- Every claim on a page traces to a Source cited in that section. Nothing comes from your own knowledge or the chat.
- Links are relative markdown links, never `[[wikilinks]]` (ADR-0002).
- One ingest = one commit.

## 1. Find the new Sources

List every file under `raw/` and drop each path that already appears in `wiki/log.md` as `raw/<path>` (any outcome counts: ingested, skipped or non-conforming). What's left is this run's batch.

```bash
python tools/validate_wiki.py wiki raw | grep '\[unlogged\]'
```

prints exactly that list (one `raw/...: [unlogged]` line per new Source).

If the maintainer passed paths or a glob, limit the batch to those. Otherwise take everything. If the batch is larger than about 30 Sources, it's a bulk ingest: stop and tell the maintainer to use the taxonomy pass (spec, "Bootstrap ingest") instead.

## 2. Read and classify each Source

Read each Source in full. Record for each:

**Conformance.** A conforming Source lives at `raw/<SourceKind>/<domain>/<slug>.md` and has frontmatter with `source_url`, `title`, `domain`, `type`, `published`. A Source that doesn't conform is **still ingested**. Its log line adds `non-conforming: <what's wrong>`.

**Trust tier**, from the domain (folder or `domain` field), else the `type` field:

| Domain / type | Trust tier |
|---|---|
| searspartsdirect.com, OEM manuals, parts-supplier repair guides | manufacturer |
| poweredoutdoors.com, other repair blogs | expert-blog |
| forum domains (reddit.com, mytractorforum.com, lawnmowerforum.com, any `type: forum`) | forum |

For an unknown domain, pick the closest tier and say why in the log line.

**Kind of content**, one or more of:

- **Problem**: a symptom as an owner reports it ("won't start", "cuts uneven").
- **Cause**: a specific reason behind one or more Problems.
- **Procedure**: step-by-step repair or maintenance.
- **Guide**: general owner know-how (fuel storage, battery care, customer intake).
- **skip**: buying guides and "best mower for…", lawn-care advice, "where to get repairs" / repair-shop and dealer listings, and anything else with no repair or maintenance value. A Source that mixes skip content with repair content is ingested for the repair content only.

## 3. Map content to pages

**Prefer updating an existing page.** Read `wiki/index.md` (Problems are matched by title and aliases) and open the candidate pages. Create a page only when nothing fits.

- Problems are keyed by symptom, generic across brands; brand detail goes to Brand notes (ADR-0001). Split a symptom family only when the sub-symptoms point to clearly different Causes ("won't crank" vs "cranks but won't start" vs "starts then dies"). Mower type and Power source are tags, not splits. A per-brand Source ("Bad Boy won't start") updates the generic Problem.
- File names are kebab-case English, named after the symptom or cause, never a brand.
- New pages: copy the matching template from `templates/`, keep every H2 in order, and delete the template's HTML comment.

## 4. Write the pages

For every page you touch:

- **Cite per section.** End each section with `Sources: [Sn](../../raw/...)`, using the page's existing S-numbers. Add a new Source to `## Sources` with its title and Trust tier, as `- [Sn](../../raw/...) — <title> (<tier>)`.
- **Keep `source_count`** equal to the distinct Sources in `## Sources`, and set `updated` to today.
- **Keep links both ways.** Problem ↔ Cause and Cause ↔ Procedure links go in both directions. Frontmatter `causes` / `problems` / `procedures` lists must match the body links. A Guide's `related` entries must be linked from `## Related`.
- **Rank "How common"** in a Problem's Possible causes table by the number of Sources naming that Cause for that Problem, weighted by Trust tier (manufacturer > expert-blog > forum; inside forum, a confirmed fix > an untested suggestion). Write it as `n of N`. State the tie-break rule above the table. Re-rank the whole table after adding Sources.
- **Conflicts.** When Sources disagree (a torque value, a gap, whether to do a step, which fix is first), never pick one silently. Add a callout in the section where it matters:

  ```markdown
  > **⚠ Conflicting advice:** <position A> ([S1](...), manufacturer) vs <position B> ([S4](...), expert-blog).
  ```

- **Single forum report.** A tip backed by one forum Source only is labelled: `(single forum report, untested)`, or `(single forum report, confirmed by the poster)` when the thread says it worked.
- **OEM part numbers** go only in Brand notes or Parts & fitment, marked "per Source, verify against catalog". Elsewhere use Part types.
- **Safety** warnings belong on every page whose repair could hurt someone.
- Sibling Problems a page mentions but which have no page yet stay as plain text, not broken links.

## 5. Update the index

Every new page gets one line in `wiki/index.md` under its page type: link, a one-line summary and, for Problems, `Aliases: "…", "…"`. When a Source adds a customer phrasing to an existing Problem, add it both to the page's `aliases` and to the index line.

## 6. Append the log entry

Append one entry to `wiki/log.md`:

```markdown
## YYYY-MM-DD | ingest | <short label for the batch>

- raw/<path> → ingested → problems/x.md, causes/y.md
- raw/<path> → skipped: buying guide
- raw/<path> → ingested → causes/y.md (non-conforming: no frontmatter)
```

Every Source in the batch gets exactly one line, including skips, starting `- raw/<path> → ` (the validator only counts these lines; a path mentioned in a Note doesn't count). Page paths after the arrow are relative to `wiki/`. Add a `Note:` paragraph for anything the next session should know (conflicts flagged, pages left for later).

## 7. Validate until clean

```bash
python tools/validate_wiki.py wiki raw
```

Fix every violation and run it again until it prints nothing and exits 0. Don't commit while it reports anything.

While the bootstrap ingest is unfinished (raw/ still holds Sources no ingest has looked at), a batch run uses `--allow-unlogged` so that Sources outside the batch don't block it. Before using the flag, confirm that the plain run lists none of this batch's paths as `[unlogged]`.

## 8. Commit

Stage only `wiki/` and commit once:

```bash
git add wiki
git commit -m "Ingest: <label>" -m "<n> ingested, <m> skipped. Pages created: …; updated: …"
```

Then report to the maintainer: Sources ingested, skipped (with reasons), non-conforming, pages created and updated, and any conflicts flagged.
