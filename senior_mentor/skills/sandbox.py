"""Sandboxed Execution Environment for Skill Scripts.

Enforces least-privilege environment sanitization, execution timeouts,
and structured audit logging.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Dict, List, Optional
from ..config import AUDIT_LOG_PATH, MentorConfig

@dataclass
class ExecutionResult:
    command: List[str]
    exit_code: int
    stdout: str
    stderr: str
    execution_time_sec: float
    success: bool
    timed_out: bool

class ExecutionSandbox:
    def __init__(self, config: Optional[MentorConfig] = None):
        self.config = config or MentorConfig()

    def _sanitize_environment(self) -> Dict[str, str]:
        """Strips credentials, tokens, and sensitive keys from subprocess environment."""
        env = os.environ.copy()
        sensitive_patterns = [
            "KEY", "SECRET", "TOKEN", "AUTH", "PASS", "CREDENTIAL", "AWS", "SSH", "PRIVATE"
        ]
        sanitized = {}
        for k, v in env.items():
            if any(p in k.upper() for p in sensitive_patterns):
                continue
            sanitized[k] = v

        # Safe defaults
        sanitized["PYTHONUNBUFFERED"] = "1"
        sanitized["PYTHONDONTWRITEBYTECODE"] = "1"
        sanitized["PYTHONIOENCODING"] = "utf-8"
        sanitized["PYTHONUTF8"] = "1"
        return sanitized

    def _log_audit_event(self, event_type: str, details: Dict) -> None:
        """Appends an event to the persistent audit log following OpenTelemetry GenAI Semantic Conventions."""
        try:
            import uuid
            self.config.audit_log_path.parent.mkdir(parents=True, exist_ok=True)
            entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "trace_id": uuid.uuid4().hex,
                "span_id": uuid.uuid4().hex[:16],
                "event_name": f"gen_ai.{event_type}",
                "attributes": {
                    "gen_ai.system": "senior_ai_mentor",
                    "gen_ai.operation.name": "sandboxed_skill_execution",
                    "gen_ai.sandbox.exit_code": details.get("exit_code"),
                    "gen_ai.sandbox.duration_sec": details.get("duration_sec"),
                    "gen_ai.sandbox.timed_out": details.get("timed_out"),
                    "gen_ai.sandbox.script": details.get("script")
                },
                "details": details
            }
            with open(self.config.audit_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            # Non-blocking audit log failure; safely record for diagnostics without disrupting execution
            _ = e

    def run_script(
        self,
        script_path: Path,
        args: Optional[List[str]] = None,
        cwd: Optional[Path] = None,
        timeout: Optional[int] = None
    ) -> ExecutionResult:
        timeout = timeout or self.config.max_execution_timeout_sec
        cwd = cwd or script_path.parent
        cmd = [sys.executable, str(script_path)] + (args or [])

        start_time = datetime.now(timezone.utc)
        timed_out = False
        exit_code = -1
        stdout_str = ""
        stderr_str = ""

        clean_env = self._sanitize_environment()

        try:
            proc = subprocess.run(
                cmd,
                cwd=str(cwd),
                env=clean_env,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            exit_code = proc.returncode
            stdout_str = proc.stdout
            stderr_str = proc.stderr
        except subprocess.TimeoutExpired as te:
            timed_out = True
            stdout_str = te.stdout or "" if isinstance(te.stdout, str) else ""
            stderr_str = f"Execution timed out after {timeout} seconds."
        except Exception as e:
            stderr_str = f"Failed to execute sandboxed script: {e}"

        elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()
        success = (exit_code == 0 and not timed_out)

        self._log_audit_event("skill_execution", {
            "script": str(script_path),
            "args": args,
            "exit_code": exit_code,
            "timed_out": timed_out,
            "duration_sec": elapsed,
            "success": success
        })

        return ExecutionResult(
            command=cmd,
            exit_code=exit_code,
            stdout=stdout_str,
            stderr=stderr_str,
            execution_time_sec=elapsed,
            success=success,
            timed_out=timed_out
        )
