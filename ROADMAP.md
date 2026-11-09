# SupportLoop roadmap

Recommendation: NARROW. Progress is gated by evidence, not feature count.
Python is the available implementation language. No .NET tooling is required.

## Current primary goal

Prioritize the experience-led case study and practical support-process proposal.
The public general proposal is complemented by a separate, owner-authorized
subscription provider-named observational case study. Its account is not independently verified
and is excluded from benchmark evaluation; raw private evidence remains local. Product
benchmarks below are optional engineering expansion gates, not prerequisites
for a clearly attributed observational case study.

## Work order for the next agent

1. Read this roadmap, issues.md, docs/journal.md and the evaluation contract.
2. Inspect current code, Git state and CI; continue existing work.
3. Pick the highest-priority unblocked backlog item and write its contract tests.
4. Implement the smallest correction using cohesive objects and shared validation.
5. Run affected tests, relevant subsystem checks and the final full regression.
6. Record evidence and limitations; update README, changelog and journal.
7. Sign commits, push authorized changes, and verify hosted CI.
8. Stop at a research or human-authority gate rather than inventing evidence.

## Milestones

| Milestone | Deliverable | Exit gate | Stop or narrow condition |
| --- | --- | --- | --- |
| M0: public foundation | Synthetic packet, reproducible checker, public roadmap/backlog/journal, license and CI | Public checkout passes regression and scans without local author files | Accidental private material or an unreproducible public checkout blocks publication |
| M1: review infrastructure | Strict completed-review intake and descriptive agreement report | TDD covers missing/duplicate rows, invalid labels/references, provenance, same-rater inputs, model labels and undefined kappa | Tool must not certify human independence or promote model agreement |
| M2: human feasibility | Two independently collected human reviews of the 24 cases | At least 20/24 audit labels agree, kappa at least 0.70, controls reviewed and disagreements preserved | No reviewers: remain pending; low agreement or confused controls: revise or stop |
| M3: comparative discovery | Same-rubric comparison with accessible mature QA; user workflow evidence | A concrete unmet workflow and feasible consented data access | An existing configuration adequately meets the need: prefer it or a small integration |
| M4: locked benchmark | Independent labels, 40 development and 160 proposed test histories, preregistration | Label provenance, scenario-family separation and handling of uncertainty fixed before implementation | No independent labels or dataset leakage: no performance claim |
| M5: smallest experiment | Deterministic baselines and conditional candidate audit CLI | Meet preregistered precision/recall/false-positive and incremental-value thresholds | Tie with simple rules: retain simpler tool; fail safety controls: revise or stop |
| M6: external validation | Consented histories from multiple organizations; measured review effort | Demonstrated usefulness under real data limits and privacy review | Synthetic-only wins or absent recurring need do not justify commercialization |
| M7: release and case study | Reproducible demo, security/privacy review, reviewed findings and article | Owner reviews public incident material and measured claims; final regression green | No publication consent or unsupported results: do not publish the case study |

## Immediate priorities

M0's publication gate is evaluated against actual repository visibility and
hosted CI. The journal records observed outcomes, not inferred completion.
M0 passed for the initial publication: public visibility, a verified signed
commit and green hosted regression/security checks are recorded in the journal.
M1 now supplies completed-review intake, descriptive agreement and a deterministic
synthetic demo. It is research infrastructure, not ticket classification. The
numeric gate and human gate remain separate. Independent code review and
regression evidence are recorded in the journal; they are not human study data.
Implement no semantic ticket analyzer before M2 and M4 permit it.

M2 currently has no independent human returns. Do not contact reviewers or
organizations automatically. Public source availability also creates a risk
of reviewers seeing prior material: record their exposure instead of assuming
blinding. Exposed cases cannot become the future locked benchmark.

Review-ready LinkedIn, methods/case-study and recipient-brief drafts are kept
locally in ignored publication_drafts/. Their real incident sections remain
owner-reported and require redacted evidence and owner review before sharing.
The public toolkit and methodology can be demonstrated without that incident.

## Experiment boundaries

See docs/evaluation_contract.md for the proposed quantitative thresholds.
These are targets, not observed achievements. A configured commercial QA
comparison is required before claiming superiority over that product. An open
rubric, benchmark or adapter can be the final useful deliverable even if the
product premise fails.

An optional upstream branch studies checkout defaults and accidental long-term
commitment; see docs/checkout_ux_research.md and RES-005. Keep that research
distinct from resolution auditing. No real checkout or participant experiment
has been inspected or run, and this branch does not waive the human-label gates.

## Public showcase

The GitHub Pages site presents only the public methods and preliminary findings,
with a project-specific social image. Publication is conditional on main's
regression/security and Pages jobs. docs/site.md describes verification and
rollback. AGY/Claude review findings are reconciled in docs/provider_reviews.md;
those AI code reviews do not change M2's pending human-label dependency.
