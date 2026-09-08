<div align="center">

# 🧠 Senior AI Engineering Mentor

**An Elite Multi-Agent Pair Programming & Engineering Mentorship System**

[![CI](https://github.com/tuboa2/senior-ai-mentor/actions/workflows/ci.yml/badge.svg)](https://github.com/tuboa2/senior-ai-mentor/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: 46 Passed](https://img.shields.io/badge/tests-46%20passed-brightgreen.svg)]()
[![Dependencies: Zero External](https://img.shields.io/badge/dependencies-0%20external-success.svg)]()
[![Platform: Linux | macOS | Windows](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()
[![Antigravity CLI: Strictly Required](https://img.shields.io/badge/Antigravity%20CLI-Strictly%20Required-red.svg)]()

*Cultivating independent engineering judgment, first-principles understanding, and mathematical rigor across Machine Learning, Data Science, Software Architecture, and AI Systems.*

[Quick Start (60s)](#-quick-start-in-60-seconds) • [Core Philosophy](#-overview--philosophy) • [Antigravity CLI Policy](#-antigravity-cli-exclusive-design-no-independent-terminal-use) • [Expert Council](#-the-14-member-expert-council) • [Daily Workflows](#-daily-workflows--usage-guide) • [Persistence Modes](#-memory--persistence-modes) • [Installation](#-installation-reference) • [Contributing](CONTRIBUTING.md)

---

</div>

## ⚡ Quick Start in 60 Seconds

Senior AI Engineering Mentor is strictly designed to operate within the **Google Antigravity CLI (`agy`)** environment.

Get up and running in 3 simple steps:

### Step 1: Install the Mentor System

Run one command in your terminal:

```bash
# On Linux & macOS:
curl -fsSL https://raw.githubusercontent.com/tuboa2/senior-ai-mentor/main/install.sh | bash

# On Windows (PowerShell):
irm https://raw.githubusercontent.com/tuboa2/senior-ai-mentor/main/install.ps1 | iex
```

### Step 2: Initialize Your Project Workspace

Navigate to your target project repository and initialize it for Antigravity CLI:

```bash
cd /path/to/my-project
agy-mentor init
```

*This provisions local `.agents/skills/`, sets up `.agents/skills.json`, configures `GEMINI.md` / `AGENTS.md`, and links global persistent memory.*

### Step 3: Start Pair Programming in Antigravity CLI!

Launch Antigravity CLI and chat directly with the 14-member Expert Council:

```bash
# Launch Antigravity CLI in your workspace
agy
```

Inside your `agy` session, interact directly using natural language or slash commands:
- `/council DuckDB vs Spark for 15GB daily log processing`
- `/mentor How should I structure my feature store?`
- `/solve Implement temporal cross-validation in pure Python`
- `/interview system_design`
- `/status`

> [!IMPORTANT]
> **No Independent Terminal Use:** This system is not a standalone terminal REPL. Independent terminal execution outside Antigravity CLI is intentionally blocked to ensure full agentic pair programming capabilities.

---

## 🌟 Overview & Philosophy

Most AI coding assistants act as **passive code generators**, delivering raw solutions that foster cognitive atrophy and developer dependency.

**Senior AI Engineering Mentor** is built on the formal architectural blueprint in [`blueprint.md`](blueprint.md). It pairs you with an **Expert Council of 14 senior engineering personas** orchestrated to challenge assumptions, debate technical trade-offs without false compromise, and adapt pedagogical scaffolding to your real-time **Zone of Proximal Development (ZPD)**.

### Core Tenets

1. **Anti-Dependency Safeguard:** The system monitors the ratio of direct code requests (`L0`) versus conceptual exploration. If direct solutions exceed **65%**, the mentor actively intervenes with Socratic scaffolding to protect your independent problem-solving capability.
2. **Strictly Prohibited Manufactured Consensus:** When engineering trade-offs or incomplete empirical data arise, the council **never** averages opinions into vague compromises. It triggers an **Experiment-First Protocol** detailing precise hypotheses, baselines, variables, and evaluation metrics with confidence intervals, escalating unresolved trade-offs to you.
3. **Adaptive Scaffolding Engine (L0 to L7):** Dynamically adjusts hints to your assessed competency—from production code (`L0`) to first-principles derivations (`L1`), pitfall warnings (`L2`), high-level conceptual nudges (`L3`), structural clues (`L4`), guided Socratic questions (`L5`), isomorphic transfer challenges (`L6`), and adversarial self-critique (`L7`).
4. **Cross-Project Persistent Memory:** Long-term learner state, tracked misconceptions, architectural decisions, and experiment outcomes persist across projects in a unified SQLite database stored in `~/.gemini/antigravity-cli/mentor_data/mentor_memory.db`.
5. **Zero External Dependencies:** Built 100% on the Python standard library (`sqlite3`, `ast`, `re`, `argparse`, `json`, `subprocess`, `dataclasses`, `typing`). Installs anywhere in seconds without dependency conflicts.

---

## 🏛️ System Architecture

```
                                 ┌─────────────────────────────────────────────────────────┐
                                 │            Orchestrator (Principal AI Lead)             │
                                 │    Synthesizes Deliberation & Selects Scaffolding Level │
                                 └────────────────────────────┬────────────────────────────┘
                                                              │
          ┌───────────────────────────────────────────────────┼───────────────────────────────────────────────────┐
          │                                                   │                                                   │
          ▼                                                   ▼                                                   ▼
┌──────────────────┐                                ┌───────────────────┐                               ┌───────────────────┐
│  Expert Council  │                                │Adaptive Scaffold  │                               │ Persistent Memory │
│   (14 Experts)   │                                │     (L0 - L7)     │                               │  & Knowledge Graph│
└─────────┬────────┘                                └─────────┬─────────┘                               └─────────┬─────────┘
          │                                                   │                                                   │
          ▼                                                   ▼                                                   ▼
┌──────────────────┐                                ┌───────────────────┐                               ┌───────────────────┐
│Disagreement &    │                                │  Anti-Dependency  │                               │ Longitudinal Eval │
│Experiment-First  │                                │     Safeguard     │                               │ & Competency Track│
└──────────────────┘                                └───────────────────┘                               └───────────────────┘
```

---

## 👥 The 14-Member Expert Council

Every query is evaluated to dynamically assemble the most relevant specialist panel from 14 permanent roles, plus dynamically spawned domain experts:

| # | Expert Persona | Title | Core Focus |
|:-:|:---|:---|:---|
| 1 | **ML Architect** | Principal ML Architect | End-to-end ML system architecture, model selection, latency budgets, operational simplicity |
| 2 | **ML Research Scientist** | Staff ML Research Scientist | Theoretical foundations, mathematical limits, paper critiques, reproducibility, ablation soundness |
| 3 | **Data Scientist** | Principal Data Scientist | Exploratory data analysis, feature engineering, business framing, domain alignment |
| 4 | **Statistician** | Senior Consulting Statistician | Statistical validity, i.i.d. assumptions, multiple hypothesis testing (BH/Bonferroni), leakage audit |
| 5 | **Math for ML Expert** | Distinguished Applied Mathematician | First-principles intuition (linear algebra, multivariate calculus, optimization, probability) |
| 6 | **Data Engineer** | Staff Data Engineer | ETL/ELT pipelines, distributed processing (DuckDB, Spark), data contracts, schema evolution |
| 7 | **MLOps Engineer** | Staff MLOps Engineer | Model deployment, CI/CD, experiment tracking, model registry, drift monitoring, serving infrastructure |
| 8 | **Software Architect** | Principal Systems Architect | Modularity, clean code, design patterns, separation of concerns, defensive programming |
| 9 | **Performance Engineer** | Staff Performance Engineer | Profiling, GPU/CPU bottlenecks, vectorization, CUDA kernel throughput, memory bandwidth |
| 10 | **AI / LLM Engineer** | Senior Generative AI Engineer | RAG architectures, multi-agent frameworks, tool use, MCP, context window efficiency, eval harnesses |
| 11 | **Code Reviewer** | Principal Code Reviewer | Code correctness, edge cases, defensive typing, test coverage, maintenance risks |
| 12 | **Red Team Reviewer** | Adversarial ML Specialist | Vulnerability probing, edge-case attacks, distribution shifts, security risks, counterexamples |
| 13 | **Pedagogical Mentor** | Lead Pedagogical Mentor | Socratic dialogue, Zone of Proximal Development tracking, metacognition, scaffolding control |
| 14 | **Technical Interviewer**| Staff Technical Interviewer | Realistic technical interviews across System Design, ML Theory, Statistics, and Coding |
| ⚡ | **Dynamic Specialists** | *On-Demand Specialist* | Dynamically spawned for niche domains: Graph ML, Causal Inference, Speech/Audio, RL, Robotics |

### The Orchestrator's Disagreement Protocol
When experts argue opposing positions (e.g., *DuckDB vs. Spark*, *Tree Models vs. Deep Learning*, *Strict Significance vs. Rapid Prototyping*), the response formats an explicit 5-part structure:
- **Positions:** Detailed arguments and theoretical rationale from each participating expert.
- **The Conflict:** Pinpoints the exact trade-off boundary.
- **The Uncertainty:** Identifies missing empirical data or traffic distribution metrics.
- **Experiment-First Protocol:** Concrete hypothesis, baseline, independent variables, and evaluation metrics with statistical confidence intervals.
- **Escalation to User:** Directly challenges you to weigh the trade-off and justify your decision.

---

## 🎓 Adaptive Scaffolding Engine (L0 to L7)

```
[L7] Adversarial Self-Critique  ──► "Find the vulnerability/leakage in your own design"
[L6] Isomorphic Transfer Challenge─► "Solve this same mathematical structure in a new domain"
[L5] Guided Socratic Dialogue   ──► "What invariant must hold when splitting time-series data?"
[L4] Architectural Clue         ──► Outline interfaces, data contracts, and class skeletons
[L3] High-Level Conceptual Hint ──► Conceptual nudge without implementation code
[L2] Pitfall Warning Catalog    ──► Classic traps, common edge cases, and failure modes
[L1] First Principles Derivation──► Theoretical derivation and mathematical mechanics
[L0] Direct Production Solution ──► Full production code and implementation
```

- **Default Behavior:** Operates in **L3–L5 (Socratic Scaffolding)** to foster self-sufficiency.
- **Anti-Dependency Safeguard:** If direct solutions (`L0`) exceed 65% of your recent interactions, an anti-dependency alert triggers, providing conceptual nudges until problem-solving autonomy is restored.

---

## 💻 Daily Workflows & Usage Guide (Antigravity CLI)

All interactions are hosted natively inside your **Google Antigravity CLI (`agy`)** session.

### 1. Antigravity CLI Chat & Slash Commands

When working inside Antigravity CLI (`agy`), simply chat naturally or invoke specialized commands:

| Slash Command | Mode / Level | Example Query & Behavior |
|:---|:---|:---|
| `/solve <query>` | **L0–L2 Direct** | `/solve implement temporal cross-validation in pure Python`<br>*Returns complete production code, first-principles derivation, and pitfall catalog.* |
| `/mentor <query>` | **L3–L5 Socratic** | `/mentor how should I structure my feature store?`<br>*Nudges with architectural clues, invariant checks, and guiding questions.* |
| `/hint <query>` | **Progressive Clue** | `/hint`<br>*Provides the next progressive clue without giving away implementation details.* |
| `/challenge <concept>`| **L6–L7 Challenge** | `/challenge data leakage`<br>*Issues an isomorphic transfer problem or asks you to find vulnerabilities in your own code.* |
| `/council <query>` | **Council Debate** | `/council DuckDB vs Spark for 15GB log processing`<br>*Explicitly convenes the 14-expert council to expose trade-offs and dissent.* |
| `/interview [domain]` | **Mock Interview** | `/interview system_design`<br>*Launches a realistic technical interview session (`system_design`, `ml_theory`, `statistics`, `coding`).* |
| `/status` | **Learner Diagnostics**| `/status`<br>*Displays your competency ratings (0–10), ZPD assessments, and anti-dependency ratio.* |
| `/refine` | **Self-Improvement** | `/refine`<br>*Reviews autonomous optimization proposals generated by the feedback engine (Phase 7).* |
| `/feedback <text>` | **Calibration** | `/feedback SVD signs can vary across numpy and scipy`<br>*Submits corrections to calibrate future mentor guidance.* |

---

### 2. Antigravity CLI Helper Subcommands (`agy-mentor`)

Inside Antigravity CLI, agents and users have access to the `agy-mentor` helper utility for workspace management, audits, and discovery:

```bash
# 1. Initialize current workspace for Antigravity CLI
agy-mentor init

# 2. View learner competency report & anti-dependency metrics
agy-mentor --status

# 3. List installed Tier 0 and Tier 1 skills
agy-mentor --skills

# 4. Security-audit an external skill folder or file with static AST analysis
agy-mentor --audit ~/.gemini/antigravity-cli/skills/my-custom-skill

# 5. Discover and audit candidate Tier 2 skills for a task
agy-mentor --discover "transformer"

# 6. View autonomous self-improvement proposals (Phase 7 feedback)
agy-mentor --refine
```

---

### 🔒 Antigravity CLI Exclusive Design (No Independent Terminal Use)

This system is **strictly engineered for Antigravity CLI (`agy`)**. It does not provide or permit an independent terminal REPL or standalone terminal chatbot.

#### Why Independent Terminal Use is Prohibited:
1. **Agentic Tool Capabilities:** The Orchestrator and 14 Expert Council personas rely on Antigravity's active pair-programming toolchain (direct workspace file editing, multi-agent subagent delegation, background task execution, and interactive diffs).
2. **Context Integrity:** Operating inside `agy` ensures full adherence to `GEMINI.md` directives, `.agents/skills.json` discovery, and real-time AST code verification.
3. **Guardrail Enforcement:** The runtime actively verifies Antigravity CLI environment markers (`ANTIGRAVITY_AGENT`, `AI_AGENT=antigravity`, `ANTIGRAVITY_CONVERSATION_ID`, `JETSKI_APP_DATA_DIR`).

If invoked in an independent terminal outside Antigravity CLI, execution is strictly blocked with the following error:

```
================================================================================
 🚫 ACCESS RESTRICTED: STRICTLY ANTIGRAVITY CLI ONLY                           
================================================================================

Senior AI Engineering Mentor is strictly configured to operate within the
Google Antigravity CLI ('agy') environment. Independent terminal use is disabled.

To interact with the Senior AI Mentor & the 14-member Expert Council:
  1. Open your project repository in your terminal.
  2. Launch Antigravity CLI:
     $ agy

  3. Pair program directly within your Antigravity CLI chat session!
================================================================================
```

---

## 🔄 Memory & Persistence Modes

The mentor uses an 8-table SQLite engine to track your long-term competency progress, past misconceptions, and Architecture Decision Records (ADRs).

### How It Works Across Workspaces:

```
                                ┌──────────────────────────────────────────────┐
                                │   Global Memory Store (~/.gemini/.../db)     │
                                │   - Learner Profile & Competency Ratings     │
                                │   - Knowledge State (EMA Mastery)            │
                                │   - Tracked Misconceptions & Past ADRs       │
                                └──────────────────────┬───────────────────────┘
                                                       │
                     ┌─────────────────────────────────┴─────────────────────────────────┐
                     ▼                                                                   ▼
       ┌───────────────────────────┐                                       ┌───────────────────────────┐
       │   Project A Workspace     │                                       │   Project B Workspace     │
       │   - .agents/skills/       │                                       │   - .agents/skills/       │
       │   - GEMINI.md / AGENTS.md │                                       │   - GEMINI.md / AGENTS.md │
       └───────────────────────────┘                                       └───────────────────────────┘
```

### 1. First-Time Setup on a New Machine (Automatic Zero-State)
When running `agy-mentor init` on a brand-new machine where no global database exists:
- Automatically creates `~/.gemini/antigravity-cli/mentor_data/`.
- Initializes all 11 database schema tables.
- Creates a baseline learner profile (5.0/10 rating across all dimensions, 0 misconceptions, 0% dependency ratio).
- Generates project `.agents/skills/`, `.agents/skills.json`, `GEMINI.md`, and `AGENTS.md`.

### 2. Multiple Projects on the Same Machine (Shared Memory)
When you run `agy-mentor init` in subsequent projects:
- Local configuration files are provisioned for that repo.
- The project **automatically connects to your existing global memory**, carrying forward your mastered concepts, past interview performance, and competency score.

### 3. Isolated Project-Only Mode (Optional)
If you want a specific project to have its own **isolated, brand-new database** without touching or sharing the global store:

```bash
# In your project directory:
export MENTOR_PERSISTENCE=local
agy-mentor init
```

*This creates a local database in `./.mentor_data/mentor_memory.db` dedicated exclusively to that workspace.*

---

## 📦 Installation Reference

### Method 1: Automated One-Command Remote Installer (Recommended)

#### 🐧 Linux & 🍏 macOS
```bash
curl -fsSL https://raw.githubusercontent.com/tuboa2/senior-ai-mentor/main/install.sh | bash
```

#### 🪟 Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/tuboa2/senior-ai-mentor/main/install.ps1 | iex
```

---

### Method 2: Git Clone & Local Script Installation

```bash
# 1. Clone the repository
git clone https://github.com/tuboa2/senior-ai-mentor.git
cd senior-ai-mentor

# 2. Run the installer
# On Linux / macOS:
chmod +x install.sh
./install.sh

# On Windows (PowerShell):
powershell -ExecutionPolicy Bypass -File install.ps1
```

---

### Method 3: Standard Python / Pip Installation

```bash
# 1. Clone and enter the repository
git clone https://github.com/tuboa2/senior-ai-mentor.git
cd senior-ai-mentor

# 2. Install package in editable mode
pip install -e .

# 3. Initialize workspace for Antigravity CLI
agy-mentor init
```

*Note: Ensure `~/.local/bin` is in your `$PATH` (e.g. `export PATH="$HOME/.local/bin:$PATH"` in `~/.bashrc` or `~/.zshrc`).*

---

## 🛡️ Three-Tier Skill Security & Sandboxing

The environment implements a defense-in-depth tiered skill model to prevent malicious code execution, prompt injections, and data exfiltration:

```
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 0: Trusted In-Repo Core Skills (.agents/skills/)                  │
│ Fully audited, deterministic, executed directly in Python runtime      │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 1: Curated Local Pool (~/.gemini/antigravity-cli/skills/)         │
│ Vetted local extensions available for council tasks                    │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 2: Dynamic Task-Based Discovery (AST Audited & Sandboxed)         │
│ Discovered on-demand, static AST scan, prompt injection regex audit,   │
│ isolated subprocess execution with OpenTelemetry GenAI audit logging   │
└────────────────────────────────────────────────────────────────────────┘
```

### Tier 0 Automated Audit Scripts
Located in [`.agents/skills/`](.agents/skills/), these utilities are invoked by Antigravity CLI subagents or in CI/CD pipelines:

#### 1. Statistical Metric Validator (`validate_stats.py`)
Calculates Welch's two-sample t-test, 95% bootstrap confidence intervals, and multiple-testing corrections (Benjamini-Hochberg FDR & Bonferroni):
```bash
python3 .agents/skills/statistical-validation/scripts/validate_stats.py \
  --sample-a 0.85,0.86,0.84,0.87,0.85 \
  --sample-b 0.81,0.82,0.80,0.83,0.81 \
  --p-values 0.01,0.04,0.08,0.20 \
  --correction bh
```

#### 2. AST Data Leakage Detector (`leakage_checker.py`)
Scans Python code AST for `fit_transform` before splits, target column leakage, and temporal inversions:
```bash
python3 .agents/skills/data-leakage-detection/scripts/leakage_checker.py --code pipeline.py
```

#### 3. Production ML Linter (`lint_ml_code.py`)
Lints ML Python files for anti-patterns: `iterrows()`, bare `except:`, missing type annotations, and hardcoded API tokens:
```bash
python3 .agents/skills/python-engineering-standards/scripts/lint_ml_code.py model.py
```

---

## 🧪 Testing & Verification

The codebase includes a comprehensive test suite covering all modules:

```bash
# Run the complete test suite
python3 -m unittest discover tests -v
```

### Test Suite Coverage (46 Tests / 100% Pass Rate):
- `tests/test_antigravity_cli_guard.py`: Antigravity CLI environment verification, runtime guard enforcement, and standalone REPL disablement.
- `tests/test_memory.py`: Profile creation, EMA mastery tracking, misconception lifecycle, ADR logging, anti-dependency ratio calculation.
- `tests/test_knowledge_graph.py`: Prerequisite graph traversal, gap analysis, fuzzy concept matching.
- `tests/test_pedagogy.py`: ZPD level assignment, anti-dependency alert triggers, explicit `/solve` and `/mentor` overrides.
- `tests/test_council_debate.py`: Expert selection heuristics, unmanufactured dissent protocol, Experiment-First protocol generation, dynamic specialist spawning.
- `tests/test_skills_security.py`: Static AST security auditing, prompt injection pattern detection, subprocess sandbox execution, timeout handling.
- `tests/test_orchestrator.py`: End-to-end slash command parsing, multi-agent debate synthesis, status reporting.
- `tests/test_advanced_features.py`: Technical interview simulation, decision rationale evaluation, Tier 2 discovery, OpenTelemetry GenAI audit logging, Phase 7 self-improvement proposals.

---

## 🤝 Community & Contributing

Contributions are welcome! Please review the following resources before contributing:

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Architectural guidelines, coding standards, and branch policies.
- **[Issue Templates](.github/ISSUE_TEMPLATE/)**: Templates for [bug reports](.github/ISSUE_TEMPLATE/bug_report.md) and [feature requests](.github/ISSUE_TEMPLATE/feature_request.md).
- **[Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md)**: Standard checklist for proposing code changes.
- **[GitHub Actions CI](.github/workflows/ci.yml)**: Continuous integration matrix across Linux, macOS, Windows on Python 3.10–3.12.

---

## 📁 Repository Structure

```
senior-ai-mentor/
├── .agents/                          # Agent workspace configuration
│   ├── skills/                       # Tier 0 Core Skills
│   │   ├── adaptive-scaffolding/
│   │   ├── code-review-protocols/
│   │   ├── data-leakage-detection/   # + scripts/leakage_checker.py
│   │   ├── dynamic-specialist-spawner/
│   │   ├── expert-council-deliberation/
│   │   ├── python-engineering-standards/ # + scripts/lint_ml_code.py
│   │   └── statistical-validation/   # + scripts/validate_stats.py
│   └── skills.json                   # Registered skills catalog
├── .github/                          # GitHub community & CI configuration
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml
├── senior_mentor/                    # Core Python Package
│   ├── council/                      # 14 Expert Personas, Debate, Mock Interview
│   │   ├── debate.py
│   │   ├── experts.py
│   │   └── interview.py
│   ├── knowledge/                    # Technical Concept Knowledge Graph
│   │   └── graph.py
│   ├── memory/                       # 8-Table SQLite Persistent Memory
│   │   └── store.py
│   ├── pedagogy/                     # Learner Model (EMA), ZPD, Scaffolding (L0-L7)
│   │   ├── learner_model.py
│   │   └── scaffolding.py
│   ├── self_improvement/             # Phase 7 Feedback & Autonomous Refinement
│   │   └── feedback.py
│   ├── skills/                       # AST Security Auditor, Sandbox & OpenTelemetry Logger
│   │   ├── auditor.py
│   │   ├── manager.py
│   │   └── sandbox.py
│   ├── cli.py                        # Antigravity CLI Guard & Subagent Tool Runner
│   ├── initializer.py                # Workspace 'agy-mentor init' Scaffolding
│   └── orchestrator.py               # Orchestrator & Multi-Agent Deliberator
├── tests/                            # Automated Verification Test Suite (46 Tests)
├── AGENTS.md                         # Multi-Agent pairing directives
├── blueprint.md                      # Complete architectural specification
├── CONTRIBUTING.md                   # Community contribution & PR guidelines
├── GEMINI.md                         # Antigravity Orchestrator directives
├── install.sh                        # Linux & macOS 1-command installer
├── install.ps1                       # Windows PowerShell 1-command installer
├── LICENSE                           # MIT License
├── pyproject.toml                    # Modern PEP 518/621 package metadata
├── setup.py                          # Setuptools entry point
└── README.md                         # Documentation & Getting Started Guide
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
