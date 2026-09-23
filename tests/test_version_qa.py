import importlib.util
import unittest
from pathlib import Path


def load_version_qa_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "version_qa.py"
    spec = importlib.util.spec_from_file_location("version_qa", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VersionQaTests(unittest.TestCase):
    def test_semver_pattern_accepts_project_version(self):
        version_qa = load_version_qa_module()

        self.assertRegex("0.1.0", version_qa.SEMVER)

    def test_current_version_metadata_is_consistent(self):
        version_qa = load_version_qa_module()

        self.assertEqual(version_qa.check_version(), [])


if __name__ == "__main__":
    unittest.main()

