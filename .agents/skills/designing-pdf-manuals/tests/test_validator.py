from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skill.py"

class ValidatorTests(unittest.TestCase):
    def test_valid_package_passes(self):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(ROOT)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("VALID", proc.stdout)

    def test_missing_skill_file_fails(self):
        with tempfile.TemporaryDirectory() as td:
            proc = subprocess.run(
                [sys.executable, str(VALIDATOR), td],
                capture_output=True,
                text=True,
            )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("INVALID", proc.stdout)

if __name__ == "__main__":
    unittest.main()
