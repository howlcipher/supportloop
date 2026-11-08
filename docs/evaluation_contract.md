# Feasibility evaluation contract

Packet contract version: 0.3.0. Rubric: 0.2.0. Human review pending.

## Question and authority

Can independent human reviewers distinguish a visible support-handling defect
from an unfavorable decision or an unknowable outcome using the same rubric?
This 24-case convenience sample is a feasibility exercise, not a prevalence
study, accuracy benchmark, or proof of market demand. Cases and author hypotheses
were authored by Codex; no independent labels have been obtained.

The public manifest locks the exact rubric, observations and reviewer templates.
Local author hypotheses are excluded and are not required to verify a checkout.
Hashes detect drift, not authenticity. Record any revisions
as a new packet version before collecting labels; never overwrite completed
returns. Filesystem separation provides procedural blinding, not access control.

## Independent labeling and agreement

Give each of two humans only their reviewer_packets/A or B directory. Neither
reviewer may be the case author or see author expectations. Copy completed
labels into ignored review_returns/ with collection time, rubric hash, case hash,
reviewer identity pseudonym and independence attestation. Do not place real names
or private histories in this synthetic packet. No reviewer contacts are initiated
by the tooling. It performs no uploads or model calls.

Require 24 completed audit_label fields per reviewer with rationale and valid
references. Reject invalid values; do not silently drop rows. Report unresolved
or incomplete returns as missing review, never as agreement. Reviewers can use
insufficient_evidence; this is a real category, not a missing row.

Primary endpoint: unweighted raw agreement and Cohen's kappa on the three
audit_label categories before adjudication. Gate: at least 20 of 24 labels agree
(the smallest count meeting 80 percent) AND kappa at least 0.70. Report the full
3-by-3 confusion matrix, marginal counts and uncertainty. If expected agreement
equals one, kappa is undefined and the gate is inconclusive. Discuss prevalence
sensitivity; the small selected sample makes this a planning gate only.

Report separate agreement and disagreements on outcome, decision and procedure,
and on author-designated justified-denial controls. Primary agreement does not
hide systematic confusion on those controls. A shared tendency to flag justified
denials, label silence as success, or infer unseen misconduct requires revising
the rubric even when aggregate agreement passes. Customer satisfaction is
descriptive and never the reference label for correctness.

Adjudication happens after recording disagreements. An adjudicator must read
the evidence and record reasons; author expectations cannot overrule independent
reviewers. Amend ambiguous cases into a new version and obtain fresh review.
No false-positive or accuracy claim against the author's key is allowed.

## Stop and go

| Condition | Action |
| --- | --- |
| No independent humans | Keep PENDING; finish packet checks only |
| Review infrastructure without humans | Intake validation, descriptive arithmetic and explicitly synthetic demonstrations are allowed; no semantic classifier or human-gate certification |
| Agreement below gate or semantic contradiction in controls | Revise rubric or stop; no analyzer |
| Gate passes with defensible controls | Design an independently labeled benchmark and recheck prior-art adequacy |
| Existing configured QA meets the constrained workflow | Prefer configuration, an integration or rubric over another product |
| Baselines match candidate later | Keep the simpler method or stop product expansion |

After feasibility, proposed performance work uses 40 development and 160 locked
test histories, separate scenario families and independent labels fixed before
implementation. Original target counts of 80 defects and 80 controls are sampling
goals, not labels to impose on reviewers. Preserve ambiguous cases, report their
counts, and do not silently exclude them to hit target balance. Final evaluation
handling must be preregistered before collection. These 24 cases are exposed
development material and may never enter a locked test set.

Proposed later gates: precision at least 90 percent, recall at least 80 percent,
control false-positive rate at most 5 percent, zero false defect accusations on
at least 40 justified-denial or legitimate-restriction controls, and at least ten
percentage points incremental recall over the strongest automated baseline at
matched precision. Count abstentions in recall and report coverage separately.
Report exact counts, uncertainty and costs. Do not claim commercial-system
outperformance without a same-input configured comparison. Synthetic results
alone do not establish production value.

## Independence and reproducibility limits

Independent execution, independent evidence, independent human labels and
independent authorship are different properties. HowlProof can check structural
contracts but cannot certify semantic ticket resolution using its existing
research checker. AI reviewers may critique packet defects if clearly labeled;
they cannot satisfy this human gate. No generated rationale counts as evidence
of market demand, vendor wrongdoing, or hidden case activity.

The review tool reports a numeric threshold separately from the human gate.
Even MET with self-declared human metadata leaves the human gate PENDING until
independence and control cases receive separate review. A successful CLI exit
means a report was produced, not that the study passed. Synthetic fixture labels
exercise validation and arithmetic only; they are not independently labeled
support scenarios. Wilson intervals describe raw agreement under an approximation
and do not establish population reliability for this selected sample.
