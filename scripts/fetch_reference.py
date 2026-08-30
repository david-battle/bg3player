#!/usr/bin/env python3
"""Fetch reference pages (feats, conditions, companions, permanent bonuses).

Resolves the conditions glossary seed from the wiki's Conditions category,
then caches rendered HTML for every needed page in data/raw_html_ref/.
Re-runnable: already fetched pages are skipped.
"""
import json
import os
import sys
import time

import requests

import reference_data as rd

OUT_SEED = "data/condition_seed.json"


def api(params):
    r = requests.get(rd.API, params={"format": "json", "formatversion": "2", **params},
                     headers={"User-Agent": rd.UA}, timeout=40)
    r.raise_for_status()
    return r.json()


def fetch_page(title):
    d = api({"action": "parse", "page": title, "prop": "text"})
    return d["parse"]["text"]


def category_members(cat):
    out, cont = [], None
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": f"Category:{cat}",
             "cmlimit": 500}
        if cont:
            p["cmcontinue"] = cont
        d = api(p)
        out += [m["title"] for m in d["query"]["categorymembers"]]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont:
            return out


def cache(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)


def main():
    os.makedirs(rd.HTMLDIR, exist_ok=True)

    conditions = category_members("Conditions")
    seed = rd.condition_seed(conditions)
    json.dump(seed, open(OUT_SEED, "w"), indent=1)
    print(f"condition seed: {len(seed)} pages")

    todo = (list(rd.MASTER_PAGES) + list(rd.COMPANION_PAGES) + list(rd.CLASS_PAGES)
            + list(rd.SUBCLASS_OF) + list(rd.RACE_PAGES)
            + list(rd.BACKGROUND_PAGES) + list(rd.ILLITHID_PAGES) + seed)
    fetched = skipped = 0
    for title in todo:
        path = os.path.join(rd.HTMLDIR, title + ".html")
        if os.path.exists(path):
            skipped += 1
            continue
        try:
            cache(path, fetch_page(title))
            fetched += 1
            time.sleep(rd.DELAY)
        except requests.RequestException as e:
            print(f"  fetch failed: {title}: {e}", file=sys.stderr)
    print(f"fetched {fetched} new pages, {skipped} already cached")


if __name__ == "__main__":
    main()