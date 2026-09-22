#!/usr/bin/env python3
"""Run quality checks for curated s4r0ut seed files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_SEED_DIR = Path("seeds")
DEFAULT_SOURCE_NOTES = Path("docs/source-notes.md")
ALLOWED_ENTRY = re.compile(r"^[a-z0-9_@.!-]+$")
PHONE_LIKE = re.compile(r"^0[5-7][0-9]{8}$")
EMAIL_LIKE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def seed_entries(path: Path) -> list[tuple[int, str]]:
    entries: list[tuple[int, str]] = []
    for index, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        entries.append((index, line))
    return entries


def check_seed_file(path: Path) -> list[str]:
    errors: list[str] = []
    entries = seed_entries(path)
    values = [entry for _, entry in entries]

    if not entries:
        errors.append(f"{path}: no seed entries")

    if values != sorted(values):
        errors.append(f"{path}: seed entries are not sorted")

    if len(values) != len(set(values)):
        errors.append(f"{path}: duplicate seed entries found")

    for index, entry in entries:
        if entry != entry.lower():
            errors.append(f"{path}:{index}: seed must be lowercase")
        if not ALLOWED_ENTRY.fullmatch(entry):
            errors.append(f"{path}:{index}: unsupported character in seed")
        if len(entry) < 2 or len(entry) > 32:
            errors.append(f"{path}:{index}: seed length outside 2..32")
        if PHONE_LIKE.fullmatch(entry):
            errors.append(f"{path}:{index}: looks like a real phone number")
        if EMAIL_LIKE.fullmatch(entry):
            errors.append(f"{path}:{index}: looks like an email address")

    return errors


def documented_seed_files(seed_dir: Path, source_notes: Path) -> list[str]:
    notes = source_notes.read_text(encoding="utf-8")
    return [
        f"{path}: missing from {source_notes}"
        for path in sorted(seed_dir.glob("*.txt"))
        if path.name not in notes
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-dir", type=Path, default=DEFAULT_SEED_DIR)
    parser.add_argument("--source-notes", type=Path, default=DEFAULT_SOURCE_NOTES)
    args = parser.parse_args()

    errors: list[str] = []
    for path in sorted(args.seed_dir.glob("*.txt")):
        errors.extend(check_seed_file(path))
    errors.extend(documented_seed_files(args.seed_dir, args.source_notes))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"OK: checked {len(list(args.seed_dir.glob('*.txt')))} seed files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

