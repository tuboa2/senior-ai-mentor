"""Senior AI Engineering Mentor Interactive CLI Interface.

Terminal REPL and command runner for interacting with the Expert Council,
adaptive scaffolding, and learner tracking.
"""

import argparse
from pathlib import Path
import sys
from typing import Optional

# Ensure UTF-8 output encoding across platforms (specifically Windows console and CI)
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception as _enc_err:
        _ = _enc_err

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from senior_mentor.orchestrator import Orchestrator, OrchestratorResponse
    from senior_mentor.config import MentorConfig, is_antigravity_cli, enforce_antigravity_cli
else:
    from .orchestrator import Orchestrator, OrchestratorResponse
    from .config import MentorConfig, is_antigravity_cli, enforce_antigravity_cli

# ANSI terminal formatting
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"

def print_antigravity_required_error() -> None:
    error_msg = f"""
{BOLD}{RED}================================================================================{RESET}
{BOLD}{RED} 🚫 ACCESS RESTRICTED: STRICTLY ANTIGRAVITY CLI ONLY                           {RESET}
{BOLD}{RED}================================================================================{RESET}

{BOLD}Senior AI Engineering Mentor is strictly configured to operate within the
Google Antigravity CLI ('agy') environment. Independent terminal use is disabled.{RESET}

To interact with the Senior AI Mentor & the 14-member Expert Council:
  1. Open your project repository in your terminal.
  2. Launch Antigravity CLI:
     {BOLD}{CYAN}$ agy{RESET}

  3. Pair program directly within your Antigravity CLI chat session!
     You can chat naturally or use mentor slash commands:
       {GREEN}/council <topic>{RESET}       Deliberate trade-offs without false compromise
       {GREEN}/mentor <query>{RESET}        Request L3-L5 Socratic scaffolding
       {GREEN}/solve <query>{RESET}         Request direct production code & derivations
       {GREEN}/hint{RESET}                  Get progressive concept clues
       {GREEN}/challenge <concept>{RESET}   Attempt isomorphic concept transfer exercises
       {GREEN}/interview [domain]{RESET}    Launch senior mock technical interviews
       {GREEN}/status{RESET}                View competency ratings & ZPD diagnostics

{YELLOW}Note: To initialize this workspace for Antigravity CLI, run:{RESET}
  {CYAN}$ ANTIGRAVITY_CLI=1 python3 -m senior_mentor.cli --init{RESET}
{BOLD}{RED}================================================================================{RESET}
"""
    try:
        print(error_msg, file=sys.stderr)
    except UnicodeEncodeError:
        safe_msg = error_msg.encode("ascii", errors="replace").decode("ascii")
        print(safe_msg, file=sys.stderr)

