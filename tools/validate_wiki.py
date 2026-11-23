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
  broken-link   - every relative link (to a page or a Source) resolves
  wikilink      - [[wikilinks]] are not used; links are relative markdown
  link-lists    - frontmatter causes/problems/procedures match the body links
  backlink      - Problem <-> Cause and Cause <-> Procedure links go both ways
  no-causes     - every Problem lists at least one Cause
  no-problems   - every Cause lists at least one Problem
"""
import re
import sys
from pathlib import Path

import yaml

MOWER_TYPES = {"push", "self-propelled", "riding", "zero-turn"}
POWER_SOURCES = {"gas", "battery", "diesel"}
DIFFICULTIES = {"easy", "moderate", "pro"}

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
    "cause": {
        "keys": ["type", "title", "problems", "part_types", "procedures",
                 "source_count", "updated"],
        "sections": ["Summary", "Before you start", "Symptoms it produces",
                     "How to confirm", "Fix", "Brand notes", "Parts & fitment",
                     "Tips & life hacks", "Sources"],
    },
    "procedure": {
        "keys": ["type", "title", "causes", "part_types", "difficulty",
                 "time_estimate", "tools", "source_count", "updated"],
        "sections": ["Before you start", "Safety", "Tools & parts", "Steps",
                     "Brand notes", "Tips & common mistakes", "Verify the fix",
                     "Sources"],
    },
}

PAGE_DIRS = ("problems", "causes", "procedures", "guides")
# Frontmatter link lists per page type: field -> folder its entries point into.
LINK_LISTS = {
    "problem": {"causes": "causes"},
    "cause": {"problems": "problems", "procedures": "procedures"},
    "procedure": {"causes": "causes"},
}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK_RE = re.compile(r"!?\[\[[^\]]*\]\]")
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


def resolve(page, link):
    """Absolute path a relative link points to, or None for URLs and same-page anchors."""
    if "://" in link or link.startswith(("#", "mailto:")):
        return None
    return (page.parent / link.split("#")[0]).resolve()


def link_list(page, fm, field):
    """Resolved targets of a frontmatter link list (empty when absent or malformed)."""
    value = fm.get(field)
    if not isinstance(value, list):
        return set()
    return {resolve(page, str(v)) for v in value} - {None}


def check_link_lists(page, wiki, fm, body):
    out = []
    body_targets = {resolve(page, l) for l in LINK_RE.findall(body)} - {None}
    for field, folder in LINK_LISTS.get(fm.get("type"), {}).items():
        listed = link_list(page, fm, field)
        linked = {t for t in body_targets if t.parent == (wiki / folder).resolve()}
        rel = lambda paths: ", ".join(sorted(p.relative_to(wiki.resolve()).as_posix() for p in paths))
        if listed - linked:
            out.append(("link-lists", f"{field} lists pages the body never links: {rel(listed - linked)}"))
        if linked - listed:
            out.append(("link-lists", f"body links {folder} missing from {field}: {rel(linked - listed)}"))
    return out


def check_vocab(field, value, allowed):
    if not isinstance(value, list) or not value:
        return [f"{field} must be a non-empty list"]
    bad = [v for v in value if v not in allowed]
    if bad:
        return [f"{field} has values outside the vocabulary: {', '.join(map(str, bad))} "
                f"(allowed: {', '.join(sorted(allowed))})"]
    return []


def check_page(path, wiki):
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

    if "difficulty" in fm and fm["difficulty"] not in DIFFICULTIES:
        out.append(("frontmatter", f"difficulty {fm['difficulty']!r} is outside the vocabulary "
                                   f"(allowed: {', '.join(sorted(DIFFICULTIES))})"))
    if "time_estimate" in fm and not (isinstance(fm["time_estimate"], str) and fm["time_estimate"].strip()):
        out.append(("frontmatter", "time_estimate must be a non-empty string"))
    if "tools" in fm and not (isinstance(fm["tools"], list) and fm["tools"]):
        out.append(("frontmatter", "tools must be a non-empty list"))

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

    for link in dict.fromkeys(LINK_RE.findall(body)):
        target = resolve(path, link)
        if target is not None and not target.exists():
            out.append(("broken-link", f"link target does not exist: {link}"))

    for wl in WIKILINK_RE.findall(body):
        out.append(("wikilink", f"wikilink {wl} used; use a relative markdown link instead"))

    out += check_link_lists(path, wiki, fm, body)

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


# (type, field) whose entries must be mirrored by (target type, target field).
BACKLINKS = [
    ("problem", "causes", "cause", "problems"),
    ("cause", "problems", "problem", "causes"),
    ("cause", "procedures", "procedure", "causes"),
    ("procedure", "causes", "cause", "procedures"),
]


def check_graph(wiki, pages):
    out = []
    fms = {}
    for page in pages:
        fm, _ = split_frontmatter(page.read_text(encoding="utf-8").replace("\r\n", "\n"))
        if fm is not None:
            fms[page.resolve()] = fm
    rel = lambda p: p.relative_to(wiki.resolve()).as_posix()
    for page, fm in fms.items():
        kind = fm.get("type")
        if kind == "problem" and not link_list(page, fm, "causes"):
            out.append((rel(page), "no-causes", "Problem lists no Causes"))
        if kind == "cause" and not link_list(page, fm, "problems"):
            out.append((rel(page), "no-problems", "Cause lists no Problems"))
        for src_type, field, dst_type, back in BACKLINKS:
            if kind != src_type:
                continue
            for target in link_list(page, fm, field):
                tfm = fms.get(target)
                if tfm is None or tfm.get("type") != dst_type:
                    continue
                if page not in link_list(target, tfm, back):
                    out.append((rel(target), "backlink",
                                f"{back} is missing a back-link to {rel(page)}, which lists this page in {field}"))
    return out


def validate(wiki, raw):
    pages = sorted(p for d in PAGE_DIRS for p in (wiki / d).rglob("*.md"))
    violations = []
    for page in pages:
        rel = page.relative_to(wiki).as_posix()
        violations += [(rel, rule, msg) for rule, msg in check_page(page, wiki)]
    violations += check_graph(wiki, pages)
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
