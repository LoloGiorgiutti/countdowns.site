#!/usr/bin/env python3
"""Generate sitemap.xml from all built HTML pages."""

import os
from datetime import date

BASE_URL = "https://countdowns.site"
ROOT = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()

EXCLUDE = {"/admin", "/custom", "/es/custom", "/pt/custom", "/fr/custom",
           "/embed", "/es/embed", "/pt/embed", "/fr/embed", "/countdowns-src"}

def get_priority(path):
    if path == "":
        return "1.0"
    if path in ("/es", "/pt", "/fr"):
        return "0.9"
    if not path.startswith(("/es/", "/pt/", "/fr/")):
        return "0.8"
    return "0.6"

def get_changefreq(path):
    if path in ("", "/es", "/pt", "/fr"):
        return "daily"
    return "weekly"

urls = []
for dirpath, _, files in os.walk(ROOT):
    if "index.html" not in files:
        continue
    rel = dirpath.replace(ROOT, "").replace("\\", "/")
    if any(part.startswith(".") for part in rel.split("/") if part):
        continue
    if any(rel == excl or rel.startswith(excl + "/") for excl in EXCLUDE):
        continue
    urls.append(rel)

urls.sort()

lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for path in urls:
    url = BASE_URL + path + "/"
    priority = get_priority(path)
    changefreq = get_changefreq(path)
    lines.append("  <url>")
    lines.append(f"    <loc>{url}</loc>")
    lines.append(f"    <lastmod>{TODAY}</lastmod>")
    lines.append(f"    <changefreq>{changefreq}</changefreq>")
    lines.append(f"    <priority>{priority}</priority>")
    lines.append("  </url>")

lines.append("</urlset>")

out = os.path.join(ROOT, "sitemap.xml")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated sitemap.xml with {len(urls)} URLs.")
