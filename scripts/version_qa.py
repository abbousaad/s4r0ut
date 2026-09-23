#!/usr/bin/env python3
"""Check s4r0ut version metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "VERSION"
CHANGELOG = ROOT / "CHANGELOG.md"
CITATION = ROOT / "CITATION.cff"

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def check_version() -> list[str]:
    errors: list[str] = []
    version = VERSION.read_text(encoding="utf-8").strip()
    changelog = CHANGELOG.read_text(encoding="utf-8")
    citation = CITATION.read_text(encoding="utf-8")

    if not SEMVER.fullmatch(version):
        errors.append(f"{VERSION}: version must use MAJOR.MINOR.PATCH")

    if f"## [{version}]" not in changelog:
        errors.append(f"{CHANGELOG}: missing entry for {version}")

    if "title:" not in citation or "repository-code:" not in citation:
        errors.append(f"{CITATION}: missing citation metadata")

    return errors


def main() -> int:
    errors = check_version()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print("OK: version metadata is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

