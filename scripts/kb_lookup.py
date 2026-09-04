#!/usr/bin/env python3
"""Precise lookup over the BG3 knowledge base masters (data/*.json).

Gives the adviser fast, grounded answers instead of eyeballing markdown.
Everything reads the tracked JSON masters, so results stay in sync with the
knowledge base. Usage examples:

    kb item --slot gloves --act 2 --effect "spell save"
    kb item --where "Sacred Pool"          # everything obtainable in an area
    kb item --name "hag's hair"            # any fuzzy name search
    kb consumable --type elixir --effect "hill giant"
    kb recipe --result "hill giant"
    kb recipe --ingredient "mugwort"
    kb ingredient --name "corpse rose"
    kb condition --name "radiating orb"
    kb feat --name "great weapon"
    kb companion --name astarion
    kb class --name wizard            # class + its subclasses
    kb subclass --name berserker      # what distinguishes a subclass
    kb race --name elf                # race/subrace traits (or list all)
    kb background --name noble        # skills + who starts with it
    kb power --tier elite             # illithid powers by tier
    kb achievement --name foehammer   # achievement unlock conditions
    kb difficulty --mode honour       # difficulty / honour-mode details
    kb buff --act two
    kb missables --act 2
"""
import argparse
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def load(name):
    with open(os.path.join(DATA, name)) as f:
        return json.load(f)


def has(tokens, *fields):
    return lambda rec: all(
        any(re.search(t, str(rec.get(f, "")), re.I) for f in fields if rec.get(f))
        for t in tokens
    )


def text_of(rec, fields):
    parts = []
    for f in fields:
        v = rec.get(f)
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    parts.append(str(item.get("list_effect", "")))
                    parts.append(str(item.get("list_where", "")))
                elif isinstance(item, str):
                    parts.append(item)
    return " ".join(p for p in parts if p)


def loc_tokens(rec):
    return text_of(rec, ["where_to_find"]).lower()


def matches_location(rec, tokens):
    hay = loc_tokens(rec)
    return all(t in hay for t in tokens)


def print_items(items, limit):
    if not items:
        print("(no matches)")
        return
    total = len(items)
    shown = items[:limit] if limit else items
    for it in shown:
        acts = ", ".join(it.get("acts") or ["Act: unknown"])
        eff = (it.get("list_rows") or [{}])
        eff = eff[0].get("list_effect", "") if eff and isinstance(eff[0], dict) else ""
        eff = re.sub(r"\s+", " ", eff).strip()
        slot = it.get("slot") or it.get("type") or ""
        prof = it.get("proficiency")
        print(f"### {it['name']} ({it['rarity']}, {slot}) - {acts}"
              + (f" [requires {prof}]" if prof else ""))
        if eff:
            print(f"  {eff}")
        wtf = it.get("where_to_find") or []
        for w in wtf[:2]:
            print(f"  Get: {re.sub(chr(10), ' ', w)}")
    if limit and total > limit:
        print(f"  ... and {total - limit} more (narrow the filters or raise --limit)")


def cmd_item(args):
    items = load("items.json")
    if args.name:
        items = [i for i in items if args.name.lower() in i["name"].lower()]
    if args.slot:
        items = [i for i in items if i.get("slot") and args.slot.lower() in i["slot"].lower()]
    if args.rarity:
        items = [i for i in items if args.rarity.lower() in (i.get("rarity") or "").lower()]
    if args.act:
        act = {"1": "Act One", "2": "Act Two", "3": "Act Three"}.get(args.act, args.act)
        items = [i for i in items if act in (i.get("acts") or [])]
    if args.effect:
        tokens = args.effect.lower().split()
        items = [i for i in items
                 if all(t in text_of(i, ["description", "list_rows", "slot"]).lower()
                        for t in tokens)]
    if args.proficiency:
        tokens = args.proficiency.lower().split()
        items = [i for i in items
                 if i.get("proficiency")
                 and all(t in i["proficiency"].lower() for t in tokens)]
    if args.where:
        tokens = args.where.lower().split()
        items = [i for i in items if matches_location(i, tokens)]
    print_items(sorted(items, key=lambda i: i["name"]), args.limit)


