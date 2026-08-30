#!/usr/bin/env python3
"""Build the races reference from the cached Races master page.

Reads data/raw_html_ref/Races.html (the wiki's playable-race comparison table),
writes data/races.json and knowledge_base/reference/races.md. Offline.
"""
import json
import os
import re

import reference_data as rd

MASTER = os.path.join(rd.HTMLDIR, "Races.html")
OUT_JSON = "data/races.json"
OUT_MD = "knowledge_base/reference/races.md"

# Curated from the wiki's race pages (verified: only Halfling and Gnome are
# Small; every other playable race is Medium).
SIZE_NOTE = ("Halflings and Gnomes are Small; all other playable races are "
             "Medium.")


def cell_text(html):
    return re.sub(r"\[\d+\]", "", rd.clean_cell(html))


def race_link(cell):
    m = re.search(r'<a[^>]*href="/wiki/([^"#]+)"', cell)
    return m.group(1) if m else ""


def is_race_cell(cell):
    name = race_link(cell)
    return bool(name) and "#" not in name and name in rd.RACE_PAGES


def subrace_of(cell):
    m = re.search(r'<img[^>]*alt="([^"]+)"', cell)
    if m and m.group(1).strip() not in ("Elf", "Half-Elf", "Dwarf", "Gnome"):
        return m.group(1).strip()
    m = re.search(r'<a[^>]*href="/wiki/[^"#]+#([^"]+)"', cell)
    return normalize_subrace(m.group(1).replace("_", " ")) if m else ""


def normalize_subrace(name):
    for plural, singular in (("Elves", "Elf"), ("Dwarves", "Dwarf"),
                             ("Halflings", "Halfling"), ("Gnomes", "Gnome"),
                             ("Tieflings", "Tiefling")):
        if name.endswith(plural):
            return name[: -len(plural)] + singular
    return name.title()


def playable_table(html):
    m = re.search(r'id="Playable_races"', html)
    if not m:
        return ""
    prev = list(re.finditer(r"<h([23])", html[:m.start()]))
    level = int(prev[-1].group(1)) if prev else 2
    close = re.search(r"</h%d>" % level, html[m.start():])
    if not close:
        return ""
    start = m.start() + close.end()
    nxt = None
    for hm in re.finditer(r"<h([23])", html[start:]):
        if int(hm.group(1)) <= level:
            nxt = hm.start()
            break
    end = start + nxt if nxt is not None else len(html)
    return html[start:end]


def parse_rows(html):
    t = re.search(r"<table.*?</table>", html, re.S)
    if not t:
        return []
    rows = []
    for row in re.findall(r"<tr.*?</tr>", t.group(0), re.S):
        raw = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
        if not raw:
            continue
        head = " ".join(cell_text(c) for c in raw)
        if any(k in head for k in ("Race and Subraces", "From Race",
                                   "From Subrace")):
            continue
        rows.append(raw)
    return rows


def classify(cells, start):
    speed, profs, feats = "", [], []
    for c in cells[start:]:
        t = c.strip()
        if not t or t == "-":
            continue
        if re.match(r"^(Standard|Fast|Slow|Base)", t):
            speed = re.sub(r"(Standard|Fast|Slow)(\d)", r"\1 \2", t)
        elif re.match(r"^(Weapons|Armour|Skills|Tool)", t):
            profs.append(t)
        else:
            feats.append(t)
    return speed, profs, feats


def combine(race, sub):
    parts = [x for x in (race, sub) if x and x.strip() not in ("", "-")]
    return " | ".join(parts)


def parse_table(html):
    records = []
    current_race = None
    race_speed = ""
    race_profs, race_feats = "", ""
    for raw in parse_rows(html):
        cells = [cell_text(c) for c in raw]
        if is_race_cell(raw[0]):
            current_race = race_link(raw[0])
            sub = subrace_of(raw[1]) if len(raw) > 1 else ""
            start = 2 if sub else 1
            speed, profs, feats = classify(cells, start)
            race_speed = speed
            race_profs = profs[0] if profs else ""
            race_feats = feats[0] if feats else ""
            records.append({
                "race": current_race,
                "subrace": sub or "",
                "speed": speed,
                "proficiencies": combine(race_profs,
                                         profs[1] if len(profs) > 1 else ""),
                "features": combine(race_feats,
                                    feats[1] if len(feats) > 1 else ""),
            })
            if current_race == "Dragonborn":
                # each dragonborn colour restates the full Draconic Ancestry,
                # so there is no separate race-level feature to inherit
                race_profs = race_feats = ""
        else:
            sub = subrace_of(raw[0])
            speed, profs, feats = classify(cells, 1)
            if profs or feats or speed:
                rec = {
                    "race": current_race,
                    "subrace": sub or "",
                    "speed": speed or race_speed,
                    "proficiencies": combine(race_profs,
                                             profs[0] if profs else ""),
                    "features": combine(race_feats,
                                        feats[0] if feats else ""),
                }
            else:
                # no content of its own: identical to the sibling subrace
                rec = dict(records[-1])
                rec["subrace"] = sub or ""
            records.append(rec)
    return records


def render(records, intro):
    lines = []
    lines.append("# Baldur's Gate 3 - Races")
    lines.append("")
    lines.append(intro)
    lines.append("")
    lines.append(
        "Unlike D&D 5e's fixed racial bonuses, BG3 gives every race a free "
        "ability score allocation: **+2 to any ability score and +1 to any "
        "other**. The per-race differences below are base speed, proficiencies "
        "and features (race-level applies to all its subraces).")
    lines.append("")
    lines.append(f"{SIZE_NOTE}")
    lines.append("")
    for r in records:
        name = r["race"] if not r["subrace"] else f"{r['race']} ({r['subrace']})"
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"- Speed: {r['speed']}")
        if r["proficiencies"]:
            lines.append(f"- Proficiencies: {r['proficiencies']}")
        if r["features"]:
            lines.append(f"- Features: {r['features']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    html = open(MASTER).read()
    seg = playable_table(html)
    records = parse_table(seg)
    intro = rd.strip_edit_markers(re.sub(r"<[^>]+>", " ", seg[:seg.find("<table")]))
    intro = rd.clean_text(intro)
    gallery = "Human Elf Drow Half-Elf Half-Orc Halfling Dwarf Gnome Tiefling " \
              "Githyanki Dragonborn"
    intro = intro.replace(gallery, "").replace("  ", " ")
    json.dump({"intro": intro, "size": SIZE_NOTE, "races": records},
              open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(records, intro))
    print(f"wrote {len(records)} race entries -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()