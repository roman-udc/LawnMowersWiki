# Fill-pass brief for a cluster writer (ticket 07)

You fill one cluster of the wiki (one child ticket, `.scratch/wiki-bootstrap/issues/NN-fill-<slug>.md`). Clusters run one at a time on the same branch, so you are the only writer right now.

## Read first

1. `CLAUDE.md`, `GLOSSARY.md`, `docs/adr/*.md`.
2. `.claude/skills/wiki-ingest/SKILL.md`: **its rules govern every page you write** (per-section citations, Trust tier ranking with `n of N`, conflict callouts, Brand notes, OEM part numbers only in Brand notes / Parts & fitment marked "per Source, verify against catalog", Safety, links both ways, index lines with aliases, log format). Its steps 1 and 2 (finding and classifying the batch) are replaced by the notes below, and its "bulk ingest: stop" rule doesn't apply: this is the approved taxonomy pass.
3. Your child ticket, and the matching entries in `.scratch/wiki-bootstrap/taxonomy-proposal.md` (each page's section lists its mapped Sources).
4. `templates/` and one existing page of each type in `wiki/` as a model (for example `wiki/problems/engine-cranks-but-wont-start.md`, `wiki/causes/old-fuel.md`, `wiki/procedures/replace-the-spark-plug.md`, `wiki/guides/customer-intake.md`).

## Where the content comes from

Every Source was read in full by an extraction pass, and its content is stored as notes grouped by target page. For each page you write:

```bash
python .scratch/wiki-bootstrap/collect_notes.py causes/<slug>             # every note for the page, by Source
python .scratch/wiki-bootstrap/collect_notes.py --sources causes/<slug>   # just the Source list
```

- The notes are the evidence: cite only what they contain, and cite the `raw/...` path the block is headed with. If a note is unclear or a number looks off, open the raw Source and check it.
- A Source in the taxonomy mapping that has no notes section for the page is not cited there (its mapping was wrong). A Source whose notes target a page the taxonomy didn't map is still used.
- `grep -rl "## unmapped" .scratch/wiki-bootstrap/notes` shows content that fit no page. If unmapped content clearly belongs to one of your pages, use it.

## Known issues from the extraction pass

- **Every Source is conforming** (checked by script: all five frontmatter keys present). Never log one as non-conforming.
- **Typos and garbled rows inside Sources** are flagged in the notes. Never cite a cell or sentence a note marks as garbled or a typo. Known cases:
  - Several brand "problems" tables (Ferris, Cub Cadet zero-turn, Hustler, John Deere zero-turn, Kubota) have scrambled low-oil and cooling-fins rows in their overheating tables.
  - Many brand tables say "Replace a bad battery" in the safety-switch row. The fix is the switch.
  - Cub Cadet and Big Dog say "minimum of 10% ethanol" once while saying maximum 10% elsewhere: cite the maximum.
  - Bad Boy, Honda and John Deere smoking articles say "engine gasket", mapped to bad-head-gasket: keep their wording.
  - Simplicity says "choke cable" for the clutch cable.
  - The Kubota and Walker won't-move intros say the drive-release levers are "in the operating position" as a cause; the body says they must be in that position for the mower to move.
- **Near-duplicate Sources** (for example Gravely and Simplicity vibration, Hustler and Cub Cadet runs-rough) still count as separate Sources in rankings.
- **Already-flagged conflicts** to call out where they matter:
  - Oiling foam filters: Weed Eater and Toro say oil a washed foam filter; Country Clipper says never oil a foam pre-filter that sits over a paper filter.
  - Lawn-Boy octane: 87 minimum in most places, 89 in the 2-cycle step.
  - Break-in oil change: 5 hours vs 5–10 hours, in the same push-mower article.
- **Part numbers that come only from shop links** are lower confidence: Sears tune-up video "id-…" product IDs and the Exmark hydraulic filter numbers in Amazon links. If used at all, they go in Parts & fitment with the "per Source, verify against catalog" caveat, and the note says where they came from.
- **Corded electric mowers** have no `power_sources` value (vocab: gas, battery, diesel). Put corded content on battery-mower-wont-start, and add a log Note that corded mowers need a vocabulary decision.

## Content outside the approved taxonomy

The taxonomy is approved, so **never create a page that isn't in it.** Fold `## unmapped` content into the nearest approved page when it fits:

- drive-release or bypass lever in the wrong position → causes/bypass-valve-open
- weak hydrostatic transmission → problems/mower-wont-move
- wrong-size blade → causes/bad-blade-adapter-or-loose-blade
- carburetor bowl gasket steps → procedures/rebuild-the-carburetor
- spark test → procedures/test-the-ignition-coil
- 2-cycle fuel mixing → guides/choosing-the-right-gas
- seat-switch multimeter test → procedures/replace-the-seat-switch

Uneven-lawn, scalping and lawn-rolling content is lawn care: skip it. Anything else that fits nowhere goes in the log Note and your ticket comment as "candidate page for the maintainer", with its Sources.

## What to write

- **Owned pages** (the "Owns" lists in your ticket, plus your Problem): create from the template, or update if the file exists (keep its S-numbers, add new ones after). Pages in the ticket that turn out to have no supporting notes are not created: say so in the log Note.
- **Shared pages owned by an earlier cluster** already exist: update them (add your Problem to their `problems` and `## Symptoms it produces`, add any new Sources) and never recreate them.
- **Shared pages owned by a later cluster** don't exist yet: name them as plain text in your Problem page, not links.
- **Pages you create that earlier clusters mentioned as plain text**: grep `wiki/problems` for the name, turn the mention into a link, add the Cause to that Problem's `causes`, its Possible causes table (re-rank it) and its Sources, so links go both ways.
- Problem pages: Possible causes table ranked by the number of Sources naming the Cause for that Problem (from `causes-named:` lines), weighted by Trust tier, written `n of N`, with the tie-break rule stated above the table. Aliases come from `alias:` lines. Related problems link the sibling Problems that exist; the rest stay plain text.
- `mower_types` / `power_sources` on Problems: only values the Sources support (vocab: push, self-propelled, riding, zero-turn / gas, battery, diesel).
- Procedures: `difficulty` easy/moderate/pro, `time_estimate` a string, `tools` a non-empty list, all from the notes. Each Procedure links back to the Causes it fixes.
- Plain language: the support agent and customers read these pages. No brand names in file names or titles.

## Finish the cluster

1. Add an index line for every new page (`wiki/index.md`, under its page type; Problems with `Aliases:`), and add new aliases to existing Problem lines.
2. Append one log entry to `wiki/log.md`: `## 2026-11-23 | ingest | fill pass: <cluster slug>`, then one `- raw/<path> → ingested → <pages>` line per Source this cluster used. A Source already logged by an earlier entry gets a new line here only if this cluster cited it on a new page. Add a `Note:` for pages dropped, Problems folded into a neighbour (with the reason), conflicts flagged, and mentions left as plain text for later clusters.
3. `python tools/validate_wiki.py --allow-unlogged wiki raw` until it prints nothing. Fix every violation, including ones in pages you only updated.
4. `python -m unittest discover tests` must pass.
5. Commit only `wiki/`: `git add wiki && git commit -m "Fill pass: <cluster slug>" -m "<n> Sources. Pages created: …; updated: …" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"`.
6. In your child ticket, tick the boxes, set `**Status:** resolved`, and append a `## Comments` entry (pages created and updated, pages dropped, conflicts flagged). Commit that as `"Resolve ticket NN"` (same co-author line).

Reply with: commit hashes, pages created and updated, pages dropped and why, conflicts flagged, and anything the next cluster must know.
