#!/usr/bin/env python3
"""Build the permanent buffs & lasting rewards reference.

Reads data/raw_html_ref/Permanent bonuses.html, writes data/permanent_buffs.json
and knowledge_base/reference/permanent_buffs.md. Offline; only depends on the
cache.
"""
import json
import os
import re

import reference_data as rd

SRC = os.path.join(rd.HTMLDIR, "Permanent bonuses.html")
OUT_JSON = "data/permanent_buffs.json"
OUT_MD = "knowledge_base/reference/permanent_buffs.md"


def blocks(html):
    """Yield (level, title, content_text) for every heading, content being the
    text between this heading and the next one."""
    heads = list(re.finditer(r"<h([234])[^>]*>(.*?)</h\1>", html, re.S))
    out = []
    for i, m in enumerate(heads):
        level = int(m.group(1))
        title = rd.strip_edit_markers(rd.clean_cell(m.group(2)))
        start = m.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(html)
        seg = html[start:end]
        seg = re.sub(r"<[^>]+>", " ", seg)
        out.append((level, title, rd.strip_edit_markers(seg)))
    return out


def render(acts):
    lines = []
    lines.append("# Baldur's Gate 3 - Permanent Buffs and Rewards")
    lines.append("")
    lines.append(
        "Permanent (or long-lasting) character enhancements and rewards, grouped "
        "by the act in which they are normally obtained. Each entry lists what "
        "the bonus does and how to unlock it. Sourced from bg3.wiki's Permanent "
        "bonuses page."
    )
    lines.append("")
    for act in acts:
        lines.append(f"## {act['act']}")
        lines.append("")
        for b in act["bonuses"]:
            lines.append(f"### {b['name']}")
            lines.append("")
            if b["description"]:
                lines.append(b["description"])
                lines.append("")
            for label, text in b["sections"].items():
                lines.append(f"**{label}:** {text}")
                lines.append("")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    html = open(SRC).read()
    acts = []
    cur_act = None
    cur_bonus = None
    for level, title, text in blocks(html):
        if level == 2:
            if title in ("Contents", "See Also", ""):
                cur_act = None
                continue
            cur_act = {"act": title, "description": text, "bonuses": []}
            acts.append(cur_act)
            cur_bonus = None
        elif level == 3 and cur_act is not None:
            cur_bonus = {"name": title, "description": text, "sections": {}}
            cur_act["bonuses"].append(cur_bonus)
        elif level == 4 and cur_bonus is not None:
            cur_bonus["sections"][title] = text
    json.dump(acts, open(OUT_JSON, "w"), indent=1)
    with open(OUT_MD, "w") as f:
        f.write(render(acts))
    n = sum(len(a["bonuses"]) for a in acts)
    print(f"wrote {n} permanent buffs across {len(acts)} acts -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()