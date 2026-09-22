import importlib.util
import unittest
from pathlib import Path


def load_seed_qa_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "seed_qa.py"
    spec = importlib.util.spec_from_file_location("seed_qa", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SeedQaTests(unittest.TestCase):
    def test_seed_qa_accepts_clean_seed_file(self):
        seed_qa = load_seed_qa_module()
        seed = Path(self._testMethodName + ".txt")
        self.addCleanup(seed.unlink, missing_ok=True)
        seed.write_text("# comment\ncasa\nkhoya\nsa7bi\n", encoding="utf-8")

        self.assertEqual(seed_qa.check_seed_file(seed), [])

    def test_seed_qa_rejects_uppercase_duplicates_and_phone_like_values(self):
        seed_qa = load_seed_qa_module()
        seed = Path(self._testMethodName + ".txt")
        self.addCleanup(seed.unlink, missing_ok=True)
        seed.write_text("Casa\ncasa\ncasa\n0612345678\n", encoding="utf-8")

        errors = seed_qa.check_seed_file(seed)

        self.assertTrue(any("lowercase" in error for error in errors))
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("real phone number" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

