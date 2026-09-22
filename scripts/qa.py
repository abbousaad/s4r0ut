#!/usr/bin/env python3
"""Run lightweight quality checks for generated s4r0ut dictionaries."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines:
        errors.append(f"{path}: empty file")

    if lines != sorted(lines):
        errors.append(f"{path}: entries are not sorted")

    if len(lines) != len(set(lines)):
        errors.append(f"{path}: duplicate entries found")

    for index, line in enumerate(lines, start=1):
        if not line:
            errors.append(f"{path}:{index}: empty line")
        if line != line.strip():
            errors.append(f"{path}:{index}: surrounding whitespace")
        if " " in line or "\t" in line:
            errors.append(f"{path}:{index}: contains whitespace")
        if len(line) < 4 or len(line) > 32:
            errors.append(f"{path}:{index}: length outside 4..32")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        default=sorted(Path("dist").glob("s4r0ut-*.txt")),
    )
    args = parser.parse_args()

    errors: list[str] = []
    for path in args.files:
        errors.extend(check_file(path))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"OK: checked {len(args.files)} dictionary files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

