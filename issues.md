# Findings and bugs report

Scope: source inspection and local reproductions, November 8, 2026.
Research gaps are distinguished from reproduced software defects. No finding
here alleges misconduct by a support vendor or proves unmet market demand.

## Reproduced and corrected in packet 0.2.0

| ID | Finding and observable failure | Correction | Regression evidence |
| --- | --- | --- | --- |
| BUG-001 | A checkout without author_material/ failed before verification could finish | Public manifest and verifier no longer require the unpublished author expectations | test_public_checkout_requires_no_author_expectations; clean public-export regression |
| BUG-002 | synthetic=false, incorrect case_count and an unsupported manifest version were accepted | Strict manifest fields and supported packet metadata are required | test_rejects_manifest_metadata_inconsistency |
| BUG-003 | Duplicate JSON keys were silently overwritten, allowing ambiguous provenance metadata | A shared bounded JSON reader rejects duplicate keys and nonfinite constants | test_rejects_duplicate_json_keys; test_nonfinite_json_is_rejected |
| BUG-004 | A CSV data row with an extra cell passed after the file was relocked | Validate exact CSV header and every row width before blank-field checks | test_rejects_extra_csv_cells |
| BUG-005 | Splitting CSV into lines discarded an embedded quoted newline, accepting it as a blank review answer | Preserve CSV newline semantics with a shared in-memory text stream | test_quoted_newline_is_not_a_blank_review_answer |

New failure tests were run against the prior implementation before fixes: five
failing assertions and one missing-file error exposed the initial BUG-001 through BUG-004 groups.
An additional targeted red test reproduced BUG-005 before its correction.
The original 15 regression contracts were retained. Additional checks exercise
path escapes and sanitized CLI errors. Author hypotheses remain local; their
absence is an intentional public contract change, not weakened label validation.

## Corrected during review infrastructure, packet 0.3.0

| ID | Finding | Correction and evidence |
| --- | --- | --- |
| BUG-006 | A response CSV was read again after its digest was checked | Parse the exact byte snapshot used for the hash; concurrent-edit regression reproduces the old issue |
| BUG-007 | Study construction reread observations and packet identities after verification | Retain immutable hash-checked packet bytes; independently reviewed fix and real filesystem-edit regression verify snapshot use and fresh-check drift detection |
| BUG-008 | Python 3.11 path resolution of a symlink loop could expose a traceback | Shared path resolver normalizes the error; Python 3.11 failure reproduction and sanitized CLI regression |

## Completed engineering gaps

GAP-001 is implemented by strict 24-row intake, schema/version/digest binding,
reference validation and immutable submission copies. GAP-002 is implemented by
per-dimension descriptive agreement, full category matrices, marginals and
undefined-kappa handling. Neither completion establishes independent labels,
reviewer authenticity or semantic resolution accuracy. Direct Python value-object
construction is a trusted programming interface; documented comparisons use
submissions returned by load_submission. The CLI always performs full intake.

## Open research, ordered by priority

| ID | Priority/type | Finding | Next action and acceptance |
| --- | --- | --- | --- |
| RES-001 | P1 research dependency | No independent human labels | Collect two reviews only when people are available. Record independence/exposure and preserve original returns. AI or author labels cannot resolve this dependency. |
| RES-002 | P2 prior-art uncertainty | Vendor documentation establishes feature overlap, not measured adequacy | Compare a configured existing rubric against the constrained target workflow before writing an analyzer. Record unavailable access honestly. |
| RES-003 | P2 external validity | The 24 authored synthetic cases are selected and intentionally clear | Obtain independently labeled, consented and more varied cases before generalizing. No production error-rate or market-demand claims from this set. |
| RES-004 | P2 observability limit | Customer-visible exports may omit the decisive outcome evidence | Measure unknown/abstention rates and human review burden. Do not force resolution labels. |
| RES-005 | P2 UX hypothesis | A preselected 12-month plan may increase accidental annual commitment for a one-month purchase goal | Capture consented initial/confirmation states and selection persistence before asserting a vendor-specific fact. If useful, preregister a synthetic checkout comparison. Measure errors and comprehension; do not infer predatory intent. |

## Retained limitations, not disguised as fixed bugs

Hashes detect drift; a writer who can replace both content and manifest can
forge them. The tool is not an authenticity service. Public packet separation
does not prove reviewer independence. Local source, tests and semantic
expectations share an author, so passing regression is not independent semantic
validation. Dependency and secret scans have bounded detection, not proof that
the repository is free of every security defect.

HowlProof's documentation inventory includes normative instructions and evidence
limits as unverified absolute phrasings. Its byte comparisons are useful but
do not certify ticket outcomes. Its recorded overall verdict for preparation
was INSUFFICIENT_EVIDENCE; do not present it as product approval.

## Provider-review follow-up

BUG-009: demo fixture generation assumed every valid case contained E1, although
the packet contract permits other identifiers. AGY identified the mismatch; a
valid rehashed non-E1 packet reproduced the failure before correction. Fixtures
now use the first observed event ID. The new integration contract retains the
pending human gate and known numeric result.

GAP-003 (low-priority enhancement): demo output is not an atomic directory
transaction. An interrupted write may leave partial files. This is retained and
documented; no automatic cleanup or overwrite is attempted. Use a new output
destination and require successful completion with the final demo manifest.
Atomic publication may be added if interrupted runs become a recurring need.

BUG-010: overflowing JSON floating literals could produce infinity despite the
nonfinite-rejection claim. A failing direct parser test now protects NaN,
Infinity and exponent overflow; finite values remain accepted.

BUG-011: the independence-claim test was confounded by the other reviewer being
unattested. A source mutation reproduced the vacuity; fully attested opposite
reviewers now isolate author/exposure flags on both sides and kill that mutant.
Template width and nonfinite tests are strengthened for the same reason.

BUG-012: snapshot tests compared resolved roots with unresolved temporary paths.
A symlinked TMPDIR reproduced failures on the prior snapshot; resolved fixture
paths pass that environment. Completed CSV width, ASCII IDs/digits and UTF-8 BOM
coverage now protect their documented intake boundaries.

GAP-004 (before M2): freeze and distribute normative submission instructions with
the actual assigned packet; a future packet revision can lock the operations
protocol and centralize rubric constants. Current reports identify tool_version
and published results must record the source commit. No semantic/blinding or
reviewer-authenticity certification is inferred from structural verification.

GAP-005 (before hosted untrusted intake): defend reads against active concurrent
filesystem writers with OS/process isolation or safe descriptor-based opening.
Current local use requires an owned stable directory; it is not a hostile-filesystem
sandbox. Complete control-subset and provenance-plausibility review before
passing M2. No automatic acceptance is enabled.
