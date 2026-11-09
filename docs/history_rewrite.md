# Authorized history rewrite

On November 9, 2026, the owner authorized redacting company and game names from
published Git branch history after the public edition had been generalized.
This is an editorial privacy change, not new evidence about the incident.

## Scope and provenance

The ten existing commits were reconstructed in their original sequence.
Historical text, filenames and commit messages were generalized; the old named
PDF was removed from historical trees. The current generic PDF remains. Original
authors and author dates were preserved. Replacement commits carry new committer
dates and signatures from the repository owner's configured signing key; these
signatures attest the rewrite, not the byte identity of the original commits.
A verified pre-rewrite bundle and old-to-new commit map remain private locally.

A scan of replacement commit objects, paths and all 141 unique reachable blobs
found none of the targeted company/game names. Current publication files were
unchanged by the redaction itself. Historical source hashes or test results can
refer to original, edited or removed artifacts; do not treat old revisions as
byte-identical reproductions or newly verified experimental results.

## Existing clones

Prefer a fresh clone of https://github.com/howlcipher/supportloop.git. Preserve
any uncommitted or unpublished work privately before replacing an older clone.
If unpublished changes must be retained, reapply only those reviewed changes to
the new history. Do not merge an old branch, restore old tags or push backup refs;
that can reintroduce the removed material. No published tags existed at rewrite.

## Hosting limits

Only the published branch history can be replaced through a Git push. Old
pull-request refs, commit URLs, workflow records, caches, forks and downloaded
copies can retain the former edition. Editable pull-request metadata can be
generalized; GitHub controls internal pull-request refs and cached objects.
No claim of complete erasure or guaranteed de-identification is made.

GitHub's [removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
describes these retention limits and potential support-assisted cleanup.
No support request or third-party message is sent by this procedure.
