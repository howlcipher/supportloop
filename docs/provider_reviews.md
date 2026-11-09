# AGY and Claude Code review reconciliation

Both requested providers reviewed commit `8e9e7411360a3680edcef861bb1ad68cb3f3f9f5` from the same frozen public-only source bundle. AGY was requested as Gemini 3.8 Flash High; Claude Code resolved the Opus alias to claude-opus-5-5 according to its runtime metadata. The initial Claude process was interrupted without a result; its successful retry is the review recorded here. No private evidence, publication drafts, author hypotheses or other reviewer findings were supplied.

These are independent AI static code/methodology reviews, not independent human labels. Neither provider ran tests or reviewed the new website. Dataset files, full reviewer packets, CI and some linked documents were omitted; raw responses preserve these limitations. Coordinator-side reproductions and final regression are separate evidence. Positive reviewer comments are not treated as blanket certification.

[AGY original response](reviews/agy_static.json) · [Claude original response](reviews/claude_static.json) · [Input identity](reviews/review_input.json) · [Structured dispositions](reviews/reconciled_findings.json)

## Every finding and disposition

### AGY-SL-01: Hardcoded event reference 'E1' in demo review fixtures introduces unverified data dependency

Original severity: low. Classification: confirmed.

Corrected dynamic event references after a valid non-E1 packet and failing integration regression reproduced the defect.

### AGY-SL-02: Symlink loop resolution in resolve_path catches RuntimeError but omits OSError

Original severity: low. Classification: false_positive.

No documented library promise normalizes every OSError to ValueError. Python 3.11 self-loop raised normalized ValueError; 3.14 nonstrict resolution returned and intake rejected it safely. Existing CLI test passes both versions. No reproduced CLI leak.

### AGY-SL-03: Test test_unknown_category_is_counted_as_a_real_label is misnamed and does not exercise the unknown category

Original severity: informational. Classification: confirmed.

Renamed the test to insufficient_evidence and asserted both category marginals. No duplicate test appended.

### AGY-SL-04: Non-atomic demo directory creation leaves unmanaged partial state on interrupted runs

Original severity: informational. Classification: out_of_scope.

Atomic output publication was not promised. Interrupted partial output is a retained limitation; documented completion/retry rules and GAP-003 track a possible enhancement. No automatic deletion or overwrite introduced.

### CLAUDE-SLR-01: Independence-claim regression test passes even if case_author and prior_exposure are ignored

Original severity: medium. Classification: confirmed.

A source mutant ignoring author/exposure survived original tests. Strengthened test isolates each flag against a fully attested opposite reviewer on both sides; mutant is now rejected.

### CLAUDE-SLR-02: Nonfinite-JSON test is vacuous, and nonfinite rejection misses overflowing float literals

Original severity: low. Classification: confirmed.

Replaced vacuous manifest-shape test with direct parser contracts and finite-value acceptance. Overflow reproduction failed before adding finite parse_float handling.

### CLAUDE-SLR-03: CSV row-width checks are not discriminated by tests; intake width check has no regression at all

Original severity: low. Classification: confirmed.

Template width test now appends an empty surplus cell. Completed intake has explicit empty/nonempty surplus and short-row regressions; existing guard retained.

### CLAUDE-SLR-04: Reviewer README.md and A/B separation are unvalidated despite 'label-contaminated' rejection claim

Original severity: low. Classification: confirmed.

Narrowed testing claims to structural labels/forms and documented free-text/order inspection as procedural. Relocking a modified packet is not an authenticity attack the tool claims to prevent; no canonical-README or isolation guarantee added.

### CLAUDE-SLR-05: Normative review protocol and intake semantics are not bound to the locked packet or the report

Original severity: low. Classification: out_of_scope.

Added tool_version to reports. Freezing/distributing normative instructions and centralizing rubric constants are before-M2 work in GAP-004; this ops guide/source is not presently manifest-locked. No human collection or acceptance claimed.

### CLAUDE-SLR-06: Regex `\d` accepts non-ASCII digits in elapsed_seconds and identifiers

Original severity: low. Classification: confirmed.

Identifiers and elapsed digits now explicitly use ASCII ranges, protected by failure tests.

### CLAUDE-SLR-07: Excel-style UTF-8 BOM returns are rejected with an undiagnosable error

Original severity: low. Classification: confirmed.

UTF-8 BOM accepted at parsing without altering raw hashed bytes; regression covers immutable originals. Type-only CLI diagnostics remain an explicit privacy trade-off.

### CLAUDE-SLR-08: Snapshot regression tests compare resolved roots to unresolved temp paths and fail on symlinked temp dirs

Original severity: low. Classification: confirmed.

Original snapshot tests fail with symlinked TMPDIR; resolved test fixtures pass in that environment.

### CLAUDE-SLR-09: Path-boundary check and open are not atomic (symlink swap / FIFO races)

Original severity: low. Classification: out_of_scope.

Active hostile filesystem writers are outside current local-file threat model. Explicit stable-owned-directory requirement and separate-open race are documented; GAP-005 blocks treating it as hosted untrusted intake.

### CLAUDE-SLR-10: ReviewSubmission is documented as 'validated' but direct construction bypasses validation; compare() revalidation is partial

Original severity: informational. Classification: confirmed.

Value-object docstring corrected to identify load_submission as the validation boundary. Trusted direct construction remains explicitly unsupported as authentication.

### CLAUDE-SLR-11: Contract-required control-case and prevalence-sensitivity reporting is not implemented

Original severity: informational. Classification: out_of_scope.

Control subsets and prevalence interpretation remain manual before-M2 gates. No study acceptance is emitted; no automatic adjustment statistic added without a preregistered interpretation.

### CLAUDE-SLR-12: collected_at accepts implausible declared times

Original severity: informational. Classification: out_of_scope.

Collection time is a self-declaration checked for format/timezone, not temporal authenticity. Manual provenance review remains required; no automatic human pass is possible.

### CLAUDE-SLR-13: Minor documentation inconsistencies

Original severity: informational. Classification: confirmed.

Agent final-gate text aligned with TESTING.md; historical four initial groups plus later fifth correction clarified.

## Remaining boundary

No blocker or high-severity finding was reported. The medium finding concerned confounded test coverage, not an observed automatic human-gate bypass. Confirmed changes preserve the pending human gate. Out-of-scope enhancements and before-study prerequisites remain visible in issues.md; they are not silently called fixed. The site is reviewed separately through static tests, browser checks and hosted deployment. Passing these checks does not establish semantic ticket accuracy or commercial value.
