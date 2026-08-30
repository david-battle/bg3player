"""Shared constants and helpers for the build & character reference pipeline.

Reference pages are cached in data/raw_html_ref/ (gitignored); the build
scripts only read that cache, so they are offline and re-runnable. Keep this
pipeline's cache separate from the equipment/consumables caches.
"""
import re
from html import unescape as html_unescape

API = "https://bg3.wiki/w/api.php"
UA = "bg3player-kb/0.1 (personal knowledge base builder)"
DELAY = 0.35

HTMLDIR = "data/raw_html_ref"

# Master list pages (one fetch each).
MASTER_PAGES = ["Feats", "Conditions", "Companions", "Permanent bonuses"]

# Companion wiki pages (origins + non-origin companions).
COMPANION_PAGES = [
    "Astarion",
    "Gale",
    "Karlach",
    "Lae'zel",
    "Shadowheart",
    "Wyll",
    "The Dark Urge",
    "Halsin",
    "Jaheira",
    "Minsc",
    "Minthara",
]

# Curated core gameplay conditions for the glossary, keyed by wiki page base
# name (each must exist as a "Name (Condition)" page or it is skipped). Chosen
# for build/gear-advice relevance: combat states, common buffs/debuffs,
# damage-over-time and control spell effects, auras and elemental effects.
# Some common conditions have no dedicated wiki page (e.g. Blessed, Weakened,
# Deafened, Exhaustion) and are intentionally omitted rather than guessed.
CURATED_CONDITIONS = [
    # Afflictions & combat states
    "Blinded", "Bleeding", "Bane", "Charmed", "Chilled", "Dazed",
    "Encrusted with Frost", "Frozen", "Frightened", "Hastened", "Hiding",
    "Incapacitated", "Lethargic", "Lightly Obscured", "Paralysed", "Petrified",
    "Poisoned", "Polymorphed", "Prone", "Radiating Orb", "Reeling",
    "Restrained", "Reverberation", "Silenced", "Sleeping", "Slowed", "Stunned",
    "Surprised", "Turned", "Wet", "Downed", "Dying", "Unconscious", "Dead",
    "Knocked Out", "Threatened", "Shrouded", "Momentum", "Pinned", "Maimed",
    "Feeble", "Exhausted",
    # Beneficial / buffs
    "Aid", "Barkskin", "Blade Ward", "Bless", "Bardic Inspiration",
    "Bull's Strength", "Cat's Grace", "Guidance", "Heroism", "Longstrider",
    "Mage Armour", "Mirror Image", "Resistance", "Shield", "Shield of Faith",
    "Stoneskin", "Freedom of Movement", "See Invisibility", "True Strike",
    "Death Ward", "Greater Invisibility", "Protection from Evil and Good",
    "Protection from Poison", "Faerie Fire", "Darkvision", "Feather Fall",
    "Jump", "False Life", "Expeditious Retreat", "Armour of Agathys",
    "Beacon of Hope", "Crusader's Mantle", "Disguise Self", "Pass Without Trace",
    "Produce Flame", "Shillelagh",
    # Resistance effects
    "Acid Resistance", "Cold Resistance", "Fire Resistance", "Force Resistance",
    "Lightning Resistance", "Necrotic Resistance", "Poison Resistance",
    "Psychic Resistance", "Radiant Resistance", "Thunder Resistance",
    # Energy / elemental
    "Burning", "Bone Chilled", "Lightning Charges", "Arcane Acuity",
    "Arcane Charge", "Arcane Synergy", "Bloodlust", "Martial Exertion", "Drunk",
    "Entangled", "Ensnared",
    # Spell effects
    "Black Tentacles", "Cloud of Daggers", "Crown of Madness", "Hold Person",
    "Hold Monster", "Heat Metal", "Phantasmal Killer", "Searing Smite",
    "Branding Smite", "Vampiric Touch", "Arms of Hadar", "Witch Bolt",
    "Moonbeam", "Guiding Bolt", "Ray of Frost", "Shocking Grasp",
    "Vicious Mockery", "Wall of Fire", "Plant Growth", "Spike Growth",
    "Blindness", "Colour Spray", "Banished", "Madness", "Confused", "Beguiled",
    "Dominated", "Psionic Weakening",
    # Auras & special
    "Aura of Protection", "Aura of Courage", "Aura of Devotion", "Aura of Hate",
    "Aura of Conquest", "Aura of Terror", "Improved Bardic Inspiration",
    "Warding Bond (Target)",
]


def condition_seed(conditions):
    """Glossary titles from the curated list that exist as real pages."""
    by_name = {}
    for title in conditions:
        if title.endswith("(Condition)"):
            by_name[title[:-11].strip()] = title
    want = set(CURATED_CONDITIONS)
    return sorted(by_name[b] for b in want if b in by_name)


def clean_text(t):
    t = html_unescape(t)
    t = re.sub(r"[\u200b\u2060\ufeff\u00ad]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def strip_edit_markers(t):
    t = re.sub(r"\[\s*edit section.*?\]", "", t, flags=re.S)
    return clean_text(t)


def clean_cell(html):
    html = re.sub(r"<br\s*/?>", ", ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", "", html)
    return clean_text(html)