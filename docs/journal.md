# Engineering journal

Public entries contain synthetic-only engineering progress. Private execution
logs, local paths, author expectations and review returns are excluded.

## November 8, 2026: discovery and feasibility preparation

Research found extensive overlap with mature QA: solution quality, configurable
rubrics, effort, reopening and inferred resolution already exist. Recommendation
was NARROW to a portable evidence-auditing experiment. No market gap or product
performance was established. Primary sources are in prior_art.md.

Prepared 24 synthetic histories with 103 events, rubric 0.1.0, two observation-only
reviewer packets, separate author hypotheses and 15 structural regression tests.
HowlPlane ran the project gates after its environment was selected explicitly.
HowlDream clustered externally authored hypotheses and generated none.
HowlWriter lint checked the rubric and contract. HowlProof compared rubric copies
and inventoried documentation claims; its overall verdict was
INSUFFICIENT_EVIDENCE. No semantic resolution claim followed from these checks.
Human review remains pending. No real incident material is included.

## November 8, 2026: public foundation started

The owner authorized a public repository, roadmap, journal, findings backlog,
TDD, OOP and DRY. Python is available; .NET is not a dependency.

Reproduced the public-checkout dependency on local author expectations and three
malformed-input defect groups before implementing fixes. Introduced a cohesive
PacketVerifier object that owns packet reads and validation. Retained the
existing verify(root) entry point and the original regression contracts.
Shared JSON loading rejects duplicate keys and nonfinite constants; CSV checks
reject surplus cells. Reads are bounded and path resolution refuses escapes.

Published-material scope is synthetic data, source, methodology and engineering
documentation. Author expectations, review returns and local run logs are
ignored. Packet contract revision 0.2.0 removes the private-file dependency;
the labeling rubric remains 0.1.0. The source distribution must be tested without
local-only files before upload.

Added the gated roadmap and findings report. Next implementation work is strict
completed-review intake, followed by descriptive agreement tooling. Neither can
substitute for missing human labels. Shipping evidence is recorded in the next
journal entry after the final regression and public export checks execute.

## November 8, 2026: prepublication verification

The local final source passes 23 tests on Python 3.11 and the host Python 3.14.
HowlPlane's three declared gates pass: lint, packet integrity and unittest.
Bandit reports no findings in runtime tooling. Dependency auditing of the pinned
development requirements reports no known vulnerabilities at the time checked.

A temporary export of only staged public files also passes all 23 tests, packet
verification, lint, Bandit and a redacted gitleaks scan. The export contains no
author hypotheses, review returns, private evidence, run logs or virtualenv.
Git whitespace checking prompted normalization of the CSV templates to LF;
manifest hashes were updated before verification. The five corrected defects
are listed in issues.md. No semantic accuracy or human agreement was measured.

The next shipping step is a signed initial commit and the authorized public
repository push. Hosted CI must be observed after that push. The next engineering
item remains GAP-001, completed-review intake; the human research gate is pending.
