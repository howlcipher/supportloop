"""Reproduce arithmetic demonstrations without inventing human study results."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.demo_reviews import build_demo

ROOT = Path(__file__).resolve().parents[1]


class DemoTests(unittest.TestCase):
    def test_demo_reproduces_known_arithmetic_and_retains_human_gate(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "demo"
            result = build_demo(ROOT, output)
            self.assertEqual(result["status"], "SYNTHETIC_DEMO_CREATED")
            reports = {
                name: json.loads((output / f"{name}_report.json").read_text())
                for name in ["agreement", "disagreement", "undefined"]
            }
            self.assertEqual(reports["agreement"]["dimensions"]["audit_label"]["agree"], 22)
            self.assertEqual(reports["agreement"]["dimensions"]["audit_label"]["kappa"], 0.875)
            self.assertEqual(reports["agreement"]["numeric_gate"], "MET")
            self.assertEqual(reports["disagreement"]["numeric_gate"], "NOT_MET")
            self.assertEqual(reports["undefined"]["numeric_gate"], "UNDEFINED")
            for report in reports.values():
                self.assertEqual(report["human_gate"], "PENDING")
                self.assertEqual(report["review_eligibility"], "INELIGIBLE_NONHUMAN")
                self.assertEqual({m["reviewer_kind"] for m in report["provenance"]}, {"synthetic"})
            for path in output.glob("*.csv"):
                self.assertNotIn("human", path.read_text())

    def test_demo_does_not_overwrite_an_existing_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            marker = Path(folder) / "keep.txt"
            marker.write_text("preserve")
            with self.assertRaises((ValueError, FileExistsError)):
                build_demo(ROOT, Path(folder))
            self.assertEqual(marker.read_text(), "preserve")

    def test_demo_outputs_are_deterministic(self):
        with tempfile.TemporaryDirectory() as folder:
            first, second = Path(folder) / "a", Path(folder) / "b"
            build_demo(ROOT, first)
            build_demo(ROOT, second)
            left = {str(p.relative_to(first)): p.read_bytes() for p in first.iterdir()}
            right = {str(p.relative_to(second)): p.read_bytes() for p in second.iterdir()}
            self.assertEqual(left, right)

    def test_cli_demo_validate_and_compare_work_without_private_material(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "demo"
            commands = [
                ["scripts.demo_reviews", "--root", str(ROOT), "--out", str(output)],
                [
                    "scripts.review_tools",
                    "validate",
                    "--root",
                    str(ROOT),
                    "--responses",
                    str(output / "agreement_synthetic_a.csv"),
                    "--metadata",
                    str(output / "agreement_synthetic_a.json"),
                ],
                [
                    "scripts.review_tools",
                    "compare",
                    "--root",
                    str(ROOT),
                    "--left",
                    str(output / "agreement_synthetic_a.csv"),
                    "--left-metadata",
                    str(output / "agreement_synthetic_a.json"),
                    "--right",
                    str(output / "agreement_synthetic_b.csv"),
                    "--right-metadata",
                    str(output / "agreement_synthetic_b.json"),
                ],
            ]
            outputs = []
            for command in commands:
                process = subprocess.run(
                    [sys.executable, "-m", *command], cwd=ROOT, capture_output=True, text=True, timeout=10
                )
                self.assertEqual(process.returncode, 0, process.stderr)
                outputs.append(json.loads(process.stdout))
            self.assertEqual(outputs[1]["origin"], "synthetic")
            self.assertEqual(outputs[2]["numeric_gate"], "MET")
            self.assertEqual(outputs[2]["human_gate"], "PENDING")


if __name__ == "__main__":
    unittest.main()
