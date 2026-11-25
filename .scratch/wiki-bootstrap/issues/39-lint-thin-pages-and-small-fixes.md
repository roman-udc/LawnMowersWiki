# 39: Widen thin pages; small accuracy fixes

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** resolved

**What to build:** Thin pages gain Sources or say their support is weak; small accuracy defects are fixed.

- [x] Thin (one Source): problems/mower-creeps-in-neutral; causes/air-in-fuel-system, bad-engine-cooling-fan, bad-front-axle, bad-glow-plugs, bad-governor, dirty-fuel-tank, loose-or-seized-wheel-bearing, overfilled-fuel-tank; procedures/adjust-the-neutral-control, clean-the-gas-tank, replace-the-starter-motor, reset-the-ignition-code, test-the-pto-clutch.
- [x] Consider merges: bad-engine-cooling-fan with cooling-shroud/fins; loose-or-seized-wheel-bearing with bad-tire.
- [x] causes/clogged-muffler-or-spark-arrestor.md: content is damaged/loose muffler; rename or source "clogged".
- [x] problems/engine-only-runs-with-choke-on.md: ranking says 6 Sources, page has 7; recount.
- [x] causes/dirty-fuel-tank.md: "Source:" labels should read "Sources:".
- [x] guides/how-clutches-work.md: S2–S4 listed but not cited.

**Resolution (2026-11-25):** No other Source in raw/ covers these pages, so each thin page now says only one Source covers it. Merges were declined because the pages name different parts and fixes. The muffler Cause is renamed to causes/damaged-or-loose-muffler.md. The choke ranking now names the 6 Sources it counts. The dirty-fuel-tank labels are fixed. The clutches Guide was already fixed in ticket 38.
