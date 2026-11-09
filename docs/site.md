# Research showcase operations

The public site is https://howlcipher.github.io/supportloop/.
Only site/ is uploaded; drafts, actual incident material, author hypotheses and
review returns are excluded from deployment. The page presents the methods
milestone, not an approved vendor-specific case study or validated classifier.

## Stack and alternatives

Plain semantic HTML and CSS need no runtime or build dependencies and are easy
to inspect. The trade-off is manual editorial updates. A React application adds
client tooling and dependencies without useful state here. A static-site generator
would help a larger publication collection, but is unnecessary for one page.
The page uses native anchors, a responsive layout, visible keyboard focus and a
skip link. No analytics, remote fonts, third-party scripts or forms are included.

## Assets and sharing

Share the Pages URL, rather than the GitHub repository URL, for the project-card
metadata. The repository has its own separately controlled preview. The page's
canonical URL, og:url, og:image and twitter:image use absolute public URLs.
assets/supportloop-social.png is an original 1200×630 diagram/typography card;
assets/evidence-flow.svg is the accessible in-page conceptual diagram. Neither
uses a profile picture, vendor logo or screenshot of a private account. The PNG
was drawn locally with Pillow and installed DejaVu fonts; serving it requires no
Pillow installation or image-generation service.

The SVG and page describe a conceptual evidence flow, not an observed empirical
result. Social platforms control their own caches and cropping. A correct HTTP
response and metadata support preview delivery but cannot guarantee a platform
refreshes an already cached card.

## Deployment

The existing regression/security workflow includes a Pages job only on main,
following successful regression and dependency/secret jobs. The job uploads
only site/ using pinned GitHub action revisions, with Pages and OIDC permissions
scoped to that job. Pull requests run regression but cannot deploy. Pages is
configured for workflow publishing. HTTPS is the intended public URL.

GitHub's [custom-workflow guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [Pages API](https://docs.github.com/en/rest/pages/pages) describe the deployment
mechanism. No private repository content is staged into the site artifact.

## Verification and rollback

Run the configured full gate before integration. Static tests protect image
metadata, image dimensions, landmarks, links and private-path exclusion. Preview
locally with python3 -m http.server --directory site, then check desktop/mobile
layout and keyboard navigation in a real browser. Test live HTML, CSS, SVG and
PNG responses after deployment and inspect canonical/social metadata.

A failed deployment is not a live-site success. Inspect the GitHub Pages job
and environment before reporting publication. To roll back, revert the site
change in a signed commit and let the same gates redeploy. Do not bypass tests
or delete unrelated owner changes. Editorial claims must track actual evidence;
new findings need journal and source-document updates before public changes.
