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

## November 8, 2026: public foundation verified

Created [howlcipher/supportloop](https://github.com/howlcipher/supportloop) as a
public repository and pushed the signed initial commit
[5e5da13](https://github.com/howlcipher/supportloop/commit/5e5da138925d351640da49f727867bf996752867).
GitHub reports the signature as verified. The
[initial hosted run](https://github.com/howlcipher/supportloop/actions/runs/42505873947)
completed successfully: Python 3.11 and 3.14 regression, packet verification,
lint, static analysis, dependency audit and Git history secret scanning.

M0 is complete for that initial publication. This entry records that observed
run; subsequent commits have their own GitHub checks and must remain green.
The 24-case study still has zero independent human returns. No analyzer,
accuracy claim, real incident account or case-study result has been released.
Next work is GAP-001 under M1, with behavior-first tests and the same regression
and privacy boundaries. Missing human evidence remains a separate dependency.

## November 8, 2026: upstream checkout UX question

Added RES-005 and a checkout UX methodology for the possibility that a preselected
12-month plan makes an intended one-month purchase easier to get wrong. The plan
covers selection persistence, commitment visibility, interaction/accessibility
checks and a possible controlled comparison using fictional checkout screens.
It does not assert a vendor-specific default, a measured causal effect or
predatory intent. The original real-world observation remains local and has
not been independently verified. No real checkout was accessed, no payment
was made and no participant study ran. This documentation change does not
implement an analyzer or change the synthetic packet or its research gates.

## November 8, 2026: completed-review infrastructure

Implemented GAP-001 and GAP-002 using behavior-first tests: strict completed
CSV/metadata intake, snapshot-bound identities and references, immutable
submission copies and per-dimension descriptive agreement reports. Explicit
synthetic provenance requires packet 0.3.0 and rubric 0.2.0. There were no
existing human returns to migrate; case observations are unchanged.

The deterministic demo produces passing, failing and undefined numeric-gate
examples while keeping the human gate pending. Fixture labels are arbitrary
arithmetic inputs, not semantic judgments or independent human labels.
The current local regression has 48 tests. Final hosted checks must correspond
to the pushed commit; source-level test success is not a study result.

An isolated code reviewer found a packet snapshot race. A failing real-edit
regression reproduced it, and the reviewer rechecked the immutable-snapshot
correction. Author-side tests also exposed a response reread race and a Python
3.11 symlink-loop traceback. No tracked files or private inputs were changed
by the reviewer. See review_m1.md for all findings and scope limits.

HowlProof supported two supplied arithmetic checks and left the practical
usefulness hypothesis inconclusive. Its overall result remains
INSUFFICIENT_EVIDENCE. HowlWriter normalized and linted three local sharing
drafts without model calls. Those drafts remain ignored for owner review; the
incident narrative is owner-reported and no recipient was contacted.

M1 software is ready for final regression and public review. M2 remains pending:
no independent human returns exist. The shareable artifact is a reproducible
research toolkit and preliminary methods report, not a validated resolution
classifier or a verified investigation of a vendor.

## Completion decision and owner review packet

PR 1 merged as signed, verified commit 4c5be0d74d6f5cc88bacaebce8c5e7003d7e7a94.
Merged-main CI 42528811778 passed Python 3.11/3.14 regression and security checks.
The discovery completion record consolidates the NARROW decision and exact
external inputs. Local evidence worksheets and review invitations are prepared;
no reviewer or vendor contacted. No classifier or semantic outcome is claimed.

## Public showcase and requested provider reviews

AGY Gemini and Claude Code separately reviewed the same frozen public source
snapshot at 8e9e741. AGY returned four findings; Claude returned thirteen after
an interrupted no-result invocation and a successful retry. Neither received
private material or the other's output, executed tests or labeled study cases.
All 17 findings are preserved with dispositions in docs/provider_reviews.md.
HowlPlane reconciliation records 11 confirmed (corrected), one false positive
and five explicitly retained out-of-scope limitations/prerequisites.

Coordinator reproductions verified the demo E1 assumption, nonfinite-float
parser gap, a vacuous independence regression and symlinked-temp test failures.
Existing contracts were strengthened, not replaced by duplicate assertions.
The strengthened independence test rejects a mutant that survived the old test.
Current local regression has 55 tests; hosted evidence must follow final merge.

A semantic HTML/CSS research showcase includes citations, methods, synthetic
arithmetic, actual limits and a dedicated original PNG sharing card. Only site/
is deployed, after existing regression/security jobs pass on main. Browser
checks reproduced and corrected narrow-screen table/navigation overflow; final
1440/390/320 layouts and keyboard skip navigation passed without page errors.
GitHub Pages was enabled for workflow publishing. Live publication is pending
successful integration and deployment; no actual incident or draft was uploaded.
