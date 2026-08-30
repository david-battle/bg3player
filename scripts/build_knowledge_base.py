#!/usr/bin/env python3
"""Build the AI-friendly markdown knowledge base from the item dataset.

Reads data/items_base.json (per-act list rows), data/items_raw/*.json (parsed
item pages) and data/item_acts.json (act assignment incl. items the wiki's
per-act lists miss), and writes:

  knowledge_base/magic_items_by_slot.md      - browse by gear slot + act
  knowledge_base/magic_items_act_<one|two|three>.md - full detail by location
  knowledge_base/magic_items_merchant_stock.md - generic +1/+2 trader stock
  knowledge_base/magic_items_undocumented.md - items whose acquisition is not
                                               documented (and unobtainable ones)
  data/items.json                            - merged machine-readable master

Designed so an AI can answer queries like "what gloves give Sleight of Hand
advantage in Act 1" without knowing item names in advance.
"""
import json
import os
import re
from collections import defaultdict
from glob import glob
from html import unescape as html_unescape

BASE = "data/items_base.json"
RAWDIR = "data/items_raw"
ACTS = "data/item_acts.json"
OUTDIR = "knowledge_base"
MASTER = "data/items.json"

SLOT_ORDER = [
    "Weapon", "Light Armour", "Medium Armour", "Heavy Armour", "Shield",
    "Helmet", "Gloves", "Boots", "Cloak", "Amulet", "Ring", "Instrument",
    "Clothing", "Camp Clothing", "Light Source",
]
RARITY_ORDER = {"Story Item": 0, "Legendary": 1, "Very Rare": 2, "Rare": 3,
                "Uncommon": 4, "Common": 5}
ACT_ORDER = ["Act One", "Act Two", "Act Three"]
ACT_LABEL = {"Act One": "Act One", "Act Two": "Act Two", "Act Three": "Act Three"}

META_LABELS = {"Rarity", "Weight", "Price", "UID", "UUID", "Stats", "Category"}
NOISE_TEXT = re.compile(
    r"^(Rings|Gloves|Boots|Helmets|Amulets|Cloaks|Shields|Instruments|Musical "
    r"Instruments|Light Sources|Underwear|Camp Clothing|Clothing|Light Armour|"
    r"Medium Armour|Heavy Armour|Greatswords|Longswords|Shortswords|Rapiers|"
    r"Scimitars|Daggers|Sickles|Clubs|Maces|Morningstars|Mauls|Quarterstaves|"
    r"Spears|Tridents|Javelins|Handaxes|Warhammers|Battleaxes|Greataxes|"
    r"Halberds|Glaives|Pikes|Flails|Warglaives|Sai|Longbows|Shortbows|Greatbows|"
    r"Heavy Crossbows|Hand Crossbows|Light Crossbows|Melee weapon|Ranged weapon|"
    r"Weapons)$",
    re.I)


def load_records():
    recs = {}
    for path in glob(os.path.join(RAWDIR, "*.json")):
        name = os.path.basename(path)[:-5]
        recs[name] = json.load(open(path))
    return recs


