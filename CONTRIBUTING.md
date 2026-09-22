# Contributing

Contributions should make the dictionary more Moroccan, more explainable, or
cleaner to use in defensive research.

## Good Contributions

- Moroccan first names, family names, and spelling variants
- Darija words in Latin script
- Regional words from different parts of Morocco
- Football, cultural, and local references
- Better generation rules
- Quality checks and statistics
- Documentation for defensive use

## Do Not Contribute

- Private leaks
- Account dumps
- Personal data
- Passwords tied to identifiable people
- Anything collected without authorization

## Seed Format

- One entry per line
- Lowercase ASCII where possible
- No empty lines
- Use `#` for comments
- Keep entries short and reusable
- Keep entries sorted
- Update `docs/source-notes.md` for new seed categories

Example:

```text
khoya
sa7bi
maghrib
casa
wydad
```

## Required Checks

Run these before opening a pull request:

```bash
python3 scripts/seed_qa.py
python3 scripts/build.py
python3 scripts/report.py
python3 scripts/qa.py
python3 -m unittest discover -s tests
```

The CI workflow runs the same quality gates and fails when generated files are
stale or seed files violate the data policy.
