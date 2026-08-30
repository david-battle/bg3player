#!/usr/bin/env python3
"""Extract the base magic-item lists from bg3.wiki per-act pages.

Downloads the "List of magic items in Act One/Two/Three" pages via the
MediaWiki API and parses the item-location tables into a structured JSON file.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://bg3.wiki/w/api.php"
OUT = "data/items_base.json"

ACTS = [
    ("Act One", "List_of_magic_items_in_Act_One"),
    ("Act Two", "List_of_magic_items_in_Act_Two"),
    ("Act Three", "List_of_magic_items_in_Act_Three"),
]

# bg3.wiki rarity color -> rarity label
RARITY_COLORS = {
    "#01BD39": "Uncommon",
    "#01BFFF": "Rare",
    "#D1017B": "Very Rare",
    "#FF5901": "Legendary",
    "#B7861D": "Legendary",
    "#B48B1D": "Legendary",
}


def fetch_wikitext(page):
    url = API + "?action=parse&page=" + urllib.parse.quote(page) + \
        "&prop=text&format=json&formatversion=2"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)["parse"]["text"]


def strip_tags(html):
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\u200b", "", text)
    text = text.replace("\xa0", " ")
    return text.strip()


def parse_tables(html):
    items = []
    tables = re.findall(
        r'<table class="wikitable sortable"[^>]*>(.*?)</table>', html, re.S)
    for table in tables:
        rows = re.findall(r"<tr>(.*?)</tr>", table, re.S)
        for row in rows[1:]:
            tds = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
            if len(tds) != 4:
                continue
            name_m = re.search(r'title="([^"]+)"', tds[0])
            if not name_m:
                continue
            color_m = re.search(r'<span style="color: (#[0-9A-Fa-f]{6});">', tds[0])
            coord_m = re.search(
                r'class="bg3wiki-coordinates">X:?\s*&nbsp;(-?\d+)&nbsp;Y:?\s*&nbsp;(-?\d+)', tds[3])
            items.append({
                "name": name_m.group(1),
                "rarity_color": color_m.group(1).upper() if color_m else None,
                "rarity": RARITY_COLORS.get(color_m.group(1).upper()) if color_m else None,
                "list_effect": strip_tags(tds[1]),
                "list_where": strip_tags(tds[2]),
                "list_location": strip_tags(tds[3]),
                "coord_x": int(coord_m.group(1)) if coord_m else None,
                "coord_y": int(coord_m.group(2)) if coord_m else None,
            })
    return items


def main():
    out = []
    for act, page in ACTS:
        html = fetch_wikitext(page)
        items = parse_tables(html)
        print(f"{act}: {len(items)} items")
        for it in items:
            it["act"] = act
            out.append(it)
        time.sleep(0.5)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {len(out)} rows -> {OUT}")


if __name__ == "__main__":
    sys.exit(main())