#!/usr/bin/env python3
"""Fetch consumable pages from bg3.wiki.

Builds data/consumables_base.json (name + type per item) from the wiki's
consumable categories, then caches the rendered HTML for every page (and the
Alchemy reference page) in data/raw_html_cons/. Re-runnable: already fetched
pages are skipped.

Usage:
  python3 scripts/fetch_consumables.py            # fetch all missing
  python3 scripts/fetch_consumables.py --limit 20 # fetch first N missing
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://bg3.wiki/w/api.php"
OUT = "data/consumables_base.json"
HTMLDIR = "data/raw_html_cons"
DELAY = 0.35
UA = "bg3player-kb/0.1 (personal knowledge base builder)"

# item type -> wiki category holding its pages
CATEGORIES = [
    ("Potion", "Potions"),
    ("Elixir", "Elixirs"),
    ("Scroll", "Scrolls"),
    ("Arrow", "Arrows"),
    ("Coating", "Coatings"),
    ("Grenade", "Grenades"),
    ("Ingredient", "Alchemical_ingredients"),
    ("Extract", "Alchemical_extracts"),
]

# reference page fetched alongside the item pages (recipe/ingredient tables)
EXTRA_PAGES = ["Alchemy"]


def api_get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def category_members(cat):
    out = []
    cont = None
    while True:
        p = {"action": "query", "list": "categorymembers",
             "cmtitle": "Category:" + cat, "cmlimit": "500", "cmtype": "page",
             "format": "json", "formatversion": "2"}
        if cont:
            p["cmcontinue"] = cont
        r = api_get(p)
        out += [m["title"] for m in r["query"]["categorymembers"]]
        cont = r.get("continue", {}).get("cmcontinue")
        if not cont:
            break
        time.sleep(0.2)
    return out


def fetch_page(name):
    data = api_get({
        "action": "parse", "page": name,
        "prop": "text|categories", "format": "json", "formatversion": "2",
    })
    if "error" in data:
        return None
    return data["parse"]


def cache_page(name):
    page = fetch_page(name)
    if page is None:
        return False
    html = page.get("text", "")
    cats = [c["category"] for c in page.get("categories", [])]
    with open(os.path.join(HTMLDIR, name + ".html"), "w") as f:
        json.dump({"title": page.get("title", name), "html": html,
                   "categories": cats}, f)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int,
                    help="fetch only first N missing pages")
    args = ap.parse_args()

    base = []
    for itype, cat in CATEGORIES:
        names = sorted(category_members(cat))
        for n in names:
            base.append({"name": n, "type": itype})
        print(f"{cat}: {len(names)}")
    with open(OUT, "w") as f:
        json.dump(base, f, indent=1)
    print(f"wrote {len(base)} rows -> {OUT}")

    os.makedirs(HTMLDIR, exist_ok=True)
    todo = [n for n in sorted({b["name"] for b in base})
            if not os.path.exists(os.path.join(HTMLDIR, n + ".html"))]
    todo += [p for p in EXTRA_PAGES
             if not os.path.exists(os.path.join(HTMLDIR, p + ".html"))]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(todo)} pages to fetch")
    errors = []
    for idx, name in enumerate(todo):
        try:
            if not cache_page(name):
                errors.append((name, "no page"))
            elif (idx + 1) % 25 == 0:
                print(f"  {idx + 1}/{len(todo)}")
        except Exception as e:
            errors.append((name, str(e)))
        time.sleep(DELAY)
    print("fetch complete")
    if errors:
        for name, err in errors:
            print(f"  ERROR {name}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())