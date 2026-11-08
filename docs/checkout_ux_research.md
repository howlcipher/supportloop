# Checkout defaults and accidental commitment

Status: research hypothesis; no vendor-specific checkout inspected or tested.
This document proposes an upstream UX investigation, not a finding of intent,
wrongdoing or legal noncompliance. The public repository contains no real
checkout screenshots, account records or payment information.

## Question

Can preselecting a 12-month subscription make an unintended annual commitment
easier when a customer intends to buy one month? Does the interface make the
selected term and total charge clear enough for that customer to notice and
correct the mismatch before confirming?

Potential impact extends into support: a checkout error may create a refund
request, followed by repeated correction effort. That is a hypothesis about the
purchase-to-support journey, not proof that a particular interface caused a
particular purchase or that a later support decision was incorrect.

## Distinguish observation from interpretation

| Proposition | Evidence needed | Current status |
| --- | --- | --- |
| An annual plan is selected by default | Dated, consented capture of initial page state and account/session context | Not independently verified |
| A previously selected monthly plan changes or fails to persist | A reproducible sequence capturing selection, navigation and the final confirmation | Not tested |
| The default increases accidental annual commitment | Controlled usability comparison with an explicit one-month purchase task | Not tested |
| Duration and total charge are easy to miss | Inspection plus measured comprehension and interaction errors | Not tested |
| The design is predatory or intentionally manipulative | Evidence beyond one confusing experience or a default selection | Not established |

Preserve a participant's description as a report, without upgrading it into an
independently verified UI fact. A current capture cannot establish what an older
checkout showed. A default may depend on a promotion, prior choice, device,
region, session state or experiment variant; record those possibilities rather
than assuming one global design. A disputed UI assessment does not settle refund
eligibility or establish what a support agent reviewed internally.

## Inspection checklist

1. Record the selected option on first load, its source and any remembered choice.
2. Inspect whether term length, total amount due now and renewal information are
   visible near selection and again at the final commitment action. Distinguish
   a monthly equivalent from the actual charge.
3. Record click targets, visual hierarchy and selection indicators. Test whether
   promotional artwork or emphasis obscures the selected option.
4. Check whether an explicit monthly choice persists through navigation, reload
   and confirmation. Do not transact to test persistence.
5. Check keyboard focus, accessible control names, announced selection state,
   zoom and mobile presentation. Record tested conditions instead of claiming
   accessibility conformance from a screenshot.
6. Determine whether the confirmation clearly summarizes the chosen term and
   permits correction before payment.
7. Map postpurchase correction steps separately: pending payment, self-service
   eligibility results, explanation quality and access to authorized review.

Do not access a private account or complete a purchase automatically. Any real
capture requires consent, redaction and an evidence record before analysis or
publication. Do not infer initial focus or interactive behavior from a still image.

## Small falsifiable usability experiment

If this research branch is pursued, use fictional checkout mockups with no real
payments or vendor branding. Compare a preselected annual plan against explicit
plan selection with no default, holding prices, wording and visual emphasis
constant. An optional monthly-default arm is a separate, preregistered contrast.
Do not silently compare multiple changing design factors.

Give participants the same goal: select and confirm a one-month subscription.
Measure selected term before confirmation, recognition of duration and total
charge, corrections, completion time and confidence in the choice. Define
accidental annual commitment as selecting the annual option despite the stated
one-month goal, and separately measure whether the participant notices it.

Preregister hypotheses, sample-size rationale, assignment, exclusion rules and
analysis before recruitment. Prefer between-participant assignment to avoid
learning the alternate layout; document any different design. Use meaningful
confidence intervals and report null results. No participant data, usability
session or experiment has been collected here. Stop this branch if it distracts
from resolution auditing without explaining a useful customer-effort mechanism.

The support audit must keep the initial purchase mistake, decision completeness,
procedural quality and verified resolution separate. UI friction does not turn
an otherwise justified policy decision into a handling defect.
