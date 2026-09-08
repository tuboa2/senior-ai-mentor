#!/usr/bin/env python3
"""Data Leakage and Contamination Checker.

Performs static code analysis and dataset validation to identify:
1. Code-level pipeline leakage (fit_transform called before split, missing shift on rolling windows)
2. Group ID overlap between train and test sets
3. Temporal causality inversion (test timestamps <= train timestamps)
"""

import argparse
import ast
import csv
import sys
from typing import List, Set, Tuple

class CodeLeakageVisitor(ast.NodeVisitor):
    def __init__(self):
        self.warnings: List[str] = []
        self.has_split = False
        self.split_line = None

    def visit_Call(self, node: ast.Call):
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr

        # Check for train_test_split
        if "train_test_split" in func_name or "split" in func_name:
            self.has_split = True
            self.split_line = node.lineno

        # Check for fit or fit_transform before split
        if func_name in ("fit", "fit_transform"):
            if not self.has_split:
                self.warnings.append(
                    f"Line {node.lineno}: '{func_name}' called before train/test split. High risk of pipeline contamination!"
                )

        # Check for rolling window without shift
        if func_name == "rolling":
            self.warnings.append(
                f"Line {node.lineno}: 'rolling' window detected. Ensure you append '.shift(1)' to prevent lookahead bias on step t."
            )

        self.generic_visit(node)

def audit_code_file(filepath: str) -> List[str]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=filepath)
        visitor = CodeLeakageVisitor()
        visitor.visit(tree)
        return visitor.warnings
    except Exception as e:
        return [f"Could not parse Python file {filepath}: {e}"]

def check_csv_leakage(
    train_path: str,
    test_path: str,
    id_col: str = None,
    time_col: str = None,
    target_col: str = None
) -> List[str]:
    issues = []
    
    # Read headers
    with open(train_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        train_rows = list(reader)
        train_header = reader.fieldnames or []

    with open(test_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        test_rows = list(reader)
        test_header = reader.fieldnames or []

    # Check 1: Group/Entity ID overlap
    if id_col and id_col in train_header and id_col in test_header:
        train_ids = {r[id_col] for r in train_rows if r.get(id_col)}
        test_ids = {r[id_col] for r in test_rows if r.get(id_col)}
        overlap = train_ids.intersection(test_ids)
        if overlap:
            sample_overlap = list(overlap)[:5]
            issues.append(
                f"CRITICAL GROUP LEAKAGE: {len(overlap)} entity IDs appear in both train and test! Examples: {sample_overlap}"
            )

    # Check 2: Temporal causality
    if time_col and time_col in train_header and time_col in test_header:
        train_times = [r[time_col] for r in train_rows if r.get(time_col)]
        test_times = [r[time_col] for r in test_rows if r.get(time_col)]
        if train_times and test_times:
            max_train_time = max(train_times)
            min_test_time = min(test_times)
            if min_test_time < max_train_time:
                issues.append(
                    f"CRITICAL TEMPORAL LEAKAGE: Min test timestamp ({min_test_time}) is earlier than max train timestamp ({max_train_time})!"
                )

    return issues

def main():
    parser = argparse.ArgumentParser(description="Audit datasets or code for data leakage.")
    parser.add_argument("--code", help="Path to Python script to audit for AST leakage patterns.")
    parser.add_argument("--train", help="Path to train CSV.")
    parser.add_argument("--test", help="Path to test CSV.")
    parser.add_argument("--id-col", help="Entity ID column for GroupKFold check.")
    parser.add_argument("--time-col", help="Timestamp column for temporal order check.")
    parser.add_argument("--target-col", help="Target column name.")
    args = parser.parse_args()

    found_any = False
    if args.code:
        print(f"Auditing code file: {args.code}...")
        warnings = audit_code_file(args.code)
        if warnings:
            found_any = True
            print("[!] LEAKAGE WARNINGS FOUND IN CODE:")
            for w in warnings:
                print(f"  - {w}")
        else:
            print("[+] Code AST check passed: No obvious pipeline leakage detected.")

    if args.train and args.test:
        print(f"\nAuditing datasets: train={args.train}, test={args.test}...")
        issues = check_csv_leakage(args.train, args.test, args.id_col, args.time_col, args.target_col)
        if issues:
            found_any = True
            print("[!] CRITICAL DATASET LEAKAGE ISSUES DETECTED:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("[+] Dataset checks passed: No entity overlap or temporal inversion found.")

    if not args.code and not (args.train and args.test):
        parser.print_help()

if __name__ == "__main__":
    main()
