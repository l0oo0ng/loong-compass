"""Exercise release identity checks without modifying the manifest."""
import json
import pathlib
import subprocess
import sys
import unittest

SCRIPT = pathlib.Path(__file__).with_name('check_version.py')


class VersionChecks(unittest.TestCase):
    def test_current_version(self):
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True)
        self.assertEqual(result.returncode, 0)

    def test_expected_tag(self):
        manifest = SCRIPT.parent.parent / 'plugins/loong/.codex-plugin/plugin.json'
        version = json.loads(manifest.read_text(encoding='utf-8'))['version']
        result = subprocess.run([sys.executable, str(SCRIPT), '--tag', 'v' + version], capture_output=True)
        self.assertEqual(result.returncode, 0)

    def test_mismatched_tag(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--tag', 'v999.999.999'], capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
