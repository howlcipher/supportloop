# Feasibility architecture decision

Status: accepted for packet tooling only. Product stack remains conditional.
Packet contract revision 0.3.0 supports a standalone public checkout without
local author hypotheses. There is still no ticket-classification component.

## Decision and alternatives

Use JSON for synthetic observations, CSV for independent labels, Markdown for
the rubric, and Python 3.11+ standard library for integrity checks. This matches
existing Howl CLI/file contracts without requiring a server or runtime packages.

| Alternative | Benefit | Cost at this stage |
| --- | --- | --- |
| Python standard library | Portable data checks, existing ecosystem fit | Interpreter distribution and strict input validation needed |
| Go | One binary, explicit types | Build/distribution work without experimental benefit |
| C#/.NET | Strong types, familiar API platform | Runtime and integration work for a file-based study |
| Existing QA configuration | Avoid building a redundant analyzer | Must test availability, privacy and portability constraints |
| Spreadsheet only | Accessible manual review | Harder reproducibility and accidental formula/label edits |

No analysis model, HTTP service, database, adapter framework or autonomous
escalation is implemented. A Python library API supports local review tooling.
Python is not a commitment to a full product stack.

## Evidence flow

```mermaid
flowchart LR
    C[Synthetic observations] --> P[Observation-only reviewer packets]
    R[Versioned rubric] --> P
    P --> A[Independent human A]
    P --> B[Independent human B]
    A --> L[Locked review returns]
    B --> L
    L --> G[Agreement and adjudication gate]
    G --> D[Conditional benchmark decision]
    H[Author hypotheses kept separate] --> Q[Post-review critique only]
```

The packet checker reads local files, validates shape and compares hashes. It
does not execute message contents or fetch links. It does not assess whether a
response was appropriate. No raw real incident evidence is included.

PacketVerifier owns the packet root and validation workflow. Shared bounded
reads enforce path boundaries; shared JSON decoding rejects ambiguous keys.
The CLI and verify(root) compatibility entry point call that same object.
Stateless case validation remains a function. This uses OOP for responsibility
and DRY for validation reuse without adding an inheritance hierarchy.

Local author hypotheses are outside the public manifest and distribution.
Review packets are separate physical copies for handoff, verified against one
canonical case set. No private file is necessary to run public regression.

## Completed-review infrastructure

ReviewStudy acquires a verified packet snapshot and validates completed CSVs
against exact metadata and the rubric. ReviewSubmission holds immutable copies
of the validated rows and declarations. Use load_submission as the public intake
boundary; direct constructors are trusted programming interfaces, not provenance
validation services. CSV parsing consumes the same bytes whose digest was checked.
Packet verification also retains the manifest and artifact bytes it checked;
calling verify() again refreshes them and detects subsequent drift.

Agreement uses exact rational intermediate counts for observed/expected nominal
agreement, then outputs JSON floats and approximate Wilson raw-agreement
intervals. Undefined kappa stays null. No semantic model is called. The numeric
threshold cannot approve the human gate, even for self-declared human inputs.

## Concurrent filesystem writers

Inputs are local files under the coordinator's control. Path resolution and
opening are separate operations: the tool does not isolate reads from an active
writer swapping symlinks or file types concurrently. Run from an owned, stable
directory, not a shared directory writable by an adversary. Bounded byte reads
and immutable verified snapshots protect parsed-byte consistency; they do not
provide kernel-enforced confinement, nonblocking FIFO safety or authenticity.
Use process/OS isolation before offering untrusted hosted intake.
