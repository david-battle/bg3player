#!/usr/bin/env python3
"""Build the illithid powers reference from the cached Illithid powers page.

Reads data/raw_html_ref/Illithid powers.html, writes data/illithid_powers.json
and knowledge_base/reference/illithid_powers.md. Offline.
"""
import json
import os
import re

import reference_data as rd

SRC = os.path.join(rd.HTMLDIR, "Illithid powers.html")
OUT_JSON = "data/illithid_powers.json"
OUT_MD = "knowledge_base/reference/illithid_powers.md"

TIERS = [("Illithid power tree", None),
         ("Elite powers", "Elite_powers"),
         ("Full ceremorphosis", "Full_ceremorphosis"),
         ("Other powers", "Other_powers")]


def parse_power_table(html):
    t = re.search(r"<table.*?</table>", html, re.S)
    if not t:
        return []
    powers = []
    for row in re.findall(r"<tr.*?</tr>", t.group(0), re.S):
        cells = [rd.clean_cell(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>",
                                                      row, re.S)]
        cells = [re.sub(r"\[\d+\]", "", c).strip() for c in cells]
        if not cells or cells[0].lower() == "power":
            continue
        while len(cells) < 4:
            cells.append("")
        powers.append({"name": cells[0], "type": cells[1],
                       "description": cells[2], "requires": cells[3]})
    return powers


def chunk_text(html):
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = rd.strip_edit_markers(txt)
    txt = txt.replace("See also: Partial-illithid", "")
    txt = txt.replace("See also: Full-illithid", "")
    txt = re.sub(r"Click on an icon[^.]*\.", "", txt)
    txt = re.sub(r"Clicking an icon[^.]*\.", "", txt)
    cut = txt.find("Power Type Description")
    if cut != -1:
        txt = txt[:cut]
    return rd.clean_text(txt)


def main():
    html = open(SRC).read()
    section = rd.heading_html(html, "List_of_illithid_powers")

    # split into chunks: base content before the first H3, then each H3 chunk
    h3s = list(re.finditer(r"<h3[^>]*>.*?</h3>", section, re.S))
    chunks = [("Illithid power tree", section[:h3s[0].start()])]
    for i, hm in enumerate(h3s):
        title = rd.strip_edit_markers(re.sub(r"<[^>]+>", "", hm.group(0)))
        title = rd.clean_text(title)
        end = h3s[i + 1].start() if i + 1 < len(h3s) else len(section)
        chunks.append((title, section[hm.end():end]))

    tiers = []
    for title, chunk in chunks:
        tiers.append({
            "name": title,
            "note": chunk_text(chunk),
            "powers": parse_power_table(chunk),
        })

    spellcasting = rd.heading_block(html, "Spellcasting_ability_modifier")
    data = {"spellcasting": spellcasting, "tiers": tiers}
    json.dump(data, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(data))
    total = sum(len(t["powers"]) for t in tiers)
    print(f"wrote {len(tiers)} tiers, {total} powers -> {OUT_JSON} and {OUT_MD}")


def render(data):
    lines = []
    lines.append("# Baldur's Gate 3 - Illithid Powers")
    lines.append("")
    lines.append(
        "The tadpole powers available by consuming Mind Flayer Parasite "
        "Specimens, plus elite (Act Three), full-ceremorphosis and story "
        "powers. Powers are gained through the power tree at camp; a power's "
        "'Requires' entry lists the prerequisite power (or 'None'). Each tier "
        "note below explains when the powers become available."
    )
    lines.append("")
    for t in data["tiers"]:
        lines.append(f"## {t['name']}")
        lines.append("")
        if t["note"]:
            lines.append(t["note"])
            lines.append("")
        for p in t["powers"]:
            lines.append(f"### {p['name']}")
            lines.append("")
            lines.append(f"- Type: {p['type']}")
            if p["requires"] and p["requires"] not in ("None", "-"):
                lines.append(f"- Requires: {p['requires']}")
            lines.append(f"- {p['description']}")
            lines.append("")
    lines.append("## Spellcasting ability")
    lines.append("")
    lines.append(data["spellcasting"])
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    main()