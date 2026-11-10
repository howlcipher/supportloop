# Testing and impact assessment

Observable behavior: reject malformed packets, non-synthetic declarations,
structured label fields, nonblank reviewer forms or locked-artifact drift;
accept valid observations with unknown timestamps.
No support classification behavior exists.

The original fifteen contracts protect accepted packet shape,
timestamp validity and cutoffs, event identity, synthetic-only input, reviewer
isolation and inert instruction-like text. They still express intended behavior.
There are no obsolete contracts to remove. Public release intentionally removes
the author-file dependency from the packet contract; observations, blank forms
and independent-label boundaries retain their behavioral protections.

Eight additional contracts now protect a public checkout without author files,
manifest metadata, duplicate keys, nonfinite JSON, surplus CSV cells, quoted
newlines, path escapes and sanitized CLI errors. Reproductions ran before the
corrections; see issues.md. The verifier object shares parsing and validation
with the compatibility function and CLI. No tests mirror class structure.

The smallest tier is the affected unittest. The integration tier verifies the
whole packet and both blank reviewer forms. The complete gate is:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/verify_packet.py
python3 -m flake8 scripts tests
python3 -m bandit -q -r scripts
python3 -m pip_audit -r requirements_dev.txt
```

Tools are development-only dependencies pinned in requirements_dev.txt. Tests,
packet checking, lint and static analysis need no network, inference or private
data. Dependency auditing queries external package/advisory services. CI also
runs a pinned, checksum-verified gitleaks history scan. Run the test/lint/packet
gate through HowlPlane using .ai-project.toml as well.
Repeat after any final source, test or configuration changes.

Twenty-five further contracts cover completed-review metadata/CSV intake,
missing/duplicate rows, invalid references/codes/dimensions, hash identities,
same-reviewer inputs, model/synthetic and self-attested human authority limits,
known confusion/kappa arithmetic, undefined kappa, immutable snapshots under
concurrent edits, Python 3.11 path errors, deterministic demo generation,
overwrite refusal and the complete demo/validate/compare CLI flow. Prior
contracts remain in place; no obsolete or duplicate tests were removed.

Packet 0.3.0 and rubric 0.2.0 are intentional pre-study contract revisions.
There are no collected human returns to migrate. The revised contracts add
synthetic provenance and metadata without changing the case observations or
weakening evidence gates.

Missing coverage: semantic accuracy, real exports, human agreement and measured
customer outcomes. These cannot be inferred from passing software tests. No HTTP
API is implemented; the library and CLI have behavioral integration tests.
Python 3.11 compatibility requires an actual 3.11 gate; do not
claim it from a newer interpreter run. The public distribution must pass the
same gate in a temporary export containing only staged or committed files,
without author_material/, review_returns/, runs/ or the local virtualenv.

Provider-review/site additions protect one further demo contract: a valid
packet without E1 must still generate valid referenced fixtures. The agreement
test is renamed to refer to insufficient_evidence and now checks both marginals;
no protection is removed or duplicated. Three static-site contracts check real
PNG dimensions and metadata, local navigation/assets, landmarks and absence of
private publication paths. Source, CI and site changes require the full gate.
Browser checks additionally exercise 1440, 390 and 320 pixel layouts, keyboard
skip navigation, console errors and document overflow. A narrow-screen table
overflow was reproduced and corrected during these checks. They do not certify
complete accessibility conformance or external social-platform cache behavior.

Further provider review strengthened existing parser, width and independence
contracts instead of appending duplicate tests. New coverage checks ASCII
identifiers, completed-row widths and BOM-preserving intake. Nonfinite parser
tests now isolate named constants and overflowing numeric literals. A source
mutation that ignored author/exposure claims survived the original test and is
rejected by the strengthened test. Symlinked temporary-directory tests were
reproduced against the old snapshot and pass with resolved fixture paths.

Named-article publication adds one contract for its separate canonical/social
identity, declared Markdown source hash, evidence notices, private-path exclusion,
working local links and actual PDF signature. The old test name suggesting no
case publication is updated to reflect authorized observational publication; its
private-input and research-limit checks remain. No backend tests are removed or
weakened. The full regression and staged public-export gate apply to the final
article, stylesheet, PDF, source and authority documentation. Test success cannot
verify the participant's report or establish improvement efficacy.

Anonymization updates the existing article contract for generic source/PDF paths
and an explicit omission notice. No backend behavior changes, tests removed or
duplicate tests added. The source hash, real assets, links and evidence notices
remain protected. Full regression, public-export checks and browser acceptance
cover the final edition; a tracked-text and extracted-PDF scan checks names.

The comprehensive audit adds one discovery-file contract: parsed sitemap URLs
must equal the two canonical public pages, resolve to local publication files
and remain unique; robots.txt must declare the sitemap. It failed before the
missing files were added. Existing 56 contracts remain intended and unchanged;
no obsolete, duplicate or weakened tests were identified in this pass. Runtime
code is unchanged. Full regression and public export apply to the final tree.
Manual review, deterministic arithmetic cross-checks and the scoped HowlProof
checks complement tests; they cannot establish semantic accuracy or human labels.