class MentorCLI:
    def __init__(self, workspace_dir: Optional[Path] = None):
        self.orchestrator = Orchestrator(workspace_dir=workspace_dir)

    def print_context(self, target_path: Optional[Path] = None) -> None:
        path = Path(target_path).resolve() if target_path else self.orchestrator.workspace_dir
        ctx = self.orchestrator.context_detector.detect(path)
        out = [
            f"\n{BOLD}{CYAN}================================================================={RESET}",
            f"{BOLD}{CYAN}     PROJECT CONTEXT & CONDITIONAL MEMORY INSPECTION             {RESET}",
            f"{BOLD}{CYAN}================================================================={RESET}",
            f"{BOLD}Workspace Directory:{RESET} `{path}`",
            (f"{BOLD}Related to AI/ML/Data Science:{RESET} {GREEN}YES (Active Engineering Domain){RESET}"
             if ctx.is_related else
             f"{BOLD}Related to AI/ML/Data Science:{RESET} {RED}NO (Unrelated / Non-Technical){RESET}"),
            f"{BOLD}Project Classification:{RESET} {CYAN}{ctx.project_type}{RESET}",
            f"{BOLD}Detection Confidence:{RESET} {BOLD}{int(ctx.confidence * 100)}%{RESET}",
            f"{BOLD}Detected Domains:{RESET} {', '.join(ctx.detected_domains) if ctx.detected_domains else 'None'}",
            f"{BOLD}Detected Frameworks:{RESET} " + (f"{GREEN}{', '.join(ctx.detected_frameworks)}{RESET}" if ctx.detected_frameworks else "None"),
            "",
            f"{BOLD}Senior AI Mentor Memory Status:{RESET} " + (
                f"{BOLD}{GREEN}🔓 RETRIEVED & MODIFICATIONS AUTHORIZED{RESET}\n  (Learner progress loaded; live updates to knowledge state and project memory are active.)"
                if ctx.modification_allowed else
                f"{BOLD}{YELLOW}🔒 LOCKED (READ-ONLY) - ZERO MUTATIONS PERMITTED{RESET}\n  (Mentor memory is protected against corruption. Queries are answered without altering progress records.)"
            ),
            ""
        ]
        if ctx.evidence:
            out.append(f"{BOLD}Detection Evidence Found:{RESET}")
            for ev in ctx.evidence:
                out.append(f"  • {ev}")
            out.append("")
        out.append(f"{BOLD}{CYAN}================================================================={RESET}\n")
        try:
            print("\n".join(out))
        except UnicodeEncodeError:
            print("\n".join(out).encode("ascii", errors="replace").decode("ascii"))

    def print_antigravity_welcome(self) -> None:
        ctx = self.orchestrator.project_context
        mem_status = f"{GREEN}🔓 Memory RETRIEVED & MODIFIABLE{RESET}" if ctx.modification_allowed else f"{YELLOW}🔒 Memory LOCKED (READ-ONLY){RESET}"
        welcome_lines = [
            f"\n{BOLD}{CYAN}================================================================={RESET}",
            f"{BOLD}{CYAN}       SENIOR AI ENGINEERING MENTOR & EXPERT COUNCIL             {RESET}",
            f"{BOLD}{CYAN}              (Strictly Antigravity CLI Environment)             {RESET}",
            f"{BOLD}{CYAN}================================================================={RESET}",
            f"{GREEN}✓ Antigravity CLI Environment Verified.{RESET}",
            f"{BOLD}Active Workspace Context:{RESET} {CYAN}{ctx.project_type}{RESET} | {mem_status}",
            f"{CYAN}You do not need a separate terminal REPL. Chat directly in this Antigravity CLI session!{RESET}\n",
            f"{BOLD}Active Mentorship Slash Commands in agy:{RESET}",
            f"  {GREEN}/council <topic>{RESET}      - Deliberate technical trade-offs (14 expert personas)",
            f"  {GREEN}/mentor <query>{RESET}       - Adaptive Socratic scaffolding (L3-L5)",
            f"  {GREEN}/solve <query>{RESET}        - Direct production implementation (L0-L2)",
            f"  {GREEN}/hint{RESET}                 - Progressive clue without spoilers",
            f"  {GREEN}/challenge <concept>{RESET}  - Isomorphic concept challenge",
            f"  {GREEN}/interview [domain]{RESET}   - Senior mock technical interview",
            f"  {GREEN}/context [path]{RESET}       - Inspect detected project context & memory lock status",
            f"  {GREEN}/status{RESET}               - Learner profile & competency score",
            f"  {GREEN}/refine{RESET}               - View autonomous self-improvement proposals",
            f"  {GREEN}/update{RESET}               - Dynamically update workspace to latest release",
            f"  {GREEN}/changelog [ver]{RESET}      - View version history & release notes",
            f"\n{BOLD}CLI Helper Flags for Antigravity Agents:{RESET}",
            f"  --context [path]  Inspect detected project context & memory lock status",
            f"  --status          Display current competency metrics",
            f"  --skills          List installed Tier 0 & Tier 1 skills",
            f"  --audit <path>    Run AST security audit on a skill",
            f"  --discover <task> Search and audit external Tier 2 skills",
            f"  --init [path]     Initialize workspace for Antigravity CLI",
            f"  --update [path]   Dynamically update project scope to latest release",
            f"  --changelog [ver] View release notes and version history in terminal",
            ""
        ]
        welcome_text = "\n".join(welcome_lines)
        try:
            print(welcome_text)
        except UnicodeEncodeError:
            print(welcome_text.encode("ascii", errors="replace").decode("ascii"))

    def format_response(self, resp: OrchestratorResponse) -> str:
        out = []

        if getattr(resp, "is_rejected", False):
            out.append(f"\n{BOLD}{RED}================================================================{RESET}")
            out.append(f"{BOLD}{RED} 🚫 QUERY REJECTED: OUTSIDE SENIOR AI MENTOR SCOPE               {RESET}")
            out.append(f"{BOLD}{RED}================================================================{RESET}")
            out.append(f"\n{YELLOW}{resp.scaffold.content}{RESET}")
            if resp.scaffold.next_action_prompt:
                out.append(f"\n{BOLD}{CYAN}Actionable Prompt:{RESET} {resp.scaffold.next_action_prompt}")
            out.append(f"\n{BOLD}{RED}================================================================{RESET}")
            return "\n".join(out)

        if resp.command_mode == "context":
            return resp.scaffold.content

        if resp.project_context:
            if resp.project_context.is_related:
                out.append(f"\n{CYAN}[Project Context: {resp.project_context.project_type} | Memory: RETRIEVED & MODIFIABLE]{RESET}")
            else:
                out.append(f"\n{YELLOW}[Project Context: Unrelated ({resp.project_context.project_type}) | Memory: LOCKED (READ-ONLY)]{RESET}")

        if resp.anti_dependency_warning:
            out.append(f"\n{YELLOW}{resp.anti_dependency_warning}{RESET}")

        if resp.interview_question:
            iq = resp.interview_question
            out.append(f"\n{BOLD}{CYAN}================================================================{RESET}")
            out.append(f"{BOLD}{CYAN}🎤 MOCK TECHNICAL INTERVIEW: {iq.title} [{iq.level} Level]{RESET}")
            out.append(f"{BOLD}{CYAN}================================================================{RESET}")
            out.append(f"\n{BOLD}Scenario:{RESET}\n{iq.scenario}\n")
            out.append(f"{BOLD}Probing Follow-Up Dimensions:{RESET}")
            for p in iq.probing_questions:
                out.append(f"  • {p}")
            out.append(f"\n{CYAN}👉 State your architectural approach and justify trade-offs.{RESET}")
            return "\n".join(out)

        if resp.zpd_status and resp.matched_concept:
            out.append(f"\n{MAGENTA}[Knowledge Graph: '{resp.matched_concept}'] ZPD: {resp.zpd_status.zone} | Recommended Level: L{resp.zpd_status.recommended_level}{RESET}")
            if resp.zpd_status.unmet_prerequisites:
                out.append(f"{RED}⚠️ Missing Prerequisites: {', '.join(resp.zpd_status.unmet_prerequisites)}{RESET}")

        # If Expert Council deliberated
        if resp.debate_synthesis:
            deb = resp.debate_synthesis
            out.append(f"\n{BOLD}{CYAN}----------------------------------------------------------------{RESET}")
            out.append(f"{BOLD}{CYAN}⚖️  EXPERT COUNCIL DELIBERATION (Participants: {', '.join(deb.participating_experts)}){RESET}")
            out.append(f"{BOLD}{CYAN}----------------------------------------------------------------{RESET}")

            for p in deb.positions:
                out.append(f"{BOLD}{GREEN}• {p['role']} ({p['title']}):{RESET} {p['position']}")
                out.append(f"  {BLUE}Rationale:{RESET} {p['rationale']}")

            if deb.has_unresolved_disagreement:
                out.append(f"\n{BOLD}{RED}⚡ THE CONFLICT (Unmanufactured Dissent):{RESET}")
                out.append(f"  {deb.conflict_statement}")
                out.append(f"\n{BOLD}{YELLOW}❓ THE UNCERTAINTY:{RESET}")
                out.append(f"  {deb.uncertainty_statement}")

                if deb.experiment_design:
                    exp = deb.experiment_design
                    out.append(f"\n{BOLD}{MAGENTA}🧪 EXPERIMENT-FIRST PROTOCOL:{RESET} {exp.title}")
                    out.append(f"  - Hypothesis: {exp.hypothesis}")
                    out.append(f"  - Baseline: {exp.baseline}")
                    out.append(f"  - Independent Variables: {', '.join(exp.independent_variables)}")
                    out.append(f"  - Metrics: {', '.join(exp.evaluation_metrics)}")
                    out.append(f"  - Expected Outcome: {exp.expected_outcomes}")

                out.append(f"\n{BOLD}{CYAN}👉 ESCALATION TO YOU:{RESET}")
                out.append(f"  {deb.escalation_question}")
            else:
                out.append(f"\n{GREEN}✓ Consensus:{RESET} {deb.consensus_summary}")

        # Pedagogical Scaffolding
        scaff = resp.scaffold
        out.append(f"\n{BOLD}{YELLOW}----------------------------------------------------------------{RESET}")
        out.append(f"{BOLD}{YELLOW}🎓 PEDAGOGICAL SCAFFOLDING [{scaff.tier} -> Level {scaff.level}: {scaff.level_name}]{RESET}")
        out.append(f"{BOLD}{YELLOW}----------------------------------------------------------------{RESET}")
        out.append(f"{scaff.content}")
        if scaff.next_action_prompt:
            out.append(f"\n{BOLD}{CYAN}Actionable Prompt:{RESET} {scaff.next_action_prompt}")

        return "\n".join(out)

    def print_status(self) -> None:
        status = self.orchestrator.get_learner_status()
        prof = status["profile"]
        header = f"""
{BOLD}{CYAN}--- LEARNER PROFILE & COMPETENCY EVALUATION ---{RESET}
Learner: {prof.name} | User ID: {prof.user_id}
Target Role: {BOLD}{prof.target_role}{RESET} | Current Assessed Level: {BOLD}{GREEN}{status['competency_tier']}{RESET}
Overall Competency Rating: {BOLD}{status['overall_score']:.1f}/10.0{RESET}
Anti-Dependency Ratio (Direct vs Socratic): {status['anti_dependency_ratio']:.0%}
Active Knowledge Concepts Tracked: {status['knowledge_count']}

{BOLD}Dimension Ratings:{RESET}"""
        try:
            print(header)
        except UnicodeEncodeError:
            print(header.encode("ascii", errors="replace").decode("ascii"))

        for ds in status["dimension_scores"]:
            filled = int(ds.score)
            empty = 10 - filled
            try:
                bar = f"{GREEN}{'█' * filled}\033[90m{'█' * empty}{RESET}"
                print(f"  - {ds.name:45s} [{bar}] {ds.score:.1f}/10")
            except UnicodeEncodeError:
                bar = f"[{'=' * filled}{'-' * empty}]"
                print(f"  - {ds.name:45s} {bar} {ds.score:.1f}/10")

        if status["unresolved_misconceptions"]:
            print(f"\n{BOLD}{RED}Active Misconceptions to Address:{RESET}")
            for m in status["unresolved_misconceptions"]:
                print(f"  - [{m.concept}] {m.pattern_description} (Seen {m.frequency}x)")

        if status["recommended_learning_plan"]:
            print(f"\n{BOLD}{YELLOW}Targeted Learning Recommendations:{RESET}")
            for plan in status["recommended_learning_plan"]:
                try:
                    print(f"  • {plan}")
                except UnicodeEncodeError:
                    print(f"  - {plan}")
        print()

    def print_skills(self) -> None:
        skills = self.orchestrator.skill_manager.list_tier0_skills()
        out = [f"\n{BOLD}{CYAN}--- TIER 0 TRUSTED CORE SKILLS (.agents/skills/) ---{RESET}"]
        for s in skills:
            out.append(f"• {BOLD}{GREEN}{s.name}{RESET} [{s.tier}] - Status: {s.risk_level}")
            out.append(f"  Description: {s.description}")

        ext = self.orchestrator.skill_manager.list_curated_external_skills(limit=10)
        if ext:
            out.append(f"\n{BOLD}{CYAN}--- TIER 1 EXTERNAL SKILLS POOL (Preview) ---{RESET}")
            for s in ext:
                out.append(f"• {BOLD}{YELLOW}{s.name}{RESET} [{s.tier}] - Status: {s.risk_level}")
                out.append(f"  Description: {s.description}")
        out.append("")
        skills_text = "\n".join(out)
        try:
            print(skills_text)
        except UnicodeEncodeError:
            print(skills_text.encode("ascii", errors="replace").decode("ascii"))

    def run_repl(self) -> None:
        """Disabled: Standalone terminal REPL is not permitted."""
        raise RuntimeError(
            "Standalone terminal REPL is disabled. Senior AI Engineering Mentor "
            "is strictly configured for use within Antigravity CLI ('agy'). "
            "Launch 'agy' in your terminal and pair program directly within your Antigravity session."
        )

