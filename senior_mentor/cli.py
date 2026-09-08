"""Senior AI Engineering Mentor Interactive CLI Interface.

Terminal REPL and command runner for interacting with the Expert Council,
adaptive scaffolding, and learner tracking.
"""

import argparse
from pathlib import Path
import sys
from typing import Optional

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from senior_mentor.orchestrator import Orchestrator, OrchestratorResponse
    from senior_mentor.config import MentorConfig
else:
    from .orchestrator import Orchestrator, OrchestratorResponse
    from .config import MentorConfig

# ANSI terminal formatting
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"

class MentorCLI:
    def __init__(self):
        self.orchestrator = Orchestrator()

    def print_banner(self) -> None:
        print(f"\n{BOLD}{CYAN}================================================================={RESET}")
        print(f"{BOLD}{CYAN}       SENIOR AI ENGINEERING MENTOR & EXPERT COUNCIL             {RESET}")
        print(f"{BOLD}{CYAN}             Adaptive Scaffolding & Engineering Judgment         {RESET}")
        print(f"{BOLD}{CYAN}================================================================={RESET}")
        print(f"{BLUE}Commands: /status, /profile, /council <topic>, /solve <q>, /mentor <q>, /hint, /challenge, /skills, /exit{RESET}\n")

    def format_response(self, resp: OrchestratorResponse) -> str:
        out = []

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
        print(f"\n{BOLD}{CYAN}--- LEARNER PROFILE & COMPETENCY EVALUATION ---{RESET}")
        print(f"Learner: {prof.name} | User ID: {prof.user_id}")
        print(f"Target Role: {BOLD}{prof.target_role}{RESET} | Current Assessed Level: {BOLD}{GREEN}{status['competency_tier']}{RESET}")
        print(f"Overall Competency Rating: {BOLD}{status['overall_score']:.1f}/10.0{RESET}")
        print(f"Anti-Dependency Ratio (Direct vs Socratic): {status['anti_dependency_ratio']:.0%}")
        print(f"Active Knowledge Concepts Tracked: {status['knowledge_count']}")

        print(f"\n{BOLD}Dimension Ratings:{RESET}")
        for ds in status["dimension_scores"]:
            bar = "█" * int(ds.score) + "░" * (10 - int(ds.score))
            print(f"  - {ds.name:45s} [{bar}] {ds.score:.1f}/10")

        if status["unresolved_misconceptions"]:
            print(f"\n{BOLD}{RED}Active Misconceptions to Address:{RESET}")
            for m in status["unresolved_misconceptions"]:
                print(f"  - [{m.concept}] {m.pattern_description} (Seen {m.frequency}x)")

        if status["recommended_learning_plan"]:
            print(f"\n{BOLD}{YELLOW}Targeted Learning Recommendations:{RESET}")
            for plan in status["recommended_learning_plan"]:
                print(f"  • {plan}")
        print()

    def print_skills(self) -> None:
        skills = self.orchestrator.skill_manager.list_tier0_skills()
        print(f"\n{BOLD}{CYAN}--- TIER 0 TRUSTED CORE SKILLS (.agents/skills/) ---{RESET}")
        for s in skills:
            print(f"• {BOLD}{GREEN}{s.name}{RESET} [{s.tier}] - Status: {s.risk_level}")
            print(f"  Description: {s.description}")

        ext = self.orchestrator.skill_manager.list_curated_external_skills(limit=10)
        if ext:
            print(f"\n{BOLD}{CYAN}--- TIER 1 EXTERNAL SKILLS POOL (Preview) ---{RESET}")
            for s in ext:
                print(f"• {BOLD}{YELLOW}{s.name}{RESET} [{s.tier}] - Status: {s.risk_level}")
                print(f"  Description: {s.description}")
        print()

    def run_repl(self) -> None:
        self.print_banner()
        while True:
            try:
                user_input = input(f"{BOLD}{GREEN}mentor> {RESET}").strip()
                if not user_input:
                    continue
                if user_input.lower() in ("/exit", "/quit", "exit", "quit"):
                    print("Exiting Senior Mentor session. Keep building!")
                    break
                elif user_input.lower() == "/status":
                    self.print_status()
                elif user_input.lower() == "/skills":
                    self.print_skills()
                elif user_input.lower() == "/refine":
                    proposals = self.orchestrator.self_improvement.analyze_improvement_opportunities()
                    print(f"\n{BOLD}{CYAN}--- AUTONOMOUS SELF-IMPROVEMENT PROPOSALS (Phase 7) ---{RESET}")
                    if not proposals:
                        print("No pending refinement proposals. System running at target accuracy.")
                    for p in proposals:
                        print(f"• {BOLD}{GREEN}{p.target_component}{RESET} ({p.current_version} -> {p.proposed_version})")
                        print(f"  Rationale: {p.rationale}")
                        print(f"  Suggested Changes: {p.suggested_changes}\n")
                elif user_input.startswith("/feedback "):
                    fb_text = user_input[10:].strip()
                    self.orchestrator.self_improvement.capture_correction(context="User manual feedback", user_correction=fb_text)
                    print(f"{GREEN}✓ Feedback captured in self-improvement loop.{RESET}")
                elif user_input.startswith("/discover "):
                    task = user_input[10:].strip()
                    print(f"\n{BOLD}{CYAN}Searching Tier 2 skills catalog for task: '{task}'...{RESET}")
                    matches = self.orchestrator.skill_manager.discover_skills_for_task(task)
                    if not matches:
                        print("No matching candidate skills found.")
                    for m in matches:
                        badge = f"{GREEN}[SAFE: {m['risk_level']}]{RESET}" if m['is_safe'] else f"{RED}[BLOCKED: {m['risk_level']}]{RESET}"
                        print(f"• {BOLD}{m['name']}{RESET} {badge}")
                        print(f"  Path: {m['path']}")
                        print(f"  Description: {m['description'][:120]}...\n")
                elif user_input.startswith("/audit "):
                    target = user_input[7:].strip()
                    report = self.orchestrator.skill_manager.audit_skill(target)
                    print(f"\nAudit Report for '{report.skill_name}':")
                    print(f"Is Safe: {report.is_safe} | Risk Level: {report.risk_level}")
                    for f in report.findings:
                        print(f"  [{f.severity}] {f.category} in {f.file}:{f.line_number} - {f.message}")
                    print()
                else:
                    resp = self.orchestrator.process_query(user_input)
                    print(self.format_response(resp))
                    print()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                break

