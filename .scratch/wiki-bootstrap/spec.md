# Spec: Lawn mower troubleshooting wiki (bootstrap)

Status: ready-for-agent

## Problem Statement

The customer-support department is building an AI agent to help customers with lawn mower repairs, choosing spare parts and installing new parts. The agent needs a knowledge base to answer from. The raw material already exists: hundreds of articles clipped from repair blogs and parts-supplier sites (forum threads will follow), stored as Sources. In that form it is unusable. The articles are organized per brand and repeat each other heavily ("Bad Boy won't start", "Ariens won't turn over", "bad Kawasaki starter solenoid"). They mix repair content with buying guides and lawn-care advice. They contradict each other at times. And they give the agent no way to go from what a customer says to the right diagnosis, fix and part.

There is also no repeatable way to keep a knowledge base current as new Sources are collected. Each new batch of articles or forum threads would otherwise need manual reorganization.

## Solution

An LLM-maintained Markdown wiki that sits between the immutable Sources and the support agent. The support agent reads it directly, starting from an index.

- **Problem** pages are keyed by the symptom as a customer would report it, and they are generic across brands. Each one opens with **Diagnostic questions** whose answers point to the likely **Causes**, followed by a quick triage checklist, the possible Causes ranked by how often the Sources mention them, Brand notes, tips, the Part types usually needed, safety notes, when to escalate, and the Sources cited.
- **Cause** pages hold the shared diagnosis and fix detail for a cause that produces several Problems.
- **Procedure** pages give step-by-step repair and maintenance instructions.
- **Guide** pages hold general owner know-how, including a shared customer-intake guide.

The maintainer drops new Sources into the raw folder and runs an ingest command. The agent then folds the new knowledge into the existing pages, records what it did in a log, checks the wiki with a deterministic validator, and commits. A lint command checks the wiki's health on demand.

The first bulk ingest of the existing ~638 Sources happens in two phases: a taxonomy pass that proposes the page list for the maintainer to approve, then a fill pass that writes the pages.

## User Stories

### Support agent (runtime consumer)

1. As the support agent, I want a single index listing every Problem with its customer-phrasing aliases, so that I can match what a customer says to the right page without searching the whole wiki.
2. As the support agent, I want Problem pages keyed by symptom rather than by brand, so that one page covers a customer's issue whatever brand they own.
3. As the support agent, I want sibling Problems that sound alike ("won't crank" vs "cranks but won't start" vs "starts then dies") to be separate pages that cross-reference each other, so that I can switch pages when the customer's answers show I picked the wrong one.
4. As the support agent, I want Diagnostic questions near the top of each Problem page, so that I ask the customer the right things before suggesting fixes.
5. As the support agent, I want each Diagnostic question to show which Causes each answer points toward, so that every answer narrows the diagnosis.
6. As the support agent, I want a shared customer-intake guide (brand, model, serial number, engine make, Mower type, age, last run), so that I collect the basics once instead of each page repeating them.
7. As the support agent, I want a quick triage checklist ordered by likelihood and how cheap the check is, so that I can lead the customer through the easiest checks first.
8. As the support agent, I want possible Causes ranked by how many Sources mention them for this Problem, so that I suggest the most common Causes first.
9. As the support agent, I want each Cause to show its telltale signs and how hard the fix is, so that I can judge whether the customer can do the repair themselves.
10. As the support agent, I want Cause pages that explain how to confirm the Cause (tests, measurements, visual checks), so that customers don't replace parts that aren't broken.
11. As the support agent, I want Cause pages to link to the Procedures that fix them, so that I can move from diagnosis to repair steps.
12. As the support agent, I want Procedure pages with difficulty, time estimate, tools, Part types, safety notes, numbered steps and a "verify the fix" section, so that I can walk a customer through installing a part.
13. As the support agent, I want "Before you start" questions on Cause and Procedure pages (e.g. engine brand, deck size, belt part number), so that I gather the details needed to pick the right part and steps.
14. As the support agent, I want Brand notes on Problem, Cause and Procedure pages, so that I can give model-specific guidance when the customer's brand has quirks.
15. As the support agent, I want the Part types for each Problem and Cause, with fitment notes, so that I can help the customer find the right spare part.
16. As the support agent, I want OEM part numbers marked as "per Source, verify against catalog", so that I never present an unverified part number as certain fitment.
17. As the support agent, I want safety warnings on every relevant page, so that I never guide a customer into a dangerous repair without warning them.
18. As the support agent, I want a "when to send to a technician" section, so that I know when to stop guiding a DIY repair and escalate.
19. As the support agent, I want conflicting advice shown explicitly, with both sides and their Sources, so that I can present the options honestly instead of silently picking one.
20. As the support agent, I want claims to reflect the Trust tier of their Sources, so that manufacturer guidance and confirmed forum fixes outrank one-off forum suggestions.
21. As the support agent, I want single-report forum tips labelled as such, so that I present them as anecdotal.
22. As the support agent, I want tips and life hacks collected on each page, so that I can share practical advice beyond the formal fix.
23. As the support agent, I want links to be standard relative markdown links, so that I can follow them with plain file-reading tools.
24. As the support agent, I want frontmatter listing Mower types and Power sources, so that I can tell quickly whether a page applies to the customer's equipment.
25. As the support agent, I want Guide pages on topics like fuel storage, winterizing and battery care, so that I can give preventive advice after resolving the Problem.
26. As the support agent, I want every page to stand on its own when read whole, so that I don't have to read many pages to answer one question.

