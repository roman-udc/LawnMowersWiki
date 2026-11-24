# 36: Fix malformed and missing conflict callouts

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** resolved

**What to build:** Every conflict is flagged with a well-formed `> **⚠ Conflicting advice:**` callout, with linked Sources and Trust tiers, on every page that repeats the advice.

- [x] Normalise malformed callouts: causes/clogged-air-filter.md (L107, L109), causes/dirty-carburetor.md (L92), causes/bent-spindle-or-bad-spindle-bearing.md (L80), causes/bent-crankshaft.md (L52), procedures/replace-the-spindle-assembly.md (L91), guides/choosing-the-right-gas.md (L38).
- [x] Add callout: procedures/start-a-mower-with-old-gas.md (starter fluid vs carb cleaner).
- [x] Add callouts or a single price page: belt prices on causes/worn-or-stretched-belt.md, guides/belt-types.md, guides/mower-parts-that-wear-out.md.
- [x] Add callout: guides/routine-service-and-maintenance.md service/oil intervals (matches tune-up and change-the-engine-oil).
- [x] Add callout or link: guides/winterizing-and-storage.md stabilizer in tank vs gas can.
- [x] Check ethanol "minimum 10%" vs "≤10%" on causes/wrong-fuel.md and causes/empty-fuel-tank.md.
- [x] Check foam-filter oiling and plug clean-vs-replace callouts are repeated on procedures/clean-or-replace-the-air-filter.md and procedures/replace-the-spark-plug.md.
- [~] Optional: pointer from guides/battery-care-and-charging.md to the charge-rate callout.

## Comments

2026-11-24: Done; see the log entry "ticket 36: conflict callouts". Ethanol and air-filter items needed no change. The optional charge-rate pointer was skipped.
