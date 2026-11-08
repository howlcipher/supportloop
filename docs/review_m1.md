# Review infrastructure code-review record

Scope: packet verification, completed-review intake, agreement arithmetic, demo
generation and associated regression tests. An isolated AI code reviewer used
read-only access to the public source and tests. It was not a human participant
and did not inspect private incident material or author expectations.

## Finding reconciliation

| Finding | Classification | Evidence and disposition |
| --- | --- | --- |
| Packet observations reread after verification | Confirmed medium integrity defect, corrected | Reviewer identified a verified-packet/observation race. A real filesystem-edit regression reproduced acceptance of changed observations. PacketVerifier now retains immutable hash-checked bytes. A new verification refreshes the snapshot and rejects disk drift. Reviewer independently rechecked the correction. |
| Direct script invocation fails | Out of documented interface scope | New commands are documented and tested as python3 -m scripts.review_tools / scripts.demo_reviews. Direct file invocation is not promised; module invocation works. No supported interface was removed. |
| Direct Python value-object construction can bypass intake | Trusted-programming interface limitation retained | The supported intake boundary is ReviewStudy.load_submission. CLI paths use it; compare validates rows and study identity, but low-level constructors are not authentication services. Documented explicitly; no human authority is granted. Revisit if an untrusted service API is added. |

The reviewer found no further actionable defect in the documented CLI flow
after the correction. It exercised targeted tests for review/demo behavior and
packet integrity. That scope does not establish semantic ticket accuracy,
production reliability or independent human agreement.

## Additional author-side falsification

Response intake originally hashed one read and parsed another. A failing
concurrent-edit test now protects parsing the exact checked byte snapshot.
A Python 3.11 symlink-loop reproduction exposed an unsanitized exception;
shared path handling now normalizes it. Arithmetic tests use independently
specified small confusion tables, including undefined kappa, rather than
asserting implementation details.

HowlProof separately evaluated two supplied deterministic arithmetic expressions
for the demo's 0.875 and -0.5 kappa cases. Those bounded checks were SUPPORTED;
the usefulness hypothesis was INCONCLUSIVE and the overall result remained
INSUFFICIENT_EVIDENCE. The arithmetic inputs were supplied synthetic assumptions,
not independently observed ticket outcomes. No result grants study acceptance.
