#!/usr/bin/env python3
"""Fetch raw rendered HTML for every magic-item page from bg3.wiki.

Caches one .html file per item in data/raw_html/. Re-runnable: already
fetched items are skipped. Use --names or --limit to test on a batch.

Usage:
  python3 scripts/fetch_item_pages.py                 # fetch all missing
  python3 scripts/fetch_item_pages.py --names "A,B"   # fetch specific
  python3 scripts/fetch_item_pages.py --limit 10      # fetch first N missing
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://bg3.wiki/w/api.php"
BASE = "data/items_base.json"
HTMLDIR = "data/raw_html"
DELAY = 0.35
UA = "bg3player-kb/0.1 (personal knowledge base builder)"


def api_get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_page(name):
    data = api_get({
        "action": "parse", "page": name,
        "prop": "text|categories", "format": "json", "formatversion": "2",
    })
    if "error" in data:
        return None
    return data["parse"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", help="comma-separated item names to fetch")
    ap.add_argument("--names-file", help="file with one item name per line")
    ap.add_argument("--limit", type=int, help="fetch only first N missing items")
    args = ap.parse_args()

    items = json.load(open(BASE))
    os.makedirs(HTMLDIR, exist_ok=True)
    names = sorted({i["name"] for i in items})
    done = {f[:-5] for f in os.listdir(HTMLDIR) if f.endswith(".html")}
    todo = [n for n in names if n not in done]
    if args.names:
        todo = [n for n in args.names.split(",") if n.strip()]
    if args.names_file:
        with open(args.names_file) as f:
            todo = [l.strip() for l in f if l.strip()]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(names)} unique items, {len(todo)} to fetch")
    errors = []
    for idx, name in enumerate(todo):
        try:
            page = fetch_page(name)
            if page is None:
                errors.append((name, "no page"))
                continue
            html = page.get("text", "")
            cats = [c["category"] for c in page.get("categories", [])]
            out = {
                "title": page.get("title", name),
                "html": html,
                "categories": cats,
            }
            with open(os.path.join(HTMLDIR, name + ".html"), "w") as f:
                json.dump(out, f)
            if (idx + 1) % 25 == 0:
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