def cmd_consumable(args):
    cons = load("consumables.json")
    if args.name:
        cons = [c for c in cons if args.name.lower() in c["name"].lower()]
    if args.type:
        cons = [c for c in cons if args.type.lower() in (c.get("type") or "").lower()]
    if args.act:
        act = {"1": "Act One", "2": "Act Two", "3": "Act Three"}.get(args.act, args.act)
        cons = [c for c in cons if act in (c.get("acts") or [])]
    if args.effect:
        tokens = args.effect.lower().split()
        cons = [c for c in cons
                if all(t in text_of(c, ["description", "properties", "where_to_find", "type"]).lower()
                       for t in tokens)]
    if args.where:
        tokens = args.where.lower().split()
        cons = [c for c in cons if matches_location(c, tokens)]
    print_items(cons, args.limit)


def cmd_recipe(args):
    recs = load("alchemy_recipes.json")
    if args.result:
        recs = [r for r in recs if args.result.lower() in r["result"].lower()]
    if args.ingredient:
        recs = [r for r in recs if args.ingredient.lower() in r["source"].lower()]
    if args.type:
        recs = [r for r in recs if args.type.lower() in (r.get("type") or "").lower()]
    if not recs:
        print("(no matching recipe)")
    for r in recs[:args.limit]:
        print(f"{r['result']} ({r['type']}): {r['specific']} (from {r['source']}) "
              f"+ any {r['generic']}. Craft lvl {r['craft_level']} / trade lvl {r['trade_level']}")


def cmd_ingredient(args):
    ing = load("ingredients.json")
    if args.name:
        ing = [i for i in ing if args.name.lower() in i["name"].lower()]
    if not ing:
        print("(no matching ingredient)")
    for i in ing[:args.limit]:
        v = i.get("first_vendor")
        where = f"{v['vendor']} ({v['location']}, {v['act']})" if v else "not documented"
        print(f"{i['name']} -> {i['extract']} ({i['family']}). First vendor: {where}")


def cmd_condition(args):
    conds = load("conditions.json")
    if args.name:
        conds = [c for c in conds if args.name.lower() in c["name"].lower()]
    if not conds:
        print("(no matching condition)")
    for c in conds[:args.limit]:
        print(f"### {c['name']}")
        for e in c.get("effects", [])[:4]:
            print(f"  {e}")
        if c.get("sources"):
            print(f"  Sources: {', '.join(c['sources'][:10])}")
        for n in c.get("notes", [])[:2]:
            print(f"  Note: {n}")


def cmd_feat(args):
    feats = load("feats.json")
    if args.name:
        feats = [f for f in feats if args.name.lower() in f["name"].lower()]
    if not feats:
        print("(no matching feat)")
    for f in feats[:args.limit]:
        print(f"### {f['name']}")
        if f.get("description"):
            print(f"  {f['description']}")
        for p in f.get("powers", []):
            print(f"  - {p['name']}: {p['description']}")


def cmd_companion(args):
    data = load("companions.json")
    comps = data["companions"]
    if args.name:
        comps = [c for c in comps if args.name.lower() in c["name"].lower()]
    if args.act:
        act = {"1": "One", "2": "Two", "3": "Three"}.get(args.act, args.act)
        comps = [c for c in comps if (c.get("recruitment_act") or "") == act]
    if not comps:
        print("(no matching companion)")
    for c in comps[:args.limit]:
        print(f"### {c['name']} ({c['role']})")
        s = c.get("stats") or {}
        stats = " ".join(f"{k} {v['score']}" for k, v in s.items()) or "not documented"
        print(f"  {c['race']} {c['class']} | stats {stats} | recruit {c['recruitment_act'] or 'n/a'}")
        if c.get("quest"):
            print(f"  Quest: {c['quest'][:160]}")
        if c.get("recruitment"):
            print(f"  Recruit: {c['recruitment'][:220]}")


