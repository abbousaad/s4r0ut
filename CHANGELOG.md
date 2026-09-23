# Changelog

All notable changes to s4r0ut are documented here.

The project uses semantic versioning:

- Patch: seed corrections, documentation, and small rule fixes.
- Minor: new seed categories, release profiles, QA metrics, or tooling.
- Major: incompatible generator behavior or data-policy changes.

## [0.1.0] - 2026-09-22

### Added

- Moroccan-focused seed corpus with 343 curated entries across 9 categories.
- Four generated dictionary profiles: strict, mini, standard, and extended.
- Reproducible builder, release reports, QA scripts, and Makefile workflow.
- Seed, rule, dictionary, report, and unit-test quality gates.
- Defensive rule files for authorized internal testing and awareness labs.
- GitHub Actions workflow using `make qa`.
- Contributor issue templates, pull request template, citation metadata, license,
  security policy, source notes, release process, and tooling documentation.
- Awareness lab and internal audit checklist.

### Benchmarks

- `s4r0ut-standard.txt`: 181,632 unique entries.
- `s4r0ut-extended.txt`: 181,858 unique entries.
- Local KasbahKeys comparison: 13,989 Moroccan keyword hits in s4r0ut-standard
  versus 5,366 in KasbahKeys using the project keyword benchmark.

