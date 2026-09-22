# Tooling Notes

s4r0ut ships ready-to-use dictionaries and small rule files for authorized
internal testing, password policy assessment, awareness labs, and defensive
research.

## Dictionary Profiles

- `dist/s4r0ut-strict.txt`: high-signal Moroccan profile.
- `dist/s4r0ut-mini.txt`: compact demo and awareness profile.
- `dist/s4r0ut-standard.txt`: default profile for internal authorized audits.
- `dist/s4r0ut-extended.txt`: broader research profile.

## Rule Files

- `rules/morocco-basic.rule`: capitalization, short numbers, and common symbols.
- `rules/morocco-years.rule`: year and Morocco-code motifs.
- `rules/morocco-separators.rule`: separators such as `-`, `_`, `.`, `@`, and `!`.
- `rules/morocco-leet.rule`: lightweight leetspeak substitutions.

## Defensive Use

Use these artifacts only where you have explicit authorization. Good use cases:

- validating password policy improvements
- measuring weak-password exposure in an internal lab
- training users on predictable local password patterns
- comparing Moroccan-focused patterns against generic dictionaries

Do not use this project for unauthorized login attempts, credential stuffing, or
attacks against systems you do not own or administer.