def cmd_buff(args):
    acts = load("permanent_buffs.json")
    if args.act:
        act = {"1": "Act One", "2": "Act Two", "3": "Act Three"}.get(args.act, args.act)
        acts = [a for a in acts if a["act"] == act]
    for a in acts:
        print(f"## {a['act']}")
        for b in a.get("bonuses", []):
            print(f"### {b['name']}")
            print(f"  {b['description']}")
            for label, text in b.get("sections", {}).items():
                print(f"  {label}: {text[:220]}")


def cmd_missables(args):
    act = {"1": "One", "2": "Two", "3": "Three"}.get(args.act, args.act)
    full = {"1": "Act One", "2": "Act Two", "3": "Act Three"}[args.act]
    print(f"## Permanent buffs in {full} (check the state file for which are still open)")
    for a in load("permanent_buffs.json"):
        if a["act"] == full:
            for b in a.get("bonuses", []):
                print(f"- {b['name']}")
    print(f"\n## Companions recruitable in Act {act}")
    for c in load("companions.json")["companions"]:
        if (c.get("recruitment_act") or "") == act:
            print(f"- {c['name']} ({c['role']})")
    print(f"\n## Notable {full} items (Legendary / Very Rare)")
    for it in load("items.json"):
        if full in (it.get("acts") or []) and it.get("rarity") in ("Legendary", "Very Rare"):
            label = it["name"] if it["rarity"] in it["name"] else f"{it['name']} ({it['rarity']})"
            print(f"- {label}")


def cmd_class(args):
    data = load("classes.json")
    classes = data["classes"]
    if args.name:
        classes = [c for c in classes if args.name.lower() in c["name"].lower()]
    if not classes:
        print("(no matching class)")
    for c in classes[:args.limit]:
        print(f"### {c['name']}")
        if c["description"]:
            print(f"  {c['description']}")
        a = c["attributes"]
        if a.get("Hit points"):
            print(f"  Hit points: {a['Hit points']}")
        if a.get("Key abilities"):
            print(f"  Key abilities: {a['Key abilities']}")
        if a.get("Spellcasting Ability"):
            print(f"  Spellcasting ability: {a['Spellcasting Ability']}")
        for label, val in c["proficiencies"].items():
            print(f"  {label}: {val}")
        subs = [s for s in data["subclasses"] if s["class"] == c["name"]]
        if subs:
            print("  Subclasses:")
            for s in subs:
                print(f"    - {s['name']}: {s['description']}")


def cmd_subclass(args):
    subs = [s for s in load("classes.json")["subclasses"]
            if args.name.lower() in s["name"].lower()]
    if not subs:
        print("(no matching subclass)")
    for s in subs[:args.limit]:
        print(f"### {s['name']} ({s['class']})")
        print(f"  {s['description']}")


def cmd_race(args):
    races = load("races.json")["races"]
    if args.name:
        races = [r for r in races
                 if args.name.lower() in (r["race"] + " " + r["subrace"]).lower()]
    if not races:
        print("(no matching race)")
    for r in races[:args.limit]:
        name = r["race"] if not r["subrace"] else f"{r['race']} ({r['subrace']})"
        print(f"### {name}")
        print(f"  Speed: {r['speed']}")
        if r["proficiencies"]:
            print(f"  Proficiencies: {r['proficiencies']}")
        if r["features"]:
            print(f"  Features: {r['features']}")


def cmd_background(args):
    bgs = [b for b in load("backgrounds.json")["backgrounds"]
           if args.name.lower() in b["name"].lower()]
    if not bgs:
        print("(no matching background)")
    for b in bgs[:args.limit]:
        print(f"### {b['name']}")
        if b["description"]:
            print(f"  {b['description']}")
        for label, val in b["skills"].items():
            print(f"  - {label}: {val}")


