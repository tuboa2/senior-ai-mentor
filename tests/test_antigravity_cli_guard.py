"""Unit tests verifying strict Antigravity CLI environment enforcement.

Ensures the Senior AI Engineering Mentor cannot be used as an independent terminal application
and requires the Google Antigravity CLI ('agy') environment.
"""

import os
import subprocess
import sys
import unittest
from unittest.mock import patch
from pathlib import Path

from senior_mentor.config import is_antigravity_cli, enforce_antigravity_cli
from senior_mentor.cli import MentorCLI

class TestAntigravityCLIGuard(unittest.TestCase):
    def test_environment_detection_without_antigravity(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(is_antigravity_cli(strict_test_bypass=True))

    def test_environment_detection_with_antigravity_agent_flag(self):
        with patch.dict(os.environ, {"ANTIGRAVITY_AGENT": "1"}, clear=True):
            self.assertTrue(is_antigravity_cli(strict_test_bypass=True))

    def test_environment_detection_with_ai_agent_flag(self):
        with patch.dict(os.environ, {"AI_AGENT": "antigravity"}, clear=True):
            self.assertTrue(is_antigravity_cli(strict_test_bypass=True))

    def test_environment_detection_with_conversation_id(self):
        with patch.dict(os.environ, {"ANTIGRAVITY_CONVERSATION_ID": "test-uuid-123"}, clear=True):
            self.assertTrue(is_antigravity_cli(strict_test_bypass=True))

    def test_environment_detection_with_explicit_cli_flag(self):
        with patch.dict(os.environ, {"ANTIGRAVITY_CLI": "1"}, clear=True):
            self.assertTrue(is_antigravity_cli(strict_test_bypass=True))

    def test_environment_detection_with_jetski_data_dir(self):
        with patch.dict(os.environ, {"JETSKI_APP_DATA_DIR": "antigravity-cli"}, clear=True):
            self.assertTrue(is_antigravity_cli(strict_test_bypass=True))

    def test_enforce_antigravity_cli_raises_outside_antigravity(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(RuntimeError) as ctx:
                enforce_antigravity_cli(strict_test_bypass=True)
            self.assertIn("strictly configured for use within the Google Antigravity CLI", str(ctx.exception))

    def test_enforce_antigravity_cli_passes_inside_antigravity(self):
        with patch.dict(os.environ, {"ANTIGRAVITY_AGENT": "1"}, clear=True):
            enforce_antigravity_cli(strict_test_bypass=True)

    def test_run_repl_is_strictly_disabled(self):
        cli = MentorCLI()
        with self.assertRaises(RuntimeError) as ctx:
            cli.run_repl()
        self.assertIn("Standalone terminal REPL is disabled", str(ctx.exception))
        self.assertIn("strictly configured for use within Antigravity CLI", str(ctx.exception))

    def test_subprocess_independent_terminal_blocked(self):
        env = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONPATH": str(Path(__file__).resolve().parent.parent)
        }
        res = subprocess.run(
            [sys.executable, "-m", "senior_mentor.cli"],
            env=env,
            capture_output=True,
            text=True
        )
        self.assertEqual(res.returncode, 1)
        self.assertIn("ACCESS RESTRICTED: STRICTLY ANTIGRAVITY CLI ONLY", res.stderr)
        self.assertIn("Independent terminal use is disabled", res.stderr)

    def test_subprocess_inside_antigravity_succeeds(self):
        env = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONPATH": str(Path(__file__).resolve().parent.parent),
            "ANTIGRAVITY_AGENT": "1"
        }
        res = subprocess.run(
            [sys.executable, "-m", "senior_mentor.cli", "--version"],
            env=env,
            capture_output=True,
            text=True
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("senior-mentor 1.0.0 (Antigravity CLI)", res.stdout)

    def test_subprocess_welcome_in_antigravity_without_args(self):
        env = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONPATH": str(Path(__file__).resolve().parent.parent),
            "ANTIGRAVITY_AGENT": "1"
        }
        res = subprocess.run(
            [sys.executable, "-m", "senior_mentor.cli"],
            env=env,
            capture_output=True,
            text=True
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("Antigravity CLI Environment Verified", res.stdout)
        self.assertIn("/council", res.stdout)

if __name__ == "__main__":
    unittest.main()
