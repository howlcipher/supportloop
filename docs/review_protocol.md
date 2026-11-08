# Completed-review protocol

Packet 0.3.0, rubric 0.2.0. This protocol implements research infrastructure.
No human feasibility result or resolution classifier is supplied.

## Inputs and provenance

Give each reviewer their observation-only packet. Preserve their original
completed CSV in ignored review_returns/; do not edit a return to improve
agreement. The CSV header is the template's exact FIELDS sequence. Require one
row per case and all rubric dimensions, objective, rationale, reason codes and
evidence references. Unknown and insufficient_evidence are real choices, not
missing rows. An unmeasured elapsed_seconds stays blank.

Each return has a JSON metadata sidecar with these exact fields:

| Field | Contract |
| --- | --- |
| schema | supportloop.review_metadata/v1 |
| reviewer_id | Pseudonym: 1 to 64 letters, digits or underscores, starting with a letter or digit; must match each CSV row |
| reviewer_kind | human, model or synthetic; must match each CSV row |
| independence_attested | Boolean declaration by the reviewer/coordinator; not proof |
| case_author | Boolean declaration of case authorship |
| prior_exposure | none_declared, study_material_seen, author_expectations_seen or unknown |
| collected_at | Timezone-aware ISO timestamp; fixture times are fictional |
| rubric_version | 0.2.0, matching each CSV row |
| packet_manifest_sha256 | SHA256 of the exact packet_manifest.json |
| rubric_sha256 | SHA256 of docs/rubric.md |
| responses_sha256 | SHA256 of the exact CSV bytes |

Intake rejects unknown metadata fields, duplicate JSON keys and nonfinite
constants. A valid digest establishes byte consistency, not who made a review.
Declared human identity does not authenticate a person. Public packet exposure
must be assessed before treating two returns as independent.

Reference E1 for an event and C1 for the first context entry. Separate codes and
references with semicolons; empty, duplicate and nonexistent entries are refused.
Reference validation establishes that an entry exists, not that it supports the
judgment. Semantic checking and control-case review remain human responsibilities.

## Validate and compare

Run from the repository root with Python 3.11+:

```bash
python3 -m scripts.review_tools validate --responses review_returns/a.csv --metadata review_returns/a.json
python3 -m scripts.review_tools compare --left review_returns/a.csv --left-metadata review_returns/a.json --right review_returns/b.csv --right-metadata review_returns/b.json
```

Both commands accept --root for an explicitly selected packet. They read bounded
regular local files, launch no model and send nothing over the network. They
write JSON to stdout; validation failures emit a sanitized error document on
stderr and exit 1. Exit 0 means the input was validated or a report was produced.
It does not mean the numeric or human study gate passed. The CLI does not echo
objective or rationale text in its reports. Provenance pseudonyms and digests
are included, so handle reports as study data too.

For library use, call ReviewStudy(root).load_submission(csv_path, metadata_path)
and study.compare(left, right). Shared parsing is also used by PacketVerifier.
Immutable response objects reduce accidental changes after intake. Reads do not
provide OS isolation or authenticity against an operator who can forge files.

## Report interpretation

Reports contain per-dimension confusion matrices, marginals, agreement
counts, raw agreement, unweighted Cohen's kappa, Wilson 95% intervals for raw
agreement, and case IDs for disagreements. No row is silently discarded.
This interval is an approximate description of agreement; the selected synthetic
sample does not justify claims of population reliability. No kappa interval is
estimated. If expected agreement is one, kappa is null and numeric_gate is
UNDEFINED. The report does not adjudicate disagreements or calculate accuracy.

For the current 24-case packet, numeric_gate is MET only when at least 20 labels
agree and kappa is at least 0.70. The independent human gate stays PENDING in
the tool, including for self-declared human inputs. Nonhuman inputs are marked
INELIGIBLE_NONHUMAN. Other returns are DECLARED_ONLY or require independence
review. A coordinator must inspect provenance and control cases separately.

## Reproducible arithmetic demonstration

```bash
python3 -m scripts.demo_reviews --out runs/review_demo
python3 -m scripts.review_tools compare --left runs/review_demo/agreement_synthetic_a.csv --left-metadata runs/review_demo/agreement_synthetic_a.json --right runs/review_demo/agreement_synthetic_b.csv --right-metadata runs/review_demo/agreement_synthetic_b.json
```

Use a new output directory on each run; the generator refuses an existing
destination. Under the packet root it writes only beneath runs/. Outputs are
deterministic for the same packet and code. demo_manifest.json records hashes.
Generated labels are arbitrary arithmetic fixtures, not judgments about the
underlying cases. Their timestamps are fictional and no human was evaluated.

| Fixture | Matching labels | Kappa | Numeric gate | Human gate |
| --- | --- | --- | --- | --- |
| agreement | 22/24 | 0.875 | MET | PENDING |
| disagreement | 0/24 | -0.5 | NOT_MET | PENDING |
| undefined | 24/24, one category | null | UNDEFINED | PENDING |

These values are reproducible software checks. They establish no resolution
accuracy, false-positive rate, review-time improvement or commercial value.
