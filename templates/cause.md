---
type: cause
title: <Cause, named after the fault, never a brand>
problems:
  - ../problems/<problem-slug>.md
part_types:
  - <generic Part type, never a SKU>
procedures:
  - ../procedures/<procedure-slug>.md
source_count: <number of distinct Sources in ## Sources>
updated: <YYYY-MM-DD>
---

# <Title>

<!-- Template for Cause pages. Copy to wiki/causes/<kebab-case-cause>.md.
     Keep every H2 below, in this order. End each section with a
     "Sources: [S1](...), [S2](...)" line (per-section citation).
     Links are relative markdown, never [[wikilinks]].
     Every Problem in `problems` must be linked from the body and must list
     this Cause back in its own `causes`. Same for `procedures` <-> the
     Procedure's `causes`. The validator enforces both. -->

## Summary

<What the fault is, why it happens, and how hard the fix is (easy / moderate / pro).>

## Before you start

<Questions to ask before picking parts or steps: engine brand and model, carburetor or EFI, part numbers on the old part, ...>

## Symptoms it produces

<Bullet list of linked Problems, with the telltale signs for each.>

- [<Problem>](../problems/<slug>.md): <telltale signs>

## How to confirm

<Tests, measurements and visual checks that prove this Cause before any part is replaced.>

## Fix

<Short fix summary, linking the Procedures that carry the steps.>

- [<Procedure>](../procedures/<slug>.md)

## Brand notes

<Brand, model-line or engine specifics. OEM part numbers only here or in Parts & fitment, marked "per Source, verify against catalog".>

## Parts & fitment

<Part types with fitment notes: what to match when buying the replacement.>

## Tips & life hacks

## Sources

- [S1](../../raw/<SourceKind>/<domain>/<slug>.md) — <title> (<Trust tier>)
