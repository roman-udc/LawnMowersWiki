# 37: Write missing Procedures

Found by [08: First full lint](08-first-full-lint.md); details in `reports/lint/2026-11-24.md`.

**Status:** needs-info

**What to build:** Repairs that Sources give real steps for have Procedure pages, and Cause pages link them instead of repeating steps inline.

- [~] Procedures named by "no Procedure page" notes where a Source has steps: replace the fuel pump, replace the primer bulb, replace the PTO clutch (problems/mower-is-vibrating.md), adjust/replace the choke cable, replace the drive belt (causes/worn-drive-belt.md).
- [x] Inline-step candidates: drain and refill the fuel tank (old-fuel, water-in-fuel, wrong-fuel; or link clean-the-gas-tank), clean the battery terminals (loose-or-corroded-battery-cables), clean under the deck (debris-on-deck-or-pulleys, oil-or-rust-on-belt).
- [x] Trim the duplicated inline steps on causes/sheared-flywheel-key.md to the Procedure link.
- [x] Standardise the "No Procedure page covers this yet" wording (bad-engine-cooling-fan, bad-governor, cracked-fuel-tank, cracked-primer-bulb).
- [x] Resolve the unlinked cooling-air rows on problems/engine-loses-power.md and problems/engine-overheats.md (link dirty-cooling-fins/bad-cooling-shroud, or add a Cause).
- [x] Link the plain-text Choosing the right gas mention on causes/wrong-fuel.md.

## Comments

2026-11-24: Done: drive belt, battery terminals, drain-and-refill fuel (clean-the-gas-tank is a deep clean, so it's a separate page), clean under the deck; flywheel-key trim; wording; cooling rows linked to bad-cooling-shroud (counts kept separate; the engine-overheats Source for that row isn't identified); Choosing the right gas link. Blocked (needs-info): fuel pump, primer bulb, PTO clutch and choke cable have no Source with real steps. The only lead is the Sears "How to replace the electric clutch on a zero-turn riding mower" guide, which is linked from a Source but isn't in raw/. Add Sources via /wiki-ingest to unblock.
