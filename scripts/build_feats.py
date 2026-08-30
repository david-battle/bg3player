#!/usr/bin/env python3
"""Build the feats reference from cached reference HTML.

Reads data/raw_html_ref/Feats.html, writes data/feats.json and
knowledge_base/reference/feats.md. Offline; only depends on the cache.
"""
import json
import os
import re

import reference_data as rd

SRC = os.path.join(rd.HTMLDIR, "Feats.html")
OUT_JSON = "data/feats.json"
OUT_MD = "knowledge_base/reference/feats.md"


def parse_feats(html):
    m = re.search(r'id="List_of_all_feats"', html)
    if not m:
        m = re.search(r"List of all feats", html)
    table = re.search(r"<table.*?</table>", html[m.start():], re.S)
    if not table:
        return []
    feats = []
    current = None
    pending = None
    for row in re.findall(r"<tr.*?</tr>", table.group(0), re.S):
        rowspan = re.search(r'<th[^>]*scope="rowgroup"[^>]*>(.*?)</th>', row, re.S)
        ths = [rd.clean_cell(t) for t in re.findall(r'<th scope="col"[^>]*>(.*?)</th>', row, re.S)]
        tds = [rd.clean_cell(t) for t in re.findall(r"<td.*?</td>", row, re.S)]
        if rowspan:
            if current:
                if pending:
                    current["items"].append([pending, ""])
                feats.append(current)
            current = {"name": rd.clean_text(rowspan.group(1)), "items": []}
            pending = None
        if current is None:
            continue
        if ths and not tds:
            if pending:
                current["items"].append([pending, ""])
            pending = ths[0]
        elif ths and tds:
            if pending:
                current["items"].append([pending, tds[0]])
                pending = None
            else:
                for th in ths:
                    current["items"].append([th, tds[0] if tds else ""])
        elif tds:
            if pending:
                current["items"].append([pending, tds[0]])
                pending = None
            elif current["items"]:
                current["items"][-1][1] = (current["items"][-1][1] + " " + tds[0]).strip()
            else:
                current["items"].append(["", tds[0]])
    if current:
        if pending:
            current["items"].append([pending, ""])
        feats.append(current)
    return feats


def render(feats):
    lines = []
    lines.append("# Baldur's Gate 3 - Feats")
    lines.append("")
    lines.append(
        "Every feat available when levelling up. Each character gains a feat at "
        "class levels 4, 8 and 12; Fighters get an extra at 6 and Rogues at 10. "
        "Powers are the distinct effects the feat grants; notes flag quirks and bugs."
    )
    lines.append("")
    lines.append(f"## Feats ({len(feats)})")
    lines.append("")
    for f in feats:
        lines.append(f"### {f['name']}")
        lines.append("")
        if f["description"]:
            lines.append(f"{f['description']}")
            lines.append("")
        for p in f["powers"]:
            lines.append(f"- **{p['name']}:** {p['description']}")
        for n in f["notes"]:
            lines.append(f"- **Note:** {n}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    html = open(SRC).read()
    raw = parse_feats(html)
    out = []
    for f in raw:
        description = ""
        powers = []
        notes = []
        for label, text in f["items"]:
            if label == "":
                description = (description + " " + text).strip()
            elif label == "Notes":
                notes.append(text)
            else:
                powers.append({"name": label, "description": text})
        out.append({"name": f["name"], "description": description,
                    "powers": powers, "notes": notes})
    json.dump(out, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(out))
    print(f"wrote {len(out)} feats -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()