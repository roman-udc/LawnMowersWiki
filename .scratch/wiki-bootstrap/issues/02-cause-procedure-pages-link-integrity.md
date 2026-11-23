# 02: Cause and Procedure pages and link integrity

**What to build:** The tracer Problem from ticket 01 now leads to real Cause pages, and from them to at least one Procedure, all linked in both directions. The validator guarantees the links hold together. A support agent can follow Problem → Cause → Procedure with plain file reads.

**Blocked by:** 01

**Status:** resolved

- [x] The Cause template (Summary → Before you start → Symptoms it produces → How to confirm → Fix → Brand notes → Parts & fitment → Tips & life hacks → Sources) and the Procedure template (Before you start → Safety → Tools & parts → Steps → Brand notes → Tips & common mistakes → Verify the fix → Sources) exist with the frontmatter from the spec, including the difficulty enum and time_estimate/tools for Procedures.
- [x] The validator supports both types: frontmatter keys and values, plus section order.
- [x] New validator rules, each with failing fixtures:
  - broken relative links
  - wikilink syntax used (links must be standard relative markdown links)
  - frontmatter link lists (causes / problems / procedures) disagree with the body
  - a back-link is missing (Problem ↔ Cause, Cause ↔ Procedure)
  - a Problem has no Causes
  - a Cause has no Problems
- [x] Every Cause linked from the tracer Problem has a real page written from its Sources, and at least one has a real Procedure.
- [x] OEM part numbers appear only in Brand notes or Parts & fitment, marked "per Source, verify against catalog".
- [x] The index and log are updated, the validator passes on the real wiki, and the work is committed.
