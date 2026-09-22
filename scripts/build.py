#!/usr/bin/env python3
"""Build s4r0ut dictionaries from transparent Moroccan seed files.

The project intentionally separates high-signal Moroccan entries from broader
generated variants. This keeps the public dictionary useful for defensive
research without making the core release look like an opaque dump.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "seeds"
DIST = ROOT / "dist"

YEARS = [str(year) for year in range(1970, 2027)]
RECENT_YEARS = [str(year) for year in range(2020, 2027)]
COMMON_SUFFIXES = [
    "1",
    "12",
    "123",
    "1234",
    "12345",
    "123456",
    "007",
    "212",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025",
    "2026",
    "@123",
    "!",
    "!!",
]
SPECIALS = ["@", "!", "_", ".", "-"]
CORE_SUFFIXES = ["123", "1234", "212", "2024", "2025", "2026", "@123", "!"]
PROFILE_FILES = {
    "strict": "s4r0ut-strict.txt",
    "standard": "s4r0ut-standard.txt",
    "extended": "s4r0ut-extended.txt",
    "mini": "s4r0ut-mini.txt",
}
LEET_MAP = {
    "a": ["4"],
    "e": ["3"],
    "i": ["1"],
    "o": ["0"],
    "s": ["5"],
    "h": ["7"],
    "q": ["9"],
}
MOROCCAN_DIGRAPHS = {
    "kh": ["5"],
    "gh": ["8"],
    "ch": ["sh"],
}
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


def read_seed(path: Path) -> list[str]:
    values: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        values.append(line)
    return values


def title_word(word: str) -> str:
    return word[:1].upper() + word[1:] if word else word


def leet_variants(word: str) -> set[str]:
    variants = {word}

    for src, replacements in MOROCCAN_DIGRAPHS.items():
        if src in word:
            for repl in replacements:
                variants.add(word.replace(src, repl))

    for src, replacements in LEET_MAP.items():
        if src in word:
            for repl in replacements:
                variants.add(word.replace(src, repl, 1))

    return variants


def generate_for_word(word: str) -> set[str]:
    variants: set[str] = set()
    bases = {word, word.lower(), title_word(word)}
    bases.update(leet_variants(word.lower()))

    for base in bases:
        variants.add(base)
        variants.add(base + base)

        for suffix in COMMON_SUFFIXES:
            variants.add(base + suffix)
            variants.add(title_word(base) + suffix)

        for year in YEARS:
            variants.add(base + year)
            variants.add(title_word(base) + year)

        for special in SPECIALS:
            variants.add(base + special)
            variants.add(base + special + "123")
            variants.add(base + special + "2024")

    return variants


def generate_strict_for_word(word: str) -> set[str]:
    variants: set[str] = set()
    bases = {word.lower(), title_word(word.lower())}
    bases.update(leet_variants(word.lower()))

    for base in bases:
        variants.add(base)
        for suffix in CORE_SUFFIXES:
            variants.add(base + suffix)
        for year in RECENT_YEARS:
            variants.add(base + year)
    return variants


def generate_combinations(seed_groups: dict[str, list[str]]) -> set[str]:
    combos: set[str] = set()
    names = seed_groups.get("names_morocco", [])
    cities = seed_groups.get("cities_regions", [])
    culture = seed_groups.get("football_culture", [])
    darija = seed_groups.get("darija_latin", [])

    for left in names[:80]:
        for right in cities[:40]:
            combos.add(left + right)
            combos.add(left + "@" + right)
            combos.add(title_word(left) + right + "123")

    for left in culture:
        for suffix in ["123", "212", "2022", "2024", "2026", "!"]:
            combos.add(left + suffix)
            combos.add(title_word(left) + suffix)

    for left in darija:
        for right in ["123", "212", "2024", "!", "@123"]:
            combos.add(left + right)

    return combos


def generate_strict_combinations(seed_groups: dict[str, list[str]]) -> set[str]:
    combos: set[str] = set()
    names = seed_groups.get("names_morocco", [])
    cities = seed_groups.get("cities_regions", [])
    culture = seed_groups.get("football_culture", [])
    darija = seed_groups.get("darija_latin", [])

    for name in names:
        for marker in ["212", "maroc", "maghrib"]:
            combos.add(name + marker)
            combos.add(title_word(name) + marker + "123")

    for city in cities:
        for suffix in ["123", "212", "2024", "2026"]:
            combos.add(city + suffix)

    for item in culture + darija:
        for suffix in ["123", "212", "2024", "!"]:
            combos.add(item + suffix)

    return combos


def clean_entries(entries: set[str], min_len: int = 4, max_len: int = 32) -> list[str]:
    return sorted(
        item
        for item in entries
        if min_len <= len(item) <= max_len and " " not in item and "\t" not in item
    )


def keyword_hits(entries: list[str]) -> int:
    return sum(
        1 for item in entries if any(keyword in item.lower() for keyword in MOROCCAN_KEYWORDS)
    )


def length_buckets(entries: list[str]) -> dict[str, int]:
    return {
        "<6": sum(1 for item in entries if len(item) < 6),
        "6-10": sum(1 for item in entries if 6 <= len(item) <= 10),
        "11-16": sum(1 for item in entries if 11 <= len(item) <= 16),
        ">16": sum(1 for item in entries if len(item) > 16),
    }


def build_profiles(seed_groups: dict[str, list[str]]) -> dict[str, list[str]]:
    strict_output: set[str] = set()
    extended_output: set[str] = set()

    for group_name, words in seed_groups.items():
        for word in words:
            if group_name == "moroccan_patterns" and word.isdigit():
                strict_output.add(word)
                for year in RECENT_YEARS:
                    extended_output.add(word + year)
                continue

            strict_output.update(generate_strict_for_word(word))
            extended_output.update(generate_for_word(word))

    strict_output.update(generate_strict_combinations(seed_groups))
    extended_output.update(generate_combinations(seed_groups))

    strict = clean_entries(strict_output)
    extended = clean_entries(strict_output | extended_output)
    standard = [item for item in extended if len(item) <= 20]
    mini = strict[:50000] if len(strict) > 50000 else strict

    return {
        "strict": strict,
        "standard": standard,
        "extended": extended,
        "mini": mini,
    }


def write_profile(name: str, entries: list[str]) -> dict[str, object]:
    path = DIST / PROFILE_FILES[name]
    path.write_text("\n".join(entries) + "\n", encoding="utf-8")
    return {
        "file": path.name,
        "entries": len(entries),
        "unique_entries": len(set(entries)),
        "min_length": min(map(len, entries)) if entries else 0,
        "max_length": max(map(len, entries)) if entries else 0,
        "length_buckets": length_buckets(entries),
        "moroccan_keyword_hits": keyword_hits(entries),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILE_FILES),
        help="Write only one profile instead of every release profile.",
    )
    args = parser.parse_args()

    DIST.mkdir(exist_ok=True)

    seed_groups: dict[str, list[str]] = {}
    for path in sorted(SEEDS.glob("*.txt")):
        seed_groups[path.stem] = read_seed(path)

    profiles = build_profiles(seed_groups)
    selected_profiles = [args.profile] if args.profile else ["strict", "mini", "standard", "extended"]

    stats = {
        "profiles": {
            profile: write_profile(profile, profiles[profile])
            for profile in selected_profiles
        },
        "seed_files": {name: len(values) for name, values in seed_groups.items()},
        "total_seeds": sum(len(values) for values in seed_groups.values()),
    }
    (DIST / "stats.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