### Wiki maintainer (human)

27. As the maintainer, I want to drop new Sources into the raw folder and run a single ingest command, so that the wiki stays current without manual editing.
28. As the maintainer, I want new Sources to follow the existing convention (raw/<SourceKind>/<domain>/<slug>.md with source_url, title, domain, type, published frontmatter), so that ingest can identify and classify them.
29. As the maintainer, I want Sources that don't follow the convention to be ingested anyway with a note in the log, so that a formatting slip doesn't block knowledge.
30. As the maintainer, I want the Sources to never be modified by the agent, so that they remain the source of truth.
31. As the maintainer, I want the first bulk ingest to start with a taxonomy pass that proposes the full list of Problems, Causes, Procedures and Guides, so that I can approve the structure before hundreds of pages are written.
32. As the maintainer, I want the taxonomy proposal to show which Sources map to each proposed page and which duplicates were merged, so that I can check the merges.
33. As the maintainer, I want the fill pass to proceed cluster by cluster after approval, so that progress is incremental and reviewable.
34. As the maintainer, I want later ingests to update existing pages and create new ones only when nothing fits, so that the wiki doesn't fill with near-duplicates.
35. As the maintainer, I want every ingest to append to a log recording each Source's outcome (ingested → pages touched, or skipped with a reason), so that I have a history of what changed and why.
36. As the maintainer, I want the ingest command to find not-yet-ingested Sources by comparing the raw folder with the log, so that I never have to say which files are new.
37. As the maintainer, I want buying guides, lawn-care advice and other non-repair Sources skipped and logged with a reason, so that they aren't re-evaluated on every ingest.
38. As the maintainer, I want the Trust tier worked out from each Source's domain or type at ingest, so that I don't have to label Sources by hand.
39. As the maintainer, I want every page to cite its Sources per section and keep a source count, so that I can audit where any claim came from.
40. As the maintainer, I want templates for each page type kept outside the wiki, so that all pages share one structure and the support agent never mistakes a template for content.
41. As the maintainer, I want each ingest to end with a clean validator run, so that structural errors never get committed.
42. As the maintainer, I want each ingest committed to git separately, so that I can see what a Source changed and roll back a bad ingest.
43. As the maintainer, I want a lint command that reports broken links, orphan pages, missing back-links, index drift, source-count mismatches, Problems without Causes, Causes without Problems, and Sources never ingested, so that I can keep the wiki healthy as it grows.
44. As the maintainer, I want lint to also list content-level suspicions (Causes mentioned in text without a page, conflicts that aren't flagged), so that I know where human or agent review is needed.
45. As the maintainer, I want to browse the wiki in Obsidian with the graph view, so that I can see the shape of the knowledge base and spot gaps visually.
46. As the maintainer, I want project instructions that point any future agent session to the templates, skills, glossary and ADRs, so that every session maintains the wiki the same way.
47. As the maintainer, I want the index split per page type if it grows past a few hundred lines, so that it stays usable as the agent's routing table.

### Support department / business

48. As the support department, I want the agent's knowledge to trace back to Sources only, not to unverified chat content, so that reps can trust and audit what the agent says.
49. As the support department, I want the wiki to name Part types rather than SKUs, so that exact part lookup is left to the parts catalog, which is the authoritative system.
50. As the support department, I want the wiki in English, matching the Sources, so that content isn't distorted by translation.

## Implementation Decisions

- **Three layers.**
  - Sources: immutable raw folder.
  - The wiki: LLM-owned and read-only for the support agent (ADR-0003).
  - The schema: templates, skills and project instructions.
- **Wiki layout.**
  - An index and an append-only log at the wiki root.
  - One folder per page type: problems, causes, procedures, guides.
  - File names are kebab-case, in English, named after the symptom or cause, never after a brand.
- **Page types and templates.** There are four templates, one per page type, kept outside the wiki. Every page starts with YAML frontmatter.
  - **Problem**
    - Frontmatter: type, title, aliases (customer phrasings), mower_types, power_sources, causes, part_types, source_count, updated.
    - Sections in order: Summary; Diagnostic questions; Quick triage; Possible causes (table: Cause link | how common | telltale signs | fix difficulty); Brand notes; Tips & life hacks; Parts commonly needed; Safety; When to send to a technician; Related problems (including "Not this problem? See…" sibling links); Sources.
  - **Cause**
    - Frontmatter: type, title, problems, part_types, procedures, source_count, updated.
    - Sections: Summary; Before you start; Symptoms it produces; How to confirm; Fix; Brand notes; Parts & fitment; Tips & life hacks; Sources.
  - **Procedure**
    - Frontmatter: type, title, causes, part_types, difficulty (easy | moderate | pro), time_estimate, tools, source_count, updated.
    - Sections: Before you start; Safety; Tools & parts; Steps (numbered); Brand notes; Tips & common mistakes; Verify the fix; Sources.
  - **Guide**
    - Frontmatter: type, title, related, source_count, updated.
    - Sections: Summary; Key facts; Recommendations; Tips & life hacks; Common mistakes; Related; Sources.
- **Diagnostic questions** are written as a table: Question | answer A → Causes | answer B → Causes. Basic intake questions live once, in a customer-intake Guide.
- **Controlled vocabularies.**
  - mower_types: push, self-propelled, riding, zero-turn.
  - power_sources: gas, battery, diesel.
  - Trust tier: manufacturer, expert-blog, forum.
- **Problem granularity.** Split a symptom family when its sub-symptoms point to clearly different Causes (ADR-0001). Mower type and Power source are tags, not page splits, unless the fixes share almost nothing.
- **Links** are standard relative markdown links, never wikilinks (ADR-0002). Problem ↔ Cause and Cause ↔ Procedure links go in both directions, and the frontmatter link lists must match the body.
- **Citation.**
  - Each page has a Sources section listing raw paths. Citations are per section, not per sentence.
  - source_count equals the number of distinct Sources cited.
  - "How common" in the causes table is ranked by how many Sources name that Cause for that Problem, weighted by Trust tier.
- **Conflicts** are shown in a "⚠ Conflicting advice" callout that names each position and its Sources. They are never silently resolved.
- **OEM part numbers** appear only in Brand notes or Parts & fitment, marked as from the Source and to be verified against the catalog.
- **Index format.** Grouped by page type, one line per page: link, a one-line summary and, for Problems, the aliases. Split per type once it passes a few hundred lines.
- **Log format.**
  - Each entry has a consistent, greppable header: date | operation | label.
  - The body lists every raw path processed with its outcome: ingested → pages touched, skipped: <reason>, or non-conforming.
  - The log is the only record of which Sources have been ingested. There is no separate manifest.
- **Skip policy.** Buying guides, lawn-care advice, "where to get repairs" listings and other content with no repair or maintenance value are skipped and logged.
- **Skills.**
  - **wiki-ingest** finds uninvestigated Sources via the log, classifies each one, updates or creates pages from the templates, updates the index, appends to the log, runs the validator until it is clean, and commits.
  - **wiki-lint** runs the validator and then an LLM content review for semantic issues.
  - The project instructions point to both skills, the templates, the glossary and the ADRs.
- **Bootstrap ingest** has two phases.
  1. Taxonomy pass: classify all ~638 Sources and produce a proposal document listing the proposed Problems, Causes, Procedures and Guides, each with its mapped Sources, merges and skips. **This is a human approval gate.**
  2. Fill pass: write the pages cluster by cluster (one Problem plus its Causes and Procedures), each cluster with a clean validator run and its own commit.
- **Validator.** A deterministic Python script with only PyYAML as a dependency. It takes a wiki root and a raw root and reports violations:
  - frontmatter keys or values don't match the page type
  - required sections are missing or out of order
  - a relative link is broken
  - frontmatter link lists disagree with the body links, or a back-link is missing
  - source_count doesn't match the Sources list
  - the index has a missing or stale entry
  - a raw file is absent from the log
  - a Problem has no Causes, or a Cause has no Problems

  Exit status is non-zero when there are violations.
- **Version control.** The project becomes a git repository, with one commit per ingest or per fill-pass cluster.
- **Obsidian.** The wiki stays visible. Sources, templates, docs and scratch stay in Obsidian's ignore filters.

## Testing Decisions

- **One test point: the validator.** Tests run it against small fixture wikis, some valid and some deliberately broken, and assert exactly which violations are reported. They don't depend on how the validator works internally.
- **What makes a good test here:** each test builds or uses a minimal fixture (a handful of pages, an index, a log, a raw folder) that shows one rule. It asserts that the right violation is reported for a broken fixture and nothing for a valid one, and checks exit status. A test never inspects the validator's internal functions.
- **Coverage:** one valid baseline fixture that passes clean, plus at least one failing fixture per validator rule listed under Implementation Decisions.
- **The ingest workflow is checked by the same test point.** Every ingest must leave the wiki passing the validator before it commits.
- **Content quality is not tested automatically.** It is covered by the maintainer's review of the taxonomy proposal and spot checks after the fill pass. These cover whether the taxonomy makes sense, whether Diagnostic questions are useful, and whether Causes are ranked plausibly.
- **Prior art:** none. The repository has no code or tests yet, and this spec sets up the first test suite.

## Out of Scope

- The customer-support agent itself (runtime, prompts, chat UI, integration into support tooling).
- RAG, embeddings, vector stores or search engines (ADR-0002). Local search is a possible later addition.
- The support agent writing back into the wiki (ADR-0003).
- SKU-level part lookup or integration with the parts catalog. The wiki names Part types only.
- Scraping or collecting new Sources. Sources are collected outside this project and dropped into the raw folder.
- Equipment other than lawn mowers (snow blowers, trimmers, etc.).
- Buying guides and lawn-care advice as wiki content.
- Images from Sources, and translating the wiki into other languages.

## Further Notes

- Domain vocabulary is defined in GLOSSARY.md: Problem, Cause, Procedure, Guide, Diagnostic question, Source, Trust tier, Brand note, Mower type, Power source, Part type. Use these terms consistently in pages, skills and tickets.
- Relevant ADRs:
  - 0001: symptom-keyed Problems with shared Causes
  - 0002: agent reads Markdown directly, no RAG
  - 0003: support agent is read-only
- The current Sources are 566 from poweredoutdoors.com (trust tier: expert-blog) and 72 from searspartsdirect.com (manufacturer). Forum Sources are expected later. When they arrive, a confirmed fix outranks an untested suggestion.
- Suggested ticket order:
  1. git init and Obsidian filters
  2. templates
  3. validator and fixture tests
  4. wiki-ingest and wiki-lint skills, plus project instructions
  5. taxonomy pass, stopping for approval
  6. fill pass, by cluster
  7. first full lint
