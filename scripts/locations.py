#!/usr/bin/env python3
"""Shared act-classification helpers for the consumables pipeline.

Reuses the item pipeline's location->act map and adds a few consumables-relevant
locations not needed for equipment.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_missing import LOC_ACTS  # noqa: E402

ACT_ORDER = ["Act One", "Act Two", "Act Three"]

CONS_EXTRA_LOCS = {
    "Myconid Colony": "Act One",
    "Druid Grove": "Act One",
    # override: LOC_ACTS lists "High Hall" as Act One, but for consumable
    # sourcing it is the Act Three High Hall (final battle area)
    "High Hall": "Act Three",
}

ALL_LOCS = dict(LOC_ACTS)
ALL_LOCS.update(CONS_EXTRA_LOCS)
LOC_NAMES = sorted(ALL_LOCS, key=len, reverse=True)


def find_acts(text):
    """Return the acts referenced by known location names in `text`."""
    acts = set()
    t = " " + text + " "
    for loc in LOC_NAMES:
        if re.search(r"(?i)(^|\W)" + re.escape(loc) + r"(\W|$)", t):
            acts.add(ALL_LOCS[loc])
    return sorted(acts, key=ACT_ORDER.index) if acts else []