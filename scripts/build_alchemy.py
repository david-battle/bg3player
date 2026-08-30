#!/usr/bin/env python3
"""Build the alchemy reference from the wiki's Alchemy page and ingredient pages.

Parses data/raw_html/Alchemy.html (recipe + extraction tables) and the parsed
ingredient records in data/consumables_raw/, then writes:

  data/alchemy_recipes.json          - result, specific extract, source
                                       ingredient, generic family, craft/trade
                                       level for every recipe
  data/ingredients.json              - ingredient -> extract + first vendor
  knowledge_base/consumables/alchemy.md - AI-friendly alchemy reference
"""
import json
import os
import re
import sys
from html import unescape as hu

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from locations import find_acts, ACT_ORDER  # noqa: E402

ALCH_HTML = "data/raw_html_cons/Alchemy.html"
RAWDIR = "data/consumables_raw"
OUTREC = "data/alchemy_recipes.json"
OUTING = "data/ingredients.json"
OUTFILE = "knowledge_base/consumables/alchemy.md"

# ingredient -> extract corrections where the wiki's recipe tables use a
# different name than the ingredient page title
EXTRACT_FIX = {
    "Ochre Jelly Slime": "Suspension of Ochre Jelly",
    "Frosted Ear": "Sublimate of Frosted Ears",
    "Xorn Scales": "Salts of Xorn Scales",
}

NO_KNOWN_USE = {"Owlbear Beak", "Harpy Feather"}


def cells(row):
    return [re.sub(r"\s+", " ", hu(re.sub(r"<[^>]+>", " ", c))).strip()
            for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]


def strip_footnotes(v):
    return re.sub(r"\[\s*\d+\s*\]", "", v).strip()


def parse_alchemy_page(html):
    """Return (recipes, extractions)."""
    recipes = []
    extractions = {}
    heads = [(m.start(), hu(re.sub(r"<[^>]+>", "", m.group(1))).strip())
             for m in re.finditer(
                 r'<h[23]><span[^>]*id="([^"]+)"[^>]*>.*?</span>(.*?)</h[23]>', html, re.S)]
    for k in range(len(heads)):
        name, label = heads[k]
        end = heads[k + 1][0] if k + 1 < len(heads) else len(html)
        seg = html[name:end]
        for t in re.findall(r'<table[^>]*class="wikitable[^"]*"[^>]*>(.*?)</table>',
                            seg, re.S):
            rows = re.findall(r"<tr>(.*?)</tr>", t, re.S)
            if not rows:
                continue
            hdr = [strip_footnotes(c) for c in cells(rows[0])]
            for r in rows[1:]:
                vals = cells(r)
                row = dict(zip(hdr, vals))
                if label in ("Potions", "Elixirs", "Grenades", "Coatings"):
                    if row.get("Result"):
                        recipes.append({
                            "result": strip_footnotes(row["Result"]),
                            "type": label[:-1].capitalize(),
                            "specific": strip_footnotes(row.get("Specific", "")),
                            "source": strip_footnotes(row.get("Source ingredient", "")),
                            "generic": strip_footnotes(row.get("Generic", "")),
                            "craft_level": strip_footnotes(row.get("Craft Level", "")),
                            "trade_level": strip_footnotes(row.get("Trade Level", "")),
                            "price_ratio": strip_footnotes(row.get("Price Ratio", "")),
                        })
                elif label == "Extractions":
                    for family, src in row.items():
                        if src and family != "Extractions":
                            extractions.setdefault(src, family)
    return recipes, extractions


def parse_vendors(rec):
    """Extract (vendor, location) pairs from where_to_find, with act."""
    out = []
    for w in rec.get("where_to_find") or []:
        for line in w.split("\n"):
            line = re.sub(r"\s+", " ", line).strip()
            if not line:
                continue
            acts = find_acts(line)
            if not acts:
                continue
            loc = next((l for l in sorted(
                _loc_names(), key=len, reverse=True)
                if re.search(r"(?i)(^|\W)" + re.escape(l) + r"(\W|$)", " " + line + " ")), None)
            if loc is None:
                continue
            vendor = _vendor_before(line, loc)
            if vendor:
                out.append({"vendor": vendor, "location": loc, "act": acts[0]})
    # dedupe keeping first per (vendor, location)
    seen, uniq = set(), []
    for v in out:
        key = (v["vendor"], v["location"])
        if key not in seen:
            seen.add(key)
            uniq.append(v)
    return uniq


def _loc_names():
    from locations import LOC_NAMES
    return LOC_NAMES


LOC_DESC = re.compile(
    r"(?i)^(the|a|an|in|at|near|on|under|inside|from|behind|within|among|"
    r"around|carried by|held by|found|located|common|commonly|random|"
    r"looted|dropped|obtainable|sold by|various|many|most|several|one can be|"
    r"one is|can be found|can be located|throughout|harvested|harvested from|"
    r"most commonly)\b")


