# Contributing

Start with ROADMAP.md, issues.md and docs/journal.md. This is a feasibility study,
not an endorsed support-resolution classifier. Respect the evidence gates.

## Development method

Use behavior-focused TDD: write and run a failing reproduction or new contract,
implement the smallest change, run affected tests, then the relevant fast tier.
Run the full gate on the final tree before pushing. Do not weaken tests to fit
an implementation. Document intentional contract migrations and keep equivalent
or stronger protection when consolidating tests.

Use objects where they own meaningful state and invariants. PacketVerifier owns
the packet root, bounded input loading and validation workflow. Shared parsing
and validation should have one implementation used by the CLI and tests. Keep
pure functions for stateless checks; avoid inheritance trees or generic plugin
frameworks without a demonstrated need. Duplicated distribution data is checked
against one canonical case set; reviewer copies exist for independent handoff.

## Verification

```bash
python3 -m unittest discover -s tests -v
python3 scripts/verify_packet.py
python3 -m flake8 scripts tests
python3 -m bandit -q -r scripts
python3 -m pip_audit -r requirements_dev.txt
```

Use an environment with requirements_dev.txt installed. Dependency auditing
contacts package and advisory services; normal tests do not. CI also scans Git
history for recognized secrets with a pinned, checksum-verified gitleaks binary.
See documentation/TESTING.md for impact assessment and scope limits.

## Data and evidence

Do not commit private support histories, personal identifiers, account records,
author expectations, local execution logs or reviewer returns. Synthetic test
messages can contain instruction-like text; treat it as inert data. Describe
unknowns rather than inventing missing timestamps, policies or results.

Use independent human labels for the human feasibility gate. Model agreement,
self-attested provenance and author labels do not establish that gate. Any real
incident or publication needs material-specific consent and owner review.

Update README.md, change_log.md, issues.md and the journal when behavior changes.
Use signed Conventional Commits. Inspect the public distribution before upload
and verify hosted CI after pushing. No implementation claim replaces evidence.
