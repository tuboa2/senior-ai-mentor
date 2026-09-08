#!/usr/bin/env python3
"""ML Python Code Linter & Standards Enforcer.

Statically analyzes Python code for common anti-patterns in AI/ML engineering:
1. iterrows() in pandas (catastrophic performance anti-pattern)
2. Bare except / pass in except blocks
3. Missing return type or argument type annotations on functions
4. eval() / exec() dynamic execution risks
5. Hardcoded secrets / API keys
"""

import argparse
import ast
import re
import sys
from typing import List

class MLStandardsVisitor(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.issues: List[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Check return annotation
        if node.returns is None and node.name != "__init__":
            self.issues.append(
                f"{self.filename}:{node.lineno}: Function '{node.name}' is missing a return type annotation."
            )
        # Check argument annotations
        for arg in node.args.args:
            if arg.arg != "self" and arg.arg != "cls" and arg.annotation is None:
                self.issues.append(
                    f"{self.filename}:{node.lineno}: Argument '{arg.arg}' in function '{node.name}' is missing a type annotation."
                )
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        if node.attr == "iterrows":
            self.issues.append(
                f"{self.filename}:{node.lineno}: Critical performance antipattern: '.iterrows()' detected. Use vectorized NumPy/Polars operations or '.itertuples()'!"
            )
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        if node.type is None:
            self.issues.append(
                f"{self.filename}:{node.lineno}: Bare 'except:' clause detected. Always catch specific exception classes."
            )
        elif len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            self.issues.append(
                f"{self.filename}:{node.lineno}: Silent exception swallowing ('except ...: pass') detected. Log errors explicitly."
            )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

        if func_name in ("eval", "exec"):
            self.issues.append(
                f"{self.filename}:{node.lineno}: Unsafe dynamic execution '{func_name}()' detected!"
            )
        self.generic_visit(node)

def lint_file(filepath: str) -> List[str]:
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for potential exposed keys
        if re.search(r'(api[_-]?key|secret|token)\s*=\s*["\'][A-Za-z0-9_\-]{16,}["\']', content, re.IGNORECASE):
            issues.append(f"{filepath}: Hardcoded API key or secret token detected! Use environment variables.")

        tree = ast.parse(content, filename=filepath)
        visitor = MLStandardsVisitor(filepath)
        visitor.visit(tree)
        issues.extend(visitor.issues)
    except Exception as e:
        issues.append(f"Linting failed for {filepath}: {e}")
    return issues

def main():
    parser = argparse.ArgumentParser(description="Lint ML Python code for production standards.")
    parser.add_argument("files", nargs="+", help="Python files to inspect")
    args = parser.parse_args()

    total_issues = 0
    for f in args.files:
        issues = lint_file(f)
        if issues:
            print(f"\n[!] Violations found in {f}:")
            for issue in issues:
                print(f"  - {issue}")
            total_issues += len(issues)
        else:
            print(f"[+] {f}: Clean! Meets production engineering standards.")

    if total_issues > 0:
        print(f"\nTotal violations: {total_issues}")
        sys.exit(1)
    else:
        print("\nAll checks passed successfully.")

if __name__ == "__main__":
    main()
