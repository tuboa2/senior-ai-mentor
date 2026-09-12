"""Unit tests for the Seamless Dynamic Update and Changelog features."""

import json
from pathlib import Path
import shutil
import tempfile
import unittest
from senior_mentor.changelog import ChangelogManager
from senior_mentor.config import MentorConfig
from senior_mentor.initializer import (
    CURRENT_FRAMEWORK_VERSION,
    check_workspace_update_available,
    get_workspace_manifest,
    initialize_workspace,
    update_workspace,
    write_workspace_manifest
)
from senior_mentor.orchestrator import Orchestrator

class TestDynamicUpdateAndChangelog(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_root = Path(self.temp_dir.name)
        self.changelog_mgr = ChangelogManager()

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_changelog_manager_versions_and_content(self):
        versions = self.changelog_mgr.list_versions()
        self.assertIn("1.2.0", versions)
        self.assertIn("1.1.2", versions)
        self.assertIn("1.1.1", versions)
        self.assertIn("1.1.0", versions)
        self.assertIn("1.0.0", versions)
        self.assertEqual(self.changelog_mgr.get_latest_version(), "1.2.0")

        notes_120 = self.changelog_mgr.get_version_notes("1.2.0")
        self.assertIsNotNone(notes_120)
        self.assertIn("Excalidraw Visual Architecture Engine", notes_120)

        notes_112 = self.changelog_mgr.get_version_notes("1.1.2")
        self.assertIsNotNone(notes_112)
        self.assertIn("ScopeGuard False Positive Eradication", notes_112)

        notes_111 = self.changelog_mgr.get_version_notes("1.1.1")
        self.assertIsNotNone(notes_111)
        self.assertIn("Dynamic Project Context Detection", notes_111)

        notes_110 = self.changelog_mgr.get_version_notes("1.1.0")
        self.assertIsNotNone(notes_110)
        self.assertIn("Scope Guard", notes_110)
        self.assertIn("Terminal & GitHub Changelog System", notes_110)

        # Non-existent version
        missing = self.changelog_mgr.format_terminal_output("9.9.9")
        self.assertIn("not found in changelog", missing)

        # Terminal color formatting
        formatted = self.changelog_mgr.format_terminal_output("1.1.0", use_color=True)
        self.assertIn("1.1.0", formatted)

    def test_check_workspace_update_available_uninitialized(self):
        uninit_dir = self.test_root / "uninit_project"
        uninit_dir.mkdir()
        needs_update, reason, details = check_workspace_update_available(uninit_dir)
        self.assertTrue(needs_update)
        self.assertIn("not yet initialized", reason)

    def test_seamless_dynamic_update_on_old_workspace(self):
        # 1. Simulate an old v1.0.0 workspace
        old_project = self.test_root / "legacy_ml_app"
        old_agents = old_project / ".agents"
        old_skills = old_agents / "skills"
        old_skills.mkdir(parents=True)

        # Create old manifest with v1.0.0
        old_manifest = {
            "framework_version": "1.0.0",
            "initialized_at": "2026-09-08T10:00:00Z",
            "last_updated_at": "2026-09-08T10:00:00Z",
            "synced_skills": ["council", "mentor"],
            "status": "up_to_date"
        }
        with open(old_agents / "manifest.json", "w", encoding="utf-8") as f:
            json.dump(old_manifest, f)

        # Create an old GEMINI.md missing Scope Guard
        (old_project / "GEMINI.md").write_text("# Old GEMINI.md without scope guard\n", encoding="utf-8")
        (old_project / "AGENTS.md").write_text("# Old AGENTS.md\n", encoding="utf-8")

        # Add a custom user skill that must be preserved
        custom_skill_dir = old_skills / "custom-fraud-detection"
        custom_skill_dir.mkdir()
        (custom_skill_dir / "SKILL.md").write_text("# Custom Fraud Detection Skill\n", encoding="utf-8")

        # 2. Verify update is detected
        needs_update, reason, details = check_workspace_update_available(old_project)
        self.assertTrue(needs_update)
        self.assertIn("behind latest release", reason)
        self.assertEqual(details["installed_version"], "1.0.0")

        # 3. Perform seamless update
        res = update_workspace(old_project, force=True, enable_global=False)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["version"], CURRENT_FRAMEWORK_VERSION)
        self.assertIn("update", res["new_skills"])
        self.assertIn("changelog", res["new_skills"])

        # 4. Verify custom skill was preserved
        self.assertTrue((custom_skill_dir / "SKILL.md").exists())
        self.assertIn("Custom Fraud Detection", (custom_skill_dir / "SKILL.md").read_text(encoding="utf-8"))

        # 5. Verify manifest updated
        new_manifest = get_workspace_manifest(old_project)
        self.assertIsNotNone(new_manifest)
        self.assertEqual(new_manifest["framework_version"], CURRENT_FRAMEWORK_VERSION)
        self.assertIn("custom-fraud-detection", new_manifest["synced_skills"])
        self.assertIn("update", new_manifest["synced_skills"])
        self.assertIn("changelog", new_manifest["synced_skills"])

        # 6. Verify GEMINI.md was updated with Scope Guard
        updated_gemini = (old_project / "GEMINI.md").read_text(encoding="utf-8")
        self.assertIn("Scope Guard & Strict Memory Isolation Protocol", updated_gemini)

        # 7. Check that workspace is now reported as up-to-date
        needs_update2, _, _ = check_workspace_update_available(old_project)
        self.assertFalse(needs_update2)

    def test_orchestrator_in_session_changelog_and_update(self):
        db_path = self.test_root / "orch_test.db"
        cfg = MentorConfig(db_path=db_path)
        orchestrator = Orchestrator(cfg)

        # Test /changelog
        resp_log = orchestrator.process_query("/changelog 1.1.0")
        self.assertEqual(resp_log.command_mode, "changelog")
        self.assertFalse(resp_log.is_rejected)
        self.assertIn("1.1.0", resp_log.scaffold.content)

        # Test /update
        target_dir = self.test_root / "test_target_workspace"
        target_dir.mkdir()
        resp_up = orchestrator.process_query(f"/update {target_dir}")
        self.assertEqual(resp_up.command_mode, "update")
        self.assertFalse(resp_up.is_rejected)
        self.assertIn(f"Workspace Synchronized to v{CURRENT_FRAMEWORK_VERSION}", resp_up.scaffold.content)
        self.assertTrue((target_dir / ".agents" / "manifest.json").exists())

if __name__ == "__main__":
    unittest.main()
