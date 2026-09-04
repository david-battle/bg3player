#!/usr/bin/env python3
"""Parse cached raw item-page HTML into structured JSON records.

Reads data/raw_html/*.html, extracts fields, writes data/items_raw/*.json.
Re-runnable and offline: only depends on the cache.
"""
import json
import os
import re
import sys
import urllib.parse
from glob import glob
from html import unescape as html_unescape

HTMLDIR = "data/raw_html"
RAWDIR = "data/items_raw"

SLOT_CATEGORIES = {
    "Rings": "Ring",
    "Amulets": "Amulet",
    "Cloaks": "Cloak",
    "Gloves": "Gloves",
    "Boots": "Boots",
    "Helmets": "Helmet",
    "Shields": "Shield",
    "Musical_Instruments": "Instrument",
    "Light_Armour": "Light Armour",
    "Medium_Armour": "Medium Armour",
    "Heavy_Armour": "Heavy Armour",
    "Camp_Clothing": "Camp Clothing",
    "Clothing": "Clothing",
    "Underwear": "Underwear",
    "Light_Sources": "Light Source",
}

RARITY_FIX = {
    "common": "Common",
    "uncommon": "Uncommon",
    "rare": "Rare",
    "veryrare": "Very Rare",
    "legendary": "Legendary",
    "story": "Story Item",
}

WEAPON_TYPES = {
    "Greatswords", "Longswords", "Shortswords", "Rapiers", "Scimitars",
    "Daggers", "Sickles", "Clubs", "Maces", "Morningstars", "Mauls",
    "Quarterstaves", "Spears", "Tridents", "Javelins", "Handaxes", "Warhammers",
    "Battleaxes", "Greataxes", "Halberds", "Glaives", "Pikes", "Flails",
    "Warglaives", "Sai", "Longbows", "Shortbows", "Greatbows", "Heavy_Crossbows",
    "Hand_Crossbows", "Light_Crossbows", "Arrows", "Bolts",
}


def strip_tags(html):
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", html)
    text = html_unescape(text)
    text = text.replace("\xa0", " ")
    text = text.replace("\u202f", " ")
    text = text.replace("\u2060", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def section(html, heading_id):
    m = re.search(r'id="' + re.escape(heading_id) + r'".*?</h2>(.*?)(?=<h2|<div id="catlinks|$)',
                  html, re.S)
    return m.group(1) if m else ""


def list_items(seg):
    lis = re.findall(r"<li>(.*?)</li>", seg, re.S)
    return [strip_tags(li) for li in lis if strip_tags(li)]


def parse_rarity(html):
    m = re.search(r"bg3wiki-tooltip-gradient-([a-z]+)(?:\"|\s|>)", html)
    return RARITY_FIX.get(m.group(1)) if m else None


def parse_description(html):
    content = re.search(r'<div class="mw-content-ltr[^"]*"[^>]*>(.*)', html, re.S)
    body = content.group(1) if content else html
    first_p = re.search(r"<p>(.*?)</p>", body, re.S)
    return strip_tags(first_p.group(1)) if first_p else ""


def parse_quote(html):
    m = re.search(r'<div class="bg3wiki-blockquote-text"[^>]*>\s*<p>(.*?)</p>', html, re.S)
    return strip_tags(m.group(1)) if m else ""


def parse_properties(html):
    seg = section(html, "Properties")
    props = []
    seen = set()
    for m in re.finditer(r'aria-label="([^"]*[Aa]rmour [Cc]lass[^"]*)"', seg):
        label, value = m.group(1).split(":", 1)
        entry = [label.strip(), value.strip()]
        key = (entry[0], entry[1])
        if key not in seen:
            props.append(entry)
            seen.add(key)
    for dl in re.finditer(r"<dl>(.*?)</dl>", seg, re.S):
        pairs = re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", dl.group(1), re.S)
        for dt, dd in pairs:
            label = strip_tags(dt)
            value = strip_tags(dd)
            key = (label, value)
            if label and key not in seen:
                props.append([label, value])
                seen.add(key)
    for li in list_items(seg):
        t = li
        if not t:
            continue
        m = re.match(r"^([A-Za-z][A-Za-z ]*?):\s*(.*)$", t, re.S)
        entry = None
        if m and len(m.group(1).split()) <= 3:
            entry = [m.group(1).strip(), m.group(2).strip()]
        else:
            entry = ["Details", t]
        key = (entry[0], entry[1])
        if key not in seen:
            props.append(entry)
            seen.add(key)
    for p in props:
        p[0] = re.sub(r"\s*\(\)$", "", p[0])
    return props


def parse_where(html):
    seg = section(html, "Where_to_find")
    return list_items(seg)


def classify(categories):
    cats = set(categories)
    slot = None
    subtype = None
    for cat, label in SLOT_CATEGORIES.items():
        if cat in cats:
            slot = label
            break
    if "Melee_weapons" in cats or "Ranged_weapons" in cats or "Weapons" in cats:
        slot = "Weapon"
        type_cat = [c for c in cats if c in WEAPON_TYPES]
        if type_cat:
            subtype = type_cat[0]
        elif "Ranged_weapons" in cats:
            subtype = "Ranged weapon"
        else:
            subtype = "Melee weapon"
    elif slot in ("Light Armour", "Medium Armour", "Heavy Armour"):
        subtype = slot.split()[0]
    return slot, subtype


def parse_proficiency(props):
    for label, value in props:
        if label == "Required Proficiency":
            return value.strip()
    return None


def main():
    os.makedirs(RAWDIR, exist_ok=True)
    files = glob(os.path.join(HTMLDIR, "*.html"))
    print(f"{len(files)} cached pages")
    for path in sorted(files):
        name = os.path.basename(path)[:-5]
        cache = json.load(open(path))
        html = cache["html"]
        cats = cache["categories"]
        slot, subtype = classify(cats)
        props = parse_properties(html)
        rec = {
            "name": name,
            "title": cache.get("title", name),
            "url": "https://bg3.wiki/wiki/" + urllib.parse.quote(cache.get("title", name).replace(" ", "_")),
            "rarity": parse_rarity(html),
            "slot": slot,
            "subtype": subtype,
            "proficiency": parse_proficiency(props),
            "description": parse_description(html),
            "quote": parse_quote(html),
            "properties": props,
            "where_to_find": parse_where(html),
            "notes": list_items(section(html, "Notes")),
            "bugs": list_items(section(html, "Bugs")),
            "categories": cats,
        }
        with open(os.path.join(RAWDIR, name + ".json"), "w") as f:
            json.dump(rec, f, indent=2)


if __name__ == "__main__":
    sys.exit(main())