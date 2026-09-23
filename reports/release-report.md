# s4r0ut Release Report

Release date: 2026-09-22

## Summary

- Total seed entries: 636
- Seed categories: 9
- Release profiles: 4

## Profiles

| Profile | Entries | Unique | Min | Max | Moroccan hits | Bytes | SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---|
| strict | 36,506 | 36,506 | 4 | 21 | 4,827 | 410,443 | `a61bca3cc97b585af4a7f0995929b71621e29ee2092be0235e76cc0230ad3411` |
| mini | 36,506 | 36,506 | 4 | 21 | 4,827 | 410,443 | `a61bca3cc97b585af4a7f0995929b71621e29ee2092be0235e76cc0230ad3411` |
| standard | 327,640 | 327,640 | 4 | 20 | 16,780 | 3,886,372 | `14baa74d67482834077b94ae09a4685013d24737dac2e96cdeb0acea01cc738a` |
| extended | 328,519 | 328,519 | 4 | 28 | 16,867 | 3,906,711 | `fc7770c7b60400d30ef828b09766d2dfa0b587ce3667d6aec7fae637de26876e` |

## Seed Files

| Seed file | Entries |
|---|---:|
| `amazigh_hassaniya_latin.txt` | 59 |
| `cities_regions.txt` | 74 |
| `darija_latin.txt` | 73 |
| `family_names_morocco.txt` | 117 |
| `football_culture.txt` | 38 |
| `institutions_culture_morocco.txt` | 60 |
| `keyboard_patterns_morocco.txt` | 38 |
| `moroccan_patterns.txt` | 30 |
| `names_morocco.txt` | 147 |

## Quality Gates

- Seed files must be sorted, unique, lowercase, documented, and free of phone/email-like values.
- Generated dictionaries must be sorted, unique, length-bounded, and whitespace-free.
- CI rebuilds the dictionaries and fails if generated files are not committed.
