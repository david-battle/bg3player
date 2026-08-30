#!/usr/bin/env python3
"""Build the difficulty / honour-mode reference from cached reference HTML.

Reads data/raw_html_ref/Difficulty.html (the wiki's Difficulty page; Honour
Mode redirects there), writes data/honour_mode.json and
knowledge_base/reference/honour_mode.md. Offline.
"""
import json
import os
import re

import reference_data as rd

SRC = os.path.join(rd.HTMLDIR, "Difficulty.html")
OUT_JSON = "data/honour_mode.json"
OUT_MD = "knowledge_base/reference/honour_mode.md"

MODES = [("Explorer", "Explorer_mode"),
         ("Balanced", "Balanced_Mode"),
         ("Tactician", "Tactician_mode"),
         ("Honour", "Honour_mode"),
         ("Custom", "Custom_mode")]


def alt_clean(html):
    html = re.sub(r"<img[^>]*alt=\"([^\"]*)\"[^>]*>", r"\1", html)
    return rd.clean_cell(html)


def mode_text(anchor):
    raw = rd.heading_html(open(SRC).read(), anchor)
    raw = re.sub(r"<style[\s\S]*?</style>", "", raw)
    txt = re.sub(r"<[^>]+>", " ", raw)
    txt = re.sub(r"See also:\s*Patch\s*notes/Patch\s*5#Honour\s*mode", "", txt)
    txt = rd.strip_edit_markers(txt)
    return rd.clean_text(txt)


def parse_custom_settings(html):
    t = re.search(r"<table.*?</table>", html, re.S)
    if not t:
        return []
    cols = ["Explorer", "Balanced", "Tactician", "Honour"]
    out = []
    for row in re.findall(r"<tr.*?</tr>", t.group(0), re.S):
        th = re.search(r"<th[^>]*>(.*?)</th>", row, re.S)
        if not th:
            continue
        setting = alt_clean(th.group(1))
        if setting.lower() in ("setting", ""):
            continue
        values = {}
        col = 0
        for td in re.findall(r"<td[^>]*>.*?</td>", row, re.S):
            cm = re.search(r'colspan="(\d+)"', td)
            span = int(cm.group(1)) if cm else 1
            val = alt_clean(td)
            for _ in range(span):
                if col < len(cols):
                    values[cols[col]] = val
                col += 1
        out.append({"setting": setting, "values": values})
    return out


def render(data):
    lines = []
    lines.append("# Baldur's Gate 3 - Difficulties and Honour Mode")
    lines.append("")
    lines.append(
        "The four standard difficulties plus Custom mode, summarised from "
        "bg3.wiki's Difficulty page. Explorer is the easiest, Balanced is the "
        "baseline, Tactician raises enemy numbers and AI, and Honour mode stacks "
        "Tactician with Legendary Actions and a single save. Only mechanics are "
        "covered — no boss guides. Rewards for beating the game on Honour mode: "
        "an in-game golden D20 skin ('Shining Honour') and the Foehammer "
        "achievement."
    )
    lines.append("")
    for m in data["modes"]:
        lines.append(f"## {m['name']} mode")
        lines.append("")
        lines.append(m["description"])
        lines.append("")
    lines.append("## Custom mode settings vs. the standard difficulties")
    lines.append("")
    lines.append(
        "Custom difficulty lets the player tweak these settings; most can be "
        "changed mid-campaign, but the Ruleset cannot and you cannot revert to "
        "a standard difficulty afterwards. The table shows each setting's "
        "default on Explorer / Balanced / Tactician / Honour.")
    lines.append("")
    lines.append("| Setting | Explorer | Balanced | Tactician | Honour |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in data["custom_settings"]:
        v = row["values"]
        lines.append(f"| {row['setting']} | {v.get('Explorer', '')} | "
                     f"{v.get('Balanced', '')} | {v.get('Tactician', '')} | "
                     f"{v.get('Honour', '')} |")
    lines.append("")
    lines.append("## Example of difficulty changes")
    lines.append("")
    lines.append(data["example"])
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    html = open(SRC).read()
    modes = [{"name": n, "description": mode_text(a)} for n, a in MODES]
    settings = parse_custom_settings(
        rd.heading_html(html, "Custom_settings_corresponding_to_the_standard_difficulties"))
    example = rd.heading_block(html, "Example_of_difficulty_changes")
    data = {"modes": modes, "custom_settings": settings, "example": example}
    json.dump(data, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(data))
    print(f"wrote {len(modes)} modes + {len(settings)} settings -> "
          f"{OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()