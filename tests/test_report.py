import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def load_report_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "report.py"
    spec = importlib.util.spec_from_file_location("report", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReportTests(unittest.TestCase):
    def test_enrich_stats_adds_size_and_sha256(self):
        report = load_report_module()
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        dist = Path(temp_dir.name)
        sample = dist / "sample.txt"
        sample.write_text("casa\n", encoding="utf-8")

        stats = {
            "profiles": {
                "sample": {
                    "file": "sample.txt",
                    "entries": 1,
                    "unique_entries": 1,
                    "min_length": 4,
                    "max_length": 4,
                    "moroccan_keyword_hits": 1,
                }
            },
            "seed_files": {"cities_regions": 1},
            "total_seeds": 1,
        }

        enriched = report.enrich_stats(stats, dist)

        self.assertEqual(enriched["profiles"]["sample"]["bytes"], 5)
        self.assertEqual(len(enriched["profiles"]["sample"]["sha256"]), 64)

    def test_markdown_report_contains_profile_table(self):
        report = load_report_module()
        stats = json.loads(
            """
            {
              "profiles": {
                "strict": {
                  "file": "s4r0ut-strict.txt",
                  "entries": 1,
                  "unique_entries": 1,
                  "min_length": 4,
                  "max_length": 4,
                  "moroccan_keyword_hits": 1,
                  "bytes": 5,
                  "sha256": "abc"
                }
              },
              "seed_files": {"cities_regions": 1},
              "total_seeds": 1
            }
            """
        )

        markdown = report.markdown_report(stats)

        self.assertIn("| strict | 1 | 1 | 4 | 4 | 1 | 5 | `abc` |", markdown)
        self.assertIn("Quality Gates", markdown)


if __name__ == "__main__":
    unittest.main()
