<div align="center">

# 🧠 Senior AI Engineering Mentor

**An Elite Multi-Agent Pair Programming & Engineering Mentorship System**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 34 Passed](https://img.shields.io/badge/tests-34%20passed-brightgreen.svg)]()
[![Dependencies: Zero External](https://img.shields.io/badge/dependencies-0%20external-success.svg)]()
[![Platform: Linux | macOS | Windows](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()
[![Antigravity AI Compatible](https://img.shields.io/badge/Antigravity%20AI-Compatible-purple.svg)]()

*Cultivating independent engineering judgment, first-principles understanding, and mathematical rigor across Machine Learning, Data Science, Software Architecture, and AI Systems.*

[Architecture](#-system-architecture) • [Expert Council](#-the-14-member-expert-council) • [Installation](#-quickstart--installation) • [Workspace Setup](#-cross-project-persistence--init) • [CLI & Slash Commands](#-cli--slash-commands-reference) • [Skill Security](#-three-tier-skill-security) • [Verification](#-testing--verification)

---

</div>

## 🌟 Overview & Philosophy

Most AI coding assistants act as **passive code generators**, giving away direct code solutions that foster cognitive atrophy and developer dependency.

**Senior AI Engineering Mentor** is built on the formal architectural blueprint in [`blueprint.md`](blueprint.md). It transforms your development environment into an elite engineering organization guided by an **Expert Council of 14 senior engineering personas** and an adaptive pedagogical mentor.

### Core Tenets

1. **Anti-Dependency Safeguard:** The system tracks the ratio of direct code requests versus conceptual exploration. If direct solutions exceed **65%**, the mentor actively intervenes with Socratic scaffolding to protect your long-term problem-solving autonomy.
2. **Strictly Prohibited Manufactured Consensus:** When engineering trade-offs or incomplete empirical data arise, the council **never** averages opinions into vague compromises. It triggers an **Experiment-First Protocol** detailing precise hypotheses, baselines, variables, and evaluation metrics, escalating unresolved trade-offs to you.
3. **Adaptive Scaffolding Engine (L0 to L7):** Dynamically adjusts hints and guidance to your real-time **Zone of Proximal Development (ZPD)**—from production code (`L0`) to first-principles derivations (`L1`), pitfall warnings (`L2`), high-level conceptual nudges (`L3`), structural clues (`L4`), guided Socratic questions (`L5`), isomorphic transfer challenges (`L6`), and adversarial self-critique (`L7`).
4. **Cross-Project Persistent Memory:** Long-term learner state, tracked misconceptions, architectural decisions, and experiment outcomes persist across projects in a unified SQLite database stored in `~/.gemini/antigravity-cli/mentor_data/mentor_memory.db`.
5. **Zero External Dependencies:** Built 100% on the Python standard library (`sqlite3`, `ast`, `re`, `argparse`, `json`, `subprocess`, `dataclasses`, `typing`). Installs anywhere in seconds without dependency hell.

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

Every query is analyzed to dynamically assemble the most relevant specialist panel from 14 permanent roles, plus dynamically spawned domain experts:

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
When experts argue opposing positions (e.g., *DuckDB vs. Spark*, *Tree Models vs. Neural Networks*, *Normality Violations vs. Pragmatic Delivery*), the response formats an explicit 5-part structure:
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

- **Default Behavior:** Operates in **L3–L5 (Socratic Scaffolding)** to build independent mastery.
- **Anti-Dependency Safeguard:** If direct solutions (`L0`) exceed 65% of your recent interactions, an anti-dependency alert triggers, forcing conceptual hints until problem-solving autonomy is restored.

---

## ⚡ Quickstart & Installation

Install the Senior Engineering Mentor environment across any operating system with a single command:

### 🐧 Linux & 🍏 macOS (One-Command Installer)

```bash
# Via cURL
curl -fsSL https://raw.githubusercontent.com/ianjamesmabbic/ai-agents/main/install.sh | bash

# Or if you have cloned the repository:
chmod +x install.sh
./install.sh
```

### 🪟 Windows (PowerShell One-Command Installer)

```powershell
# Via PowerShell
irm https://raw.githubusercontent.com/ianjamesmabbic/ai-agents/main/install.ps1 | iex

# Or if you have cloned the repository:
powershell -ExecutionPolicy Bypass -File install.ps1
```

### 🐍 Standard Python / Pip Installation

```bash
git clone https://github.com/ianjamesmabbic/ai-agents.git
cd ai-agents
pip install -e .
```

*Note: Automatically creates global wrapper binaries `mentor` and `agy-mentor` in `~/.local/bin` (or Windows Scripts directory).*

---

## 🛠️ Cross-Project Persistence & Init

To equip **any existing or new repository** on your machine with the Senior AI Engineering Mentor while sharing global memory:

```bash
# Navigate to any project workspace
cd /path/to/my-new-project

# Initialize workspace configuration
mentor --init
```

### What `mentor --init` Does:
1. **Creates `.agents/skills/`** in your project containing all Tier 0 core skills and standalone audit utilities.
2. **Generates `.agents/skills.json`**, registering core skills with Antigravity and the local agent runtime.
3. **Installs `GEMINI.md` and `AGENTS.md`**, configuring Antigravity pair programming directives and the 14-member council.
4. **Connects to Global Persistence (`~/.gemini/antigravity-cli/mentor_data/mentor_memory.db`)**, ensuring your learner profile, tracked misconceptions, architectural decisions, and competency ratings stay unified across all projects.

---

## 💻 CLI & Slash Commands Reference

### 1. In Antigravity Chat (Pair Programming)

When working inside Antigravity, the directives are active automatically. Use slash commands to guide the session:

| Slash Command | Mode / Level | Behavior |
|:---|:---|:---|
| `/solve <query>` | **L0–L2 Direct** | Immediate production code, first-principles derivation, and pitfall warnings. |
| `/mentor <query>` | **L3–L5 Socratic** | Guiding questions, architectural clues, and conceptual nudges. |
| `/hint <query>` | **Progressive Clue** | Step-by-step hints without revealing implementation code. |
| `/challenge <concept>`| **L6–L7 Challenge** | Issues an isomorphic transfer problem or asks you to critique your own design. |
| `/council <query>` | **Council Debate** | Convenes the 14-expert council, exposing trade-offs without manufactured consensus. |
| `/interview [domain]` | **Mock Interview** | Conducts a rigorous technical interview (`system_design`, `ml_theory`, `statistics`, `coding`). |
| `/status` | **Learner Diagnostics**| Displays competency ratings (0–10), ZPD assessments, and anti-dependency ratio. |
| `/refine` | **Self-Improvement** | Reviews autonomous optimization proposals generated by the feedback engine (Phase 7). |
| `/feedback <text>` | **Calibration** | Submits direct feedback or corrections to refine mentor calibration over time. |

### 2. Standalone Terminal CLI (`mentor`)

The `mentor` CLI provides direct access to council deliberation, skills discovery, interviews, and security audits:

```bash
# Launch interactive REPL session
mentor

# Display learner competency evaluation & anti-dependency ratio
mentor --status

# Launch a mock technical interview (system_design, ml_theory, statistics, coding)
mentor --interview ml_theory

# Deliberate on an architectural trade-off via one-shot query
mentor "Should we use DuckDB or Spark for our 15GB daily log processing pipeline?"

# Request a direct solution with full implementation
mentor "/solve implement temporal out-of-fold cross-validation in pure Python"

# Discover and security-audit Tier 2 external skills for a task
mentor --discover "transformer model training"

# Security-audit an external skill folder or file
mentor --audit ~/.gemini/antigravity-cli/skills/my-custom-skill

# Inspect Phase 7 autonomous self-improvement proposals
mentor --refine

# List all installed Tier 0 and Tier 1 skills
mentor --skills
```

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

### Standalone Tier 0 Audit Scripts
Located in [`.agents/skills/`](.agents/skills/), these utilities run standalone in any CI/CD pipeline or local terminal:

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

## 🧠 Memory Store & Knowledge Graph

Persistent memory is backed by SQLite with 8 dedicated tables:

1. **`learner_profiles`**: Long-term mastery ratings across 5 engineering dimensions (0.0 to 10.0 scale).
2. **`knowledge_state`**: Exponential Moving Average (EMA) concept mastery scores.
3. **`misconceptions`**: Tracked conceptual gaps, active versus resolved states.
4. **`decisions`**: Architecture Decision Records (ADRs) with rationale and council dissent.
5. **`experiments`**: Experiment-First logs (hypotheses, metrics, confidence intervals).
6. **`projects`**: Multi-project tracking linking local directories to global learner history.
7. **`feedback`**: User feedback records driving autonomous self-refinement.
8. **`component_versions`**: Component revision history for continuous prompt/system optimization.

The **Technical Knowledge Graph** (`senior_mentor/knowledge/graph.py`) maps machine learning and software engineering concepts with prerequisite relationships, enabling automated gap analysis and Zone of Proximal Development identification.

---

## 🧪 Testing & Verification

The codebase comes with a comprehensive test suite covering all modules:

```bash
# Run the complete test suite
python3 -m unittest discover tests -v
```

### Test Suite Coverage (34 Tests / 100% Pass Rate):
- `tests/test_memory.py`: Profile creation, EMA mastery tracking, misconception lifecycle, ADR logging, anti-dependency ratio calculation.
- `tests/test_knowledge_graph.py`: Prerequisite graph traversal, gap analysis, fuzzy concept matching.
- `tests/test_pedagogy.py`: ZPD level assignment, anti-dependency alert triggers, explicit `/solve` and `/mentor` overrides.
- `tests/test_council_debate.py`: Expert selection heuristics, unmanufactured dissent protocol, Experiment-First protocol generation, dynamic specialist spawning.
- `tests/test_skills_security.py`: Static AST security auditing, prompt injection pattern detection, subprocess sandbox execution, timeout handling.
- `tests/test_orchestrator.py`: End-to-end slash command parsing, multi-agent debate synthesis, status reporting.
- `tests/test_advanced_features.py`: Technical interview simulation, decision rationale evaluation, Tier 2 discovery, OpenTelemetry GenAI audit logging, Phase 7 self-improvement proposals.

---

## 📁 Repository Structure

```
ai-agents/
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
│   ├── cli.py                        # Standalone REPL & Terminal CLI
│   ├── initializer.py                # Cross-Project 'mentor init' Scaffolding
│   └── orchestrator.py               # Orchestrator & Multi-Agent Deliberator
├── tests/                            # Automated Verification Test Suite (34 Tests)
├── AGENTS.md                         # Multi-Agent pairing directives
├── blueprint.md                      # Complete architectural specification
├── GEMINI.md                         # Antigravity Orchestrator directives
├── install.sh                        # Linux & macOS 1-command installer
├── install.ps1                       # Windows PowerShell 1-command installer
├── pyproject.toml                    # Modern PEP 518/621 package metadata
├── setup.py                          # Setuptools entry point
└── README.md                         # Documentation & Getting Started Guide
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
