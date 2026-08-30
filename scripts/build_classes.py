#!/usr/bin/env python3
"""Build the classes + subclasses reference from cached reference HTML.

Reads data/raw_html_ref/ for each class and subclass page, writes
data/classes.json and knowledge_base/reference/classes_subclasses.md.
Offline; only depends on the cache.
"""
import json
import os
import re

import reference_data as rd

OUT_JSON = "data/classes.json"
OUT_MD = "knowledge_base/reference/classes_subclasses.md"


def parse_class(title):
    html = open(os.path.join(rd.HTMLDIR, title + ".html")).read()
    attrs = rd.parse_dl(rd.heading_html(html, "Attributes"))
    profs = rd.parse_dl(rd.heading_html(html, "Starting_Proficiencies"))
    multi = rd.parse_dl(rd.heading_html(html, "Multiclass_Proficiencies"))
    return {
        "name": title,
        "description": rd.heading_block(html, "Overview"),
        "attributes": attrs,
        "proficiencies": profs,
        "multiclass": multi,
        "subclasses": sorted(
            s for s, c in rd.SUBCLASS_OF.items() if c == title),
    }


def parse_subclass(title):
    html = open(os.path.join(rd.HTMLDIR, title + ".html")).read()
    desc = ""
    for p in re.findall(r"<p>(.*?)</p>", html, re.S)[:3]:
        t = rd.clean_cell(p)
        t = re.sub(r"\[\s*(?:url\s*)?\d+\s*\]", "", t)
        t = re.sub(r"^[^.]*? is (?:one of the [Ss]ubclasses?|a subclass) of "
                   r"[^.,]+\.\s*", "", t)
        t = t.strip()
        if t:
            desc = t
            break
    return {
        "name": title,
        "class": rd.SUBCLASS_OF[title],
        "description": desc,
    }


def render(classes, subclasses):
    by_class = {}
    for s in subclasses:
        by_class.setdefault(s["class"], []).append(s)

    lines = []
    lines.append("# Baldur's Gate 3 - Classes and Subclasses")
    lines.append("")
    lines.append(
        "The 12 classes and every subclass. Each class entry gives its role, "
        "hit points, key abilities, spellcasting ability (where relevant) and "
        "starting proficiencies, then the subclasses with a one-line summary "
        "of what sets each apart. Multiclass proficiencies are what a character "
        "gains for dipping into the class. There are no full level tables here; "
        "that detail lives on bg3.wiki's per-class pages."
    )
    lines.append("")
    for c in classes:
        lines.append(f"## {c['name']}")
        lines.append("")
        if c["description"]:
            lines.append(c["description"])
            lines.append("")
        a = c["attributes"]
        if a:
            hp = a.get("Hit points") or a.get("Hit Points") or ""
            key = a.get("Key abilities", "")
            sca = a.get("Spellcasting Ability", "")
            row = f"- Hit points: {hp}" if hp else ""
            if key:
                row += f"{' | ' if row else '- '}Key abilities: {key}"
            if sca:
                row += f" | Spellcasting ability: {sca}"
            lines.append(row)
        p = c["proficiencies"]
        if p:
            for label, val in p.items():
                lines.append(f"- {label}: {val}")
        m = c["multiclass"]
        if m:
            for label, val in m.items():
                if val:
                    lines.append(f"- Multiclass {label}: {val}")
        subs = by_class.get(c["name"], [])
        if subs:
            lines.append("")
            lines.append("Subclasses:")
            for s in subs:
                d = s["description"] or "no description on the wiki"
                lines.append(f"- **{s['name']}** - {d}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    classes = [parse_class(t) for t in rd.CLASS_PAGES]
    subclasses = [parse_subclass(t) for t in rd.SUBCLASS_OF]
    data = {"classes": classes, "subclasses": subclasses}
    json.dump(data, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(classes, subclasses))
    print(f"wrote {len(classes)} classes + {len(subclasses)} subclasses -> "
          f"{OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()