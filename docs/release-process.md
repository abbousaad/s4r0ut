# Release Process

Use this process for tagged releases so every public dictionary is reproducible
and defensible.

## Checklist

1. Update seed files and source notes.
2. Update `VERSION` and `CHANGELOG.md`.
3. Rebuild all profiles.
4. Run Python syntax checks.
5. Run unit tests.
6. Run dictionary QA.
7. Compare `s4r0ut-standard` against relevant baseline dictionaries.
8. Commit generated dictionaries and updated stats.
9. Tag the release.

## Commands

```bash
make qa
make compare
```

## Versioning

Use simple semantic tags:

- Patch: seed corrections, documentation, small rule fixes
- Minor: new seed categories, new release profile, new QA metric
- Major: incompatible generator behavior or data-policy change
