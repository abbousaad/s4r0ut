# Awareness Lab

This lab helps teams understand why local password patterns matter without
testing real accounts or exposing private data.

## Goal

Show how predictable Moroccan-specific patterns can weaken passwords, then turn
that lesson into better password-manager adoption, stronger passphrases, and
better authentication policy.

## Audience

- Security awareness sessions
- University cybersecurity clubs
- Internal blue-team training
- Password policy workshops

## Safety Rules

- Use only toy hashes, demo accounts, or synthetic examples.
- Do not test real user accounts.
- Do not collect participant passwords.
- Do not ask people to reveal old or current passwords.
- Do not run tests against systems without written authorization.

## Suggested Flow

1. Explain local password patterns.
2. Show examples from `dist/s4r0ut-strict.txt`.
3. Compare generic weak passwords with Moroccan-specific variants.
4. Demonstrate safer alternatives: long passphrases, password managers, and MFA.
5. Close with a policy checklist users can apply immediately.

## Demo Dataset

Use a tiny synthetic file for training:

```text
casa2024
khoya123
maghrib212
wydad2024
zin@123
```

These examples are intentionally simple and should not be treated as real
passwords from real users.

## Discussion Prompts

- Which patterns feel local or familiar?
- Which patterns are easy to guess from public context?
- How can password managers remove the need for memorable but weak patterns?
- What should an organization block, warn about, or monitor in password policy?

## Recommended Takeaways

- Do not use names, cities, clubs, phone-like motifs, or recent years.
- Prefer password managers and unique generated passwords.
- Use MFA, especially for email, banking, cloud, and admin accounts.
- Treat password education as a design problem, not a blame exercise.

