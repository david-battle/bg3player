#!/usr/bin/env python3
"""Build the consumables knowledge base from the parsed records.

Reads data/consumables_raw/*.json for potions, elixirs, scrolls, arrows,
coatings and grenades, assigns acts from vendor/location mentions, and writes:

  data/consumables.json                    - machine-readable master
  knowledge_base/consumables/potions_elixirs.md
  knowledge_base/consumables/scrolls.md
  knowledge_base/consumables/arrows_coatings_grenades.md
  knowledge_base/consumables/camp_supplies.md
"""
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from locations import find_acts  # noqa: E402
from build_knowledge_base import clean_text  # noqa: E402

RAWDIR = "data/consumables_raw"
MASTER = "data/consumables.json"
OUTDIR = "knowledge_base/consumables"

TYPES = ["Potion", "Elixir", "Scroll", "Arrow", "Coating", "Grenade"]

RARITY_ORDER = {"Legendary": 0, "Very Rare": 1, "Rare": 2, "Uncommon": 3,
                "Common": 4}
ACT_ORDER = ["Act One", "Act Two", "Act Three"]

NOISE = re.compile(
    r"^(Elixirs|Potions|Scrolls|Arrows|Coatings|Grenades|Alchemical "
    r"Ingredients|Alchemical Extracts|Single Use|Consumable|Dye|Category|"
    r"Finesse|Thrown|Rarity|Weight|Price|UID|UUID|Stats)$", re.I)

KEEP_LABELS = {"Effect", "Duration", "Damage", "Extra damage", "Range", "AoE",
               "Saving Throw", "Damage Type", "Target", "Radius",
               "Bonus Action", "Action", "Spell", "Recharge"}

# camp-supply vendors per town-like area (curated; supply packs are also sold
# by most general-goods merchants)
CAMP_SUPPLIES = [
    ("Act One", "Emerald Grove (Druid Grove)",
     "Arron (general goods); Okta also sells camp supplies specifically."),
    ("Act One", "Risen Road Toll House",
     "Cyrel (consumables)."),
    ("Act One", "Goblin Camp",
     "Grat the Trader (general goods)."),
    ("Act One", "Underdark - Myconid Colony",
     "Blurg and Derryth Bonecloak (general/alchemy supplies)."),
    ("Act Two", "Last Light Inn",
     "Quartermaster Talli (general; also gives free supplies when first met)."),
    ("Act Two", "Moonrise Towers",
     "Roah Moonglow (general goods)."),
    ("Act Three", "Rivington",
     "Exxvikyap (Rivington General) and Mattis (Requisitioned Barn)."),
    ("Act Three", "Lower City",
     "Most general merchants; the Act 3 city camp also has a supply elevator "
     "behind Withers that sells one supply pack per night."),
]


def compact_props(props):
    out = []
    for label, value in props:
        if label == "Details":
            t = value.strip()
            if not t or NOISE.match(t) or t.startswith(("UID", "UUID", "Stats")):
                continue
            out.append(t)
        elif label in KEEP_LABELS:
            out.append(f"{label}: {value}")
        elif label not in ("Rarity", "Weight", "Price", "UID", "UUID", "Stats",
                           "Category", "Details"):
            out.append(f"{label}: {value}")
    seen = set()
    return " | ".join(clean_text(d) for d in out
                      if not (d in seen or seen.add(d)))


def where_lines(rec):
    lines = []
    seen = set()
    for w in rec.get("where_to_find") or []:
        for line in w.split("\n"):
            t = clean_text(line)
            if t and t not in seen:
                lines.append(t)
                seen.add(t)
    return lines


