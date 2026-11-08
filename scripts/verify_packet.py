"""Verify synthetic packet structure and locked bytes; never judge ticket meaning."""

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from types import MappingProxyType


FIELDS = ["case_id", "objective", "outcome", "decision", "procedure", "satisfaction",
          "audit_label", "reason_codes", "evidence_refs", "rationale", "elapsed_seconds",
          "reviewer_kind", "reviewer_id", "rubric_version"]


def require(condition, message):
    """Fail without echoing potentially sensitive input values."""
    if not condition:
        raise ValueError(message)


def resolve_path(path):
    """Normalize paths with the same sanitized error on supported Python versions."""
    try:
        return Path(path).resolve()
    except RuntimeError:
        raise ValueError("invalid filesystem path") from None


def timestamp(value):
    """Parse a timezone-aware ISO datetime; absent event times remain unknown."""
    if value is None:
        return None
    require(isinstance(value, str) and "T" in value, "invalid timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError("invalid timestamp") from None
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None, "timezone required")
    return parsed


def validate_case(case):
    """Validate observation-only fields, event identity and cutoff consistency."""
    require(isinstance(case, dict), "case must be an object")
    require(set(case) == {"id", "synthetic", "export_scope", "as_of", "context", "events"},
            "case fields differ from observation contract")
    require(isinstance(case["id"], str) and re.fullmatch(r"SL\d{2}", case["id"]), "invalid case id")
    require(case["synthetic"] is True, "only explicitly synthetic data accepted")
    require(isinstance(case["export_scope"], str) and
            case["export_scope"] in {"provided_window", "partial_export"}, "invalid export scope")
    cutoff = timestamp(case["as_of"])
    require(cutoff is not None, "cutoff required")
    require(isinstance(case["context"], list), "context must be a list")
    require(all(isinstance(item, str) and item.strip() for item in case["context"]), "invalid context")
    events = case["events"]
    require(isinstance(events, list) and events, "events required")
    seen = set()
    for event in events:
        require(isinstance(event, dict) and set(event) == {"id", "at", "kind", "actor", "text"},
                "invalid event fields")
        identifier = event["id"]
        require(isinstance(identifier, str) and re.fullmatch(r"E[1-9]\d*", identifier), "invalid event id")
        require(identifier not in seen, "duplicate event id")
        seen.add(identifier)
        require(isinstance(event["kind"], str) and event["kind"] in {"message", "status", "artifact"},
                "invalid event kind")
        require(isinstance(event["actor"], str) and
                event["actor"] in {"customer", "support", "system", "record"}, "invalid event actor")
        require(isinstance(event["text"], str) and event["text"].strip(), "event text required")
        at = timestamp(event["at"])
        require(at is None or at <= cutoff, "event occurs after cutoff")


