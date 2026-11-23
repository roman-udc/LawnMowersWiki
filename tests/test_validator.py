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


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "fixture"
        shutil.copytree(BASELINE, self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def run_validator(self):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root / "wiki"), str(self.root / "raw")],
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
        rules = re.findall(r"\[([a-z-]+)\]", out)
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

    # --- sections -------------------------------------------------------
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


if __name__ == "__main__":
    unittest.main()
