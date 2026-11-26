# Glossary

## Problem

A symptom of faulty equipment, phrased the way an owner or customer would report it ("engine won't start", "blades won't engage", "mower cuts uneven"). A Problem is the entry point for diagnosis. It is generic across brands, and brand-specific detail sits inside it as Brand notes.

_Avoid_: issue, fault, failure (these blur the line between Problem and Cause)

## Cause

A specific underlying reason that produces one or more Problems ("bad starter solenoid", "clogged carburetor", "stretched deck belt"). One Cause can explain several Problems, and one Problem usually has several possible Causes.

_Avoid_: root cause, diagnosis

## Procedure

Step-by-step instructions for one repair or maintenance task ("replace a starter solenoid", "level a mower deck"). A Cause points to the Procedures that fix it.

_Avoid_: how-to, tutorial

## Guide

General owner know-how that isn't tied to a single Cause ("fuel storage and ethanol", "winterizing", "battery care"). Buying advice and lawn-care advice are not Guides.

## Diagnostic question

A question put to the customer to narrow down which Cause is behind their Problem, or which Procedure or Guide applies (e.g. "Does the engine click when you turn the key?"). Its value comes from how each possible answer shifts the likely Causes.

## Source

One immutable document collected from a forum, blog or manufacturer site. It is never edited. Every claim in the knowledge base traces back to at least one Source.

_Avoid_: article (too narrow, since forum threads are also Sources), raw file

## Trust tier

How much weight a Source's claims carry: **manufacturer** (OEM manuals, parts-supplier repair guides) > **expert** (notes written by the wiki's own lawn-mower specialist, kept in `raw/Expert/`) > **expert-blog** > **forum**. Within forum Sources, a confirmed fix ("that fixed it") outranks an untested suggestion.

## Brand note

Detail about a Problem or Cause that applies only to particular brands, model lines or engines (for example, where the solenoid sits on a Kawasaki engine).

## Mower type

The form of the equipment: push, self-propelled, riding / lawn tractor, zero-turn.

## Power source

What drives the equipment: gas, battery (cordless electric), diesel.

## Part type

A generic, replaceable component named by function ("starter solenoid", "deck belt", "spark plug"), as opposed to a specific SKU or OEM part number.

_Avoid_: part, SKU (when the generic category is meant)
