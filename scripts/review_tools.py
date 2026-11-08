"""Read-only review intake and descriptive agreement; no resolution classifier."""

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
from typing import Mapping

from scripts.verify_packet import FIELDS, PacketVerifier, require, timestamp

DIMENSIONS = {
    "audit_label": ("review_needed", "no_supported_defect", "insufficient_evidence"),
    "outcome": ("supported_achieved", "supported_not_achieved", "partial", "unknown"),
    "decision": ("complete", "incomplete", "not_applicable", "unknown"),
    "procedure": ("supported_concern", "no_observed_concern", "unknown"),
    "satisfaction": ("positive", "negative", "mixed", "not_expressed"),
}
REASONS = {
    "review_needed": {
        "missing_reason",
        "failed_step_repeated",
        "unanswered_objective",
        "unsupported_completion",
        "contradictory_outcome",
        "partial_request_ignored",
        "other_visible_concern",
    },
    "insufficient_evidence": {"missing_history", "missing_policy", "unknown_timing", "other_missing_context"},
    "no_supported_defect": {"none"},
}


def external_reader(path):
    """Bound explicit submission reads without scanning other files or directories."""
    path = Path(path)
    return PacketVerifier(path.parent), path.name


def tokens(value):
    parts = [part.strip() for part in value.split(";")]
    require(all(parts) and len(parts) == len(set(parts)), "empty or duplicate reference/code")
    return set(parts)


def agreement(left, right, categories):
    """Nominal agreement with exact intermediate arithmetic and Wilson interval.

    The interval describes raw agreement under a binomial approximation; it
    does not generalize this selected study to a deployment population.
    """
    require(len(left) == len(right) and len(left) > 0, "nonempty aligned labels required")
    require(len(categories) > 0 and len(set(categories)) == len(categories), "invalid category domain")
    require(all(value in categories for value in [*left, *right]), "unknown category")
    matrix = {a: {b: 0 for b in categories} for a in categories}
    for a, b in zip(left, right):
        matrix[a][b] += 1
    count = len(left)
    agree_count = sum(matrix[c][c] for c in categories)
    margins_left = {c: sum(matrix[c].values()) for c in categories}
    margins_right = {c: sum(matrix[a][c] for a in categories) for c in categories}
    observed = Fraction(agree_count, count)
    expected = sum(Fraction(margins_left[c] * margins_right[c], count * count) for c in categories)
    kappa = None if expected == 1 else float((observed - expected) / (1 - expected))
    p, z = float(observed), 1.959963984540054
    denominator = 1 + z * z / count
    center = (p + z * z / (2 * count)) / denominator
    half_width = z * math.sqrt(p * (1 - p) / count + z * z / (4 * count * count)) / denominator
    return {
        "count": count,
        "agree": agree_count,
        "raw_agreement": p,
        "kappa": kappa,
        "expected_agreement": float(expected),
        "matrix": matrix,
        "marginals": {"left": margins_left, "right": margins_right},
        "raw_agreement_wilson_95": [max(0, center - half_width), min(1, center + half_width)],
    }


@dataclass(frozen=True)
class ReviewSubmission:
    """Validated immutable copies of self-declared metadata and response rows."""

    metadata: Mapping
    rows: Mapping

    def __post_init__(self):
        object.__setattr__(self, "metadata", MappingProxyType(dict(self.metadata)))
        object.__setattr__(
            self,
            "rows",
            MappingProxyType({case_id: MappingProxyType(dict(row)) for case_id, row in self.rows.items()}),
        )


