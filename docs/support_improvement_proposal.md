# A clearer path from correction request to support decision

Status: proposed service workflow, November 9, 2026. Not piloted or validated.
This public proposal contains no actual incident narrative, account information,
transaction details or reconstructed support quotations.

## Purpose

Make a correction request understandable when self-service cannot complete it.
The goal is a clear decision and visible next steps, not an automatic refund or
a requirement to build another AI product. A justified denial can complete a
support decision without granting the customer's preferred outcome.

## Proposed handling

1. Preserve the original request and correction-attempt time. Explain the
   available path during pending payment and after settlement without promising
   eligibility or outcomes that have not been determined.
2. Acknowledge the failed self-service step. Retain supplied context and avoid
   asking for it again unless there is a necessary reason. Explain why a repeated
   step could now work if a relevant condition changed.
3. Separate the decisions: eligibility explanation, missing information and
   exception review. Route only to review paths actually authorized by policy.
4. Acknowledge ownership and next action. State the responsible team or queue,
   what remains pending, and a realistic update expectation. Do not equate routing
   with a completed individual review or promise an exception.
5. Provide a specific decision. Explain the applicable condition and relevant
   case facts to the appropriate level of detail; identify any available review
   path. An unfavorable outcome is not by itself evidence of poor handling.
6. Confirm execution separately. If a remedy is approved, verify that the
   correction took effect. When execution evidence is absent, say it is unknown.

Possible visible states include awaiting settlement, awaiting customer
information, pending authorized review, decision explained and remedy execution
confirmed. These are proposed labels, not observations of any vendor's system.

## Checkout inspection questions

Is the term explicitly chosen? Does the chosen option persist? Is the full
immediate charge clear beside final confirmation? Can a mistaken choice be
corrected through an understandable path? Inspect the actual interface before
making a vendor-specific claim. Confusion does not establish intent.

## A falsifiable improvement pilot

With consented data, define the observation window, inclusion rules and
completion criteria before comparing the proposed workflow with existing
practice. Retain original histories and legitimate-denial/necessary-retry controls.
Do not improve a metric by omitting difficult or unknown cases.

| Proposed measure | Definition to fix before collection |
| --- | --- |
| Decision completeness | Decisions meeting a stated explanation/next-step checklist divided by all decisions in scope |
| Repeated referrals | Cases receiving an unchanged failed-step referral without a stated useful change, divided by cases with a prior failed step |
| Repeated information requests | Cases asked again for already supplied information without a recorded necessary reason, divided by eligible cases |
| Review acknowledgement | Eligible review requests with a visible owner/next action acknowledgement, divided by all eligible requests |
| Decision and execution time | Separate intervals from request to complete decision and from approval to confirmed execution; report pending cases and cutoffs |
| Customer understanding | A defined check of whether the customer can identify the next step; satisfaction is recorded separately |

No baseline values, target improvements, sample size or achieved effect is
invented here. The pilot design must justify these choices before collection.
Customer-visible evidence may be incomplete; report missing context and the
review effort needed to apply the checklist.

## Relation to the case study and optional software

Personal observational writing can present a reported timeline, sources,
unknowns and recommendations without passing an automated-product benchmark.
It cannot establish prevalence, manipulation, refund entitlement or efficacy
from one account. Stronger incident claims need their supporting artifacts.

The existing SupportLoop toolkit is supporting methods infrastructure. Its
synthetic agreement fixtures do not establish effectiveness of this workflow.
Independent labeling and comparison gates apply before expanding automated
classification or making accuracy, superiority or market-demand claims.
