# 38: Tighten Problem boundaries and cross-links

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** needs-triage

**What to build:** Problems stay keyed on one symptom (ADR-0001) and route readers to their neighbours.

- [ ] problems/engine-hard-to-start-when-cold.md: keep cold-specific causes; route general no-start causes to engine-wont-crank and engine-cranks-but-wont-start.
- [ ] problems/engine-cranks-but-wont-start.md: drop or down-rank causes that stop cranking; link engine-wont-crank.
- [ ] problems/engine-dies-when-hot.md: add Related links and a triage question vs engine-starts-then-dies and engine-overheats.
- [ ] problems/mower-is-leaking-oil.md and mower-is-smoking.md: cross-link.
- [ ] causes/worn-or-stretched-belt.md: link worn-drive-belt for the drive-belt sentence or drop it.
- [ ] Procedure/Guide duplication: guides/how-clutches-work.md vs procedures/test-the-pto-clutch.md; guides/reading-wiring-schematics.md vs procedures/read-a-wiring-schematic.md.
