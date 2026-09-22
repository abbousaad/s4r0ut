# Release Process

Use this process for tagged releases so every public dictionary is reproducible
and defensible.

## Checklist

1. Update seed files and source notes.
2. Rebuild all profiles.
3. Run Python syntax checks.
4. Run unit tests.
5. Run dictionary QA.
6. Compare `s4r0ut-standard` against relevant baseline dictionaries.
7. Commit generated dictionaries and updated stats.
8. Tag the release.

## Commands

```bash
python3 scripts/build.py
python3 -m py_compile scripts/build.py scripts/compare.py scripts/qa.py scripts/report.py scripts/seed_qa.py
python3 -m unittest discover -s tests
python3 scripts/seed_qa.py
python3 scripts/report.py
python3 scripts/qa.py
python3 scripts/compare.py dist/s4r0ut-standard.txt ../KasbahKeys/KasbahKeys.txt
```

## Versioning

Use simple semantic tags:

- Patch: seed corrections, documentation, small rule fixes
- Minor: new seed categories, new release profile, new QA metric
- Major: incompatible generator behavior or data-policy change
