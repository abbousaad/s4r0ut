import importlib.util
import unittest
from pathlib import Path


def load_qa_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "qa.py"
    spec = importlib.util.spec_from_file_location("qa", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QaTests(unittest.TestCase):
    def test_qa_accepts_sorted_unique_dictionary(self):
        qa = load_qa_module()
        dictionary = Path(self._testMethodName + ".txt")
        self.addCleanup(dictionary.unlink, missing_ok=True)
        dictionary.write_text("casa\ncasa123\nrabat2024\n", encoding="utf-8")

        self.assertEqual(qa.check_file(dictionary), [])

    def test_qa_rejects_unsorted_duplicates_and_whitespace(self):
        qa = load_qa_module()
        dictionary = Path(self._testMethodName + ".txt")
        self.addCleanup(dictionary.unlink, missing_ok=True)
        dictionary.write_text("rabat\ncasa\ncasa\nbad value\n", encoding="utf-8")

        errors = qa.check_file(dictionary)

        self.assertTrue(any("not sorted" in error for error in errors))
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("contains whitespace" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
