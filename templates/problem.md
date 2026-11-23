---
type: problem
title: <Symptom as a customer would say it>
aliases:
  - <other customer phrasing>
mower_types: [<push | self-propelled | riding | zero-turn>]
power_sources: [<gas | battery | diesel>]
causes:
  - ../causes/<cause-slug>.md
part_types:
  - <generic Part type, never a SKU>
source_count: <number of distinct Sources in ## Sources>
updated: <YYYY-MM-DD>
---

# <Title>

<!-- Template for Problem pages. Copy to wiki/problems/<kebab-case-symptom>.md.
     Keep every H2 below, in this order. End each section with a
     "Sources: [S1](...), [S2](...)" line (per-section citation).
     Links are relative markdown, never [[wikilinks]].
     Basic intake (brand, model, serial, engine, age) lives in the
     customer-intake Guide, so don't repeat it here. -->

## Summary

<What the symptom looks like and the short version of why it happens.>

## Diagnostic questions

| Question | Answer A → Causes | Answer B → Causes |
|---|---|---|
| <Question for the customer> | <answer> → [Cause](../causes/<slug>.md) | <answer> → [Cause](../causes/<slug>.md) |

## Quick triage

<Numbered checks, ordered by likelihood and by how cheap the check is.>

## Possible causes

<Ranked by how many Sources name the Cause for this Problem, weighted by Trust tier.>

| Cause | How common | Telltale signs | Fix difficulty |
|---|---|---|---|
| [<Cause>](../causes/<slug>.md) | <n of N Sources> | <signs> | <easy / moderate / pro> |

## Brand notes

<Brand, model-line or engine specifics. OEM part numbers go only here, marked "per Source, verify against catalog".>

## Tips & life hacks

## Parts commonly needed

<Part types with fitment notes.>

## Safety

## When to send to a technician

## Related problems

<Sibling Problems that sound alike: "Not this problem? See …">

## Sources

- [S1](../../raw/<SourceKind>/<domain>/<slug>.md) — <title> (<Trust tier>)