def load_records():
    recs = {}
    for fn in os.listdir(RAWDIR):
        if not fn.endswith(".json"):
            continue
        r = json.load(open(os.path.join(RAWDIR, fn)))
        recs[r["name"]] = r
    return recs


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    records = load_records()
    items = {n: r for n, r in records.items() if r["type"] in TYPES}

    # act assignment from vendor/location mentions
    for name, rec in items.items():
        text = " ".join(where_lines(rec))
        acts = find_acts(text)
        rec["acts"] = acts
        rec["act_source"] = "location" if acts else "unknown"

    # ---- master JSON ----
    with open(MASTER, "w") as f:
        json.dump(sorted(items.values(), key=lambda r: (r["type"], r["name"])),
                  f, indent=1)
    print(f"wrote {MASTER}: {len(items)} items")

    def block(name, rec):
        act = ", ".join(rec["acts"]) if rec["acts"] else "unknown"
        lines = [f"### {name}",
                 f"- Type: {rec['type']} | Rarity: {rec['rarity']} | Act: {act}"]
        eff = compact_props(rec["properties"])
        if eff:
            lines.append(f"- Effect: {eff}")
        w = where_lines(rec)
        if w:
            lines.append("- How to get:")
            for l in w:
                lines.append(f"  - {l}")
        elif not rec["acts"]:
            lines.append("- How to get: Acquisition not documented on bg3.wiki.")
        lines.append("")
        return "\n".join(lines)

    def group_sections(recs):
        by_act = defaultdict(list)
        for name in sorted(recs, key=lambda n: (RARITY_ORDER.get(recs[n]["rarity"], 9), n)):
            r = recs[name]
            key = r["acts"][0] if r["acts"] else "Unknown act"
            by_act[key].append(name)
        out = []
        for act in ACT_ORDER + (["Unknown act"] if "Unknown act" in by_act else []):
            if act not in by_act:
                continue
            out.append(f"\n## {act}\n")
            for name in by_act[act]:
                out.append(block(name, recs[name]))
        return out

    # ---- potions + elixirs ----
    pot = {n: r for n, r in items.items() if r["type"] in ("Potion", "Elixir")}
    out = ["# Baldur's Gate 3 - Potions and Elixirs\n",
           "All potions and elixirs (including mundane ones), with effects, "
           "duration info, and where to get them. Effects last until a long "
           "rest unless stated otherwise; elixirs replace each other's effects "
           "when drunk.\n",
           "Acts: Act One / Act Two / Act Three. 'Act: unknown' = no specific "
           "vendor/location documented on bg3.wiki (often sold throughout the "
           "game or found as random loot).\n"]
    for t in ("Potion", "Elixir"):
        sub = {n: r for n, r in pot.items() if r["type"] == t}
        out.append(f"\n## {t}s ({len(sub)})\n")
        out.extend(group_sections(sub))
    with open(os.path.join(OUTDIR, "potions_elixirs.md"), "w") as f:
        f.write("\n".join(out))
    print("wrote potions_elixirs.md")

    # ---- scrolls ----
    sc = {n: r for n, r in items.items() if r["type"] == "Scroll"}
    out = ["# Baldur's Gate 3 - Scrolls\n",
           f"All {len(sc)} spell scrolls, with the spell effect and where to "
           "get them. Scrolls can be used by any class; Wizards can learn the "
           "spell from a scroll for a gold cost.\n"]
    out.extend(group_sections(sc))
    with open(os.path.join(OUTDIR, "scrolls.md"), "w") as f:
        f.write("\n".join(out))
    print("wrote scrolls.md")

    # ---- arrows, coatings, grenades ----
    acg = {n: r for n, r in items.items() if r["type"] in ("Arrow", "Coating", "Grenade")}
    out = ["# Baldur's Gate 3 - Special Arrows, Coatings and Grenades\n",
           "Special arrows (any arrow with a special property), weapon "
           "coatings, and throwable grenades/bombs, with effects and where to "
           "get them.\n"]
    for t in ("Arrow", "Coating", "Grenade"):
        sub = {n: r for n, r in acg.items() if r["type"] == t}
        out.append(f"\n## {t}s ({len(sub)})\n")
        out.extend(group_sections(sub))
    with open(os.path.join(OUTDIR, "arrows_coatings_grenades.md"), "w") as f:
        f.write("\n".join(out))
    print("wrote arrows_coatings_grenades.md")

    # ---- camp supplies ----
    out = ["# Baldur's Gate 3 - Camp Supplies\n",
           "Camp supplies feed your party during long rests (40 supply per "
           "rest). Supply packs (40) and individual food/drink are sold by "
           "most general-goods merchants and found as loot throughout the "
           "game. These are the earliest or most convenient vendors per "
           "town-like area.\n"]
    cur = None
    for act, area, note in CAMP_SUPPLIES:
        if act != cur:
            out.append(f"\n## {act}\n")
            cur = act
        out.append(f"- **{area}**: {note}")
    out.append("")
    with open(os.path.join(OUTDIR, "camp_supplies.md"), "w") as f:
        f.write("\n".join(out))
    print("wrote camp_supplies.md")


if __name__ == "__main__":
    sys.exit(main())