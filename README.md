# s4r0ut

[![qa](https://github.com/abbousaad/s4r0ut/actions/workflows/qa.yml/badge.svg)](https://github.com/abbousaad/s4r0ut/actions/workflows/qa.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Defensive Research](https://img.shields.io/badge/use-defensive%20research-green.svg)](SECURITY.md)

**s4r0ut** is a Moroccan-focused password research dictionary for defensive
security, awareness, password policy testing, and authorized audits.

The project aims to become the best public Moroccan password-pattern resource by
combining:

- Moroccan names and spelling variants
- Darija words written in Latin script
- Amazigh, Hassaniya, and regional terms written in Latin script
- Moroccan cities, regions, football clubs, and cultural references
- Common local numeric patterns, years, and country-code motifs
- Transparent generation rules
- Quality checks and reproducible builds

## Defensive Purpose

This repository is intended for:

- Password policy research
- Security awareness training
- Authorized penetration testing
- Internal defensive audits
- Academic and threat-intelligence analysis

Do not use this project for unauthorized access, credential attacks against
systems you do not own, or any illegal activity.

## Project Layout

```text
seeds/
  names_morocco.txt
  family_names_morocco.txt
  darija_latin.txt
  cities_regions.txt
  football_culture.txt
  amazigh_hassaniya_latin.txt
  keyboard_patterns_morocco.txt
  institutions_culture_morocco.txt
  moroccan_patterns.txt

rules/
  morocco-basic.rule
  morocco-years.rule
  morocco-separators.rule
  morocco-leet.rule

scripts/
  build.py
  report.py

dist/
  s4r0ut-strict.txt
  s4r0ut-mini.txt
  s4r0ut-standard.txt
  s4r0ut-extended.txt
  stats.json
```

## Build

Current version: `0.1.0`

```bash
make build
```

The builder reads all seed files, generates Moroccan-specific variants, removes
duplicates, sorts the output, and writes:

- `dist/s4r0ut-strict.txt`
- `dist/s4r0ut-mini.txt`
- `dist/s4r0ut-standard.txt`
- `dist/s4r0ut-extended.txt`
- `dist/stats.json`

Build a single profile:

```bash
python3 scripts/build.py --profile strict
```

Compare against another dictionary:

```bash
python3 scripts/compare.py dist/s4r0ut-standard.txt ../KasbahKeys/KasbahKeys.txt
```

Run quality checks:

```bash
make qa
```

Generate release reports:

```bash
make report
```

Run unit tests:

```bash
make test
```

## Release Profiles

- `strict`: highest Moroccan signal, conservative transforms
- `mini`: compact high-signal release for quick demos and awareness
- `standard`: practical default profile for authorized internal testing
- `extended`: broader generated variants for research

Current release report:

| Profile | Entries | Moroccan keyword hits |
|---|---:|---:|
| `strict` | 19,726 | 2,967 |
| `mini` | 19,726 | 2,967 |
| `standard` | 181,632 | 13,989 |
| `extended` | 181,858 | 14,029 |

Current local benchmark against KasbahKeys:

| Metric | s4r0ut standard | KasbahKeys |
|---|---:|---:|
| Unique entries | 181,632 | 373,578 |
| Shared entries | 3,250 | 3,250 |
| Moroccan keyword hits | 13,989 | 5,366 |

## What Makes It Moroccan

The value of this project is not raw size. It is signal:

- Darija transliteration variants such as `khoya`, `5oya`, `sa7bi`, `zin`
- Morocco references such as `maroc`, `maghrib`, `212`, `dima`, `atlas`
- Football references such as `wac`, `wydad`, `raja`, `far`, `botola`
- City and region patterns such as `casa`, `kech`, `rabat`, `tanger`
- Common password suffixes such as years, `123`, `@123`, and `!`

## Growth Roadmap

- Add more Moroccan family names and regional variants
- Add Amazigh, Hassaniya, and regional Darija vocabulary
- Add clean benchmark stats against generic lists
- Add Hashcat/JtR rule files
- Add release profiles: mini, standard, extended, and strict Morocco-only
- Add documentation for awareness workshops and defensive use cases

## Data Policy

Accepted data:

- Public, non-sensitive vocabulary
- Synthetic transformations
- Cultural and linguistic password-pattern research
- User-submitted seed words without personal/private data

Not accepted:

- Fresh private leaks
- Personal identifiers tied to real people
- Account dumps
- Passwords from unauthorized collection
- Data that exposes private individuals

See also:

- [Awareness lab](docs/awareness-lab.md)
- [Internal audit checklist](docs/internal-audit-checklist.md)
- [Changelog](CHANGELOG.md)
- [Source notes](docs/source-notes.md)
- [Tooling notes](docs/tooling.md)
- [Release report](reports/release-report.md)
- [Release process](docs/release-process.md)
- [Security policy](SECURITY.md)
