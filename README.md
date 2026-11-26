# Lawn Mower Wiki

## In plain words

This is a library of lawn-mower repair knowledge, written so that an AI support agent can answer customer questions from it.

- A customer describes what is wrong in their own words ("my mower clicks but won't start").
- The wiki turns that into a **Problem** page, which lists the possible **Causes**, the questions to ask the customer, and the **Procedures** that fix each Cause.
- Every fact in the wiki points back to the article or manual it came from, so it can be checked.

Nobody writes the wiki pages from scratch. You collect good articles and save them into the `raw/` folder. Claude Code then reads them and writes or updates the wiki pages for you (**ingest**). Every so often you ask Claude Code for a health check of the wiki (**lint**). Your job as the specialist is to feed it good material, read the pages with an expert eye, and correct anything that is wrong.

The finished wiki (the `wiki/` folder) is loaded into a separate support-agent project. That agent reads it as context when it answers support staff and customers, and it never changes the wiki itself. Better pages here mean better answers there.

---

## Tutorial

1. [Set up your computer](#1-set-up-your-computer)
2. [How the wiki is organised](#2-how-the-wiki-is-organised)
3. [Walkthrough: diagnosing a customer's problem](#3-walkthrough-diagnosing-a-customers-problem)
4. [Walkthrough: adding new Sources (ingest)](#4-walkthrough-adding-new-sources-ingest)
5. [Walkthrough: checking wiki health (lint)](#5-walkthrough-checking-wiki-health-lint)
6. [Correcting mistakes](#6-correcting-mistakes)
7. [Everyday routine](#7-everyday-routine)
8. [How the support agent uses the wiki](#8-how-the-support-agent-uses-the-wiki)

### 1. Set up your computer

These steps are for Windows and assume you already have access to the GitHub repository.

1. **Install the tools**
   - [Git for Windows](https://git-scm.com/download/win)
   - [Python 3](https://www.python.org/downloads/). Tick "Add Python to PATH" during install.
   - [Obsidian](https://obsidian.md/download)
   - [Claude Code](https://docs.claude.com/en/docs/claude-code/setup). Sign in with your Claude account when it first starts.
2. **Download the wiki.** Open a terminal (PowerShell) in the folder where you want it and run:
   ```powershell
   git clone https://github.com/roman-udc/LawnMowersWiki.git
   cd LawnMowersWiki
   pip install -r requirements.txt
   ```
   The last line installs PyYAML, which the wiki checker needs.
3. **Open it in Obsidian.** In Obsidian choose *Open folder as vault* and pick the `LawnMowersWiki` folder. You can now browse the pages, click links between them, and use the graph view.
4. **Start Claude Code in the same folder.** In the terminal, inside `LawnMowersWiki`, run:
   ```powershell
   claude
   ```
   Then set the model and effort level for the session:
   ```
   /model opus
   /effort low
   ```
   Claude Code picks up the project's instructions and its two skills, `/wiki-ingest` and `/wiki-lint`, on its own.

Keep Obsidian open for reading and editing and Claude Code open for the heavy lifting. Both work on the same files.

### 2. How the wiki is organised

```
LawnMowersWiki/
├── raw/            Sources: saved articles and manuals. Never edited.
│   ├── Articles/<site>/<article>.md
│   └── Expert/in-house/<topic>.md   your own expert notes
├── wiki/           The wiki itself, written by Claude Code.
│   ├── index.md    The table of contents: every page, one line each.
│   ├── log.md      Diary of every change (ingest, lint, fix).
│   ├── problems/   Symptoms as a customer says them.
│   ├── causes/     The faults behind the symptoms.
│   ├── procedures/ Step-by-step repairs.
│   └── guides/     General owner know-how.
├── templates/      The blank layout for each page type.
├── reports/lint/   Health-check reports from /wiki-lint.
├── GLOSSARY.md     Exact meaning of every term used here.
├── tools/validate_wiki.py   The automatic checker.
└── .claude/skills/ The ingest and lint skills.
```

#### Page types

| Type | What it is | Example |
|---|---|---|
| **Problem** | A symptom in the customer's words. This is where diagnosis starts. It covers all brands, with brand-specific detail in *Brand notes*. | "Engine won't crank or turn over" |
| **Cause** | A specific fault that produces one or more Problems. | "Bad starter solenoid" |
| **Procedure** | Step-by-step instructions for one repair or maintenance task. | "Replace the spark plug" |
| **Guide** | General know-how not tied to one Cause. | "Fuel storage and ethanol" |

They link together like this:

```
Problem ──(possible causes)──▶ Cause ──(how to fix)──▶ Procedure
                                         Guide (background know-how)
```

Every page follows its template in `templates/`, keeping the same sections in the same order. A Problem page, for example, has: Summary, Diagnostic questions, Quick triage, Possible causes, Brand notes, Tips & life hacks, Parts commonly needed, Safety, When to send to a technician, Related problems, Sources.

#### index.md and log.md

- **`wiki/index.md`** is the routing table. Each Problem line lists its *aliases*, which are the many ways customers phrase the same symptom ("turns over but won't start", "cranks but won't fire"). The support agent finds the right Problem by matching what a customer says against these aliases.
- **`wiki/log.md`** is append-only. Each entry starts with `## YYYY-MM-DD | operation | label`, where the operation is `ingest`, `lint` or `fix`, and lists which Sources went into which pages.

#### Sources and trust tiers

A **Source** is one file in `raw/`. Every section of every page cites the Sources it relies on, and you can follow those links to check a claim. Sources are never edited once saved.

Not all Sources are equally reliable, so each one gets a **trust tier**:

1. **manufacturer**: OEM manuals and parts-supplier repair guides (for example searspartsdirect.com)
2. **expert**: your own notes in `raw/Expert/`
3. **expert-blog**: repair blogs (for example poweredoutdoors.com)
4. **forum**: forum posts. A confirmed fix ("that fixed it") counts for more than an untested suggestion.

When Sources disagree, the higher tier wins, and the page flags the conflict instead of silently picking one. For exact definitions of all the terms, see [GLOSSARY.md](GLOSSARY.md).

### 3. Walkthrough: diagnosing a customer's problem

This is how the support agent uses the wiki, and it's also the best way to review pages yourself. Say a customer writes: *"My riding mower just clicks when I turn the key."*

1. **Open `wiki/index.md`** and look in the Problems list for an alias that matches. "Clicks but won't start" and "just clicks or hums when I turn the key" both sit under **Engine won't crank or turn over**.
2. **Open that Problem page** (`wiki/problems/engine-wont-crank.md`):
   - The **Summary** says what the symptom means.
   - **Diagnostic questions** are what you'd ask the customer ("Is there a click, a hum or nothing at all?"). Each answer makes some Causes more likely and others less.
   - **Quick triage** gives the fast checks, cheapest and most likely first.
   - **Possible causes** links to each Cause page.
3. **Open the likely Cause**, for example a weak battery or a bad starter solenoid. Read *How to confirm* to check that this really is the fault, then *Fix*, which links to the Procedure.
4. **Open the Procedure** for the tools, safety notes, steps and how to check the repair worked.
5. **Check the Sources** at the bottom of any page if a claim looks wrong to you. If it is wrong, see [Correcting mistakes](#6-correcting-mistakes).

### 4. Walkthrough: adding new Sources (ingest)

**What ingest does.** The `/wiki-ingest` skill finds every file in `raw/` that is not yet in `log.md` and reads each one. It decides which page types the content belongs to and either updates existing pages or creates new ones from the templates. Along the way it cites the Source, flags conflicts with other Sources, updates `index.md` and `log.md`, runs the checker until it is clean, and makes one commit. Buying guides, lawn-care tips and repair-shop listings are skipped and logged as skipped.

**Steps**

1. **Save the Source into `raw/`.**
   - *With the Obsidian Web Clipper* (browser extension): clip the article into `raw/Articles/<site>/`, for example `raw/Articles/poweredoutdoors.com/`.
   - *By hand*: create a `.md` file in the same kind of folder and paste the text in.

   Start each file with this header if you can (ingest still accepts files without it, but logs them as non-conforming):
   ```yaml
   ---
   source_url: https://example.com/article
   title: Article title
   domain: example.com
   type: article          # article, manual, forum, expert-note …
   published: '2024-05-01'
   ---
   ```
2. **Commit the new Sources** so they are saved in Git. Ask Claude Code: *"commit the new files in raw/"*.
3. **Run the skill** in Claude Code:
   ```
   /wiki-ingest
   ```
4. **Read Claude's report.** It lists the Sources ingested or skipped (with reasons) and the pages created or updated, and it flags any conflicts. Open a few of the changed pages in Obsidian and check them with your expert eye.
5. **Push**: ask Claude *"push"* or run `git push`.

### 5. Walkthrough: checking wiki health (lint)

**What lint does.** The `/wiki-lint` skill is a health check. First it runs the automatic checker (`tools/validate_wiki.py`), which catches broken links, missing or out-of-order sections, wrong page headers, one-way links between Problems, Causes and Procedures, pages missing from the index, and Sources missing from the log. Then Claude reads the content and looks for:

- missing pages (a Cause that many pages mention but no page covers)
- conflicts between Sources that nobody flagged
- claims that newer Sources have overtaken
- Problems that overlap and could be merged
- thin pages built on too little material

It writes a report to `reports/lint/<date>.md` with two parts. **Structural violations (must fix)** are real errors. **Content suspicions (needs review)** need a human judgement, which is where your expertise comes in. Lint changes no wiki pages by itself.

**Steps**

1. Run `/wiki-lint` in Claude Code.
2. Open the new report in `reports/lint/`. Go through the suspicions and decide which ones are real.
3. Tell Claude which items to fix, for example *"apply lint 2026-11-25-2 items 1-4"*. Claude edits the pages, re-runs the checker, logs a `fix` entry and commits.
4. Push.

A good rhythm is a lint after every few ingests, and always before a new copy of the wiki goes to the support agent.

### 6. Correcting mistakes

Every claim in the wiki must cite a Source, including corrections that come from your own knowledge. So there are two kinds of fix:

**A. Factual corrections** (a wrong torque value, a wrong cause, a missing step). Write your knowledge down as a Source, then ingest it.

1. Create a note in `raw/Expert/in-house/`, for example `raw/Expert/in-house/kawasaki-fr-solenoid-location.md`:
   ```yaml
   ---
   source_url: ''
   title: Solenoid location on Kawasaki FR engines
   domain: in-house
   type: expert-note
   published: '2026-11-26'
   ---

   # Solenoid location on Kawasaki FR engines

   The page "Bad starter solenoid" says … This is wrong: on FR-series engines
   the solenoid is … (state the correct fact, which models it applies to,
   and why you know).
   ```
2. Commit it, then run `/wiki-ingest`. Claude treats your note as an **expert**-tier Source: it corrects the affected pages, cites your note, and flags any conflict with weaker Sources.

**B. Typos and wording** (no facts change). Fix the text directly in Obsidian, then ask Claude Code: *"validate the wiki, log a fix entry for my edit and commit"*.

Never edit files in `raw/`. If a Source is wrong, write an expert note that corrects it.

### 7. Everyday routine

1. `git pull`, to get the latest version.
2. Start `claude` in the folder, then run `/model opus` and `/effort low`.
3. Do the work: add Sources and `/wiki-ingest`, review pages, make corrections, `/wiki-lint`.
4. Make sure everything is committed, then `git push`.

All work goes straight onto the `main` branch. If anything looks broken, ask Claude Code to *"run the validator"* (`python tools/validate_wiki.py wiki raw`). It should print nothing.

### 8. How the support agent uses the wiki

The support-agent project loads the `wiki/` folder, and only that folder, as its context. The agent starts at `index.md`, matches the customer's words against the Problem aliases, and follows the plain relative links to Problem, Cause, Procedure and Guide pages. It does not search through `raw/` and never changes the wiki. That is why clear aliases, accurate pages and working links matter more than anything else here.