def main() -> None:
    parser = argparse.ArgumentParser(description="Senior AI Engineering Mentor CLI.")
    parser.add_argument("--version", action="version", version="senior-mentor 1.0.0")
    parser.add_argument("query", nargs="?", help="One-shot query to ask the mentor")
    parser.add_argument("--status", action="store_true", help="Print learner status and competency report")
    parser.add_argument("--skills", action="store_true", help="List installed Tier 0 and Tier 1 skills")
    parser.add_argument("--audit", help="Run security audit on a skill folder or name")
    parser.add_argument("--discover", help="Discover and audit Tier 2 external skills for a specific task")
    parser.add_argument("--refine", action="store_true", help="View autonomous self-improvement proposals")
    parser.add_argument("--interview", nargs="?", const="system_design", help="Launch mock technical interview")
    parser.add_argument("--init", nargs="?", const=".", help="Initialize a project workspace for Senior Engineering Mentor")
    args = parser.parse_args()

    cli = MentorCLI()

    if args.init or (args.query and args.query.strip().lower() == "init"):
        target_path = Path(args.init if args.init else ".").resolve()
        from .initializer import initialize_workspace
        res = initialize_workspace(target_path, enable_global=True)
        print(f"\n{BOLD}{GREEN}✓ Initialized Senior Engineering Mentor in: {target_path}{RESET}")
        for m in res["messages"]:
            print(f"  • {m}")
        if res["created_files"]:
            print(f"\nCreated/Updated {len(res['created_files'])} configuration files:")
            for f in res["created_files"]:
                print(f"  + {f}")
        print(f"\n{CYAN}This project is now configured for both local Antigravity pair programming and global memory persistence.{RESET}\n")
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
        cli.run_repl()

if __name__ == "__main__":
    main()
