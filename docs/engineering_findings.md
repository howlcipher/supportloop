# Answered Is Not Resolved: engineering findings so far

Status: preliminary methods and software report. No independently labeled
support-resolution experiment has been completed. Recommendation remains NARROW.

## Problem and prior art

A workflow status, a substantive decision and a fulfilled customer objective
are distinct facts. A justified denial may complete a support decision while
leaving the requested benefit unfulfilled. An unseen outcome may remain unknown
despite a polite response or a closed ticket.

Broad QA functionality overlaps mature products. Zendesk documents solution
and comprehension categories and customizable autoscoring. Intercom separately
defines answered conversations and assumed versus confirmed resolutions.
Those documents establish documented feature overlap, not measured accuracy or
adequacy for this proposed workflow. [Zendesk categories](https://support.zendesk.com/hc/en-us/articles/7043747123354-Understanding-autoscoring-categories),
[Intercom metrics](https://www.intercom.com/help/en/articles/7022438-reporting-metrics-attributes).

A possible opportunity is a portable, inspectable evidence contract for
local exports. It may turn out that an existing QA configuration, a rubric or
an integration is sufficient. No user interviews, purchasing evidence or
same-input commercial-tool comparison have established a market gap.

## Implemented scope

This research toolkit contains 24 synthetic histories with 103 events,
observation-only review packets, a versioned rubric, strict completed-review
intake, and descriptive agreement reports. It validates referenced event IDs,
not the truth or relevance of a reviewer's interpretation. It does not extract
the customer's objective automatically or classify a ticket's resolution.

Python's standard library handles local files, hashing, CSV validation and
statistics. PacketVerifier owns packet boundaries and shared parsing. ReviewStudy
binds completed submissions to one packet/rubric identity; immutable submission
copies limit accidental mutation. The CLI and library use the same logic.
An HTTP service was deferred because it adds an attack and deployment surface
without helping the current file-based experiment.

Reports separate a numeric threshold from human authority. It records
self-declared origins without authenticating them, retains insufficient_evidence
as a category, and leaves the human gate pending even when numeric agreement is
high. This prevents arithmetic success from becoming evidence of an independent
human study through this tool's own verdict.

## Demonstration and falsification

Three deterministic fixture pairs exercise a passing numeric threshold, a
failing threshold and undefined kappa. They produce 22/24 matching labels with
kappa 0.875; 0/24 with kappa -0.5; and 24/24 in a single category with null kappa.
The generator identifies these as synthetic, and every report retains the
pending human gate. Follow review_protocol.md to reproduce them.

These examples test arithmetic and provenance handling. The fixture judgments
are deliberately arbitrary, so agreement with them cannot establish ticket
audit accuracy or superiority over a baseline.

Failure-oriented tests cover malformed rows, incompatible identifiers, missing
cases, invalid references, same-reviewer comparisons and claimed human origins.
During development a failing concurrent-edit test exposed a double-read issue:
the CSV could change after its hash was checked. Intake now parses the exact
byte snapshot used for that check. A Python 3.11 symlink-loop test also exposed
an unsanitized error; shared path handling now normalizes the failure.

An isolated AI code reviewer identified a separate packet reread race; the
correction and its recheck are recorded in review_m1.md. HowlProof also checked
two supplied arithmetic expressions, supporting their internal calculations
while leaving the usefulness hypothesis inconclusive and the overall verdict
INSUFFICIENT_EVIDENCE. Neither operation evaluated the correctness of ticket
judgments or the actual origin of reviewer declarations.

## Upstream checkout and downstream support

An optional research branch asks whether annual-plan defaults make an intended
one-month purchase easier to get wrong. No vendor-specific checkout has been
inspected here. The branch proposes testing term and price comprehension,
selection persistence and correction opportunities before asserting causation
or intent.

W3C's explanatory guidance for financial/error-sensitive submissions discusses
confirmation, correction or reversibility. Its redundant-entry guidance concerns
information repeated in the same process and provides documented exceptions, including for security and information
that is no longer valid. These are useful inspection references; they do not prove
that a particular checkout or ticket workflow violates a standard.
[Error prevention](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html),
[redundant entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html).

## Evidence still required

There are no independent human returns, no adjudicated gold labels and no
production performance results. Customer-visible exports may omit the decisive
evidence. Hashes detect drift, not authenticity; self-attested provenance can
be fabricated. The cases share an author, are selected rather than representative,
and are publicly exposed. They cannot become a future locked test set.

The next empirical gate is independent human feasibility, followed by a strong
baseline comparison and an independently labeled benchmark. If agreement is
unstable or an existing tool adequately handles the workflow, narrow or stop.
Real incident publication requires separately reviewed evidence and consent.