def cmd_power(args):
    tiers = load("illithid_powers.json")["tiers"]
    if args.tier:
        tiers = [t for t in tiers if args.tier.lower() in t["name"].lower()]
    if args.name:
        tiers = [dict(t, powers=[p for p in t["powers"]
                                 if args.name.lower() in p["name"].lower()])
                 for t in tiers]
    for t in tiers:
        if not t["powers"]:
            continue
        print(f"## {t['name']} ({len(t['powers'])})")
        for p in t["powers"][:args.limit]:
            print(f"### {p['name']} [{p['type']}]")
            if p["requires"] and p["requires"] not in ("None", "-"):
                print(f"  Requires: {p['requires']}")
            print(f"  {p['description']}")


def cmd_achievement(args):
    ach = load("achievements.json")
    if args.name:
        ach = [a for a in ach if args.name.lower() in a["name"].lower()]
    if not ach:
        print("(no matching achievement)")
    for a in ach[:args.limit]:
        print(f"### {a['name']}")
        print(f"  {a['description']}")
        if a["hidden"]:
            print("  (hidden until unlocked)")


def cmd_difficulty(args):
    d = load("honour_mode.json")
    if args.mode:
        modes = [m for m in d["modes"] if args.mode.lower() in m["name"].lower()]
        for m in modes[:args.limit]:
            print(f"## {m['name']} mode")
            print(f"  {m['description']}")
        return
    for m in d["modes"]:
        print(f"## {m['name']}: {m['description'][:90]}")
    print("\n## Custom settings defaults")
    cols = ["Explorer", "Balanced", "Tactician", "Honour"]
    for s in d["custom_settings"]:
        v = s["values"]
        row = ", ".join(f"{c}={v.get(c, '')}" for c in cols)
        print(f"  {s['setting']}: {row}")


def main():
    p = argparse.ArgumentParser(prog="kb", description="BG3 knowledge base lookup")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(cmd, help_text):
        sp = sub.add_parser(cmd, help=help_text)
        sp.add_argument("--limit", type=int, default=0, help="max results (0 = all)")
        return sp

    sp = add("item", "search equipment by slot/act/effect")
    sp.add_argument("--slot"); sp.add_argument("--act"); sp.add_argument("--rarity")
    sp.add_argument("--name"); sp.add_argument("--effect"); sp.add_argument("--where")
    sp.add_argument("--proficiency", help="armour proficiency required, e.g. 'light'")

    sp = add("consumable", "search consumables by type/act/effect")
    sp.add_argument("--type"); sp.add_argument("--act"); sp.add_argument("--name")
    sp.add_argument("--effect"); sp.add_argument("--where")

    sp = add("recipe", "find an alchemy recipe")
    sp.add_argument("--result"); sp.add_argument("--ingredient"); sp.add_argument("--type")

    sp = add("ingredient", "ingredient -> extract + first vendor")
    sp.add_argument("--name", required=True)

    sp = add("condition", "condition effects + sources")
    sp.add_argument("--name", required=True)

    sp = add("feat", "feat details")
    sp.add_argument("--name", required=True)

    sp = add("companion", "companion details or recruitable per act")
    sp.add_argument("--name"); sp.add_argument("--act")

    sp = add("class", "class details + subclasses")
    sp.add_argument("--name")

    sp = add("subclass", "subclass distinguishing description")
    sp.add_argument("--name", required=True)

    sp = add("race", "race/subrace traits (list all without --name)")
    sp.add_argument("--name")

    sp = add("background", "background skills + who starts with it")
    sp.add_argument("--name", required=True)

    sp = add("power", "illithid powers by tier or name")
    sp.add_argument("--name"); sp.add_argument("--tier")

    sp = add("achievement", "achievement unlock conditions")
    sp.add_argument("--name")

    sp = add("difficulty", "difficulty / honour-mode details or settings")
    sp.add_argument("--mode")

    sp = add("buff", "permanent buffs (optionally per act)")
    sp.add_argument("--act")

    sp = add("missables", "time-sensitive things for an act (buffs, companions, rare items)")
    sp.add_argument("--act", required=True)

    args = p.parse_args()
    globals()["cmd_" + args.cmd](args)


if __name__ == "__main__":
    main()