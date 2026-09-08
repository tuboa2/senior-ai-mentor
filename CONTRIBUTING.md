# Contributing to Senior AI Engineering Mentor

Thank you for your interest in contributing to the **Senior AI Engineering Mentor** project!

This repository adheres to the architectural design specified in [`blueprint.md`](blueprint.md). Our core mission is to build genuine, independent engineering capability across Machine Learning, Data Science, Software Architecture, and AI Research.

---

## Table of Contents

1. [Core Architectural Principles](#core-architectural-principles)
2. [Development Setup](#development-setup)
3. [Reporting Issues](#reporting-issues)
4. [Submitting Pull Requests (PRs)](#submitting-pull-requests-prs)
5. [GitHub Actions & Continuous Integration](#github-actions--continuous-integration)
6. [Code Style & Verification Standards](#code-style--verification-standards)
7. [License](#license)

---

## Core Architectural Principles

When proposing changes, ensure your contributions honor these foundational tenets:

- **Zero External Dependencies:** Core functionality (`senior_mentor/`) relies exclusively on the Python 3.10+ standard library (`sqlite3`, `ast`, `re`, `argparse`, `json`, `subprocess`, `dataclasses`, `typing`). Do not introduce external runtime dependencies unless isolated within optional Tier 1/2 skills.
- **Strictly Prohibited Manufactured Consensus:** Never flatten expert debates into vague compromises. Always follow the **Experiment-First Protocol** (hypothesis, baseline, variables, metrics, confidence intervals).
- **Anti-Dependency Safeguard:** Protect the learner's problem-solving autonomy. Changes to the pedagogical engine must respect the Zone of Proximal Development (ZPD) and throttle direct solutions if direct answers exceed 65%.
- **AST Sandboxing & Security:** All external skill discovery tools must pass static AST security auditing (blocking subprocess exploitation, token exfiltration, network egress, and prompt injection patterns).

---

## Development Setup

### 1. Fork & Clone

```bash
git clone https://github.com/tuboa2/senior-ai-mentor.git
cd senior-ai-mentor
```

### 2. Install in Editable Mode

```bash
# Using the automated local installer:
chmod +x install.sh
./install.sh

# Or directly via pip:
pip install -e .
mentor init
```

### 3. Run the Verification Test Suite

Verify that all unit and integration tests pass:

```bash
python3 -m unittest discover tests -v
```

All 34 tests must pass cleanly before submitting any pull request.

---

## Reporting Issues

We welcome bug reports, feature proposals, and security disclosures.

### 1. Bug Reports
Before submitting a bug report:
- Search existing [GitHub Issues](https://github.com/tuboa2/senior-ai-mentor/issues) to avoid duplicates.
- Ensure the issue can be reproduced on the latest `main` branch.
- Include the following details:
  - Operating System & Python version (`python3 --version`).
  - Terminal output and exact command executed (e.g., `mentor --status` or `python3 -m unittest discover tests`).
  - Minimal reproducible example or code snippet.
  - Expected vs. actual behavior.

### 2. Feature Requests & Enhancements
Feature requests should align with [`blueprint.md`](blueprint.md). When proposing a new feature:
- Describe the engineering problem it solves.
- Specify which Expert Council members or architectural tiers (0, 1, or 2) are affected.
- Outline the proposed interface, schema changes (if modifying SQLite tables in `senior_mentor/memory/store.py`), and backward-compatibility considerations.

### 3. Security Vulnerabilities
If you discover a security vulnerability (such as a bypass in `senior_mentor/skills/auditor.py` or sandbox execution), please report it responsibly by opening a confidential security advisory on GitHub or contacting the maintainers directly.

---

## Submitting Pull Requests (PRs)

### PR Workflow

1. **Create a Feature Branch:**
   ```bash
   git checkout -b feat/your-feature-name
   # or for bug fixes:
   git checkout -b fix/issue-description
   ```

2. **Make Atomic, Well-Documented Commits:**
   Follow conventional commits:
   - `feat: add causal inference specialist to dynamic spawner`
   - `fix: resolve AST visitor edge case in leakage checker`
   - `docs: clarify cross-project workspace initialization`
   - `test: add unit test for Benjamini-Hochberg adjustment with ties`

3. **Verify Local Quality Standards:**
   Run all linters and tests locally:
   ```bash
   # 1. Run unit and integration tests
   python3 -m unittest discover tests -v

   # 2. Lint Python code using the repository's ML code linter
   python3 .agents/skills/python-engineering-standards/scripts/lint_ml_code.py senior_mentor/cli.py senior_mentor/orchestrator.py

   # 3. Test CLI commands end-to-end
   python3 -m senior_mentor.cli --status
   python3 -m senior_mentor.cli --skills
   ```

4. **Push & Open a Pull Request:**
   Push your branch to your fork and open a PR targeting the `main` branch of `tuboa2/senior-ai-mentor`.
   Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md).

---

## GitHub Actions & Continuous Integration

This repository uses GitHub Actions (`.github/workflows/ci.yml`) to automatically validate every push and pull request across multiple operating systems and Python versions.

### CI Matrix & Automated Checks:
- **Operating Systems:** `ubuntu-latest`, `macos-latest`, `windows-latest`.
- **Python Versions:** `3.10`, `3.11`, `3.12`.
- **Automated Verification Steps:**
  1. Package installation in editable mode (`pip install -e .`).
  2. Full test suite execution (`python -m unittest discover tests -v`).
  3. CLI binary execution verification (`mentor --version`, `mentor --status`, `mentor --skills`).
  4. Cross-project workspace initialization test (`mentor init`).
  5. Standalone Tier 0 utility validation (`validate_stats.py`, `leakage_checker.py`, `lint_ml_code.py`).

A green CI run is required for all PR merges.

---

## Code Style & Verification Standards

All Python code must strictly conform to:
- **Type Annotations:** Explicit type hints for all function signatures and return values (`typing.List`, `typing.Dict`, `typing.Optional`, etc.).
- **Defensive Error Handling:** Never use bare `except:` clauses. Catch specific exceptions (`ValueError`, `FileNotFoundError`, `sqlite3.DatabaseError`).
- **AST & Security Compliance:** No dynamic `eval()` or un-sanitized shell execution.
- **Documentation:** Clear docstrings explaining rationale, design decisions, and algorithmic complexity.

---

## License

By contributing to this repository, you agree that your contributions will be licensed under the [MIT License](LICENSE).