def clean_text(t):
    t = html_unescape(t)
    t = re.sub(r"\[\s*See:\s*[^\]]*\]", "", t)
    t = re.sub(r"(\d)([A-Z][a-z]+)", r"\1 \2", t)
    t = re.sub(r"([a-z])([A-Z][a-z]+)", r"\1 \2", t)
    t = re.sub(r"\(\s*\+\s*\)", "(+)", t)
    t = re.sub(r"\(\s*Recharge:", "(Recharge:", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def compact_effect(props):
    out = []
    for label, value in props:
        if label in ("Damage", "Extra damage"):
            out.append(f"{label}: {value}")
        elif label == "Armour class":
            out.append(f"AC {value}")
        elif label == "Details":
            t = value.strip()
            if not t or NOISE_TEXT.match(t) or t.startswith("UID"):
                continue
            out.append(t)
        elif label in META_LABELS or label.startswith("Required Proficiency"):
            continue
        else:
            out.append(f"{label}: {value}")
    seen = set()
    return " | ".join(clean_text(d) for d in out if not (d in seen or seen.add(d)))


def short_where(rec, base_row=None):
    if rec.get("where_to_find"):
        return rec["where_to_find"][0]
    if base_row and base_row.get("list_where"):
        return base_row["list_where"]
    return ""


def acquisition_methods(rec, base_row=None):
    methods = []
    seen = set()
    for w in rec.get("where_to_find") or []:
        w = clean_text(w)
        if w and w not in seen:
            methods.append(w)
            seen.add(w)
    if base_row and base_row.get("list_where"):
        lw = clean_text(base_row["list_where"])
        if lw and lw not in seen:
            methods.append(lw)
            seen.add(lw)
    return methods


def item_block(rec, acts=None, note=None, base_row=None):
    out = []
    out.append(f"### {rec['name']}")
    slot = rec["slot"] + (f" ({rec['subtype']})" if rec["subtype"] else "")
    out.append(f"- Rarity: {rec['rarity']} | Slot: {slot}"
               + (f" | Act: {', '.join(acts)}" if acts else " | Act: unknown"))
    if rec["description"]:
        out.append(f"- Description: {clean_text(rec['description'])}")
    effect = compact_effect(rec["properties"])
    if effect:
        out.append(f"- Effect: {effect}")
    methods = acquisition_methods(rec, base_row)
    if methods:
        out.append("- How to get:")
        for m in methods:
            out.append(f"  - {m}")
    elif note:
        out.append(f"- How to get: {clean_text(note)}")
    elif acts is None:
        out.append("- How to get: Acquisition not documented on bg3.wiki.")
    if rec.get("notes"):
        out.append("- Notes:")
        for n in rec["notes"]:
            out.append(f"  - {clean_text(n)}")
    if rec.get("bugs"):
        out.append("- Bugs:")
        for b in rec["bugs"]:
            out.append(f"  - {clean_text(b)}")
    out.append("")
    return "\n".join(out)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    recs = load_records()
    base = json.load(open(BASE))
    acts = json.load(open(ACTS))
    base_rows = defaultdict(list)
    for r in base:
        base_rows[r["name"]].append(r)
    base_names = set(base_rows)

    items = {}
    for name, rec in recs.items():
        info = acts.get(name, {"acts": [], "source": "unknown"})
        if info["source"] == "excluded":
            continue
        items[name] = (rec, info)

    # ---------- merged master JSON ----------
    master = []
    for name in sorted(items):
        rec, info = items[name]
        m = dict(rec)
        m["acts"] = info.get("acts", [])
        m["act_source"] = info.get("source")
        m["act_note"] = info.get("note")
        m["list_rows"] = base_rows.get(name, [])
        master.append(m)
    with open(MASTER, "w") as f:
        json.dump(master, f, indent=2)

    # ---------- by-slot browse file ----------
    by_slot = defaultdict(list)
    for name, (rec, info) in items.items():
        by_slot[rec["slot"]].append((name, rec, info))
    for slot in by_slot:
        by_slot[slot].sort(
            key=lambda x: (ACT_ORDER.index(x[2]["acts"][0]) if x[2]["acts"] else 9,
                           RARITY_ORDER.get(x[1]["rarity"], 9), x[0]))

    lines = []
    lines.append("# Baldur's Gate 3 - Magic Items by Slot\n")
    lines.append(
        "Browsable index for gear-set planning. Each entry shows slot, rarity, "
        "the act(s) it can be obtained in, a compact effect, and how to get it.\n")
    lines.append("Acts: Act One / Act Two / Act Three. "
                 "Rarity: Story, Legendary, Very Rare, Rare, Uncommon, Common. "
                 "'Act: unknown' = acquisition not documented on bg3.wiki.\n")
    for slot in SLOT_ORDER:
        its = by_slot.get(slot)
        if not its:
            continue
        lines.append(f"\n## {slot} ({len(its)} items)\n")
        for name, rec, info in its:
            effect = compact_effect(rec["properties"])
            where = clean_text(short_where(rec, base_rows[name][0] if base_rows.get(name) else None))
            act_str = ", ".join(info["acts"]) if info["acts"] else "unknown"
            lines.append(f"### {name}")
            lines.append(f"- Rarity: {rec['rarity']} | Slot: {rec['slot']}"
                         + (f" ({rec['subtype']})" if rec["subtype"] else "")
                         + f" | Act: {act_str}")
            if effect:
                lines.append(f"- Effect: {effect}")
            if where:
                lines.append(f"- How to get: {where}")
            lines.append("")
    with open(os.path.join(OUTDIR, "magic_items_by_slot.md"), "w") as f:
        f.write("\n".join(lines))

    # ---------- per-act detail files ----------
    for act in ACT_ORDER:
        rows = [r for r in base if r["act"] == act]
        by_location = defaultdict(list)
        for r in rows:
            loc = (r["list_location"] or "").split("\n")[0].strip()
            by_location[loc].append(r)
        out = []
        out.append(f"# Baldur's Gate 3 - Magic Items in {act}\n")
        out.append(
            "Full reference for every magic equipment item obtainable in this "
            "act, sorted by in-game location. Coordinates (X, Y) are in-game "
            "map coordinates.\n")
        for loc in sorted(by_location):
            out.append(f"\n## {loc}\n")
            for r in sorted(by_location[loc], key=lambda x: x["name"]):
                rec = recs.get(r["name"])
                if not rec:
                    continue
                out.append(item_block(rec, acts=[r["act"]], base_row=r))
        # additional items in this act not covered by the wiki's list page
        extra = sorted(
            (name for name, (rec, info) in items.items()
             if name not in base_names and info["source"] != "stock"
             and act in info["acts"]),
            key=lambda n: (RARITY_ORDER.get(recs[n]["rarity"], 9), n))
        if extra:
            out.append(f"\n## Additional items in {act} (not on the wiki's list page)\n")
            out.append(
                "These items are obtainable in this act but are missing from "
                "bg3.wiki's per-act list; acts were assigned from item-page "
                "location info.\n")
            for name in extra:
                out.append(item_block(recs[name], acts=[act], note=acts[name].get("note")))
        with open(os.path.join(OUTDIR, f"magic_items_{act.lower().replace(' ', '_')}.md"), "w") as f:
            f.write("\n".join(out))
        print(f"wrote magic_items_{act.lower().replace(' ', '_')}.md")

    # ---------- merchant stock appendix ----------
    stock_items = sorted(
        (name for name, (rec, info) in items.items() if info["source"] == "stock"),
        key=lambda n: n)
    if stock_items:
        lines = ["# Baldur's Gate 3 - Generic Magic Merchant Stock\n",
                 "Enchanted +1/+2 weapons, armour and shields sold generically by "
                 "traders (level-gated in some cases), rather than at a fixed "
                 "location. Available across acts.\n"]
        for name in stock_items:
            lines.append(item_block(recs[name], acts=["Act One", "Act Two", "Act Three"],
                                    note=acts[name].get("note")))
        with open(os.path.join(OUTDIR, "magic_items_merchant_stock.md"), "w") as f:
            f.write("\n".join(lines))
        print("wrote magic_items_merchant_stock.md")

    # ---------- undocumented + unobtainable appendix ----------
    undoc = sorted(name for name, (rec, info) in items.items()
                   if not info["acts"] and info["source"] == "unknown")
    unob = json.load(open(ACTS))
    unob = sorted(n for n, v in unob.items() if v["source"] == "excluded")
    lines = ["# Baldur's Gate 3 - Items Without Documented Acquisition\n",
             "Two categories:\n",
             "1. **Acquisition not documented** - these magic items exist but "
             "bg3.wiki does not record where/how they are obtained. Do not "
             "assume a location for them.\n",
             "2. **Not obtainable in the current game** - Early Access-only "
             "items, inaccessible variants, or conjured items. Do not recommend "
             "these to a player.\n"]
    if undoc:
        lines.append("\n## Acquisition not documented\n")
        for name in undoc:
            lines.append(item_block(recs[name], acts=None))
    if unob:
        lines.append("\n## Not obtainable in the current game\n")
        for name in unob:
            rec = recs.get(name)
            if rec:
                note = json.load(open(ACTS))[name].get("note", "")
                lines.append(item_block(rec, acts=[], note=note))
    with open(os.path.join(OUTDIR, "magic_items_undocumented.md"), "w") as f:
        f.write("\n".join(lines))
    print("wrote magic_items_undocumented.md")
    print("wrote magic_items_by_slot.md")
    print(f"wrote {MASTER}")


if __name__ == "__main__":
    main()