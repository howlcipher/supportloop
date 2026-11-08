# Testing and impact assessment

Observable behavior: reject malformed, non-synthetic, label-contaminated or
drifted feasibility packets; accept valid observations with unknown timestamps.
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

Missing coverage: semantic accuracy, real exports, human agreement, completed
label intake and agreement computation. These are unimplemented and cannot be
inferred from a passing structural gate. No API or acceptance test of a product
is applicable. Python 3.11 compatibility requires an actual 3.11 gate; do not
claim it from a newer interpreter run. The public distribution must pass the
same gate in a temporary export containing only staged or committed files,
without author_material/, review_returns/, runs/ or the local virtualenv.
