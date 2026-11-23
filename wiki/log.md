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

## 2026-11-23 | ingest | causes and procedure for engine cranks but won't start

- raw/Articles/poweredoutdoors.com/clean-a-push-mower-carburetor.md → ingested → causes/dirty-carburetor.md
- raw/Articles/poweredoutdoors.com/cub-cadet-zero-turn-cranks-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/guide-to-lawn-mower-air-filters-differences-how-to-clean-them.md → ingested → causes/clogged-air-filter.md
- raw/Articles/poweredoutdoors.com/husqvarna-mower-turns-over-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/john-deere-mower-turns-over-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/lawn-mower-isnt-getting-gas.md → ingested → causes/bad-fuel-pump.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md
- raw/Articles/poweredoutdoors.com/lawn-mower-turns-over-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md, procedures/replace-the-spark-plug.md
- raw/Articles/poweredoutdoors.com/lawn-mower-wont-start-when-cold.md → ingested → causes/clogged-air-filter.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/riding-mower-only-runs-choke-on.md → ingested → causes/dirty-carburetor.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/riding-mower-turns-over-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/bad-ignition-coil.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/low-compression.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md, procedures/replace-the-spark-plug.md
- raw/Articles/poweredoutdoors.com/scag-zero-turn-mower-turns-over-but-wont-start.md → ingested → causes/bad-fuel-pump.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/fouled-spark-plug.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md, causes/wrong-choke-setting.md
- raw/Articles/poweredoutdoors.com/start-a-lawn-mower-with-old-gas.md → ingested → causes/bad-fuel-pump.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/old-fuel.md, causes/plugged-fuel-cap-vent.md
- raw/Articles/searspartsdirect.com/how-to-clean-the-air-filter-in-your-lawn-tractor.md → ingested → causes/clogged-air-filter.md
- raw/Articles/searspartsdirect.com/how-to-keep-lawn-mower-gas-from-going-bad.md → ingested → causes/old-fuel.md
- raw/Articles/searspartsdirect.com/how-to-rebuild-a-riding-lawn-mower-carburetor.md → ingested → causes/dirty-carburetor.md, causes/disconnected-fuel-solenoid.md
- raw/Articles/searspartsdirect.com/how-to-replace-a-riding-lawn-mower-carburetor.md → ingested → causes/disconnected-fuel-solenoid.md
- raw/Articles/searspartsdirect.com/how-to-replace-a-riding-lawn-mower-fuel-filter.md → ingested → causes/clogged-fuel-filter.md
- raw/Articles/searspartsdirect.com/how-to-replace-a-riding-lawn-mower-ignition-coil.md → ingested → causes/bad-ignition-coil.md
- raw/Articles/searspartsdirect.com/how-to-replace-a-riding-lawn-mower-spark-plug.md → ingested → causes/fouled-spark-plug.md, procedures/replace-the-spark-plug.md
- raw/Articles/searspartsdirect.com/how-to-replace-the-flywheel-key-on-a-riding-lawn-mower.md → ingested → causes/sheared-flywheel-key.md
- raw/Articles/searspartsdirect.com/how-to-tune-up-a-riding-lawn-mower-video.md → ingested → causes/fouled-spark-plug.md, procedures/replace-the-spark-plug.md
- raw/Articles/searspartsdirect.com/riding-lawn-mower-engine-spins-but-wont-start-video.md → ingested → causes/bad-fuel-pump.md, causes/bad-ignition-coil.md, causes/clogged-air-filter.md, causes/clogged-fuel-filter.md, causes/clogged-fuel-line.md, causes/dirty-carburetor.md, causes/disconnected-fuel-solenoid.md, causes/fouled-spark-plug.md, causes/low-compression.md, causes/old-fuel.md, causes/sheared-flywheel-key.md, procedures/replace-the-spark-plug.md
- raw/Articles/searspartsdirect.com/runs-rough-or-misfires.ridtr03.md → ingested → causes/low-compression.md, causes/sheared-flywheel-key.md

Note: in problems/engine-cranks-but-wont-start.md, the sibling Problem links turned into plain text until those pages exist

## 2026-11-23 | ingest | customer-intake Guide

- raw/Articles/searspartsdirect.com/how-to-find-the-age-of-your-craftsman-riding-lawn-mower-or-lawn-tractor.md → ingested → guides/customer-intake.md
- raw/Articles/searspartsdirect.com/how-to-measure-a-mower-blade.md → ingested → guides/customer-intake.md
- raw/Articles/searspartsdirect.com/what-are-the-riding-mower-parts-that-require-replacement-most-often.md → ingested → guides/customer-intake.md
- raw/Articles/poweredoutdoors.com/push-mower-is-leaking-gas.md → ingested → guides/customer-intake.md
- raw/Articles/poweredoutdoors.com/replace-exmark-mower-deck-parts.md → ingested → guides/customer-intake.md

Note: problems/engine-cranks-but-wont-start.md's Diagnostic questions now link to the customer-intake Guide. Each of these Sources was used only for intake content; their repair content is not yet ingested.
