# Change log

## Unreleased

### Review infrastructure, packet 0.3.0 and rubric 0.2.0

Added strict completed-review CSV/metadata intake, immutable submissions,
descriptive per-dimension agreement reports and a deterministic synthetic demo.
Reports preserve uncertainty and keep human approval separate from numeric
thresholds. Added CLI/library integration and failure-oriented tests.
Fixed response and packet snapshot races and Python 3.11 symlink-loop errors.
Independent code review found and rechecked the packet snapshot correction.

Added a review protocol and preliminary engineering findings. Publication drafts
stay local for owner review. No semantic classifier, independent human labels,
customer-outcome results or vendor-specific incident publication is claimed.

### Public foundation, packet 0.2.0

Added a bounded UX research plan for annual subscription defaults, selection
persistence, price/term visibility and accidental commitment. Vendor-specific
behavior and design intent remain unverified; no real incident is published.

The synthetic research foundation is public at howlcipher/supportloop. The
initial signed commit passed hosted regression/security CI on Python 3.11 and
3.14. Subsequent commits are checked by the same workflow.

Added a gated roadmap, findings and bugs report, public engineering journal,
contribution guidance, MIT license and regression/security CI. Continued with
Python and standard-library runtime code. Added a PacketVerifier object with
shared bounded file/JSON validation and retained the verify(root) entry point.

Fixed dependence on unpublished author files, unchecked manifest metadata,
duplicate JSON keys, surplus CSV cells and quoted-newline blank-field handling.
Excluded author expectations, private evidence, review returns and local run logs
from publication. Added failing reproductions before fixes and retained prior
regression contracts. Human feasibility remains pending; no analyzer or real
incident results are published.

### Initial local preparation, packet 0.1.0

Prepared a local feasibility study with 24 synthetic histories, 103 events,
rubric 0.1.0, two blank observation-only reviewer packets and separate author
hypotheses. Added a hashed manifest, standard-library packet checker, behavioral
failure tests, HowlPlane project commands, evaluation gates and case study plan.
No independent human labels or analyzer results exist. Human feasibility is
pending because reviewers are unavailable. No product release or publication.

## Discovery completion record

Documented the NARROW decision, verified milestone evidence and remaining human,
comparison, incident and publication gates. Prepared local review worksheets.
No runtime, tests, dependencies or evaluation thresholds changed.

## Research showcase and provider review

Added a static GitHub Pages showcase, original project diagram and 1200×630 PNG
social card, with canonical/Open Graph/Twitter metadata. Deployment publishes
only site/ after existing regression/security jobs pass on main. No tracking,
external fonts, framework or runtime dependency was added.

Corrected demo fixtures to cite an event actually present in each valid case,
with a failing non-E1 packet integration test before the fix. Clarified the
insufficient-evidence agreement test and retained its category-count assertions.
Provider findings are preserved with explicit reconciliation and review limits.

Further provider findings corrected finite-float parsing, BOM-aware CSV intake,
ASCII identifiers/digits, confounded independence tests, row-width coverage and
symlinked-temporary-directory test portability. Reports include tool_version;
trust boundaries and before-study prerequisites remain explicit. Original review
responses and all 17 dispositions are public. Final local suite contains 55 tests.

## Deployment runtime follow-up

The first successful Pages deployment reported deprecated Node 20 action
runtimes. Updated to released, SHA-pinned configure-pages v6.0.0,
upload-pages-artifact v5.0.0 and deploy-pages v5.0.1. Pinned Ubuntu 24.04 to
avoid an implicit runner-image migration. Application and site bytes unchanged.
