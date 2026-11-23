"""Fixture tests for tools/validate_wiki.py.

Each test copies the valid baseline fixture, breaks exactly one rule, runs the
validator as a subprocess and checks only its output and exit status.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "tools" / "validate_wiki.py"
BASELINE = Path(__file__).resolve().parent / "fixtures" / "valid"
PAGE = Path("wiki/problems/engine-wont-start.md")
CAUSE = Path("wiki/causes/old-fuel.md")
PROC = Path("wiki/procedures/drain-the-fuel-tank.md")
GUIDE = Path("wiki/guides/customer-intake.md")


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "fixture"
        shutil.copytree(BASELINE, self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def run_validator(self, *flags):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), *flags, str(self.root / "wiki"), str(self.root / "raw")],
            capture_output=True, text=True, encoding="utf-8",
        )
        return proc.returncode, proc.stdout

    def edit(self, rel, old, new):
        path = self.root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture edit target missing in {rel}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_only_rule(self, rule):
        code, out = self.run_validator()
        self.assertNotEqual(code, 0, out)
        rules = re.findall(r"^\S+: \[([a-z-]+)\] ", out, re.MULTILINE)
        self.assertTrue(rules, out)
        self.assertEqual(set(rules), {rule}, out)
        return out

    # --- baseline -------------------------------------------------------
    def test_valid_baseline_is_clean(self):
        code, out = self.run_validator()
        self.assertEqual(out.strip(), "")
        self.assertEqual(code, 0)

    # --- frontmatter ----------------------------------------------------
    def test_missing_frontmatter_key(self):
        self.edit(PAGE, "source_count: 2\n", "")
        # only the frontmatter rule fires, not source-count
        out = self.assert_only_rule("frontmatter")
        self.assertIn("source_count", out)

    def test_unknown_frontmatter_key(self):
        self.edit(PAGE, "updated: 2024-01-01\n", "updated: 2024-01-01\nbrand: Toro\n")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("brand", out)

    def test_invalid_mower_type(self):
        self.edit(PAGE, "mower_types: [push, riding]", "mower_types: [push, tractor]")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("tractor", out)

    def test_invalid_power_source(self):
        self.edit(PAGE, "power_sources: [gas]", "power_sources: [electric]")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("electric", out)

    def test_missing_frontmatter_block(self):
        path = self.root / PAGE
        text = path.read_text(encoding="utf-8")
        path.write_text(text.split("---\n", 2)[2], encoding="utf-8")
        self.assert_only_rule("frontmatter")

    def test_invalid_difficulty(self):
        self.edit(PROC, "difficulty: easy", "difficulty: hard")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("hard", out)

    def test_procedure_without_tools(self):
        self.edit(PROC, "tools: [siphon pump, gas can]", "tools: []")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("tools", out)

    def test_procedure_without_time_estimate(self):
        self.edit(PROC, "time_estimate: 15 minutes\n", "")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("time_estimate", out)

    def test_unknown_cause_frontmatter_key(self):
        self.edit(CAUSE, "updated: 2024-01-01\n", "updated: 2024-01-01\naliases: [x]\n")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("aliases", out)

    def test_unknown_guide_frontmatter_key(self):
        self.edit(GUIDE, "updated: 2024-01-01\n", "updated: 2024-01-01\ncauses: []\n")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("causes", out)

    def test_guide_missing_related_key(self):
        self.edit(GUIDE, "related:\n  - ../problems/engine-wont-start.md\n", "")
        out = self.assert_only_rule("frontmatter")
        self.assertIn("related", out)

    # --- sections -------------------------------------------------------
    def test_guide_missing_section(self):
        self.edit(GUIDE, "## Common mistakes\n\nConfusing the engine model with the mower model.\n\n", "")
        out = self.assert_only_rule("sections")
        self.assertIn("Common mistakes", out)

    def test_guide_sections_out_of_order(self):
        self.edit(GUIDE, "## Key facts\n\nThe model tag is under the seat.\n\n", "")
        self.edit(GUIDE, "## Related\n", "## Key facts\n\nThe model tag is under the seat.\n\n## Related\n")
        out = self.assert_only_rule("sections")
        self.assertIn("order", out)

    def test_cause_missing_section(self):
        self.edit(CAUSE, "## How to confirm\n\nSmell it.\n\n", "")
        out = self.assert_only_rule("sections")
        self.assertIn("How to confirm", out)

    def test_procedure_sections_out_of_order(self):
        self.edit(PROC, "## Safety\n\nWork outside.\n\n", "")
        self.edit(PROC, "## Sources\n", "## Safety\n\nWork outside.\n\n## Sources\n")
        out = self.assert_only_rule("sections")
        self.assertIn("order", out)

    def test_missing_section(self):
        self.edit(PAGE, "## Brand notes\n\nNone.\n\n", "")
        out = self.assert_only_rule("sections")
        self.assertIn("Brand notes", out)

    def test_sections_out_of_order(self):
        self.edit(PAGE, "## Quick triage\n\n1. Check the gas.\n\n", "")
        self.edit(PAGE, "## Summary\n", "## Quick triage\n\n1. Check the gas.\n\n## Summary\n")
        out = self.assert_only_rule("sections")
        self.assertIn("order", out)

    # --- source_count ---------------------------------------------------
    def test_source_count_mismatch(self):
        self.edit(PAGE, "source_count: 2", "source_count: 3")
        out = self.assert_only_rule("source-count")
        self.assertIn("3", out)

    def test_duplicate_source_counts_once(self):
        self.edit(
            PAGE,
            "- [S2](../../raw/Articles/example.com/old-gas.md)\n",
            "- [S2](../../raw/Articles/example.com/old-gas.md)\n"
            "- [S2 again](../../raw/Articles/example.com/old-gas.md)\n",
        )
        code, out = self.run_validator()
        self.assertEqual((code, out.strip()), (0, ""))

    # --- index ----------------------------------------------------------
    def test_page_missing_from_index(self):
        self.edit("wiki/index.md", "- [Engine won't start](problems/engine-wont-start.md)", "- (removed)")
        out = self.assert_only_rule("index")
        self.assertIn("engine-wont-start.md", out)

    def test_stale_index_entry(self):
        self.edit(
            "wiki/index.md", "## Causes\n",
            "## Causes\n\n- [Ghost](causes/ghost.md) — no such page\n",
        )
        out = self.assert_only_rule("index")
        self.assertIn("ghost.md", out)

    # --- links ----------------------------------------------------------
    def test_broken_relative_link(self):
        self.edit(PAGE, "## Related problems\n\nNone yet.",
                  "## Related problems\n\nSee [Engine won't crank](engine-wont-crank.md).")
        out = self.assert_only_rule("broken-link")
        self.assertIn("engine-wont-crank.md", out)

    def test_broken_source_link(self):
        self.edit(CAUSE, "How long has it sat?",
                  "How long has it sat? Sources: [S9](../../raw/Articles/example.com/missing.md)")
        out = self.assert_only_rule("broken-link")
        self.assertIn("missing.md", out)

    def test_external_and_anchor_links_are_not_checked(self):
        self.edit(PAGE, "None yet.", "See [docs](https://example.com/x) and [top](#summary).")
        code, out = self.run_validator()
        self.assertEqual((code, out.strip()), (0, ""))

    def test_wikilink_is_rejected(self):
        self.edit(CAUSE, "Smell it.", "Smell it, then see [[drain-the-fuel-tank]].")
        out = self.assert_only_rule("wikilink")
        self.assertIn("[[drain-the-fuel-tank]]", out)

    def test_frontmatter_lists_cause_body_does_not_link(self):
        path = self.root / PAGE
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("[Old fuel](../causes/old-fuel.md)", "Old fuel"), encoding="utf-8")
        out = self.assert_only_rule("link-lists")
        self.assertIn("old-fuel.md", out)

    def test_body_links_procedure_frontmatter_does_not_list(self):
        self.edit(CAUSE, "  - ../procedures/drain-the-fuel-tank.md\n", "")
        self.edit(CAUSE, "procedures:\n", "procedures: []\n")
        self.edit(PROC, "  - ../causes/old-fuel.md\n", "")
        self.edit(PROC, "causes:\n", "causes: []\n")
        self.edit(PROC, "Fixes [Old fuel](../causes/old-fuel.md).", "Fixes old fuel.")
        out = self.assert_only_rule("link-lists")
        self.assertIn("drain-the-fuel-tank.md", out)
        self.assertIn("causes/old-fuel.md", out)

    def test_guide_related_page_body_does_not_link(self):
        self.edit(GUIDE, "- [Engine won't start](../problems/engine-wont-start.md)\n", "- None\n")
        out = self.assert_only_rule("link-lists")
        self.assertIn("engine-wont-start.md", out)

    def test_cause_missing_back_link_to_problem(self):
        self.edit(CAUSE, "  - ../problems/engine-starts-then-dies.md\n", "")
        self.edit(CAUSE, "- [Engine starts then dies](../problems/engine-starts-then-dies.md)\n", "")
        out = self.assert_only_rule("backlink")
        self.assertIn("engine-starts-then-dies.md", out)

    def test_procedure_missing_back_link_to_cause(self):
        self.edit(PROC, "  - ../causes/old-fuel.md\n", "")
        self.edit(PROC, "causes:\n", "causes: []\n")
        self.edit(PROC, "Fixes [Old fuel](../causes/old-fuel.md).", "Fixes old fuel.")
        out = self.assert_only_rule("backlink")
        self.assertIn("drain-the-fuel-tank.md", out)

    def test_cause_missing_back_link_to_procedure(self):
        self.edit(CAUSE, "  - ../procedures/drain-the-fuel-tank.md\n", "")
        self.edit(CAUSE, "procedures:\n", "procedures: []\n")
        self.edit(CAUSE, "[Drain the fuel tank](../procedures/drain-the-fuel-tank.md).", "Drain the tank.")
        out = self.assert_only_rule("backlink")
        self.assertIn("old-fuel.md", out)

    # --- graph completeness ---------------------------------------------
    def add_page(self, src, dst, replacements, index_section):
        text = (self.root / src).read_text(encoding="utf-8")
        for old, new in replacements:
            self.assertIn(old, text)
            text = text.replace(old, new)
        (self.root / dst).write_text(text, encoding="utf-8")
        link = Path(dst).relative_to("wiki").as_posix()
        self.edit("wiki/index.md", f"## {index_section}\n", f"## {index_section}\n\n- [New]({link}) — new\n")

    def test_problem_without_causes(self):
        self.add_page(PAGE, "wiki/problems/mower-smokes.md", [
            ("causes:\n  - ../causes/old-fuel.md\n", "causes: []\n"),
            ("[Old fuel](../causes/old-fuel.md)", "Old fuel"),
        ], "Problems")
        out = self.assert_only_rule("no-causes")
        self.assertIn("mower-smokes.md", out)

    def test_cause_without_problems(self):
        self.add_page(CAUSE, "wiki/causes/bad-coil.md", [
            ("problems:\n  - ../problems/engine-wont-start.md\n  - ../problems/engine-starts-then-dies.md\n", "problems: []\n"),
            ("procedures:\n  - ../procedures/drain-the-fuel-tank.md\n", "procedures: []\n"),
            ("- [Engine won't start](../problems/engine-wont-start.md)\n- [Engine starts then dies](../problems/engine-starts-then-dies.md)\n", "- None\n"),
            ("[Drain the fuel tank](../procedures/drain-the-fuel-tank.md)", "Drain it"),
        ], "Causes")
        out = self.assert_only_rule("no-problems")
        self.assertIn("bad-coil.md", out)

    # --- log coverage ---------------------------------------------------
    def add_source(self, rel="raw/Articles/example.com/new-tip.md"):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\ntitle: New tip\n---\nBody\n", encoding="utf-8")
        return rel

    def test_source_missing_from_log(self):
        self.add_source()
        out = self.assert_only_rule("unlogged")
        self.assertIn("raw/Articles/example.com/new-tip.md", out)

    def test_non_conforming_source_outside_convention_is_still_checked(self):
        self.add_source("raw/stray-note.txt")
        out = self.assert_only_rule("unlogged")
        self.assertIn("raw/stray-note.txt", out)

    def test_skipped_source_counts_as_logged(self):
        rel = self.add_source()
        self.edit("wiki/log.md", "→ ingested → problems/engine-wont-start.md\n",
                  f"→ ingested → problems/engine-wont-start.md\n- {rel} → skipped: buying guide\n")
        code, out = self.run_validator()
        self.assertEqual((code, out.strip()), (0, ""))

    def test_source_named_only_in_a_note_is_unlogged(self):
        rel = self.add_source()
        with (self.root / "wiki" / "log.md").open("a", encoding="utf-8") as log:
            log.write(f"\nNote: {rel} still to do.\n")
        out = self.assert_only_rule("unlogged")
        self.assertIn(rel, out)

    def test_allow_unlogged_flag_suppresses_the_rule(self):
        self.add_source()
        code, out = self.run_validator("--allow-unlogged")
        self.assertEqual((code, out.strip()), (0, ""))

    def test_allow_unlogged_flag_keeps_other_rules(self):
        self.add_source()
        self.edit(PAGE, "source_count: 2", "source_count: 9")
        code, out = self.run_validator("--allow-unlogged")
        self.assertNotEqual(code, 0)
        self.assertIn("[source-count]", out)
        self.assertNotIn("[unlogged]", out)

    def test_missing_log_is_reported(self):
        (self.root / "wiki" / "log.md").unlink()
        out = self.assert_only_rule("unlogged")
        self.assertIn("log.md is missing", out)


if __name__ == "__main__":
    unittest.main()
