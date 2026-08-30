#!/usr/bin/env python3
"""Build the backgrounds reference from cached reference HTML.

Reads data/raw_html_ref/ for each background page, writes data/backgrounds.json
and knowledge_base/reference/backgrounds.md. Offline.
"""
import json
import os
import re

import reference_data as rd

OUT_JSON = "data/backgrounds.json"
OUT_MD = "knowledge_base/reference/backgrounds.md"


def parse_li(html):
    """Parse <ul><li><b>Label</b>: value</li>...</ul> into {label: value}."""
    out = {}
    for li in re.findall(r"<li[^>]*>(.*?)</li>", html, re.S):
        bm = re.search(r"<b[^>]*>(.*?)</b>\s*:?\s*(.*)", li, re.S)
        if bm:
            label = rd.clean_text(re.sub(r"<[^>]+>", "", bm.group(1)))
            out[label] = rd.clean_cell(bm.group(2))
    return out


def parse_background(title):
    html = open(os.path.join(rd.HTMLDIR, title + ".html")).read()
    return {
        "name": title,
        "description": rd.first_paragraph(html),
        "skills": parse_li(rd.heading_html(html, "Background_features")),
    }


def render(backgrounds):
    lines = []
    lines.append("# Baldur's Gate 3 - Backgrounds")
    lines.append("")
    lines.append(
        "The 12 backgrounds a character can pick at creation (plus the special "
        "Haunted One granted to The Dark Urge). Each background grants two skill "
        "proficiencies; in BG3 backgrounds do not carry a mechanical feature, "
        "only the skills and their inspiration themes. The notes below list who "
        "starts with each background by default."
    )
    lines.append("")
    for b in backgrounds:
        lines.append(f"## {b['name']}")
        lines.append("")
        if b["description"]:
            lines.append(b["description"])
            lines.append("")
        for label, value in b["skills"].items():
            lines.append(f"- **{label}:** {value}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    backgrounds = [parse_background(t) for t in rd.BACKGROUND_PAGES]
    json.dump({"backgrounds": backgrounds}, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(backgrounds))
    print(f"wrote {len(backgrounds)} backgrounds -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()