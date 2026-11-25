# 40: Check for superseded claims by published date

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** resolved

**What to build:** Claims on high-Source-count pages are checked against Source `published` dates; the first lint did not compare dates.

- [x] For pages with conflict callouts and the top Problems, compare `published` and Trust tier of the Sources on each side; report or flag superseded claims.

**Resolution (2026-11-25):** Report at `reports/lint/2026-11-25.md`. 6 suspicions; items 1–2 (blade interval, paper filter) have a newer same-tier Source and are the ones to act on. No wiki page was edited; applying the fixes is a separate decision.
