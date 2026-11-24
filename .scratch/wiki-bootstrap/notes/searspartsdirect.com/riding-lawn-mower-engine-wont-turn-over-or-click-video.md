---
path: raw/Articles/searspartsdirect.com/riding-lawn-mower-engine-wont-turn-over-or-click-video.md
title: Riding lawn mower engine won't turn over or click video
tier: manufacturer
conforming: yes
brand: Craftsman
mower_types: [riding]
power_sources: [gas]
---

## page: problems/engine-wont-crank
- alias: "riding mower does nothing when I turn the key, not even a click"
- causes-named: incorrect-starting-procedure, weak-or-dead-battery, loose-or-corroded-battery-cables, bad-starter-solenoid, bad-wiring-or-ground, blown-fuse, bad-ignition-switch, bad-safety-switch
- fact: Click on turning the key means the starter solenoid coil is getting power from the battery through the ignition switch. No click: solenoid failed or coil isn't getting power.
- tip: First make sure the parking brake is set and blades are disengaged; mower won't start otherwise.
- fact: Demo mower is a Craftsman; wiring and components differ on other models; see model wiring diagram.
- tools: work gloves, safety goggles, multimeter, wire brush, clip-on meter probes, wrench set

## page: causes/incorrect-starting-procedure
- fact: Parking brake not set or blades engaged prevents starting.

## page: guides/reading-wiring-schematics
- fact: Starting system: positive red battery cable to one of two large terminal posts on the starter solenoid. Black wire on the other large post carries power to starter motor. A small red wire branches off the red post through the ignition switch to the coil at the bottom of the solenoid. Key to start: ignition switch sends power via white wire to energize the coil, which closes an internal contact sending power from red battery cable to black wire to starter motor.

## page: causes/weak-or-dead-battery
- confirm: Ignition off; lift seat to reach battery (this model); multimeter on DC volts, red probe to positive, black to negative. Good: more than 12 V DC. Under 12 V: weak or dead; won't power solenoid coil.
- fix: Recharge with charger, or jump-start (12 V battery models, in a pinch); replace if it won't recharge.

## page: procedures/test-the-battery
- step 1: Work gloves and goggles; ignition off. step 2: access battery. step 3: DC volts across terminals; over 12 V good.

## page: causes/loose-or-corroded-battery-cables
- confirm: Check voltage at the red solenoid post (red probe on red post, black on battery negative): should be over 12 V.
- fix: If under 12 V, clean corrosion off battery terminals and cable leads with wire brush; recheck; if still under 12 V replace the red battery cable.
- safety: Don't let the meter lead touch both solenoid posts at once (severe spark; shorting across posts sends current to starter). Source strongly discourages deliberately shorting across posts with an insulated screwdriver to start the engine: dangerous and overrides safety switches.

## page: procedures/test-the-starter-solenoid
- step 1: Pull the white and black wires off the solenoid spades.
- step 2: Multimeter on DC volts; clip red probe to white wire female spade, black probe to black wire female spade (clip-on probes, or a helper to turn the key).
- step 3: Key to start, note reading, key off.
- fact: Battery voltage (>12 V): coil gets power but isn't closing internal contact: replace starter solenoid. 0 V: break in circuit to coil; solenoid likely OK; test coil circuit.

## page: causes/bad-starter-solenoid
- confirm: Voltage present at coil wires with key at start but no click = solenoid bad.

## page: causes/bad-wiring-or-ground
- confirm (ground side): Black wire on the coil grounds to the metal frame. Disconnect negative then positive battery cable to kill power and tuck cables away; multimeter on resistance between black wire female spade and bare metal on frame (author used deck height lever). Near 0 ohms = grounded. Infinite = find and repair break in black ground wiring.
- confirm (white wire): If all components OK, there is a break in the white wire between ignition switch and solenoid coil; find and repair.
- confirm (red wire): Resistance from solenoid post with red wire to the female plug spade with red wire on the ignition switch harness: near 0 ohms; infinite = repair break in red wire.

## page: causes/blown-fuse
- confirm: Hot side circuit: fuse, ignition switch, brake switch, blade switch. Fuse on this mower is next to the starter solenoid; must pull out battery and battery box; move zip tie, pull fuse. Broken element = blown. Or continuity: probe each lead; near 0 ohms good, infinite = blown.
- fix: Replace. Fuse blew because of a short in a component or wiring; find and fix cause (source links a blown-fuse video). If OK reinstall and secure with zip tie.

## page: procedures/test-and-replace-a-fuse
- step 1: Remove battery and battery box (this model) to reach fuse beside solenoid. step 2: move zip tie, pull fuse. step 3: inspect element or measure resistance across leads; infinite = replace. step 4: find the cause of the short.

## page: causes/bad-ignition-switch
- confirm: Open hood; pull wire harness off switch; release locking tabs and push switch out of dash; push harness plug through hole for access. Key to start should connect red wire on B terminal to white wire on S terminal. Resistance between B and S prongs with key at start: near 0 ohms good; infinite = replace.

## page: causes/bad-safety-switch
- confirm (brake interlock switch): remove air duct mounting screws and duct; carefully move fuel tank aside (drain some fuel if too heavy); remove lower right dash fastener and lower dash; note prongs with white wires; pull harness; ohms across the two prongs: near 0 good; infinite = replace.
- confirm (blade switch): remove clutch lever assembly mounting screws and pull assembly down slightly; note and disconnect harness; ohms across the white wire prongs: near 0 good; infinite = replace.

## page: procedures/replace-the-ignition-switch
- fact: Source links a video for replacement; test steps above show removal from dash.

## page: procedures/replace-the-starter-solenoid
- fact: Source links a video; no steps in text.

## page: procedures/replace-the-seat-switch
- fact: Not covered; see brake interlock and blade switch tests only.

## page: procedures/jump-start-the-battery
- fact: Source mentions jumper cables can jump-start a riding mower with a 12 V battery in a pinch (links separate video).

## page: procedures/charge-the-battery
- fact: Source mentions recharging with a charger (links separate video).

## unmapped
- none
