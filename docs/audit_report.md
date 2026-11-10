# Comprehensive audit: software, evidence and publication

Audit run date: November 10, 2026 UTC, from evaluator timestamps. Starting
revision: `4ee81ce`. Recommendation remains **NARROW**. The observational case
and methods are useful public deliverables; no validated ticket analyzer exists.

## Outcome

The pass reproduced and corrected one missing publication capability, corrected
three documentation/provenance issues, and retained one informational evaluator
finding. No new high-severity software or security defect was reproduced within
the reviewed scope. This is not an exhaustive correctness or security guarantee.

The full regression passes 57 tests on Python 3.11 and 3.14. Packet verification,
flake8, Bandit and dependency auditing pass. The packet still reports
human_gate=PENDING and semantic_accuracy=NOT_EVALUATED. No private incident
artifacts, author expectations or review returns were used for this audit.

## Scope and method

The coordinator inspected every runtime module, its tests, packet/label contracts,
public incident narrative, research summaries, source/PDF binding, static site,
workflow, publication authority and history-rewrite documentation. Correctness,
regression, trust boundaries, test adequacy, architecture and simplicity were
separate review lenses, not fabricated independent reviewers. Local independent
execution by HowlProof complements this author-side inspection; it does not
supply independent human labels or semantic verification.

| Surface | Evidence examined or exercised | Limit |
| --- | --- | --- |
| Packet | Canonical observations, hashes, reviewer copies, field/size/path checks and failure tests | Integrity is not authenticity; relocking both data and manifest can forge provenance |
| Review intake | Complete CSV/metadata binding, references, dimensions, immutable bytes, sanitized failures | Identity and independence remain declarations; trusted constructors are not an intake/authentication boundary |
| Statistics | Existing exact confusion-table tests plus 5,000 deterministic generated comparisons with a separate marginal-count calculation | Same coordinator authored the cross-check; no support judgments or new empirical sample |
| CLI | Real help/misuse invocations by HowlProof; demo/validate/compare integration tests | Fixed misuse catalogue and owned stable files, not hostile-filesystem isolation |
| Publication | Source hash, link/assets/PDF checks, evidence wording, original project image and new sitemap contract | No inspection of historical checkout, ticket originals, transaction logs or public support post |
| Website | Independent Chromium rendering of both pages at 320, 390, 768 and 1440 pixels; metadata/link checks | Not complete accessibility conformance, indexing or social-cache certification |
| Security/release | Credential-pattern scan, pinned CI actions, scoped workflow authority, Bandit and dependency advisory audit | Pattern/advisory coverage is bounded; this is not a penetration test or hostile-service approval |
| Research | Revisited primary-source product descriptions and existing stop/go gates | No interviews, configured commercial benchmark or production outcomes |
| History | Rewrite scope, private recovery backup, source-tree mapping and retained-hosting caveats | Old hosting references and external copies are not erased |

## Findings and dispositions

| ID | Severity | Evidence | Disposition |
| --- | --- | --- | --- |
| AUD-001 | Low | HowlProof web.metadata failed for absent robots.txt and sitemap.xml; the new parsed-sitemap test failed before files existed | Added both files, restricted sitemap entries to current canonical public pages, and verified the fix with HowlProof |
| AUD-002 | Low | ROADMAP.md still called the published site methods-only although the authorized case was live | Corrected current scope and final case-text capitalization; earlier journal entries remain historical |
| AUD-003 | Low | Prior-art shorthand did not clearly distinguish offering a solution from execution, and understated loop/intent/question overlap | Qualified terminology and refreshed primary-source descriptions; no accuracy or unmet-market claim added |
| AUD-004 | Low | Adjacent review/CI prose retained original commit IDs after history rewrite without mappings | Added rewritten IDs and verified reviewed-tree equivalence; raw provider responses and input record remain unmodified |
| AUD-005 | Informational | HowlProof's expanded lexical inventory lists absolute phrasings, including normative instructions and evidence limits | Inventory retained; normative instructions and evidence limits are not false merely because a keyword matched |

robots.txt under a GitHub Pages project path does not control host-root crawler
policy. Adding it satisfies the declared publication convention, not a security
requirement or guarantee of search indexing. The sitemap remains directly
retrievable. No indexing, cache removal or guaranteed de-identification is claimed.

