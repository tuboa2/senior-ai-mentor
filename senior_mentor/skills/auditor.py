"""Security Auditor for AI Agent Skills.

Defends against ClawHavoc campaigns, supply-chain poisoning, prompt injection
in SKILL.md, and malicious code execution vectors (CVE-2025-59536 patterns).
"""

from dataclasses import dataclass, field
import ast
import re
from pathlib import Path
from typing import List, Tuple

@dataclass
class AuditFinding:
    severity: str  # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    category: str
    message: str
    file: str
    line_number: int = 0

@dataclass
class SkillAuditReport:
    skill_path: str
    skill_name: str
    is_safe: bool
    risk_level: str  # "TRUSTED", "ELEVATED", "BLOCKED"
    findings: List[AuditFinding] = field(default_factory=list)

class SkillSecurityAuditor:
    # Dangerous shell & system patterns
    DANGEROUS_CODE_PATTERNS = [
        (re.compile(r"rm\s+-rf\s+[/~]", re.IGNORECASE), "CRITICAL", "Destructive recursive file deletion"),
        (re.compile(r"curl\s+.*\|\s*(sh|bash)", re.IGNORECASE), "CRITICAL", "Piped remote shell execution"),
        (re.compile(r"(nc|netcat|ncat)\s+.*-e", re.IGNORECASE), "CRITICAL", "Reverse shell attempt"),
        (re.compile(r"(cat|grep)\s+.*(\.env|\.ssh|id_rsa|\.aws|credentials)", re.IGNORECASE), "CRITICAL", "Credential harvesting attempt"),
        (re.compile(r"chmod\s+[0-7]*777", re.IGNORECASE), "HIGH", "Insecure wide-open permissions"),
        (re.compile(r"eval\s*\(", re.IGNORECASE), "HIGH", "Unsafe dynamic evaluation"),
        (re.compile(r"os\.system\s*\(", re.IGNORECASE), "MEDIUM", "Unsanitized os.system call")
    ]

    # Prompt injection patterns in SKILL.md
    PROMPT_INJECTION_PATTERNS = [
        (re.compile(r"ignore\s+(all\s+)?(previous|prior)\s+(instructions|directives|rules)", re.IGNORECASE), "CRITICAL", "Instruction override prompt injection"),
        (re.compile(r"you\s+are\s+now\s+in\s+(developer|unrestricted|god)\s+mode", re.IGNORECASE), "CRITICAL", "Jailbreak mode declaration"),
        (re.compile(r"reveal\s+(system\s+prompt|all\s+secrets|api\s+keys)", re.IGNORECASE), "HIGH", "System secret extraction attempt"),
        (re.compile(r"[\u200B-\u200D\uFEFF]", re.UNICODE), "HIGH", "Hidden zero-width characters detected")
    ]

    def audit_skill_directory(self, skill_dir: Path) -> SkillAuditReport:
        skill_name = skill_dir.name
        findings: List[AuditFinding] = []

        if not skill_dir.exists() or not skill_dir.is_dir():
            return SkillAuditReport(str(skill_dir), skill_name, False, "BLOCKED", [
                AuditFinding("CRITICAL", "Filesystem", f"Directory {skill_dir} does not exist", str(skill_dir))
            ])

        # 1. Audit SKILL.md
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            findings.append(AuditFinding("HIGH", "Specification", "Missing required SKILL.md file", str(skill_md)))
        else:
            findings.extend(self._audit_markdown(skill_md))

        # 2. Audit all python and shell scripts
        for script_path in skill_dir.rglob("*"):
            if script_path.is_file():
                if script_path.suffix == ".py":
                    findings.extend(self._audit_python_file(script_path))
                elif script_path.suffix in [".sh", ".bash"]:
                    findings.extend(self._audit_shell_file(script_path))

        # Determine overall safety
        has_critical = any(f.severity == "CRITICAL" for f in findings)
        has_high = any(f.severity == "HIGH" for f in findings)

        if has_critical:
            risk = "BLOCKED"
            is_safe = False
        elif has_high:
            risk = "ELEVATED"
            is_safe = False
        else:
            risk = "TRUSTED"
            is_safe = True

        return SkillAuditReport(
            skill_path=str(skill_dir),
            skill_name=skill_name,
            is_safe=is_safe,
            risk_level=risk,
            findings=findings
        )

    def _audit_markdown(self, path: Path) -> List[AuditFinding]:
        findings = []
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()

            # Verify YAML Frontmatter
            if not content.startswith("---"):
                findings.append(AuditFinding("MEDIUM", "Metadata", "Missing YAML frontmatter block", str(path), 1))

            for line_no, line in enumerate(lines, 1):
                for pattern, severity, msg in self.PROMPT_INJECTION_PATTERNS:
                    if pattern.search(line):
                        findings.append(AuditFinding(severity, "Prompt Security", msg, str(path), line_no))

        except Exception as e:
            findings.append(AuditFinding("HIGH", "I/O", f"Failed to read markdown file: {e}", str(path)))
        return findings

    def _audit_shell_file(self, path: Path) -> List[AuditFinding]:
        findings = []
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()
            for line_no, line in enumerate(lines, 1):
                for pattern, severity, msg in self.DANGEROUS_CODE_PATTERNS:
                    if pattern.search(line):
                        findings.append(AuditFinding(severity, "Dangerous Shell Command", msg, str(path), line_no))
        except Exception as e:
            findings.append(AuditFinding("HIGH", "I/O", f"Failed to read shell script: {e}", str(path)))
        return findings

    def _audit_python_file(self, path: Path) -> List[AuditFinding]:
        findings = []
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()

            # Regex scan
            for line_no, line in enumerate(lines, 1):
                for pattern, severity, msg in self.DANGEROUS_CODE_PATTERNS:
                    if pattern.search(line):
                        findings.append(AuditFinding(severity, "Dangerous Code Pattern", msg, str(path), line_no))

            # AST Analysis
            try:
                tree = ast.parse(content, filename=str(path))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        func_name = ""
                        if isinstance(node.func, ast.Name):
                            func_name = node.func.id
                        elif isinstance(node.func, ast.Attribute):
                            func_name = node.func.attr
                        
                        if func_name in ("exec", "eval"):
                            findings.append(AuditFinding("HIGH", "AST Security", f"Dynamic execution with '{func_name}'", str(path), node.lineno))
            except SyntaxError as se:
                findings.append(AuditFinding("MEDIUM", "AST Syntax", f"Syntax error in python file: {se}", str(path)))

        except Exception as e:
            findings.append(AuditFinding("HIGH", "I/O", f"Failed to inspect python file: {e}", str(path)))
        return findings
