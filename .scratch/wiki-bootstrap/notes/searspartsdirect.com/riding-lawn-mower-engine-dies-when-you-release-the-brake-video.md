---
path: raw/Articles/searspartsdirect.com/riding-lawn-mower-engine-dies-when-you-release-the-brake-video.md
title: Riding lawn mower engine dies when you release the brake video
tier: manufacturer
conforming: yes
brand: none
mower_types: [riding]
power_sources: [gas]
---

## page: problems/engine-starts-then-dies
- alias: "riding mower dies when I release the brake"
- causes-named: bad-safety-switch, bad-wiring-or-ground
- symptom: Engine shuts off when brake is released, even with the operator seated.
- fact: Most riding mowers have a seat switch that kills the engine if the brake is released and nobody is in the seat (essential safety device). A broken or unplugged switch kills the engine even when seated.

## page: causes/bad-safety-switch
- symptom: Seat switch broken or its wire harness unplugged; if unplugged, engine always shuts off on brake release (so it can't be bypassed).
- confirm: Lift seat and check the seat switch harness is securely plugged in. If unsure, remove the seat: pull retaining bolt, press seat adjustment lever and slide seat fully forward, use slot screwdriver to release the locking tab and pull seat off the bracket (hold the adjustment lever against the seat bottom so it doesn't fall). Reconnect a loose harness.
- confirm: If plugged in: unplug harness, remove switch from seat by rotating a quarter turn and pulling out; replace if visibly damaged.
- confirm: Multimeter on resistance: touch each inside spade with a probe: near 0 ohms with plunger released; press plunger in: infinite resistance. Repeat on the outside spades: near 0 ohms released, infinite pressed. Fail any = replace the seat switch.
- tools: wrench set, slot screwdriver, multimeter

## page: causes/bad-wiring-or-ground
- symptom: If the switch passes all resistance checks, a short in the wire harness could shut off the engine on brake release; check the harness and repair damaged wires.

## page: procedures/test-the-seat-switch
- fact: (not an approved slug; see unmapped) the resistance test above.

## page: procedures/replace-the-seat-switch
- fact: Source says replace the seat switch if resistance tests fail and links to a separate replace guide; removal of switch from seat: rotate quarter turn and pull out (see above).

## unmapped
- procedures/test-the-seat-switch: suggested slug; the multimeter test (inside/outside spades, near 0 ohms released, infinite pressed) has no matching approved page except replace-the-seat-switch.
