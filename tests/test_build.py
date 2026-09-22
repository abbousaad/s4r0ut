import importlib.util
import unittest
from pathlib import Path


def load_build_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "build.py"
    spec = importlib.util.spec_from_file_location("build", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildTests(unittest.TestCase):
    def test_leet_variants_include_moroccan_digraphs(self):
        build = load_build_module()

        variants = build.leet_variants("khoya")

        self.assertIn("5oya", variants)

    def test_strict_profile_is_subset_of_extended_profile(self):
        build = load_build_module()
        seed_groups = {
            "names_morocco": ["yassine"],
            "cities_regions": ["casa"],
            "football_culture": ["wydad"],
            "darija_latin": ["khoya"],
            "moroccan_patterns": ["212"],
        }

        profiles = build.build_profiles(seed_groups)

        self.assertTrue(set(profiles["strict"]).issubset(set(profiles["extended"])))
        self.assertIn("khoya123", profiles["strict"])
        self.assertIn("5oya123", profiles["strict"])

    def test_clean_entries_filters_whitespace_and_extreme_lengths(self):
        build = load_build_module()

        clean = build.clean_entries({"casa", "bad value", "abc", "a" * 33, "rabat2024"})

        self.assertEqual(clean, ["casa", "rabat2024"])


if __name__ == "__main__":
    unittest.main()
