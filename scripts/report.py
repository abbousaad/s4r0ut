#!/usr/bin/env python3
"""Generate human-readable and machine-readable s4r0ut release reports."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
REPORTS = ROOT / "reports"
VERSION = ROOT / "VERSION"
CHANGELOG = ROOT / "CHANGELOG.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_size(path: Path) -> int:
    return path.stat().st_size


def load_stats(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def release_date() -> str:
    version = VERSION.read_text(encoding="utf-8").strip()
    changelog = CHANGELOG.read_text(encoding="utf-8")
    match = re.search(rf"^## \[{re.escape(version)}\] - (\d{{4}}-\d{{2}}-\d{{2}})$", changelog, re.MULTILINE)
    if not match:
        raise ValueError(f"CHANGELOG.md is missing a release date for {version}")
    return match.group(1)


def enrich_stats(stats: dict, dist_dir: Path) -> dict:
    enriched = json.loads(json.dumps(stats))
    for profile in enriched["profiles"].values():
        path = dist_dir / profile["file"]
        profile["bytes"] = file_size(path)
        profile["sha256"] = sha256(path)
    return enriched


def markdown_report(stats: dict) -> str:
    lines = [
        "# s4r0ut Release Report",
        "",
        f"Release date: {release_date()}",
        "",
        "## Summary",
        "",
        f"- Total seed entries: {stats['total_seeds']}",
        f"- Seed categories: {len(stats['seed_files'])}",
        f"- Release profiles: {len(stats['profiles'])}",
        "",
        "## Profiles",
        "",
        "| Profile | Entries | Unique | Min | Max | Moroccan hits | Bytes | SHA-256 |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]

    for name, profile in stats["profiles"].items():
        lines.append(
            "| {name} | {entries:,} | {unique:,} | {min_len} | {max_len} | "
            "{hits:,} | {bytes:,} | `{sha}` |".format(
                name=name,
                entries=profile["entries"],
                unique=profile["unique_entries"],
                min_len=profile["min_length"],
                max_len=profile["max_length"],
                hits=profile["moroccan_keyword_hits"],
                bytes=profile["bytes"],
                sha=profile["sha256"],
            )
        )

    lines.extend(
        [
            "",
            "## Seed Files",
            "",
            "| Seed file | Entries |",
            "|---|---:|",
        ]
    )

    for name, count in sorted(stats["seed_files"].items()):
        lines.append(f"| `{name}.txt` | {count:,} |")

    lines.extend(
        [
            "",
            "## Quality Gates",
            "",
            "- Seed files must be sorted, unique, lowercase, documented, and free of phone/email-like values.",
            "- Generated dictionaries must be sorted, unique, length-bounded, and whitespace-free.",
            "- CI rebuilds the dictionaries and fails if generated files are not committed.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stats", type=Path, default=DIST / "stats.json")
    parser.add_argument("--dist-dir", type=Path, default=DIST)
    parser.add_argument("--out-dir", type=Path, default=REPORTS)
    args = parser.parse_args()

    args.out_dir.mkdir(exist_ok=True)
    stats = enrich_stats(load_stats(args.stats), args.dist_dir)

    (args.out_dir / "release-report.json").write_text(
        json.dumps(stats, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "release-report.md").write_text(
        markdown_report(stats),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
