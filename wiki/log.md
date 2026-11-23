# Log

Append-only record of every operation on the wiki, and the only record of which Sources have been ingested. Each entry header is `## YYYY-MM-DD | operation | label` (grep with `^## `). The body lists each raw path with its outcome: `ingested → pages touched`, `skipped: <reason>` or `non-conforming`.

## 2026-11-23 | ingest | tracer bullet: engine cranks but won't start

- raw/Articles/poweredoutdoors.com/lawn-mower-turns-over-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/poweredoutdoors.com/riding-mower-turns-over-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/poweredoutdoors.com/husqvarna-mower-turns-over-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/poweredoutdoors.com/john-deere-mower-turns-over-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/poweredoutdoors.com/cub-cadet-zero-turn-cranks-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/poweredoutdoors.com/scag-zero-turn-mower-turns-over-but-wont-start.md → ingested → problems/engine-cranks-but-wont-start.md
- raw/Articles/searspartsdirect.com/riding-lawn-mower-engine-spins-but-wont-start-video.md → ingested → problems/engine-cranks-but-wont-start.md