The original review snapshot and its rewritten equivalent share Git tree ID
`a9b395ac7e8675edce534ca8957b4080bd89e829`. This supports source equivalence at
that snapshot, not a new review of later additions or a rerun of old CI.

## What HowlProof actually ran

HowlProof version: 0.2.0b1. Authority: ADVISORY. Evaluator implementation hashes,
individual limitations and immutable target digests are retained in local bundles
outside the evaluated repository. No additional model/provider was invoked.

| Run | Result | Interpretation |
| --- | --- | --- |
| hp-20261110-043814-0eb3749ac55e | INSUFFICIENT_EVIDENCE; 2 verified checks, 1 informational finding | Original documentation-only config has no acceptance criteria; inventories phrasing and compares rubric copies |
| hp-20261110-043841-a07958e06c43 | REJECT; 7/8 checks verified, metadata failed | Broader contract correctly failed its required discovery-metadata criterion |
| hp-20261110-044122-213ff7a160df | VERIFIED_FIXED for HP-OPS-0002 | Re-executed web.metadata against changed files; lifecycle recorded, no silent dismissal |
| hp-20261110-044144-a1ea971157d3 | PROVEN within the declared engineering scope; 8/8 checks verified, 2/2 criteria satisfied | Static credential patterns, CI supply chain, review CLI misuse, rubric copies, site links, metadata and responsive rendering |

The successful run retains the informational documentation inventory. There are
no failed, skipped, unavailable, simulated or inapplicable checks in that scoped
run. Its positive verdict does not extend to unchecked behavior. External links
were not fetched by HowlProof in the offline engineering pass. The coordinator's
separate primary-source research is not an output of that check.

The run above preceded assembly of this report. Final-tree regression and a
fresh scoped evaluation are required before integration; current CI remains the
source for the integrated commit's regression status. Local run artifacts retain
that final verification rather than rewriting these historical run records.

Reproduce the declared engineering checks with an installed HowlProof and its
browser tooling:

```bash
howlproof validate coordination/howlproof_audit.yaml
howlproof evaluate . --config coordination/howlproof_audit.yaml --evidence-root /tmp/supportloop-proof
```

Use an evidence root outside the repository. Keep the original howlproof.yaml
for its deliberately narrower documentation inventory. HowlProof's Python
profile expects a pyproject/pytest/ruff packaging surface; this standard-library
unittest toolkit does not declare one. Do not add packaging or pretend those
checks ran merely to obtain a positive verdict. HowlPlane and the configured
project commands independently execute the actual unittest/packet/lint gates.

## Research and incident conclusions

The public narrative consistently attributes the experience to the customer,
preserves the November 8 observation cutoff, and does not infer ticket closure,
unseen internal work, SLA breach, refund entitlement or manipulative intent.
The checkout-default concern remains a reported perception requiring historical
screens or a separately designed experiment. A justified denial can be a complete
decision. No new original incident evidence was supplied or independently verified.

Primary-source review still supports extensive overlap. [Zendesk's category
documentation](https://support.zendesk.com/hc/en-us/articles/7043747123354-Understanding-autoscoring-categories)
describes proposal/comprehension checks; its [QA product page](https://www.zendesk.com/service/quality-assurance/)
also advertises loop detection. [Intercom's metric definitions](https://www.intercom.com/help/en/articles/7022438-reporting-metrics-attributes)
separate answered, assumed and confirmed states. [Chatwoot's Captain reporting](https://www.chatwoot.com/hc/user-guide/articles/1791891433-captain-overview-and-reports)
includes reopening and closure persistence. These are documented features and
vendor claims, not independently benchmarked correctness. The expanded details
and source-access limitation are recorded in [prior art](prior_art.md).

A portable evidence contract remains an unvalidated opportunity. Do not expand
into an automatic ticket grader until the independent-human and benchmark gates
permit it. This audit is useful engineering evidence, not a passed feasibility
study or proof that organizations need another product.

## Retained limits and next gates

Independent human reviews remain unavailable. Existing GAP-003 tracks interrupted
demo output; GAP-004 requires frozen operational instructions before collecting
labels; GAP-005 excludes active hostile filesystem writers and hosted untrusted
intake. Collection-time plausibility and control-subset interpretation still need
manual provenance/methodology review. None is silently reclassified as fixed.

The observational case may be shared within its existing authorization and
qualifications. Original private artifacts, new evidence and third-party messages
retain their separate authority boundaries. No vendor, reviewer or social-media
contact was initiated by this audit.