class ReviewStudy:
    """Bind complete submissions to one verified packet and rubric revision."""

    RUBRIC_VERSION = "0.2.0"
    METADATA_FIELDS = {
        "schema",
        "reviewer_id",
        "reviewer_kind",
        "independence_attested",
        "case_author",
        "prior_exposure",
        "collected_at",
        "rubric_version",
        "packet_manifest_sha256",
        "rubric_sha256",
        "responses_sha256",
    }

    def __init__(self, root):
        self.packet = PacketVerifier(root)
        self.packet.verify()
        self.cases = self.packet.read_cases("data/cases.json")
        self.manifest_sha256 = hashlib.sha256(self.packet.read_bytes("packet_manifest.json")).hexdigest()
        self.rubric_sha256 = hashlib.sha256(self.packet.read_bytes("docs/rubric.md")).hexdigest()

    def validate_metadata(self, metadata, responses):
        require(
            isinstance(metadata, dict) and set(metadata) == self.METADATA_FIELDS, "invalid metadata fields"
        )
        require(metadata["schema"] == "supportloop.review_metadata/v1", "invalid metadata schema")
        require(
            isinstance(metadata["reviewer_id"], str)
            and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_]{0,63}", metadata["reviewer_id"]),
            "invalid reviewer id",
        )
        require(metadata["reviewer_kind"] in ("human", "model", "synthetic"), "invalid reviewer kind")
        require(
            type(metadata["independence_attested"]) is bool and type(metadata["case_author"]) is bool,
            "attestations must be booleans",
        )
        require(
            metadata["prior_exposure"]
            in ("none_declared", "study_material_seen", "author_expectations_seen", "unknown"),
            "invalid exposure value",
        )
        require(timestamp(metadata["collected_at"]) is not None, "collection timestamp required")
        require(metadata["rubric_version"] == self.RUBRIC_VERSION, "incompatible rubric version")
        require(metadata["packet_manifest_sha256"] == self.manifest_sha256, "packet identity mismatch")
        require(metadata["rubric_sha256"] == self.rubric_sha256, "rubric identity mismatch")
        require(
            metadata["responses_sha256"] == hashlib.sha256(responses).hexdigest(), "response digest mismatch"
        )

    def validate_row(self, row, metadata):
        require(row["case_id"] in self.cases, "unknown case id")
        require(row["objective"].strip() and row["rationale"].strip(), "objective and rationale required")
        for name, domain in DIMENSIONS.items():
            require(row[name] in domain, "invalid dimension value")
        for name in ("reviewer_id", "reviewer_kind", "rubric_version"):
            require(row[name] == metadata[name], "row and metadata disagree")
        require(
            row["elapsed_seconds"] == "" or re.fullmatch(r"0|[1-9]\d*", row["elapsed_seconds"]),
            "invalid elapsed seconds",
        )
        require(
            tokens(row["reason_codes"]) <= REASONS[row["audit_label"]], "invalid reason code for category"
        )
        case = self.cases[row["case_id"]]
        available = {event["id"] for event in case["events"]}
        available.update(f"C{index + 1}" for index in range(len(case["context"])))
        require(tokens(row["evidence_refs"]) <= available, "unknown evidence reference")

    def load_submission(self, responses, metadata):
        """Reject an incomplete or mismatched submission; never silently discard rows."""
        reader, name = external_reader(responses)
        content = reader.read_bytes(name)
        meta_reader, meta_name = external_reader(metadata)
        meta = meta_reader.read_json(meta_name)
        self.validate_metadata(meta, content)
        table = reader.parse_csv(content)
        require(bool(table) and table[0] == FIELDS, "invalid CSV header")
        require(
            len(table) == len(self.cases) + 1 and all(len(row) == len(FIELDS) for row in table[1:]),
            "incomplete CSV or invalid row width",
        )
        rows = {}
        for values in table[1:]:
            row = dict(zip(FIELDS, values))
            self.validate_row(row, meta)
            require(row["case_id"] not in rows, "duplicate case row")
            rows[row["case_id"]] = row
        require(set(rows) == set(self.cases), "missing case rows")
        return ReviewSubmission(meta, rows)

    def compare(self, left, right):
        """Compare recorded judgments without certifying origin or their correctness."""
        require(
            isinstance(left, ReviewSubmission) and isinstance(right, ReviewSubmission),
            "validated submissions required",
        )
        require(left.metadata["reviewer_id"] != right.metadata["reviewer_id"], "distinct reviewers required")
        for submission in (left, right):
            require(
                submission.metadata["packet_manifest_sha256"] == self.manifest_sha256
                and submission.metadata["rubric_sha256"] == self.rubric_sha256,
                "incompatible study identity",
            )
            require(set(submission.rows) == set(self.cases), "incomplete compared case set")
            for row in submission.rows.values():
                self.validate_row(row, submission.metadata)
        ids = sorted(self.cases)
        stats = {
            name: agreement([left.rows[c][name] for c in ids], [right.rows[c][name] for c in ids], domain)
            for name, domain in DIMENSIONS.items()
        }
        audit = stats["audit_label"]
        numeric_gate = (
            "UNDEFINED"
            if audit["kappa"] is None
            else "MET" if audit["agree"] >= 20 and audit["kappa"] >= 0.70 else "NOT_MET"
        )
        metadata = [dict(sub.metadata) for sub in (left, right)]
        eligibility = "DECLARED_ONLY"
        if any(m["reviewer_kind"] != "human" for m in metadata):
            eligibility = "INELIGIBLE_NONHUMAN"
        elif any(
            m["case_author"] or not m["independence_attested"] or m["prior_exposure"] != "none_declared"
            for m in metadata
        ):
            eligibility = "REQUIRES_INDEPENDENCE_REVIEW"
        return {
            "schema": "supportloop.agreement_report/v1",
            "packet_manifest_sha256": self.manifest_sha256,
            "rubric_sha256": self.rubric_sha256,
            "dimensions": stats,
            "numeric_gate": numeric_gate,
            "human_gate": "PENDING",
            "review_eligibility": eligibility,
            "provenance": metadata,
            "disagreements": {
                name: [c for c in ids if left.rows[c][name] != right.rows[c][name]] for name in DIMENSIONS
            },
            "limitations": [
                "Identity and independence are self-declared, not authenticated.",
                "Agreement is not correctness or resolution verification.",
                "Human gate requires independent review of provenance and control cases.",
                "Wilson intervals do not establish population reliability on a selected sample.",
                "No adjudication, accuracy evaluation or customer-impact experiment occurred.",
            ],
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "compare"):
        command = commands.add_parser(name)
        command.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
        if name == "validate":
            command.add_argument("--responses", type=Path, required=True)
            command.add_argument("--metadata", type=Path, required=True)
        else:
            for flag in ("left", "right", "left-metadata", "right-metadata"):
                command.add_argument(f"--{flag}", type=Path, required=True)
    args = parser.parse_args()
    try:
        study = ReviewStudy(args.root)
        if args.command == "validate":
            submission = study.load_submission(args.responses, args.metadata)
            result = {
                "status": "SUBMISSION_VALIDATED",
                "cases": len(submission.rows),
                "origin": submission.metadata["reviewer_kind"],
                "origin_assurance": "DECLARED_ONLY",
                "human_gate": "PENDING",
            }
        else:
            result = study.compare(
                study.load_submission(args.left, args.left_metadata),
                study.load_submission(args.right, args.right_metadata),
            )
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (ValueError, TypeError, KeyError, OSError, csv.Error, RecursionError) as error:
        print(json.dumps({"status": "ERROR", "reason": type(error).__name__}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
