import importlib.util
import unittest
from pathlib import Path


def load_rule_qa_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "rule_qa.py"
    spec = importlib.util.spec_from_file_location("rule_qa", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RuleQaTests(unittest.TestCase):
    def test_rule_qa_accepts_clean_rule_file(self):
        rule_qa = load_rule_qa_module()
        rule_file = Path(self._testMethodName + ".rule")
        self.addCleanup(rule_file.unlink, missing_ok=True)
        rule_file.write_text("# comment\n:\nc\n$1$2$3\n", encoding="utf-8")

        self.assertEqual(rule_qa.check_rule_file(rule_file), [])

    def test_rule_qa_rejects_duplicates_and_long_rules(self):
        rule_qa = load_rule_qa_module()
        rule_file = Path(self._testMethodName + ".rule")
        self.addCleanup(rule_file.unlink, missing_ok=True)
        rule_file.write_text("$1\n$1\n" + "$1" * 20 + "\n", encoding="utf-8")

        errors = rule_qa.check_rule_file(rule_file)

        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("too long" in error for error in errors))

    def test_rule_qa_rejects_whitespace(self):
        rule_qa = load_rule_qa_module()
        rule_file = Path(self._testMethodName + ".rule")
        self.addCleanup(rule_file.unlink, missing_ok=True)
        rule_file.write_text("$. $1\n", encoding="utf-8")

        errors = rule_qa.check_rule_file(rule_file)

        self.assertTrue(any("contains whitespace" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

