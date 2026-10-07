"""Validate the real built site, without depending on removable example posts."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.nav_links = []
        self.nav_depth = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav":
            self.nav_depth += 1
        if tag == "a" and self.nav_depth and "nav-link" in attrs.get("class", "").split():
            self.nav_links.append(attrs.get("href"))
        for attr in ("href", "src", "poster"):
            if attrs.get(attr):
                self.links.append(attrs[attr])

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav_depth -= 1


def check(root):
    errors = []
    expected_nav = ["/", "/topics/", "/projects/", "/extra/"]
    for route in expected_nav:
        path = root / route.lstrip("/") / "index.html"
        if not path.is_file():
            errors.append(f"Missing main page: {route}")
            continue
        page = Page(path.read_text(encoding="utf-8"))
        if page.nav_links != expected_nav:
            errors.append(f"Wrong navigation on {route}: {page.nav_links}")

    pages = list(root.rglob("*.html"))
    if not pages:
        errors.append("No HTML pages were built")
    for path in pages:
        page = Page(path.read_text(encoding="utf-8"))
        for link in page.links:
            url = urlsplit(link)
            # External destinations are outside this deterministic local check.
            if url.scheme or url.netloc or not url.path:
                continue
            target = (root / unquote(url.path).lstrip("/")) if url.path.startswith("/") else (path.parent / unquote(url.path))
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"Link escapes site: {path.relative_to(root)} -> {link}")
            elif not target.is_file() and not (target / "index.html").is_file():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {link}")

    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"PASS: four navigation pages and local links/assets in {len(pages)} HTML files")


if __name__ == "__main__":
    check(Path(sys.argv[1]).resolve())
