# Per-Source notes for the fill pass (ticket 07)

Every Source to ingest is read in full once, and its content is written here as notes grouped by target wiki page. Cluster writers then build pages from the notes with `python .scratch/wiki-bootstrap/collect_notes.py <page>` instead of rereading every Source. These notes are scratch, not part of the wiki.

## File

One file per Source: `notes/<domain>/<slug>.md` (the Source's own folder and file name under `raw/Articles/`).

```markdown
---
path: raw/Articles/<domain>/<slug>.md
title: <Source title from its frontmatter>
tier: manufacturer | expert-blog | forum
conforming: yes            # or: "no: <what's wrong>" (missing frontmatter keys, wrong folder, ...)
brand: <brand the Source is about, or none>
mower_types: [push, self-propelled, riding, zero-turn]   # only the types the Source covers
power_sources: [gas]                                     # gas / battery / diesel
---

## page: problems/<slug>
...
## page: causes/<slug>
...
## unmapped
...
```

## Rules

- **Read the whole Source.** The taxonomy mapping (`taxonomy-classification.jsonl`) is only a hint. Add a `## page:` section only for pages the Source actually supports, and add sections for pages the hint missed.
- **Page slugs come from `notes-slugs.txt`** (the approved taxonomy, 196 pages). Use them exactly. Content that fits no listed page goes under `## unmapped`, with a suggested slug and a one-line reason.
- **Only what the Source says.** Paraphrase closely and keep every specific: numbers with units (gaps, torques, psi, volumes, intervals, ages), part types, tool names, ordered steps, warnings and conditions ("only on Kohler engines"). Add nothing from your own knowledge. Mark opinion or hedged claims as such.
- **OEM part numbers** are copied exactly, under a `- brand/part:` bullet.
- Lines start with a tag so writers can sort them:
  - `- alias: "<customer phrasing of the symptom>"` (Problem sections only)
  - `- causes-named: <cause-slug>, <cause-slug>, ...`: in a Problem section, every Cause the Source names for that symptom, in the Source's order
  - `- symptom:` telltale signs (Cause sections: name the Problem slug)
  - `- confirm:` how to test or check it
  - `- fix:` fix summary; `- step N:` ordered Procedure steps
  - `- tools:` / `- parts:` / `- difficulty:` / `- time:`
  - `- safety:` warnings
  - `- brand:` brand, model-line or engine specifics; `- brand/part:` OEM part numbers
  - `- tip:` tips and life hacks; `- mistake:` common mistakes
  - `- pro:` when to send it to a technician
  - `- fact:` anything else worth citing (Guides especially)
- **Skip content**: buying advice, lawn-care advice and repair-shop listings get no notes. If the entire Source is skip content, write the frontmatter plus `skip: <reason>` and no sections.
