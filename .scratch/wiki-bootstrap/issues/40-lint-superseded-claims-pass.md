# 40: Check for superseded claims by published date

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** needs-triage

**What to build:** Claims on high-Source-count pages are checked against Source `published` dates; the first lint did not compare dates.

- [ ] For pages with conflict callouts and the top Problems, compare `published` and Trust tier of the Sources on each side; report or flag superseded claims.