def _vendor_before(line, loc):
    head = line.split(loc, 1)[0]
    head = re.sub(r"(?i)^(sold by\s*:?|obtainable from |purchased from )+", "", head)
    head = re.sub(r"^\s*\d+x\s*[-–]?\s*", "", head)
    head = re.sub(r"^(\([^)]*\)\s*)+", "", head)
    head = re.sub(r"(?i)\s+(at|in)\s+(?:the\s+)?$", "", head)
    head = re.sub(r"(?i)\s+(?:at|in|near|on|under|inside|outside)\s+[A-Z][\w' ]*$", "", head)
    head = head.strip(" ,.:;")
    for kw in ("such as", "including"):
        if kw.lower() in head.lower():
            head = head.split(kw, 1)[-1].strip(" ,.:;")
            break
    if not head or LOC_DESC.match(head):
        return None
    if re.search(r"(?i)\b(merchants|traders|stash|random loot)\b", head):
        return None
    if len(head) > 40:
        return None
    return head


def first_vendor(rec):
    vendors = parse_vendors(rec)
    if not vendors:
        return None
    vendors.sort(key=lambda v: ACT_ORDER.index(v["act"]))
    return vendors[0]


def main():
    html = json.load(open(ALCH_HTML))["html"]
    recipes, extractions = parse_alchemy_page(html)
    print(f"{len(recipes)} recipes, {len(extractions)} extraction families")

    # ingredient records
    records = {}
    for fn in os.listdir(RAWDIR):
        if not fn.endswith(".json"):
            continue
        r = json.load(open(os.path.join(RAWDIR, fn)))
        records[r["name"]] = r

    # ingredient -> extract from recipe tables (source -> specific)
    src_extract = {}
    for rcp in recipes:
        if rcp["source"] and rcp["specific"]:
            src_extract.setdefault(rcp["source"], rcp["specific"])
    for ing, ext in EXTRACT_FIX.items():
        src_extract.setdefault(ing, ext)

    ingredients = []
    for name, rec in sorted(records.items()):
        if rec["type"] != "Ingredient":
            continue
        extract = rec.get("extract_of") or src_extract.get(name)
        family = extractions.get(name) or (extract.split(" of ", 1)[0]
                                           if extract and " of " in extract else None)
        fv = first_vendor(rec)
        ingredients.append({
            "name": name,
            "extract": extract,
            "family": family,
            "no_known_use": name in NO_KNOWN_USE or (not extract and not family),
            "first_vendor": fv,
            "sold_by": parse_vendors(rec),
        })

    with open(OUTREC, "w") as f:
        json.dump(recipes, f, indent=1)
    with open(OUTING, "w") as f:
        json.dump(ingredients, f, indent=1)
    print(f"wrote {OUTREC}, {OUTING}")

    # ---- render alchemy.md ----
    lines = []
    lines.append("# Baldur's Gate 3 - Alchemy\n")
    lines.append(
        "Crafting reference: combine **3 ingredients** to make an **extract**, "
        "then combine one **specific extract** with any extract of a second "
        "**generic family** to craft a potion, elixir, grenade or coating. "
        "Craft/Trade Levels gate which characters and traders can craft/sell "
        "the result.\n")
    lines.append("Rarity: Common for ingredients/extracts; "
                 "consumable results are mostly Common/Uncommon.\n")

    lines.append("\n## Ingredients and where to get them\n")
    lines.append(
        "First vendor = earliest-act trader that sells the ingredient, so the "
        "AI can point a player at the first place to stock up. Most ingredients "
        "are also random world loot; world locations are not tracked here.\n")
    for ing in ingredients:
        lines.append(f"### {ing['name']}")
        extract = ing["extract"] or "no known use"
        lines.append(f"- Extract: {extract}"
                     + (f" (from the {ing['family']} family)" if ing["family"] else ""))
        fv = ing["first_vendor"]
        if fv:
            lines.append(f"- First vendor: {fv['vendor']} ({fv['location']}, {fv['act']})")
        else:
            lines.append("- First vendor: not documented on bg3.wiki")
        lines.append("")

    lines.append("## Extracts\n")
    lines.append(
        "Extracts are the building blocks of every recipe. Each comes from a "
        "specific ingredient (above); combine one specific extract with any "
        "extract of the matching generic family to craft the result.\n")
    by_fam = {}
    for rcp in recipes:
        by_fam.setdefault(rcp["type"], []).append(rcp)
    for fam in ("Potion", "Elixir", "Grenade", "Coating"):
        lines.append(f"\n### {fam} recipes ({len(by_fam.get(fam, []))})\n")
        lines.append("| Result | Specific extract | Source ingredient | Generic | "
                     "Craft Lv | Trade Lv | Price ratio |")
        lines.append("|---|---|---|---|---|---|---|")
        for rcp in by_fam.get(fam, []):
            lines.append(f"| {rcp['result']} | {rcp['specific']} | "
                         f"{rcp['source'] or '—'} | {rcp['generic'] or '—'} | "
                         f"{rcp['craft_level'] or '—'} | {rcp['trade_level'] or '—'} | "
                         f"{rcp['price_ratio'] or '—'} |")
        lines.append("")

    os.makedirs(os.path.dirname(OUTFILE), exist_ok=True)
    with open(OUTFILE, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUTFILE}")


if __name__ == "__main__":
    sys.exit(main())