class PacketVerifier:
    """Own a public packet's boundaries, file reads and structural checks.

    Author hypotheses are deliberately outside this public verification contract.
    This class certifies neither semantic labels nor independent human review.
    """

    VERSION = "0.3.0"
    MAX_FILE_BYTES = 2_000_000
    MANIFEST_FIELDS = {"schema", "version", "created_on", "synthetic", "case_count", "human_gate", "sha256"}
    REVIEWER_FILES = {"cases.json", "rubric.md", "labels.csv", "README.md"}

    def __init__(self, root):
        self.root = resolve_path(root)
        self._snapshot = None

    def path(self, relative):
        """Resolve a local packet path while refusing escapes through symlinks."""
        require(isinstance(relative, str) and not Path(relative).is_absolute(), "invalid packet path")
        path = self.root / relative
        require(resolve_path(path).is_relative_to(self.root), "packet path escapes root")
        return path

    def read_bytes(self, relative):
        """Bound reads so a malformed local packet cannot demand arbitrary memory."""
        require(isinstance(relative, str), "invalid packet path")
        if self._snapshot is not None and relative in self._snapshot:
            return self._snapshot[relative]
        path = self.path(relative)
        require(path.is_file(), "packet input must be a regular file")
        with path.open("rb") as handle:
            content = handle.read(self.MAX_FILE_BYTES + 1)
        require(len(content) <= self.MAX_FILE_BYTES, "packet file exceeds size limit")
        return content

    @staticmethod
    def unique_object(pairs):
        """Reject ambiguous JSON instead of silently keeping the final key."""
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    @staticmethod
    def reject_constant(_value):
        raise ValueError("nonfinite JSON constant")

    @classmethod
    def parse_json(cls, content):
        return json.loads(content.decode("utf-8"),
                          object_pairs_hook=cls.unique_object, parse_constant=cls.reject_constant)

    def read_json(self, relative):
        return self.parse_json(self.read_bytes(relative))

    @staticmethod
    def parse_csv(content):
        """Parse a previously acquired byte snapshot without reading the file again."""
        return list(csv.reader(io.StringIO(content.decode("utf-8"), newline=""), strict=True))

    def read_csv(self, relative):
        """Preserve quoted newlines for both templates and completed reviews."""
        return self.parse_csv(self.read_bytes(relative))

    def locked_paths(self):
        paths = {"data/cases.json", "docs/rubric.md", "docs/evaluation_contract.md"}
        paths.update(f"reviewer_packets/{who}/{name}" for who in ("A", "B")
                     for name in self.REVIEWER_FILES)
        return paths

    def verify_manifest(self):
        """Validate metadata as well as hashes; hashes alone do not define a study."""
        manifest_bytes = self.read_bytes("packet_manifest.json")
        manifest = self.parse_json(manifest_bytes)
        require(isinstance(manifest, dict) and set(manifest) == self.MANIFEST_FIELDS,
                "manifest fields differ from contract")
        require(manifest["schema"] == "supportloop.feasibility_manifest/v1", "invalid manifest schema")
        require(manifest["version"] == self.VERSION, "unsupported packet version")
        require(manifest["created_on"] == "2026-11-08", "unexpected packet creation date")
        require(manifest["synthetic"] is True, "manifest must describe synthetic data")
        require(type(manifest["case_count"]) is int and manifest["case_count"] == 24,
                "manifest case count mismatch")
        require(manifest["human_gate"] == "PENDING", "manifest cannot certify human review")
        require(isinstance(manifest["sha256"], dict) and set(manifest["sha256"]) == self.locked_paths(),
                "manifest locked file set mismatch")
        snapshot = {"packet_manifest.json": manifest_bytes}
        for name, expected in manifest["sha256"].items():
            require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "invalid digest")
            content = self.read_bytes(name)
            require(hashlib.sha256(content).hexdigest() == expected, "locked artifact drift")
            snapshot[name] = content
        self._snapshot = MappingProxyType(snapshot)

    def read_cases(self, relative):
        cases = self.read_json(relative)
        require(isinstance(cases, list) and len(cases) == 24, "exactly 24 cases required")
        for case in cases:
            validate_case(case)
        by_id = {case["id"]: case for case in cases}
        require(len(by_id) == 24, "duplicate case id")
        return by_id

    def verify_reviewer(self, reviewer, by_id):
        prefix = f"reviewer_packets/{reviewer}"
        folder = self.path(prefix)
        require({p.name for p in folder.iterdir()} == self.REVIEWER_FILES,
                "unexpected reviewer file; potential blinding leak")
        require(self.read_cases(f"{prefix}/cases.json") == by_id, "reviewer observations differ")
        require(self.read_bytes(f"{prefix}/rubric.md") == self.read_bytes("docs/rubric.md"),
                "reviewer rubric mismatch")
        # csv.reader exposes row widths; DictReader can hide surplus cells under a None key.
        rows = self.read_csv(f"{prefix}/labels.csv")
        require(bool(rows) and rows[0] == FIELDS, "reviewer columns mismatch")
        data = rows[1:]
        require(len(data) == 24 and all(len(row) == len(FIELDS) for row in data),
                "reviewer row width or count mismatch")
        require({row[0] for row in data} == set(by_id), "reviewer case ids mismatch")
        require(all(all(value == "" for value in row[1:]) for row in data), "reviewer sheet must be blank")
        return len(data)

    def verify(self):
        self._snapshot = None
        try:
            self.verify_manifest()
            by_id = self.read_cases("data/cases.json")
            counts = {who: self.verify_reviewer(who, by_id) for who in ("A", "B")}
            return {"status": "STRUCTURE_VERIFIED", "cases": len(by_id), "reviewer_rows": counts,
                    "human_gate": "PENDING", "semantic_accuracy": "NOT_EVALUATED"}
        except Exception:
            self._snapshot = None
            raise


def verify(root):
    """Compatibility entry point shared by the CLI and existing callers."""
    return PacketVerifier(root).verify()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="root of the synthetic feasibility packet")
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.root), indent=2))
    except (ValueError, TypeError, KeyError, OSError, csv.Error, RecursionError) as error:
        print(json.dumps({"status": "ERROR", "reason": type(error).__name__}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
