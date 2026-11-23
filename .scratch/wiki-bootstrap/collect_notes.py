"""Collect the fill-pass notes for one wiki page from every per-Source notes file.

Usage:
  python .scratch/wiki-bootstrap/collect_notes.py causes/old-fuel        # all notes for a page
  python .scratch/wiki-bootstrap/collect_notes.py --sources causes/old-fuel   # just the Source list
  python .scratch/wiki-bootstrap/collect_notes.py --missing              # batch paths with no notes file

Each block is headed by the Source path, title and Trust tier.
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
NOTES = HERE / "notes"


def load(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm = {}
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            try:
                fm = yaml.safe_load(text[4:end]) or {}
            except yaml.YAMLError:
                fm = {}
            text = text[end + 5:]
    sections = {}
    for m in re.finditer(r"^## page: *(\S+)\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        sections[m.group(1).strip().removesuffix(".md")] = m.group(2).strip()
    return fm, sections


def notes_files():
    return sorted(p for p in NOTES.rglob("*.md") if p.parent != NOTES and "batches" not in p.parts)


def main(argv):
    if argv and argv[0] == "--missing":
        have = {str(load(p)[0].get("path")) for p in notes_files()}
        for b in sorted((NOTES / "batches").glob("*.txt")):
            for line in b.read_text().split():
                if line not in have:
                    print(line)
        return
    only_sources = argv and argv[0] == "--sources"
    page = (argv[1] if only_sources else argv[0]).removesuffix(".md")
    sys.stdout.reconfigure(encoding="utf-8")
    for p in notes_files():
        fm, sections = load(p)
        if page in sections:
            head = f"{fm.get('path')} | {fm.get('title')} | {fm.get('tier')}"
            if only_sources:
                print(head)
            else:
                print(f"=== {head} | brand: {fm.get('brand')} | types: {fm.get('mower_types')}\n{sections[page]}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
