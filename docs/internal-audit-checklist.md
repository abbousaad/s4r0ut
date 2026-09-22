# Internal Audit Checklist

Use this checklist when applying s4r0ut in an authorized internal password-policy
review or lab assessment.

## Authorization

- Written authorization exists.
- Scope is documented.
- Systems, accounts, and data sources are approved.
- Testing window and contacts are defined.
- Results handling is agreed in advance.

## Data Handling

- No fresh private leaks are imported.
- No account dumps are committed or shared.
- Any test hashes are synthetic, internal, or explicitly authorized.
- Findings are reported in aggregate where possible.
- Sensitive outputs are stored according to internal policy.

## Profile Selection

- Use `strict` for quick high-signal checks.
- Use `mini` for demos and awareness.
- Use `standard` for practical internal policy testing.
- Use `extended` only when broader research coverage is justified.

## Execution Notes

- Record the s4r0ut commit hash.
- Record the release report hash for each dictionary used.
- Record all extra rules or filters.
- Avoid testing beyond the approved scope.
- Stop if unexpected sensitive data appears.

## Reporting

- Focus on policy, training, and remediation.
- Do not shame individual users.
- Recommend password-manager adoption.
- Recommend MFA for critical accounts.
- Add local weak-pattern examples to awareness content without exposing real user secrets.

