#!/usr/bin/env python3
"""Compare a s4r0ut profile with another password dictionary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

MOROCCAN_KEYWORDS = [
    "maroc",
    "morocco",
    "maghrib",
    "casa",
    "rabat",
    "marrakech",
    "kech",
    "tanger",
    "fes",
    "agadir",
    "oujda",
    "nador",
    "safi",
    "kenitra",
    "raja",
    "wydad",
    "wac",
    "rca",
    "atlas",
    "khoya",
    "khouya",
    "sa7bi",
    "sahbi",
    "zin",
    "zwina",
    "dima",
    "212",
]


def read_entries(path: Path) -> set[str]:
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip()
    }


def keyword_hits(entries: set[str]) -> int:
    return sum(
        1 for item in entries if any(keyword in item.lower() for keyword in MOROCCAN_KEYWORDS)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    args = parser.parse_args()

    left = read_entries(args.left)
    right = read_entries(args.right)
    overlap = left & right

    report = {
        "left_file": str(args.left),
        "right_file": str(args.right),
        "left_entries": len(left),
        "right_entries": len(right),
        "overlap": len(overlap),
        "left_unique_to_file": len(left - right),
        "right_unique_to_file": len(right - left),
        "left_moroccan_keyword_hits": keyword_hits(left),
        "right_moroccan_keyword_hits": keyword_hits(right),
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

