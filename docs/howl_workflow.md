# Howl coordination and gates

## Mission

Prepare a reproducible feasibility packet without implementing a ticket analyzer
or claiming independent semantic validation. HowlPlane owns task specification,
verification commands, run artifacts and stop/go state through its existing CLI.
No persistent agent swarm or model dispatch is needed for this stage.

```bash
VIRTUAL_ENV="$PWD/.venv" howlplane --repo . verify --project-dir . --task-id SL-FEASIBILITY-001 --output runs/verification.json
```

The .ai-project.toml manifest declares unittest, packet integrity and lint gates.
The prepared task specification is in coordination/task.json. These are software
checks only. Plane cannot grant itself human labels or publication consent.

## Responsibilities

| Component | Current useful operation | Boundary |
| --- | --- | --- |
| HowlPlane | Task specification, project verification, evidence records | Does not turn structural checks into semantic validation |
| HowlDream | Cluster externally authored hypotheses; prior-art hooks for later discovery | Generated none when only clustering; default mock exploration is not research |
| HowlProof | Source acquisition; bounded documentation checks and later independent evaluator execution | Existing evaluators cannot determine actual ticket resolution or replace independent human labels |
| HowlWriter | Deterministic lint on study documentation; later drafting from an approved claim ledger | Lint is not factual verification; remote private-material egress needs explicit consent |
| Human reviewers | Independent labels, ambiguity reports and later adjudication | Not available yet; author/model labels do not substitute |

Actual run outputs, exit codes, source-tree hashes and limitations are recorded
in runs/. A configured future pipeline is not an executed mission. No nested
Codex or other remote model is required or launched for packet preparation.

## Progression

1. Prepare packet and run structural gates. Finish authorized local work.
2. Wait for two independent humans. Their absence is a research dependency,
   not permission for a model to sign the human gate.
3. Lock returns, calculate agreement under the contract, adjudicate separately.
4. If feasible, design the larger locked benchmark and check whether an existing
   configured QA system meets the intended user's constraints.
5. Only then implement a small baseline and conditional candidate analyzer using
   behavior-first tests. Keep Proof's evaluator and human labels independent.
6. Compare against strong simple and rubric baselines; stop if value is absent.
7. Seek consented external validation. No contacts happen automatically.
8. Review privacy, licensing, reproducibility and final regression before release.
9. Obtain owner review of all public text and artifacts before publication.

No broad implementation approval overrides these evidence gates.

## Observed integration limits

Plane's task enum did not accept research; this task uses test_improvement.
Its initial verification selected the Plane runtime and failed to import
flake8. An explicit project environment resolved that environment mismatch.
This is not evidence that packet tests failed. The normal system and Python 3.11
test runs also exercise the tooling without relying on Plane's runtime.

Proof's initial unconfigured documentation run was NOT_APPLICABLE and returned
INSUFFICIENT_EVIDENCE. howlproof.yaml now declares documentation and rubric
copies for an actual byte comparison and claim inventory. Acceptance remains
unset, so the overall Proof verdict remains INSUFFICIENT_EVIDENCE by design.
Its lexical inventory flags some normative reviewer instructions as absolute
claims. Preserve that inventory; it does not show those instructions were
violated or establish their empirical truth. No domain verdict is inferred.