def main() -> None:
    # Check if this is an initialization, update, changelog, or context inspection command
    is_init = ("--init" in sys.argv or (len(sys.argv) > 1 and sys.argv[1].lower() == "init"))
    is_update = ("--update" in sys.argv or (len(sys.argv) > 1 and sys.argv[1].lower() == "update"))
    is_changelog = ("--changelog" in sys.argv or (len(sys.argv) > 1 and sys.argv[1].lower() == "changelog"))
    is_context = ("--context" in sys.argv or (len(sys.argv) > 1 and sys.argv[1].lower() == "context"))

    if not is_antigravity_cli() and not (is_init or is_update or is_changelog or is_context):
        print_antigravity_required_error()
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1].lower() == "init":
        target_path = Path(sys.argv[2] if len(sys.argv) > 2 else ".").resolve()
        try:
            from .initializer import initialize_workspace
        except (ImportError, ValueError):
            from senior_mentor.initializer import initialize_workspace
        res = initialize_workspace(target_path, enable_global=True)
        print(f"\n{BOLD}{GREEN}✓ Initialized Senior Engineering Mentor for Antigravity CLI in: {target_path}{RESET}")
        for m in res["messages"]:
            print(f"  • {m}")
        if res["created_files"]:
            print(f"\nCreated/Updated {len(res['created_files'])} configuration files:")
            for f in res["created_files"]:
                print(f"  + {f}")
        print(f"\n{CYAN}This project is now configured for Antigravity CLI pair programming.{RESET}")
        print(f"{BOLD}Run {GREEN}agy{RESET}{BOLD} to begin!{RESET}\n")
        return

    if len(sys.argv) > 1 and sys.argv[1].lower() == "update":
        target_path = Path(sys.argv[2] if len(sys.argv) > 2 else ".").resolve()
        try:
            from .initializer import update_workspace
        except (ImportError, ValueError):
            from senior_mentor.initializer import update_workspace
        res = update_workspace(target_path, force=True, enable_global=True)
        print(f"\n{BOLD}{GREEN}✓ Dynamic Workspace Update Complete [v{res['version']}]{RESET}")
        print(f"Target Directory: {target_path}")
        if res.get("new_skills"):
            print(f"\n{BOLD}Newly Installed Core Skills:{RESET}")
            for s in res["new_skills"]:
                print(f"  + /{s}")
        if res.get("updated_skills"):
            print(f"\n{BOLD}Refreshed Core Skills:{RESET}")
            for s in res["updated_skills"]:
                print(f"  * /{s}")
        if res.get("updated_files"):
            print(f"\nUpdated {len(res['updated_files'])} Configuration & Directive Files:")
            for f in res["updated_files"]:
                print(f"  ~ {f}")
        for m in res.get("messages", []):
            print(f"  • {m}")
        print(f"\n{CYAN}Your project scope is now fully updated to v{res['version']}!{RESET}")
        print(f"{BOLD}Run {GREEN}agy{RESET}{BOLD} to begin!{RESET}\n")
        return

    if len(sys.argv) > 1 and sys.argv[1].lower() == "changelog":
        target_ver = sys.argv[2] if len(sys.argv) > 2 else None
        try:
            from .changelog import ChangelogManager
        except (ImportError, ValueError):
            from senior_mentor.changelog import ChangelogManager
        cm = ChangelogManager()
        print(cm.format_terminal_output(target_ver, use_color=True))
        return

    if len(sys.argv) > 1 and sys.argv[1].lower() == "context":
        target_path = Path(sys.argv[2] if len(sys.argv) > 2 else ".").resolve()
        cli = MentorCLI(workspace_dir=target_path)
        cli.print_context(target_path)
        return

    parser = argparse.ArgumentParser(
        description="Senior AI Engineering Mentor (Strictly Antigravity CLI Only)."
    )
    parser.add_argument("--version", action="version", version="senior-mentor 1.1.1 (Antigravity CLI)")
    parser.add_argument("query", nargs="?", help="One-shot query for Antigravity subagent invocation")
    parser.add_argument("--status", action="store_true", help="Print learner status and competency report")
    parser.add_argument("--context", nargs="?", const=".", help="Inspect detected project context and memory lock status")
    parser.add_argument("--skills", action="store_true", help="List installed Tier 0 and Tier 1 skills")
    parser.add_argument("--audit", help="Run security audit on a skill folder or name")
    parser.add_argument("--discover", help="Discover and audit Tier 2 external skills for a specific task")
    parser.add_argument("--refine", action="store_true", help="View autonomous self-improvement proposals")
    parser.add_argument("--interview", nargs="?", const="system_design", help="Launch mock technical interview")
    parser.add_argument("--init", nargs="?", const=".", help="Initialize a project workspace for Antigravity CLI")
    parser.add_argument("--update", nargs="?", const=".", help="Dynamically update workspace skills, directives, and manifests to latest release")
    parser.add_argument("--changelog", nargs="?", const="", help="View version history and release notes in terminal")
    args = parser.parse_args()

    cli = MentorCLI()

    if args.init:
        target_path = Path(args.init).resolve()
        try:
            from .initializer import initialize_workspace
        except (ImportError, ValueError):
            from senior_mentor.initializer import initialize_workspace
        res = initialize_workspace(target_path, enable_global=True)
        print(f"\n{BOLD}{GREEN}✓ Initialized Senior Engineering Mentor for Antigravity CLI in: {target_path}{RESET}")
        for m in res["messages"]:
            print(f"  • {m}")
        if res["created_files"]:
            print(f"\nCreated/Updated {len(res['created_files'])} configuration files:")
            for f in res["created_files"]:
                print(f"  + {f}")
        print(f"\n{CYAN}This project is now configured for Antigravity CLI pair programming.{RESET}")
        print(f"{BOLD}Run {GREEN}agy{RESET}{BOLD} to begin!{RESET}\n")
        return
    elif args.update is not None:
        target_path = Path(args.update).resolve()
        try:
            from .initializer import update_workspace
        except (ImportError, ValueError):
            from senior_mentor.initializer import update_workspace
        res = update_workspace(target_path, force=True, enable_global=True)
        print(f"\n{BOLD}{GREEN}✓ Dynamic Workspace Update Complete [v{res['version']}]{RESET}")
        print(f"Target Directory: {target_path}")
        if res.get("new_skills"):
            print(f"\n{BOLD}Newly Installed Core Skills:{RESET}")
            for s in res["new_skills"]:
                print(f"  + /{s}")
        if res.get("updated_skills"):
            print(f"\n{BOLD}Refreshed Core Skills:{RESET}")
            for s in res["updated_skills"]:
                print(f"  * /{s}")
        if res.get("updated_files"):
            print(f"\nUpdated {len(res['updated_files'])} Configuration & Directive Files:")
            for f in res["updated_files"]:
                print(f"  ~ {f}")
        for m in res.get("messages", []):
            print(f"  • {m}")
        print(f"\n{CYAN}Your project scope is now fully updated to v{res['version']}!{RESET}")
        print(f"{BOLD}Run {GREEN}agy{RESET}{BOLD} to begin!{RESET}\n")
        return
    elif args.changelog is not None:
        target_ver = args.changelog if args.changelog else None
        try:
            from .changelog import ChangelogManager
        except (ImportError, ValueError):
            from senior_mentor.changelog import ChangelogManager
        cm = ChangelogManager()
        print(cm.format_terminal_output(target_ver, use_color=True))
        return
    elif args.context is not None:
        target_path = Path(args.context).resolve()
        cli = MentorCLI(workspace_dir=target_path)
        cli.print_context(target_path)
        return
    elif args.status:
        cli.print_status()
    elif args.skills:
        cli.print_skills()
    elif args.discover:
        print(f"\n--- TIER 2 DYNAMIC DISCOVERY: '{args.discover}' ---")
        matches = cli.orchestrator.skill_manager.discover_skills_for_task(args.discover)
        if not matches:
            print("No matching candidate skills found.")
        for m in matches:
            status = "SAFE (TRUSTED)" if m['is_safe'] else f"BLOCKED ({m['risk_level']})"
            print(f"• {m['name']} [{status}]")
            print(f"  Path: {m['path']}")
            print(f"  Description: {m['description'][:120]}...\n")
    elif args.refine:
        proposals = cli.orchestrator.self_improvement.analyze_improvement_opportunities()
        print(f"\n--- AUTONOMOUS SELF-IMPROVEMENT PROPOSALS (Phase 7) ---")
        if not proposals:
            print("No pending refinement proposals. System running at target accuracy.")
        for p in proposals:
            print(f"• {p.target_component} ({p.current_version} -> {p.proposed_version})")
            print(f"  Rationale: {p.rationale}")
            print(f"  Suggested Changes: {p.suggested_changes}\n")
    elif args.interview:
        resp = cli.orchestrator.process_query(f"/interview {args.interview}")
        print(cli.format_response(resp))
    elif args.audit:
        report = cli.orchestrator.skill_manager.audit_skill(args.audit)
        print(f"\nAudit Report for '{report.skill_name}':")
        print(f"Is Safe: {report.is_safe} | Risk Level: {report.risk_level}")
        for f in report.findings:
            print(f"  [{f.severity}] {f.category} in {f.file}:{f.line_number} - {f.message}")
    elif args.query:
        resp = cli.orchestrator.process_query(args.query)
        print(cli.format_response(resp))
    else:
        cli.print_antigravity_welcome()

if __name__ == "__main__":
    main()
