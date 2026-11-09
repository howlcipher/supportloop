# SupportLoop agent instructions

Read README.md, docs/rubric.md and docs/evaluation_contract.md before work.
Honor ~/.howlplane/.agents/rules/ and check ~/.howlplane/.agents/skills/.

This is a public feasibility study, not a deployed product. All evaluation histories
are synthetic. A separate owner-authorized observational case study omits provider
and game names; it is not benchmark data or independently verified.
Do not read author_material/ before a blinded review. Reviewer packets contain
only observations. Author expectations are hypotheses, never independent labels.
Do not identify model agreement as human agreement. No product analyzer until
the human feasibility gate passes. Publication of this synthetic repository is
authorized. Private evidence and real incident publication still require explicit
consent for the material and destination. On November 9, 2026 the owner authorized
the constructive case-study narrative and PDF on the SupportLoop public site
and its source repository. This does not authorize raw private artifacts, external
messages, LinkedIn posting or claims beyond the reported evidence cutoff.
Author hypotheses and review returns
stay ignored. Public verification must work without those local files.

Use Python 3.11+ and standard library runtime dependencies for packet tooling.
Run python3 -m unittest discover -s tests -v while changing validation behavior.
The final gate is python3 scripts/verify_packet.py, unittest, and
python3 -m flake8 scripts tests, Bandit and dependency audit.
See documentation/TESTING.md for exact commands and the public-export gate.

Read ROADMAP.md and issues.md, take the highest-priority unblocked item, and
update docs/journal.md at meaningful checkpoints. Reproduce a bug or define a
new observable contract in tests before implementation. Use cohesive objects
where they own state or invariants, and share validation logic instead of
duplicating it. Avoid inheritance or abstractions without a concrete need.
Retain compatibility entry points unless a documented migration is warranted.
Run the complete configured regression on the final tree before pushing; verify
hosted CI. Sign commits. No fabricated reviewers, metrics or permissions.

The current public edition omits provider and game names at the owner's request.
Earlier named files are archived locally; Git history is not rewritten.
