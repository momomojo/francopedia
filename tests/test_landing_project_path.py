"""Regression coverage for project-path navigation on GitHub Pages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
import unittest


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.brand_href = None

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attributes = dict(attrs)
        if "brand" in attributes.get("class", "").split():
            self.brand_href = attributes.get("href")


class LandingProjectPathTests(unittest.TestCase):
    def test_brand_link_resolves_to_project_root_from_landing_path(self):
        parser = AnchorParser()
        landing = Path(__file__).parents[1] / "landing" / "index.html"
        parser.feed(landing.read_text(encoding="utf-8"))

        self.assertIsNotNone(parser.brand_href)
        assert parser.brand_href is not None
        resolved = urlparse(
            urljoin(
                "https://momomojo.github.io/francopedia/landing/",
                parser.brand_href,
            )
        )

        self.assertEqual(resolved.path, "/francopedia/")


if __name__ == "__main__":
    unittest.main()
