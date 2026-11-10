"""Protect public-page assets, share metadata and navigation boundaries."""

import hashlib
import struct
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / "site"
BASE = "https://howlcipher.github.io/supportloop/"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.links = []
        self.meta = {}
        self.images = []
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta":
            self.meta[attrs.get("property", attrs.get("name"))] = attrs.get("content")
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs)


class SiteTests(unittest.TestCase):
    def page(self, filename="index.html"):
        parser = Page()
        parser.feed((ROOT / filename).read_text())
        return parser

    def test_social_preview_is_a_project_image_with_real_dimensions(self):
        page = self.page()
        for name in ["og:image", "twitter:image"]:
            self.assertEqual(page.meta[name], BASE + "assets/supportloop-social.png")
        self.assertEqual(page.meta["og:url"], BASE)
        self.assertEqual(page.meta["twitter:card"], "summary_large_image")
        data = (ROOT / "assets/supportloop-social.png").read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", data[16:24]), (1200, 630))
        self.assertTrue(page.meta["og:image:alt"])

    def test_discovery_files_list_only_canonical_public_pages(self):
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap = ET.fromstring((ROOT / "sitemap.xml").read_bytes())
        locations = [node.text for node in sitemap.findall("s:url/s:loc", namespace)]
        canonical = [self.page().canonical, self.page("case-study.html").canonical]
        self.assertEqual(len(locations), len(set(locations)))
        self.assertEqual(set(locations), set(canonical))
        robots = (ROOT / "robots.txt").read_text()
        self.assertIn("User-agent: *", robots)
        self.assertIn("Sitemap: " + BASE + "sitemap.xml", robots)
        for location in locations:
            self.assertTrue(location.startswith(BASE))
            relative = location.removeprefix(BASE) or "index.html"
            self.assertTrue((ROOT / relative).is_file())

    def test_navigation_and_images_resolve_without_private_material(self):
        page = self.page()
        for href in page.links:
            parsed = urlsplit(href)
            if parsed.scheme:
                self.assertEqual(parsed.scheme, "https")
            elif href.startswith("#"):
                self.assertIn(href[1:], page.ids)
            else:
                target = (ROOT / parsed.path).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()))
                self.assertTrue(target.is_file())
        self.assertTrue(page.images)
        for attrs in page.images:
            self.assertTrue(attrs.get("alt"))
            self.assertTrue((ROOT / attrs["src"]).is_file())
        for tag in ["header", "nav", "main", "footer"]:
            self.assertIn(tag, page.tags)
        self.assertEqual(page.tags.count("h1"), 1)
        self.assertNotIn("script", page.tags)

    def test_site_keeps_private_inputs_out_and_research_limits_explicit(self):
        text = (ROOT / "index.html").read_text()
        for forbidden in ["publication_drafts/", "private_evidence/", "author_material/", "review_returns/"]:
            self.assertNotIn(forbidden, text)
        self.assertIn("Human feasibility: pending", text)
        self.assertIn("Synthetic arithmetic", text)
        self.assertIn("No measured ticket accuracy", text)

    def test_authorized_case_has_own_share_identity_and_evidence_limits(self):
        page = self.page("case-study.html")
        url = BASE + "case-study.html"
        self.assertEqual(page.canonical, url)
        self.assertEqual(page.meta["og:url"], url)
        self.assertEqual(page.meta["og:image"], BASE + "assets/supportloop-social.png")
        self.assertEqual(page.meta["twitter:image"], page.meta["og:image"])
        source = ROOT.parent / "docs/subscription_case_study.md"
        self.assertEqual(
            page.meta["supportloop:source-sha256"], hashlib.sha256(source.read_bytes()).hexdigest()
        )
        text = (ROOT / "case-study.html").read_text()
        self.assertIn("Provider names are omitted", text)
        self.assertIn("Customer-reported account", text)
        self.assertIn("November 8, 2026", text)
        self.assertIn("not independently verified", text)
        self.assertNotIn("almost predatory", text)
        self.assertEqual(page.tags.count("h1"), 1)
        self.assertNotIn("script", page.tags)
        for forbidden in ["publication_drafts/", "private_evidence/", "author_material/", "review_returns/"]:
            self.assertNotIn(forbidden, text)
        for href in page.links:
            parsed = urlsplit(href)
            if parsed.scheme:
                self.assertEqual(parsed.scheme, "https")
            elif href.startswith("#"):
                self.assertIn(href[1:], page.ids)
            else:
                target = (ROOT / parsed.path).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()))
                self.assertTrue(target.is_file())
        pdf = ROOT / "assets/subscription-support-case-study.pdf"
        self.assertTrue(pdf.read_bytes().startswith(b"%PDF-"))


if __name__ == "__main__":
    unittest.main()
