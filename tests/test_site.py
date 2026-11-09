"""Protect public-page assets, share metadata and navigation boundaries."""

import struct
import unittest
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

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "meta":
            self.meta[attrs.get("property", attrs.get("name"))] = attrs.get("content")
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs)


class SiteTests(unittest.TestCase):
    def page(self):
        parser = Page()
        parser.feed((ROOT / "index.html").read_text())
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

    def test_site_has_no_local_private_files_or_case_publication(self):
        text = (ROOT / "index.html").read_text()
        for forbidden in ["publication_drafts/", "private_evidence/", "author_material/", "review_returns/"]:
            self.assertNotIn(forbidden, text)
        self.assertIn("Human feasibility: pending", text)
        self.assertIn("Synthetic arithmetic", text)
        self.assertIn("No measured ticket accuracy", text)


if __name__ == "__main__":
    unittest.main()
