#!/usr/bin/env python3
"""Build the achievements reference from cached reference HTML.

Reads data/raw_html_ref/Achievements.html, writes data/achievements.json and
knowledge_base/reference/achievements.md. Offline.
"""
import json
import os
import re

import reference_data as rd

SRC = os.path.join(rd.HTMLDIR, "Achievements.html")
OUT_JSON = "data/achievements.json"
OUT_MD = "knowledge_base/reference/achievements.md"


def parse_table(html):
    t = re.search(r"<table.*?</table>", html, re.S)
    if not t:
        return []
    out = []
    for row in re.findall(r"<tr.*?</tr>", t.group(0), re.S):
        cells = [rd.clean_cell(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>",
                                                      row, re.S)]
        cells = [re.sub(r"\[\d+\]", "", c).strip() for c in cells]
        if len(cells) < 3 or cells[1].lower() == "name":
            continue
        while len(cells) < 4:
            cells.append("")
        out.append({"name": cells[1], "description": cells[2],
                    "hidden": cells[3].lower() == "yes"})
    return out


def render(achievements):
    hidden = sum(1 for a in achievements if a["hidden"])
    lines = []
    lines.append("# Baldur's Gate 3 - Achievements")
    lines.append("")
    lines.append(
        f"All {len(achievements)} achievements with their unlock conditions "
        f"({hidden} are hidden — their names stay blank until you earn them). "
        "Act-locked and missable achievements are not flagged separately here; "
        "the description is the unlock condition. The in-game golden D20 "
        "('Shining Honour') and the Foehammer achievement require completing "
        "the campaign on Honour mode (see honour_mode.md)."
    )
    lines.append("")
    for a in sorted(achievements, key=lambda a: a["name"].lower()):
        lines.append(f"### {a['name']}")
        lines.append("")
        lines.append(a["description"])
        if a["hidden"]:
            lines.append("")
            lines.append("*Hidden until unlocked.*")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    html = open(SRC).read()
    achievements = parse_table(html)
    json.dump(achievements, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(achievements))
    print(f"wrote {len(achievements)} achievements -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()