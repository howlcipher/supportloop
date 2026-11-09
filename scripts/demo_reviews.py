"""Generate deterministic arithmetic fixtures; no human or semantic evaluation."""

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

from scripts.review_tools import DIMENSIONS, REASONS, ReviewStudy
from scripts.verify_packet import FIELDS, require, resolve_path


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def fixture(study, output, reviewer_id, labels):
    """Write explicitly synthetic response/metadata fixtures with bound hashes."""
    csv_path = output / f"{reviewer_id}.csv"
    rows = []
    for case_id, label in zip(sorted(study.cases), labels):
        rows.append(
            dict(
                zip(
                    FIELDS,
                    [
                        case_id,
                        "Arithmetic fixture; not a semantic objective assessment",
                        "unknown",
                        "unknown",
                        "unknown",
                        "not_expressed",
                        label,
                        sorted(REASONS[label])[0],
                        study.cases[case_id]["events"][0]["id"],
                        "Generated label for arithmetic only; does not assess this case",
                        "",
                        "synthetic",
                        reviewer_id,
                        study.RUBRIC_VERSION,
                    ],
                )
            )
        )
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    metadata = {
        "schema": "supportloop.review_metadata/v1",
        "reviewer_id": reviewer_id,
        "reviewer_kind": "synthetic",
        "independence_attested": False,
        "case_author": True,
        "prior_exposure": "study_material_seen",
        "collected_at": "2026-11-08T00:00:00Z",
        "rubric_version": study.RUBRIC_VERSION,
        "packet_manifest_sha256": study.manifest_sha256,
        "rubric_sha256": study.rubric_sha256,
        "responses_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
    }
    metadata_path = output / f"{reviewer_id}.json"
    write_json(metadata_path, metadata)
    return study.load_submission(csv_path, metadata_path)


def build_demo(root, output):
    """Produce three repeatable arithmetic examples in a new directory only."""
    root, output = resolve_path(root), resolve_path(output)
    require(not output.exists(), "demo destination already exists")
    if output.is_relative_to(root):
        relative = output.relative_to(root)
        require(
            relative.parts and relative.parts[0] == "runs", "demo output must be in runs or outside packet"
        )
    study = ReviewStudy(root)
    output.mkdir(parents=True, exist_ok=False)
    balanced = list(DIMENSIONS["audit_label"]) * 8
    near = balanced.copy()
    near[0], near[1] = near[1], near[0]
    rotated = balanced[1:] + balanced[:1]
    constant = ["no_supported_defect"] * 24
    scenarios = {
        "agreement": (balanced, near),
        "disagreement": (balanced, rotated),
        "undefined": (constant, constant),
    }
    for name, (left, right) in scenarios.items():
        a = fixture(study, output, f"{name}_synthetic_a", left)
        b = fixture(study, output, f"{name}_synthetic_b", right)
        write_json(output / f"{name}_report.json", study.compare(a, b))
    record = {
        "status": "SYNTHETIC_DEMO_CREATED",
        "human_gate": "PENDING",
        "semantic_accuracy": "NOT_EVALUATED",
        "fixture_time_is_not_observed_collection": True,
        "limitations": "Generated labels demonstrate arithmetic, not evidence-backed ticket judgments.",
        "files_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(output.iterdir())
            if p.is_file()
        },
    }
    write_json(output / "demo_manifest.json", record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--out", type=Path, required=True, help="new directory; existing destinations refused"
    )
    args = parser.parse_args()
    try:
        result = build_demo(args.root, args.out)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, TypeError, KeyError, OSError, csv.Error, RecursionError) as error:
        print(json.dumps({"status": "ERROR", "reason": type(error).__name__}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
