# 03: Guide pages and the customer-intake Guide

**What to build:** General owner know-how gets its own page type, and the shared customer-intake Guide exists. The support agent can collect the basics (brand, model, serial number, engine make, Mower type, age, when it last ran) from one place, and Problem pages link to it instead of repeating those questions.

**Blocked by:** 01

**Status:** resolved

- [x] The Guide template (Summary → Key facts → Recommendations → Tips & life hacks → Common mistakes → Related → Sources) exists with the frontmatter from the spec.
- [x] The validator supports the Guide type (frontmatter and section order), with a passing fixture and failing fixtures.
- [x] A real customer-intake Guide exists. Each intake question explains why it matters (e.g. the serial number determines part fitment), and the Guide cites Sources where they exist.
- [x] The tracer Problem's Diagnostic questions link to the customer-intake Guide.
- [x] The index and log are updated, the validator passes, and the work is committed.
