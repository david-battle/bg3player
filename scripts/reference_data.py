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
MASTER_PAGES = ["Feats", "Conditions", "Companions", "Permanent bonuses",
                "Races", "Achievements", "Difficulty"]

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

# The 12 base class pages (each has Overview / Class information / subclasses).
CLASS_PAGES = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
    "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard",
]

# Every subclass page, mapped to its parent class. The parent class is stated
# on the page but the mapping is curated so grouping never depends on prose.
SUBCLASS_OF = {
    "Berserker": "Barbarian", "Wildheart": "Barbarian",
    "Wild Magic (barbarian subclass)": "Barbarian",
    "Giant (barbarian subclass)": "Barbarian",
    "College of Lore": "Bard", "College of Valour": "Bard",
    "College of Swords": "Bard", "College of Glamour": "Bard",
    "Bladesinging": "Bard",
    "Life Domain": "Cleric", "Light Domain": "Cleric",
    "Trickery Domain": "Cleric", "Knowledge Domain": "Cleric",
    "Nature Domain": "Cleric", "Tempest Domain": "Cleric",
    "War Domain": "Cleric", "Death Domain": "Cleric",
    "Circle of the Land": "Druid", "Circle of the Moon": "Druid",
    "Circle of the Spores": "Druid", "Circle of the Stars": "Druid",
    "Battle Master": "Fighter", "Eldritch Knight": "Fighter",
    "Champion": "Fighter", "Arcane Archer": "Fighter",
    "Way of the Open Hand": "Monk", "Way of Shadow": "Monk",
    "Way of the Four Elements": "Monk", "Way of the Drunken Master": "Monk",
    "Oath of Devotion": "Paladin", "Oath of the Ancients": "Paladin",
    "Oath of Vengeance": "Paladin", "Oath of the Crown": "Paladin",
    "Oathbreaker": "Paladin",
    "Beast Master": "Ranger", "Hunter": "Ranger",
    "Gloom Stalker": "Ranger", "Swarmkeeper": "Ranger",
    "Thief": "Rogue", "Assassin": "Rogue",
    "Arcane Trickster": "Rogue", "Swashbuckler": "Rogue",
    "Draconic Bloodline": "Sorcerer",
    "Wild Magic (sorcerer subclass)": "Sorcerer",
    "Storm Sorcery": "Sorcerer", "Shadow Magic": "Sorcerer",
    "The Fiend": "Warlock", "The Great Old One": "Warlock",
    "The Archfey": "Warlock", "The Hexblade": "Warlock",
    "Abjuration School": "Wizard", "Conjuration School": "Wizard",
    "Divination School": "Wizard", "Enchantment School": "Wizard",
    "Evocation School": "Wizard", "Illusion School": "Wizard",
    "Necromancy School": "Wizard", "Transmutation School": "Wizard",
}

# The 11 playable races (not the transformation states Full/Partial-illithid,
# which are covered by the illithid powers page).
RACE_PAGES = [
    "Dragonborn", "Drow", "Dwarf", "Elf", "Githyanki", "Gnome", "Half-Elf",
    "Half-Orc", "Halfling", "Human", "Tiefling",
]

# The 12 character backgrounds.
BACKGROUND_PAGES = [
    "Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero",
    "Guild Artisan", "Haunted One", "Noble", "Outlander", "Sage", "Soldier",
    "Urchin",
]

# Single page carrying the full tadpole power tree.
ILLITHID_PAGES = ["Illithid powers"]

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


def heading_html(html, anchor):
    """Raw HTML after the heading whose span has the given id, until the next
    heading of the same or higher level (so sub-section headings are kept)."""
    m = re.search(r'id="' + re.escape(anchor) + r'"', html)
    if not m:
        return ""
    prev = list(re.finditer(r"<h([234])", html[:m.start()]))
    level = int(prev[-1].group(1)) if prev else 3
    close = re.search(r"</h%d>" % level, html[m.start():])
    if not close:
        return ""
    start = m.start() + close.end()
    nxt = None
    for hm in re.finditer(r"<h([234])", html[start:]):
        if int(hm.group(1)) <= level:
            nxt = hm.start()
            break
    end = start + nxt if nxt is not None else len(html)
    return html[start:end]


def heading_block(html, anchor):
    """Text version of heading_html (tags stripped, edit markers removed)."""
    seg = re.sub(r"<[^>]+>", " ", heading_html(html, anchor))
    return strip_edit_markers(seg)


def parse_dl(html):
    """Parse <dl><dt>label</dt><dd>value</dd>...</dl> blocks into a dict,
    joining multiple <dd> values per <dt> with spaces."""
    out = {}
    for dm in re.finditer(r"<dl>(.*?)</dl>", html, re.S):
        body = dm.group(1)
        for dtm in re.finditer(
                r"<dt[^>]*>(.*?)</dt>\s*((?:<dd[^>]*>.*?</dd>\s*)*)", body, re.S):
            label = clean_text(re.sub(r"<[^>]+>", "", dtm.group(1)))
            dds = [clean_cell(dd) for dd in re.findall(r"<dd[^>]*>(.*?)</dd>",
                                                       dtm.group(2), re.S)]
            out[label] = " ".join(x for x in dds if x)
    return out


def first_paragraph(html):
    m = re.search(r"<p>(.*?)</p>", html, re.S)
    return clean_cell(m.group(1)) if m else ""