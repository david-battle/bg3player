#!/usr/bin/env python3
"""Build the companions reference from cached reference HTML.

Reads data/raw_html_ref/Companions.html (master) plus the per-companion pages,
writes data/companions.json and knowledge_base/reference/companions.md.
Offline; only depends on the cache.
"""
import json
import os
import re

import reference_data as rd

MASTER = os.path.join(rd.HTMLDIR, "Companions.html")
OUT_JSON = "data/companions.json"
OUT_MD = "knowledge_base/reference/companions.md"

ORIGINS = ["Astarion", "Gale", "Karlach", "Lae'zel", "Shadowheart", "Wyll",
           "The Dark Urge"]

# Manual act assignments where the wiki page does not state the act but it is
# unambiguous from the described location/context.
ACT_OVERRIDES = {"Karlach": "One"}


def infobox(html):
    m = re.search(r'<aside class="portable-infobox.*?</aside>', html, re.S)
    if not m:
        return {}
    box = m.group(0)
    out = {}
    for dm in re.finditer(r'data-source="([^"]+)"[^>]*>(.*?)</div>\s*</div>', box, re.S):
        key, inner = dm.group(1), dm.group(2)
        vm = re.search(r'<div class="pi-data-value[^>]*>(.*)$', inner, re.S)
        if vm:
            val = re.sub(r"\[\d+\]", "", rd.clean_cell(vm.group(1)))
            out[key] = val
        else:
            out[key] = rd.clean_cell(inner)
    return out


def stats_table(html):
    for t in re.findall(r"<table.*?</table>", html, re.S):
        rows = re.findall(r"<tr.*?</tr>", t, re.S)
        if len(rows) < 2:
            continue
        head = [rd.clean_cell(c) for c in re.findall(r"<t[dh].*?</t[dh]>", rows[0], re.S)]
        if head == ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            vals = [rd.clean_cell(c) for c in re.findall(r"<t[dh].*?</t[dh]>", rows[1], re.S)]
            out = {}
            for k, v in zip(head, vals):
                m = re.match(r"(\d+)(?:\(([+-]?\d+)\))?", v or "")
                out[k] = {"score": int(m.group(1)) if m else None,
                          "mod": m.group(2) if m else None}
            return out
    return {}


def parse_companion(title):
    html = open(os.path.join(rd.HTMLDIR, title + ".html")).read()
    ib = infobox(html)
    stats = stats_table(html)
    recruitment = rd.heading_block(html, "Recruitment")
    cut = recruitment.find("Leaving the party")
    if cut != -1:
        recruitment = recruitment[:cut].strip()
    rm = re.search(r"Act (One|Two|Three)", recruitment)
    return {
        "name": title,
        "role": "Origin" if title in ORIGINS else "Non-origin companion",
        "race": ib.get("race"),
        "subrace": ib.get("subrace"),
        "class": ib.get("class"),
        "subclass": ib.get("subclass"),
        "background": ib.get("background"),
        "hometown": ib.get("hometown"),
        "stats": stats,
        "quest": (rd.heading_block(html, "Companion_quest")
                  or rd.heading_block(html, "Personal_quest")),
        "recruitment_act": rm.group(1) if rm else ACT_OVERRIDES.get(title),
        "recruitment": recruitment,
        "leaving": rd.heading_block(html, "Leaving_the_party"),
        "romance": rd.heading_block(html, "Romance"),
    }


def parse_master():
    html = open(MASTER).read()
    hirelings = []
    m = re.search(r'id="Hirelings"', html)
    n = re.search(r'id="Recruitment_locations"', html)
    for li in re.findall(r"<li[^>]*>(.*?)</li>", html[m.start():n.start()], re.S):
        titles = [t for t in re.findall(r'<a[^>]*title="([^"]+)"', li)
                  if t != "View source image"]
        if len(titles) >= 3:
            hirelings.append({"name": titles[-3], "race": titles[-2], "class": titles[-1]})
    removal = rd.heading_block(html, "Permanent_removal")
    return hirelings, removal


def render(companions, hirelings, removal):
    lines = []
    lines.append("# Baldur's Gate 3 - Companions")
    lines.append("")
    lines.append(
        "Companions who can join the party: the seven origin characters (with "
        "their own personal quests) and the four non-origin companions who can "
        "be recruited later. Stats shown are the companion's default starting "
        "scores; the default class can be changed but the story treats the "
        "original as canonical. Recruitment, leaving conditions and romance "
        "notes are from each companion's bg3.wiki page. See the permanent "
        "buffs file for per-character permanent bonuses (e.g. Volo's Ersatz Eye)."
    )
    lines.append("")
    lines.append("## Companions")
    lines.append("")
    for c in companions:
        lines.append(f"### {c['name']}")
        lines.append("")
        race = c["race"] or ""
        if c["subrace"] and c["subrace"] != "None":
            race = f"{race} ({c['subrace']})"
        cls = c["class"] or ""
        if c["subclass"] and c["subclass"] != "None":
            cls = f"{cls} ({c['subclass']})"
        lines.append(f"- Role: {c['role']} | Race: {race} | Class: {cls} | "
                     f"Background: {c['background']} | Hometown: {c['hometown']}")
        stats = c["stats"]
        if stats:
            parts = ", ".join(f"{k} {v['score']}" for k, v in stats.items())
            lines.append(f"- Starting stats: {parts}")
        if c["quest"]:
            lines.append(f"- Personal quest: {c['quest']}")
        if c["recruitment_act"]:
            lines.append(f"- Recruitable in {c['recruitment_act']}: {c['recruitment']}")
        elif c["recruitment"]:
            lines.append(f"- Recruitment: {c['recruitment']}")
        if c["leaving"]:
            lines.append(f"- Leaving the party: {c['leaving']}")
        if c["romance"]:
            lines.append(f"- Romance: {c['romance']}")
        lines.append("")
    lines.append("## Hirelings")
    lines.append("")
    lines.append(
        "Hirelings can be bought from Withers for 200 gold after he joins the "
        "camp; they can be respec'd freely. Default race/class shown."
    )
    lines.append("")
    for h in hirelings:
        lines.append(f"- **{h['name']}** - {h['race']} {h['class']}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(removal)
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    hirelings, removal = parse_master()
    companions = [parse_companion(t) for t in rd.COMPANION_PAGES]
    data = {"companions": companions, "hirelings": hirelings,
            "permanent_removal": removal}
    json.dump(data, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(companions, hirelings, removal))
    print(f"wrote {len(companions)} companions + {len(hirelings)} hirelings -> "
          f"{OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()