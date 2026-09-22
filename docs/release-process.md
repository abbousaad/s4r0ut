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
make qa
make compare
```

## Versioning

Use simple semantic tags:

- Patch: seed corrections, documentation, small rule fixes
- Minor: new seed categories, new release profile, new QA metric
- Major: incompatible generator behavior or data-policy change
