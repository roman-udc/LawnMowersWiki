# 35: Fill cluster: Guides cluster

Child of [07: Fill pass](07-fill-pass.md). Cluster 27 of 27 in `.scratch/wiki-bootstrap/taxonomy-proposal.md` ("Clusters for the fill pass").

**Blocked by:** 34

**Status:** resolved

**What to build:** every Guide from the taxonomy, plus Procedures with no owning Cause (replace-the-seat), written or updated from all mapped Sources under the `/wiki-ingest` rules.

Cluster definition, as approved:

27. **Guides cluster**: all 16 Guides, plus Procedures with no owning Cause (replace-the-seat) and Causes with no Problem (none).

Blocking: this child waits for every earlier cluster that owns a page it shares and for the previous cluster, since clusters commit one at a time to the same index and log. 

- [x] Every mapped Source is read in full (via the per-Source notes in `.scratch/wiki-bootstrap/notes/`); mappings the Source doesn't support are dropped.
- [x] Owned pages are created from `templates/` (or updated if they exist), with per-section citations, Trust tier ranking, conflict callouts, Brand notes and OEM part number caveats.
- [x] Shared pages owned by earlier clusters are updated, not recreated; links go both ways.
- [x] Index and log are updated; `python tools/validate_wiki.py --allow-unlogged wiki raw` is clean; the cluster gets its own commit.

## Comments

**2026-11-24, fill pass (commit 6ed1ff6).**
- Created: 15 Guides (battery-care-and-charging 29, belt-types 8, choosing-the-right-gas 44, cleaning-the-mower 26, electric-mower-care-and-safety 19, engine-cooling-times 9, engine-oil-guide 27, fuel-storage-and-stabilizers 61, how-clutches-work 5, mower-got-wet 10, mower-parts-that-wear-out 28, reading-wiring-schematics 7, routine-service-and-maintenance 48, winterizing-and-storage 28, zero-turn-safety 14 Sources); procedures/replace-the-seat (3), linked to causes/bad-safety-switch, whose Fix already says to replace a worn seat.
- Updated: guides/customer-intake (S6, warranty/recall lookup by serial number); causes/bad-safety-switch (procedure back-link); Guide links in the Tips sections of 44 Problem, Cause and Procedure pages; index.
- Dropped: no pages.
- Un-skipped during the skip review: a-guide-to-choosing-a-cordless-lawn-mower, should-i-get-an-electric-riding-mower (electric-mower-care-and-safety), best-zero-turn-mower-tires-for-hills, choosing-between-a-residential-commercial-zero-turn-mower (zero-turn-safety).
- Conflicts flagged: octane 87 vs 89; E30 vs E35; stabilizer into the tank vs into the can; full-charge voltage and charge time; cover type; battery in vs out for winter; basement storage; foam filter oiling; break-in oil change hours; drive belt life.
- Source errors not cited: REC-90 "up to 0%", "minimum 10% ethanol", Exmark garbled ethanol sentence, battery "ohmmeter", zero-charge freeze-table row, belt "3.75 inches".
- Spot-check: 15 citations on the three largest Guides, 0 errors.
