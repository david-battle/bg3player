#!/usr/bin/env python3
"""Parse cached consumable pages into structured JSON records.

Reads data/raw_html_cons/*.html for every consumable in
data/consumables_base.json, writes data/consumables_raw/*.json. Offline; only
depends on the cache.

For alchemical ingredients the page's "Combine 3 of these to create X" line is
captured as `extract_of`.
"""
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_item_pages import (  # noqa: E402
    strip_tags, parse_rarity, parse_description, parse_quote,
    parse_properties, parse_where,
)

BASE = "data/consumables_base.json"
HTMLDIR = "data/raw_html_cons"
RAWDIR = "data/consumables_raw"

TYPE_CATEGORIES = {
    "Potions": "Potion",
    "Elixirs": "Elixir",
    "Scrolls": "Scroll",
    "Arrows": "Arrow",
    "Coatings": "Coating",
    "Grenades": "Grenade",
    "Alchemical_ingredients": "Ingredient",
    "Alchemical_extracts": "Extract",
}

def classify_type(categories):
    for cat in categories:
        if cat in TYPE_CATEGORIES:
            return TYPE_CATEGORIES[cat]
    return None


def parse_extract_of(html, extract_names):
    # first <a title="X"> in the lead paragraph whose title is a known
    # extract page (handles the wiki's many verb-phrase variants)
    lead = html[:8000]
    for m in re.finditer(r'<a[^>]*title="([^"]+)"', lead):
        if m.group(1) in extract_names:
            return m.group(1)
    return None


def main():
    os.makedirs(RAWDIR, exist_ok=True)
    base = json.load(open(BASE))
    extract_names = {b["name"] for b in base if b["type"] == "Extract"}
    missing = []
    for entry in base:
        name = entry["name"]
        path = os.path.join(HTMLDIR, name + ".html")
        if not os.path.exists(path):
            missing.append(name)
            continue
        cache = json.load(open(path))
        html = cache["html"]
        cats = cache["categories"]
        rec = {
            "name": name,
            "title": cache.get("title", name),
            "url": "https://bg3.wiki/wiki/" + urllib.parse.quote(
                cache.get("title", name).replace(" ", "_")),
            "type": classify_type(cats) or entry["type"],
            "rarity": parse_rarity(html),
            "description": parse_description(html),
            "quote": parse_quote(html),
            "properties": parse_properties(html),
            "where_to_find": parse_where(html),
            "notes": [],  # filled by section parse below
            "bugs": [],
            "extract_of": parse_extract_of(html, extract_names),
            "categories": cats,
        }
        for hname, field in (("Notes", "notes"), ("Bugs", "bugs")):
            seg = re.search(
                r'id="' + hname + r'".*?</h2>(.*?)(?=<h2|<div id="catlinks|$)',
                html, re.S)
            if seg:
                rec[field] = [
                    strip_tags(li) for li in re.findall(r"<li>(.*?)</li>", seg.group(1), re.S)
                    if strip_tags(li)
                ]
        with open(os.path.join(RAWDIR, name + ".json"), "w") as f:
            json.dump(rec, f, indent=1)
    if missing:
        print(f"MISSING pages (not cached): {len(missing)}")
        for m in missing:
            print("  " + m)
        sys.exit(1)
    print(f"wrote {len(base)} records -> {RAWDIR}")


if __name__ == "__main__":
    sys.exit(main())