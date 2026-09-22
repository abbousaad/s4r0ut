#!/usr/bin/env python3
"""Build s4r0ut dictionaries from transparent Moroccan seed files."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "seeds"
DIST = ROOT / "dist"

YEARS = [str(year) for year in range(1970, 2027)]
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


def main() -> None:
    DIST.mkdir(exist_ok=True)

    seed_groups: dict[str, list[str]] = {}
    for path in sorted(SEEDS.glob("*.txt")):
        seed_groups[path.stem] = read_seed(path)

    output: set[str] = set()
    for words in seed_groups.values():
        for word in words:
            output.update(generate_for_word(word))

    output.update(generate_combinations(seed_groups))

    clean = sorted(
        item
        for item in output
        if 4 <= len(item) <= 32 and " " not in item and "\t" not in item
    )

    mini_path = DIST / "s4r0ut-mini.txt"
    mini_path.write_text("\n".join(clean) + "\n", encoding="utf-8")

    stats = {
        "dictionary": mini_path.name,
        "entries": len(clean),
        "seed_files": {name: len(values) for name, values in seed_groups.items()},
        "min_length": min(map(len, clean)) if clean else 0,
        "max_length": max(map(len, clean)) if clean else 0,
    }
    (DIST / "stats.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

