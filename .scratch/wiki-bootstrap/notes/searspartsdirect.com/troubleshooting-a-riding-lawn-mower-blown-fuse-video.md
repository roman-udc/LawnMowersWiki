---
path: raw/Articles/searspartsdirect.com/troubleshooting-a-riding-lawn-mower-blown-fuse-video.md
title: Troubleshooting a riding lawn mower blown fuse video
tier: manufacturer
conforming: yes
brand: Craftsman (example model in video; method general)
mower_types: [riding]
power_sources: [gas]
---

## page: causes/blown-fuse
- fact: Most often caused by a short circuit: a damaged wire or failed component lets current flow to the metal frame through an unintended path; the fuse blows to stop it, preventing wiring damage and fires. Replacing the fuse is easy; unless the short is found and repaired, it keeps blowing.
- fact: An intermittent short is hard to find.
- parts: fuse, ignition switch, dash wire harness, engine wire harness, chassis wire harness

## page: procedures/test-and-replace-a-fuse
- tools: multimeter (DC voltage and resistance), several spare fuses, work gloves, wiring diagram and parts diagram (owner's manual often has both; some SearsPartsDirect parts diagrams include wiring diagrams via model number search)
- step 1: Remove the blown fuse from the holder. Method: measure voltage across the fuse holder with a multimeter, isolating circuit branches with the ignition switch and by disconnecting wires; voltage through the holder or a fuse that blows after isolating a branch means a short in that branch.
- step 2 (key off): Set multimeter to DC voltage; probes in opposite sides of the fuse holder. No voltage: go to the run circuit test. Voltage: short is in the red wire between fuse holder and ignition switch, or in the switch. Unplug the switch and recheck: no voltage = switch is the short (replace it); still voltage = short in the red wire between holder and switch plug; repair it.
- step 3 (run circuit): With probes out, install a new fuse, turn key to run, then off, pull the fuse and see if it blew. In run, an internal switch contact sends current from terminal B to A1 to energize the blue wire. Fuse blows = short in ignition switch, blue wire, or a harness connected to the blue wire. Fuse doesn't blow = intermittent short; wiggle each wire harness back and forth and retest; a harness that blows the fuse when wiggled contains the shorted wire; repair. If not found, replace fuse; if it blows again repeat the whole process.
- step 4 (check ignition switch): Unplug the harness from the back of the switch; release locking tabs and pull the switch out of the dash. Contact spades are labeled. Key in run: multimeter (resistance) should read near 0 ohms between B and A1 and infinite resistance between B and all other spades. If resistance is measured between B and any spade except A1, replace the switch (internal contacts failed). If OK, reinstall and reconnect.
- step 5 (harnesses; example tractor has dash, chassis and engine harnesses): Dash: unplug the engine and chassis harnesses from the dash harness; install new fuse; briefly key to run; off; check fuse; blown = short in the blue wire of the dash harness; repair or replace. Engine: reconnect the engine harness and repeat; blown = short in engine harness. Chassis: if no blow with engine harness connected, the short is in the chassis harness.
- tip: Look up the engine harness part number by the engine model number, not the tractor model number (engine parts are listed separately).
- tip: Use your own mower's wiring diagram if wiring differs from the example.

## page: causes/bad-ignition-switch
- fact: Defective internal ignition switch contacts can cause a short in the run position; test resistance between spades B and A1 and others (see above); replace if B shows resistance to any spade except A1.

## page: causes/bad-wiring-or-ground
- fact: Broken wire or damaged harness (dash, chassis, engine) shorts to the frame and blows the fuse; find and repair the wire or replace the harness.

## page: procedures/read-a-wiring-schematic
- fact: Use a wiring diagram and parts diagram to track circuits and find harness connections; blue wire = run circuit energized from ignition switch A1; red wire = fuse holder to ignition switch (in the example Craftsman).

## page: procedures/replace-the-ignition-switch
- fact: Unplug wire harness from the back, release locking tabs, pull the switch out of the dash. (Full steps are in a separate linked video.)

## page: problems/engine-wont-crank
- fact: A blown fuse can prevent starting/running; electrical short diagnosis as above.
