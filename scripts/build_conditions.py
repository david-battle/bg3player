#!/usr/bin/env python3
"""Build the conditions glossary from cached reference HTML.

Reads data/raw_html_ref/* (Condition).html, writes data/conditions.json and
knowledge_base/reference/conditions.md. Offline; only depends on the cache.
"""
import json
import os
import re

import reference_data as rd

OUT_JSON = "data/conditions.json"
OUT_MD = "knowledge_base/reference/conditions.md"
SEED = "data/condition_seed.json"


def first_effects_table(html):
    for t in re.findall(r"<table.*?</table>", html, re.S):
        cells = [rd.clean_cell(c) for c in re.findall(r"<t[dh].*?</t[dh]>", t, re.S)]
        if "Effects" in cells:
            return t
    return None


def tooltip_effects(html):
    m = re.search(r'<div class="bg3wiki-tooltip-box[^"]*">', html)
    if not m:
        return []
    end = re.search(r"<h2", html[m.start():])
    seg = html[m.start(): m.start() + (end.start() if end else 8000)]
    return [rd.clean_cell(li) for li in re.findall(r"<li[^>]*>(.*?)</li>", seg, re.S)]


def section_items(html, section_id):
    m = re.search(r'id="' + re.escape(section_id) + r'"', html)
    if not m:
        return []
    nxt = re.search(r"<h[12]", html[m.start() + 10:])
    seg = html[m.start(): m.start() + 10 + (nxt.start() if nxt else len(html))]
    return [rd.clean_cell(li) for li in re.findall(r"<li[^>]*>(.*?)</li>", seg, re.S)]


def parse_condition(name, html):
    base = name.removesuffix(" (Condition)")
    effects = []
    table = first_effects_table(html)
    if table:
        for row in re.findall(r"<tr.*?</tr>", table, re.S):
            cells = [rd.clean_cell(c) for c in re.findall(r"<t[dh].*?</t[dh]>", row, re.S)]
            if len(cells) >= 2 and (cells[0] == base or base.startswith(cells[0])):
                effects.append(cells[-1])
    else:
        effects = tooltip_effects(html)
    sources = []
    m = re.search(r'<div class="bg3wiki-condition-sources".*?</div>', html, re.S)
    if m:
        for li in re.findall(r"<li[^>]*>(.*?)</li>", m.group(0), re.S):
            a = re.search(r'<a[^>]*title="([^"]+)"', li)
            if a:
                sources.append(rd.clean_text(a.group(1)))
            else:
                sources.append(rd.clean_cell(li))
    notes = section_items(html, "Notes")
    return {"effects": [e for e in effects if e], "sources": sources, "notes": notes}


def render(conds):
    lines = []
    lines.append("# Baldur's Gate 3 - Conditions Glossary")
    lines.append("")
    lines.append(
        "Core gameplay conditions that come up when evaluating gear, spells and "
        "consumables. Effects and sources are taken from each condition's "
        "bg3.wiki page. This is a curated core list, not the full 1,500+ "
        "condition pages on the wiki. Some common conditions (e.g. Blessed, "
        "Weakened, Deafened, Exhaustion) have no dedicated wiki page and are "
        "omitted rather than guessed."
    )
    lines.append("")
    lines.append(f"## Conditions ({len(conds)})")
    lines.append("")
    for c in conds:
        lines.append(f"### {c['name']}")
        lines.append("")
        if c["effects"]:
            for e in c["effects"]:
                lines.append(f"- **Effect:** {e}")
        else:
            lines.append("- **Effect:** no description on wiki page")
        if c["sources"]:
            lines.append(f"- Sources: {', '.join(c['sources'])}")
        for n in c["notes"]:
            lines.append(f"- **Note:** {n}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    seed = set(json.load(open(SEED)))
    recs = {}
    for name in seed:
        path = os.path.join(rd.HTMLDIR, name + ".html")
        if os.path.exists(path):
            recs[name] = parse_condition(name, open(path).read())
    out = [{"name": n, **v} for n, v in sorted(recs.items())]
    json.dump(out, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(out))
    print(f"wrote {len(out)} conditions -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()