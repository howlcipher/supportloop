# SupportLoop: Answered Is Not Resolved

Open research into evidence-backed support-ticket audits.
Recommendation remains **NARROW**. This is a research packet and integrity checker,
not a support analyzer or a released product. There are no measured accuracy,
customer-value or market-demand results.

See the [discovery completion decision](docs/completion_decision.md) for completed
work, evidence boundaries and the exact inputs still required.

The [GitHub Pages research showcase](https://howlcipher.github.io/supportloop/)
presents the public methods, findings and limitations with a dedicated project
sharing image. Deployment uses pinned Node 24 actions on Ubuntu 24.04.
See [site operations](docs/site.md) for deployment and preview checks.

The immediate practical deliverable is a [support improvement proposal](docs/support_improvement_proposal.md)
and an [experience-led subscription support case study](https://howlcipher.github.io/supportloop/case-study.html).
The narrative is customer-reported through November 8, 2026 and not independently
verified. Its [source text](docs/subscription_case_study.md) and downloadable PDF explain
limits and propose improvements; no pilot result or refund entitlement is claimed.
Optional product validation remains
gated; it is not a prerequisite for an honestly qualified observational account.

## Current deliverables

1. Twenty-four synthetic histories with 103 observable events in data/cases.json.
2. A versioned [labeling rubric](docs/rubric.md) and [evaluation contract](docs/evaluation_contract.md).
3. Two observation-only [reviewer packets](reviewer_packets/), separately ordered,
   with blank CSV forms. Give each reviewer only their directory.
4. Author expectations kept locally outside the public distribution, not used as gold labels.
5. A hashed packet manifest and standard-library structural checker with failure tests.
6. [Architecture](docs/architecture.md), [Howl coordination](docs/howl_workflow.md),
   [prior art](docs/prior_art.md), and a [case study plan](docs/case_study_plan.md).
7. Strict completed-review intake and descriptive agreement reports, with a
   [reproducible arithmetic demo](docs/review_protocol.md).

**Human feasibility gate: PENDING.** Independent human reviews have not been collected.
No human agreement, adjudication, model-based ticket analysis or product
implementation has occurred. A successful packet check does not pass this gate.

## Try the research toolkit

Python 3.11+ runs the demo without installing runtime dependencies:

```bash
python3 scripts/verify_packet.py
python3 -m scripts.demo_reviews --out runs/first_demo
python3 -m scripts.review_tools compare --left runs/first_demo/agreement_synthetic_a.csv --left-metadata runs/first_demo/agreement_synthetic_a.json --right runs/first_demo/agreement_synthetic_b.csv --right-metadata runs/first_demo/agreement_synthetic_b.json
```

Use a new destination each time; existing directories are refused. The demo
produces generated arithmetic fixtures, not support judgments: 22/24 agreement
with kappa 0.875, complete disagreement, and undefined kappa for one-category
agreement. Every report keeps the human gate pending. No accuracy or customer
benefit is demonstrated. See [engineering findings](docs/engineering_findings.md)
for scope and limitations. Invoke the new tools with `python3 -m scripts...`.
See [sharing guidance](SHARING.md) for a defensible early-project demonstration
and the evidence still needed for an incident case study.

## Run local checks

Python 3.11+ is the intended tooling baseline. Runtime uses only the standard
library. Development checks use the tools pinned in requirements_dev.txt.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements_dev.txt
```

Run the checks with that environment's interpreter:

```bash
.venv/bin/python scripts/verify_packet.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m flake8 scripts tests
```

See [testing and impact assessment](documentation/TESTING.md). HowlPlane can run
the same commands from .ai-project.toml; actual run records belong in runs/.
For Plane, select the project environment explicitly with
`VIRTUAL_ENV="$PWD/.venv" howlplane --repo . verify --project-dir .`.
Dependency installation contacts the package index. The packet checker, tests
and lint run locally without model calls or private data. See the CI workflow
for separate security checks, including an advisory-database dependency audit.

## Review safely

The coordinator may keep local author expectations in the ignored author_material/
directory; no published command or test requires them. Distribute only
reviewer_packets/A or B to each reviewer. The packet
contains synthetic observations, not the owner's incident or a real vendor's
policy. Reviewer instructions distinguish supported outcomes, explained denials,
procedural concerns and unknowns. Store completed returns in ignored
review_returns/, preserving original submissions and hashes.

The [review protocol](docs/review_protocol.md) defines complete CSV/metadata
submissions and report interpretation. Intake checks digests and references;
it does not authenticate reviewers or assess semantic correctness. There is no
automatic ticket grader. Do not report author-label agreement as accuracy or
add a classifier before the human and benchmark gates are satisfied.

## Scope and limitations

Established support QA documents solution-offered checks, custom rubrics, effort,
reopening and inferred resolution. Offering a solution does not prove execution.
The unvalidated gap is a portable, local,
inspectable evidence contract. We may conclude that a rubric or an integration
is more useful than a separate product.

This selected synthetic set cannot estimate real failure rates, legal rights,
vendor wrongdoing, or production performance. Hashes detect byte changes, not
truth. Packet separation is procedural blinding, not filesystem isolation.
Instruction-like text is deliberately included as untrusted case data.

## Project work

Follow the gated [roadmap](ROADMAP.md), [findings and bugs](issues.md), and
[engineering journal](docs/journal.md). Contributions follow [TDD, OOP and DRY](CONTRIBUTING.md).
Packet version 0.3.0 and rubric 0.2.0 add explicit synthetic review provenance
and completed-review metadata. No prior human returns existed to migrate; old
version metadata is rejected. No human result or classifier release is implied.

Code and synthetic study material are provided under the [MIT license](LICENSE).
This repository and the bounded observational case narrative are
authorized for publication. Additional private incident artifacts, new destinations
or empirical claims still require their supporting evidence and appropriate consent.

An [upstream UX research plan](docs/checkout_ux_research.md) examines whether
annual-plan defaults can make an intended one-month purchase error-prone.
This remains a hypothesis, not a verified finding about a vendor or its intent.

The current public edition omits company and game names to focus on process
improvement. Published branch history was subsequently rewritten with owner authorization.
Old pull-request references, caches and external clones may retain the earlier
edition; this is not a guarantee of de-identification. See the
[history rewrite record](docs/history_rewrite.md) before using an older clone.

The [comprehensive audit](docs/audit_report.md) records reproduced findings,
scoped HowlProof results and remaining evidence limits. The optional
[engineering audit contract](coordination/howlproof_audit.yaml) supplements the
original documentation-only Proof configuration; neither validates ticket outcomes. The case source, rendered article and PDF
remain bound to the same editorial revision.
