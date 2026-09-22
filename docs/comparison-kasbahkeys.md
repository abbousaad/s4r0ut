# Comparison: s4r0ut and KasbahKeys

KasbahKeys is valuable because it provides a large ready-to-use Moroccan-themed
wordlist. s4r0ut is designed to become a stricter research project: transparent
seed files, reproducible generation, explicit release profiles, and quality
metrics.

## Current Difference

- KasbahKeys favors raw volume in one final list.
- s4r0ut favors explainability, reproducibility, and Moroccan-specific signal.

## Strategic Positioning

s4r0ut should not try to win only by line count. It should win by being the
cleanest Moroccan password-pattern project:

- clear seed provenance
- strict defensive data policy
- repeatable generator
- multiple release profiles
- comparison tooling
- documented research roadmap

## Comparison Command

From the `s4r0ut` repository:

```bash
python3 scripts/compare.py dist/s4r0ut-standard.txt ../KasbahKeys/KasbahKeys.txt
```

## Current Local Benchmark

Generated on 2026-09-22 from the local clones under
`02_Cybersecurity_Excellence/`.

| Metric | s4r0ut standard | KasbahKeys |
|---|---:|---:|
| Unique entries | 181,632 | 373,578 |
| Shared entries | 3,250 | 3,250 |
| Unique to file | 178,382 | 370,328 |
| Moroccan keyword hits | 13,989 | 5,366 |

Interpretation:

- KasbahKeys currently wins on raw size.
- s4r0ut currently wins on reproducibility and Moroccan-keyword density by this
  simple benchmark.
- The next step is improving the benchmark with stronger linguistic categories,
  not only keyword matching.
