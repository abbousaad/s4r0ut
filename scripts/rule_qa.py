#!/usr/bin/env python3
"""Run lightweight quality checks for s4r0ut rule files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_RULE_DIR = Path("rules")
ALLOWED_CHARS = set(":cu$0123456789@!_.-abcdefghijklmnopqrstuvwxyz")


def rule_lines(path: Path) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    for index, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        lines.append((index, line))
    return lines


def check_rule_file(path: Path) -> list[str]:
    errors: list[str] = []
    rules = rule_lines(path)
    values = [rule for _, rule in rules]

    if not rules:
        errors.append(f"{path}: no rule entries")

    if len(values) != len(set(values)):
        errors.append(f"{path}: duplicate rule entries found")

    for index, rule in rules:
        if rule != rule.strip():
            errors.append(f"{path}:{index}: surrounding whitespace")
        if " " in rule or "\t" in rule:
            errors.append(f"{path}:{index}: contains whitespace")
        if len(rule) > 32:
            errors.append(f"{path}:{index}: rule too long")
        unsupported = sorted(set(rule) - ALLOWED_CHARS)
        if unsupported:
            errors.append(f"{path}:{index}: unsupported characters {''.join(unsupported)!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule-dir", type=Path, default=DEFAULT_RULE_DIR)
    args = parser.parse_args()

    errors: list[str] = []
    files = sorted(args.rule_dir.glob("*.rule"))
    for path in files:
        errors.extend(check_rule_file(path))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"OK: checked {len(files)} rule files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

