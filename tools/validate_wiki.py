#!/usr/bin/env python3
"""Deterministic structural validator for the lawn mower wiki.

Usage: python tools/validate_wiki.py <wiki_root> <raw_root>

Prints one line per violation as `<page>: [<rule>] <message>` and exits 1 when
any are found, 0 when the wiki is clean. Only dependency: PyYAML.

Rules (see .scratch/wiki-bootstrap/spec.md, "Validator"):
  frontmatter   - keys and controlled-vocabulary values match the page type
  sections      - required H2 sections present and in template order
  source-count  - source_count equals the distinct Sources in ## Sources
  index         - every page is in index.md; every index link resolves
"""
import re
import sys
from pathlib import Path

import yaml

MOWER_TYPES = {"push", "self-propelled", "riding", "zero-turn"}
POWER_SOURCES = {"gas", "battery", "diesel"}

SCHEMAS = {
    "problem": {
        "keys": ["type", "title", "aliases", "mower_types", "power_sources",
                 "causes", "part_types", "source_count", "updated"],
        "sections": ["Summary", "Diagnostic questions", "Quick triage",
                     "Possible causes", "Brand notes", "Tips & life hacks",
                     "Parts commonly needed", "Safety",
                     "When to send to a technician", "Related problems",
                     "Sources"],
    },
}

PAGE_DIRS = ("problems", "causes", "procedures", "guides")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
H2_RE = re.compile(r"^## +(.+?)\s*$", re.MULTILINE)


def split_frontmatter(text):
    """Return (frontmatter dict or None, body)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None, text
    return (data if isinstance(data, dict) else None), text[end + 5:]


def section(body, name):
    """Text of the H2 section `name`, up to the next H2 (or '')."""
    m = re.search(r"^## +" + re.escape(name) + r"\s*$", body, re.MULTILINE)
    if not m:
        return ""
    nxt = H2_RE.search(body, m.end())
    return body[m.end():nxt.start() if nxt else len(body)]


def check_vocab(field, value, allowed):
    if not isinstance(value, list) or not value:
        return [f"{field} must be a non-empty list"]
    bad = [v for v in value if v not in allowed]
    if bad:
        return [f"{field} has values outside the vocabulary: {', '.join(map(str, bad))} "
                f"(allowed: {', '.join(sorted(allowed))})"]
    return []


def check_page(path):
    out = []
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm, body = split_frontmatter(text)
    if fm is None:
        return [("frontmatter", "missing or unparseable YAML frontmatter")]
    schema = SCHEMAS.get(fm.get("type"))
    if schema is None:
        return [("frontmatter", f"unknown page type: {fm.get('type')!r}")]

    keys = schema["keys"]
    missing = [k for k in keys if k not in fm]
    extra = [k for k in fm if k not in keys]
    if missing:
        out.append(("frontmatter", f"missing keys: {', '.join(missing)}"))
    if extra:
        out.append(("frontmatter", f"unexpected keys: {', '.join(extra)}"))
    if "mower_types" in fm:
        out += [("frontmatter", m) for m in check_vocab("mower_types", fm["mower_types"], MOWER_TYPES)]
    if "power_sources" in fm:
        out += [("frontmatter", m) for m in check_vocab("power_sources", fm["power_sources"], POWER_SOURCES)]

    found = H2_RE.findall(body)
    required = schema["sections"]
    absent = [s for s in required if s not in found]
    if absent:
        out.append(("sections", f"missing sections: {', '.join(absent)}"))
    present = [s for s in found if s in required]
    expected = [s for s in required if s in found]
    if present != expected:
        out.append(("sections", f"sections out of order: {' -> '.join(present)} "
                                f"(expected {' -> '.join(expected)})"))

    if "source_count" in fm and "Sources" in found:
        cited = {t for t in LINK_RE.findall(section(body, "Sources")) if "raw/" in t}
        if fm["source_count"] != len(cited):
            out.append(("source-count", f"source_count is {fm['source_count']} but "
                                        f"{len(cited)} distinct Sources are listed"))
    return out


def check_index(wiki, pages):
    out = []
    index = wiki / "index.md"
    if not index.exists():
        return [("index.md", "index", "index.md is missing")]
    targets = set()
    for link in LINK_RE.findall(index.read_text(encoding="utf-8")):
        if "://" in link:
            continue
        target = (wiki / link.split("#")[0]).resolve()
        targets.add(target)
        if not target.exists():
            out.append(("index.md", "index", f"entry points to a missing page: {link}"))
    for page in pages:
        if page.resolve() not in targets:
            out.append((page.relative_to(wiki).as_posix(), "index", "page is not listed in index.md"))
    return out


def validate(wiki, raw):
    pages = sorted(p for d in PAGE_DIRS for p in (wiki / d).rglob("*.md"))
    violations = []
    for page in pages:
        rel = page.relative_to(wiki).as_posix()
        violations += [(rel, rule, msg) for rule, msg in check_page(page)]
    violations += check_index(wiki, pages)
    return violations


def main(argv):
    if len(argv) != 3:
        print("usage: validate_wiki.py <wiki_root> <raw_root>", file=sys.stderr)
        return 2
    wiki, raw = Path(argv[1]), Path(argv[2])
    for root in (wiki, raw):
        if not root.is_dir():
            print(f"not a directory: {root}", file=sys.stderr)
            return 2
    sys.stdout.reconfigure(encoding="utf-8")
    violations = validate(wiki, raw)
    for rel, rule, msg in violations:
        print(f"{rel}: [{rule}] {msg}")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
