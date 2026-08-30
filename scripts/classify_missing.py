#!/usr/bin/env python3
"""Assign act(s) to every item, including items missing from the wiki's
per-act list pages.

Output: data/item_acts.json  {item_name: {acts: [...], source: "...", note: "..."}}

Sources:
  list     - from the per-act list rows (authoritative, multi-act aware)
  location - from matching a known location name in the item page text
  override - manual mapping for special/conditional items
  stock    - generic merchant-stock items (all acts)
"""
import json
import os
import re
from glob import glob

BASE = "data/items_base.json"
RAWDIR = "data/items_raw"
OUT = "data/item_acts.json"

ACT_ORDER = ["Act One", "Act Two", "Act Three"]

# location name -> act (from wiki list sections + location page categories)
LOC_ACTS = {
    # --- act one locations ---
    "Nautiloid": "Act One", "Overgrown Ruins": "Act One", "Dank Crypt": "Act One",
    "Emerald Grove": "Act One", "Sacred Pool": "Act One", "Secluded Chamber": "Act One",
    "Secluded Cove": "Act One", "Hidden Vault": "Act One", "Ravaged Beach": "Act One",
    "Forest": "Act One", "Blighted Village": "Act One", "Sunlit Wetlands": "Act One",
    "The Risen Road": "Act One", "Waukeen's Rest": "Act One", "Risen Road Toll House": "Act One",
    "Mountain Pass": "Act One", "Goblin Camp": "Act One", "Shattered Sanctum": "Act One",
    "Worg Pens": "Act One", "Underdark": "Act One", "Grymforge": "Act One",
    "Rosymorn Monastery Trail": "Act One", "Rosymorn Monastery": "Act One",
    "Crèche Y'llek": "Act One", "Ebonlake Grotto": "Act One", "Arcane Tower": "Act One",
    "Selûnite Outpost": "Act One", "Adamantine Forge": "Act One", "Abandoned Refuge": "Act One",
    "Whispering Depths": "Act One", "Owlbear Nest": "Act One", "The Hollow": "Act One",
    "Dread Hollow": "Act One", "Apothecary's Cellar": "Act One", "Tadpoling Centre": "Act One",
    "Defiled Temple": "Act One", "Underground Passage": "Act One", "Overgrown Tunnel": "Act One",
    "Decrepit Village": "Act One", "The Festering Cove": "Act One", "Riverside Teahouse": "Act One",
    "Zhentarim Basement": "Act One", "Zhentarim Hideout": "Act One", "Tiefling Hideout": "Act One",
    "Campsite (Act One)": "Act One", "High Hall": "Act One",
    # --- act two locations ---
    "Ruined Battlefield": "Act Two", "Last Light Inn": "Act Two", "Last Light Inn Cellar": "Act Two",
    "Last Light Inn - Cellar": "Act Two", "Reithwin Town": "Act Two", "Reithwin Tollhouse": "Act Two",
    "Gauntlet of Shar": "Act Two", "Grand Mausoleum": "Act Two", "Sharran Sanctuary": "Act Two",
    "Shadowfell": "Act Two", "Moonrise Towers": "Act Two", "Moonrise Towers Prison": "Act Two",
    "Moonrise Towers Rooftop": "Act Two", "Mind Flayer Colony": "Act Two", "House of Healing": "Act Two",
    "The Waning Moon": "Act Two", "Waning Moon": "Act Two", "Mason's Guild": "Act Two",
    "House in Deep Shadows": "Act Two", "Reithwin Graveyard": "Act Two",
    "House of Healing Morgue": "Act Two", "Campsite (Act Two)": "Act Two",
    # --- act three locations ---
    "Campsite (Act Three)": "Act Three", "Astral Plane": "Act Three", "Jungle": "Act Three",
    "Rivington": "Act Three", "Rivington General": "Act Three", "Wyrm's Crossing": "Act Three",
    "Wyrm's Rock Fortress": "Act Three", "Lower City": "Act Three", "Lower City Sewers": "Act Three",
    "Undercity": "Act Three", "Bhaal Temple": "Act Three", "Murder Tribunal": "Act Three",
    "Counting House": "Act Three", "The Counting House": "Act Three", "Guildhall": "Act Three",
    "Devil's Fee": "Act Three", "Sharess' Caress": "Act Three", "The Blushing Mermaid": "Act Three",
    "Blushing Mermaid": "Act Three", "Elfsong Tavern": "Act Three", "Sorcerous Sundries": "Act Three",
    "Stormshore Armoury": "Act Three", "Stormshore Tabernacle": "Act Three",
    "Water Queen's House": "Act Three", "Circus of the Last Days": "Act Three",
    "Open Hand Temple": "Act Three", "Open Hand Temple Cellar": "Act Three",
    "Philgrave's Mansion": "Act Three", "Felogyr's Fireworks": "Act Three",
    "Flymm Cargo": "Act Three", "Fraygo's Flophouse": "Act Three", "Gur Camp": "Act Three",
    "Cazador's Dungeon": "Act Three", "Lady Jannath's Estate": "Act Three",
    "Heapside Prison": "Act Three", "Angleiron's Cellar": "Act Three", "Golbraith's Cellar": "Act Three",
    "Knight's of the Shield Hideout": "Act Three", "Knights of the Shield Hideout": "Act Three",
    "Forge of the Nine": "Act Three", "Steel Watch Foundry": "Act Three",
    "Old Garlow's Place": "Act Three", "Highberry's Home": "Act Three", "Lora's House": "Act Three",
    "Lavernica's Home": "Act Three", "Elerrathin's Home": "Act Three", "Carm's Garms": "Act Three",
    "Danthelon's Dancing Axe": "Act Three", "Chromatic Scale": "Act Three",
    "House of Hope": "Act Three", "Ramazith's Tower": "Act Three", "The Dragon's Sanctum": "Act Three",
    "Dragon's Sanctum": "Act Three", "Wyrmway": "Act Three", "Western Beach": "Act Three",
    "Hhune Mausoleum": "Act Three", "Ancient Lair": "Act Three", "Abandoned Windmill": "Act Three",
    "The Lodge - Basement Docks": "Act Three", "The High Hall": "Act Three",
    "Sorcerous Vault": "Act Three", "Cloister of Sombre Embrace": "Act Three",
    "Szarr Palace": "Act Three", "House of Grief": "Act Three",
}

# manual overrides for special/conditional items missing from the act lists
OVERRIDES = {
    "Dagger of Shar": ("Act One", "Wielded by Shadowheart during her Act One camp confrontation with Lae'zel."),
    "Devotee's Mace": ("Act One, Act Two, Act Three", "Obtained via the Cleric Divine Intervention 'Arm Thy Servant' once the party reaches level 10+."),
    "Infernal Mask": ("Act Three", "Carried by Orpheus if freed and recruited during the Upper City assault."),
    "Mask of the Shapeshifter": ("Act One", "In the Traveller's Chest at the campsite (Deluxe Edition item; available from the start)."),
    "Murderous Cut": ("Act Three", "Carried by several Bhaal cultists throughout Act Three."),
    "Netherstone-Studded Gauntlet": ("Act Three", "Carried by Enver Gortash during the quest Get Gortash's Netherstone."),
    "Nightsong's Armour": ("Act Two", "Worn by Aylin; not normally lootable."),
    "Shar's Sting": ("Act One", "Variant of the Ritual Dagger of Shar (identical except name)."),
    "Undead Slayer Crossbow": ("Act Three", "Obtainable only via specific exploits from The Long Arm of the Gur."),
    "Shield (Hope)": ("Act Three", "House of Hope; wielded by Hope. No longer lootable since Patch 6."),
    "Helm of Balduran": ("Act Three", "In the Dragon's Sanctum after defeating Ansur (Wyrmway quest)."),
    "Selûne's Spear of Night": ("Act Two", "Given to Shadowheart by Aylin at the campsite after the Nightsong encounter."),
    "Sickle of BOOOAL": ("Act One", "The Festering Cove; carried by Pooldripp the Zealous or given by BOOOAL."),
    "Smuggler's Ring": ("Act One", "The Risen Road; on a skeleton hidden in a bush by the river."),
    "Balduran's Giantslayer": ("Act Three", "The Dragon's Sanctum; on the corpse of Ansur."),
    "Orphic Hammer": ("Act Three", "House of Hope; on the central pedestal in the Archive."),
    "Gauntlets of Hill Giant Strength": ("Act Three", "House of Hope; on a pedestal in the Archive."),
    "Gloves of Soul Catching": ("Act Three", "House of Hope; sold by the merchant in the Devil's Den."),
    "Robe of the Weave": ("Act Three", "Sorcerous Sundries; sold by Lorroakan."),
    "Markoheshkir": ("Act Three", "Ramazith's Tower; inside a Globe of Invulnerability."),
    "Helldusk Armour": ("Act Three", "House of Hope; carried by Raphael."),
    "Helldusk Gloves": ("Act Three", "House of Hope; carried by Raphael."),
    "Helldusk Helmet": ("Act Three", "House of Hope; carried by Raphael."),
    "Hellfire Greataxe": ("Act Three", "House of Hope; dropped by Yurgir."),
    "Rhapsody": ("Act Three", "Cazador's Dungeon; carried by Cazador Szarr."),
    "Woe": ("Act Three", "Cazador's Dungeon; reward for defeating Cazador Szarr."),
    "Sarevok's Wretched Armour": ("Act Three", "Murder Tribunal; carried by Sarevok."),
    "Amulet of Greater Health": ("Act Three", "House of Hope; on the pedestal."),
    "Scarab of Protection": ("Act Three", "Looted from a sarcophagus / chest in the Lower City."),
    "True Love's Caress": ("Act Three", "Dolor Amarus / the masked murderer in the Lower City."),
    "Spell Savant Amulet": ("Act Three", "Sold by Vicar Humbletoes at Stormshore Tabernacle."),
    "Headband of Intellect": (None, "Unobtainable version; the obtainable item is 'Warped Headband of Intellect'."),
    "Amulet of Elemental Torment": ("Act Three", "House of Hope; carried by Hope during the fight against Raphael. (Previously sold by Act One merchants; moved to House of Hope in Patch 3.)"),
    "Protective Plate": ("Act Two", "House of Healing Morgue; worn by the Hollow Armour at the bottom of the pit."),
    "Spider's Lyre": ("Act One", "Held by Minthara in the Goblin Camp (pickpocketed/killed/knocked out, or given if the party sides with her), or dropped by Nere in Grymforge if killed."),
}

# generic merchant-stock items (available from traders across acts)
STOCK = {
    "Battleaxe +1", "Breastplate +2", "Chain Mail +1", "Chain Mail +2",
    "Chain Shirt +1", "Chain Shirt +2", "Flail +1", "Flail +2", "Glaive +1",
    "Glaive +2", "Halberd +1", "Half Plate Armour +1", "Half Plate Armour +2",
    "Hide Armour +1", "Hide Armour +2", "Leather Armour +1", "Leather Armour +2",
    "Light Hammer +1", "Longbow +2", "Longsword +1", "Mace +1", "Maul +1",
    "Morningstar +1", "Padded Armour +1", "Padded Armour +2", "Pike +1",
    "Plate Armour +2", "Quarterstaff +1", "Quarterstaff +2", "Rapier +1",
    "Rapier +2", "Ring Mail Armour +1", "Ring Mail Armour +2", "Scale Mail +1",
    "Scale Mail +2", "Scale Mail Armour +1", "Scimitar +1", "Scimitar +2",
    "Shortbow +1", "Shortsword +1", "Shortsword +2", "Spear +1", "Spear +2",
    "Splint Armour +1", "Splint Armour +2", "Studded Leather Armour +1",
    "Studded Leather Armour +2", "Trident +1", "Trident +2", "Warhammer +1",
    "Longbow +1", "Greatclub +1", "Greatclub +2", "Greataxe +1", "Greataxe +2",
    "Handaxe +1", "Dart +1", "Dart +2", "Studded Shield +1", "Robe +1",
    "Shield +2", "Dagger +1", "Greatsword +1", "War Pick +1", "Plate Armour +1",
}

# not obtainable in the current game (Early Access only / conjured / dupes)
EXCLUDED = {
    "Doom Axe": "Early Access only; replaced by Doom Hammer in the full release.",
    "Gloves of Succour": "Early Access only; replaced by Gloves of Heroism.",
    "Ring of Restorative Gravity": "Early Access only.",
    "Shadow Blade (weapon)": "Created via the Shadow Blade spell; not a lootable item.",
    "Headband of Intellect": "Unobtainable version; the obtainable item is Warped Headband of Intellect.",
    "Battered Lute": "Only a cosmetic/broken version used in a quest; not an equipable magic item.",
    "Featherlight Boots": "Early Access only.",
    "Gloves of Fire Resistance": "Early Access only.",
    "Gloves of Flint and Steel": "Early Access only.",
    "Ilmater's Aid": "Early Access only.",
    "Ring of Fire": "Early Access only.",
    "Circlet of Fire": "Not present in the launch version of the game.",
    # --- cut / unfinished / unreleased items (bg3.wiki has no acquisition data) ---
    "Flail of Dread Skulls": "Cut content; appears to be an earlier, unfinished version of the Shattered Flail.",
    "Singing Sword": "Cut content; appears to be an earlier version of Phalar Aluve (grants neither Sing nor Shriek).",
    "Spiderstep Staff": "Cut content; unused - intended for Minthara's trial.",
    "Ring of Crabsight": "Cut content; intended for an unfinished/cut quest.",
    "Vampiric Gloves": "Cut content; intended for an unfinished Cazador's Palace area.",
    "Enforcer Club": "Unobtainable; appears in Dammon's Act Two treasure table with quantity 0.",
    "Enforcer Helmet": "Unobtainable; appears in Dammon's Act Two treasure table with quantity 0.",
    "Enforcer Shield": "Unobtainable; appears in Dammon's Act Two treasure table with quantity 0.",
    "Oathbreaker Knight Armour": "Not lootable; the Oathbreaker Knight's armour is a visual override.",
    "Robust Chain Shirt": "Replaced; originally Sergeant Thrinn's reward, substituted with Armour of Uninhibited Kushigo.",
    "Steadfast Maul": "No documented acquisition; shares the Shattered Flail's Tenacity mechanic (unfinished/EA-era).",
    "Tough Sunrises": "No documented acquisition; shares the Shattered Flail's Tenacity mechanic (unfinished/EA-era).",
    "Planeslayer Flail": "No documented acquisition; shares the Shattered Flail's Tenacity mechanic (unfinished/EA-era).",
    "Light Crossbow of Speed": "Legacy item from Baldur's Gate 1/2; no documented acquisition in BG3.",
    "The Clover": "No documented acquisition; appears to be an unfinished variant sharing the Knife of the Undermountain King's Organ Rearranger passive.",
    # --- no documented acquisition in the current game ---
    "A Sparking Promise": "No documented acquisition; not found in the current game.",
    "Allandra's Whelm": "No documented acquisition; not found in the current game.",
    "Arduous Flame Blade": "No documented acquisition; not found in the current game.",
    "Blood-Bound Blade": "No documented acquisition; not found in the current game.",
    "Briskwind Boots": "No documented acquisition; not found in the current game.",
    "Cloak of Avarice": "No documented acquisition; not found in the current game.",
    "Combination Axe": "No documented acquisition; not found in the current game.",
    "Dauntless Amulet": "No documented acquisition; not found in the current game.",
    "Deadly Channeller Gloves": "No documented acquisition; not found in the current game.",
    "Executioner Sword": "No documented acquisition; not found in the current game.",
    "Gargoyle Boots": "No documented acquisition; not found in the current game.",
    "Githyanki Breastplate": "No documented acquisition; not found in the current game.",
    "Githyanki Longsword (Psionic)": "No documented acquisition; not found in the current game.",
    "Goblinbane Dagger": "No documented acquisition; not found in the current game.",
    "Hag's Ring": "No documented acquisition; not found in the current game.",
    "Hat Of Uproarious Laughter": "No documented acquisition; not found in the current game.",
    "Helm of Arcane Gate": "No documented acquisition; not found in the current game.",
    "Infernal Longsword": "No documented acquisition; not found in the current game.",
    "Infernal Warhammer": "No documented acquisition; not found in the current game.",
    "Ironwood Breastplate": "No documented acquisition; not found in the current game.",
    "Kruznabir's Asylum Amulet": "No documented acquisition; not found in the current game.",
    "Magical Hand Crossbow": "No documented acquisition; not found in the current game.",
    "Mind Sundering Dagger": "No documented acquisition; not found in the current game.",
    "Moonblade": "No documented acquisition; not found in the current game.",
    "Nightsinger's Half-Plate": "No documented acquisition; not found in the current game.",
    "Promise": "No documented acquisition; not found in the current game.",
    "Rebound Battleaxe": "No documented acquisition; not found in the current game.",
    "Render of Scrumptious Flesh": "No documented acquisition; not found in the current game.",
    "Robe of Spell Resistance": "No documented acquisition; not found in the current game.",
    "Sanguine Blade": "No documented acquisition; not found in the current game.",
    "Shadow Battleaxe": "No documented acquisition; not found in the current game.",
    "Shadowstep Boots": "No documented acquisition; not found in the current game.",
    "Synaptic Needle Amulet": "No documented acquisition; not found in the current game.",
    "Tenacious Boots": "No documented acquisition; not found in the current game.",
    "The Fork-Lightning Fingers": "No documented acquisition; not found in the current game.",
    "Tightening Orbit Helm": "No documented acquisition; not found in the current game.",
    "Torment Drinker Armour": "No documented acquisition; not found in the current game.",
    "Treacleflow Amulet": "No documented acquisition; not found in the current game.",
    "Verminsign": "No documented acquisition; not found in the current game.",
    "Vicious Shortsword": "No documented acquisition; not found in the current game.",
    "Wakeful Amulet": "No documented acquisition; not found in the current game.",
}

STOCK_NOTE = "Generic merchant stock; available from various traders (details in How to get)."

EA_ONLY_HINTS = ("Early Access only", "Early access only", "(Early Access only)")
INACCESSIBLE_HINTS = ("inaccessible", "Inaccessible")


def find_locations(text, locs):
    found = set()
    t = " " + text + " "
    for loc in locs:
        if re.search(r"(?i)(^|\W)" + re.escape(loc) + r"(\W|$)", t):
            found.add(loc)
    return found


def main():
    base = json.load(open(BASE))
    base_acts = {}
    for r in base:
        base_acts.setdefault(r["name"], set()).add(r["act"])
    locs = sorted(LOC_ACTS, key=len, reverse=True)

    out = {}
    for path in glob(os.path.join(RAWDIR, "*.json")):
        name = os.path.basename(path)[:-5]
        rec = json.load(open(path))
        if name in EXCLUDED:
            out[name] = {"acts": [], "source": "excluded", "note": EXCLUDED[name]}
            continue
        texts_all = []
        texts_all += rec.get("where_to_find") or []
        if rec.get("description"):
            texts_all.append(rec["description"])
        texts_all += rec.get("notes") or []
        joined = " ".join(texts_all)
        if any(h in joined for h in EA_ONLY_HINTS):
            out[name] = {"acts": [], "source": "excluded",
                         "note": "Early Access only; not obtainable in the current game."}
            continue
        if any(h in rec.get("description", "") for h in INACCESSIBLE_HINTS):
            out[name] = {"acts": [], "source": "excluded",
                         "note": "Inaccessible item; not obtainable by the player."}
            continue
        if name in base_acts:
            out[name] = {"acts": sorted(base_acts[name]), "source": "list"}
            continue
        if name in STOCK:
            out[name] = {"acts": ["Act One", "Act Two", "Act Three"],
                         "source": "stock", "note": STOCK_NOTE}
            continue
        if name in OVERRIDES:
            acts, note = OVERRIDES[name]
            out[name] = {"acts": ([a for a in ACT_ORDER if a in acts] if acts else []),
                         "source": "override", "note": note}
            continue
        # location-based classification
        acts = set()
        hits = []
        texts = []
        texts += rec.get("where_to_find") or []
        if rec.get("description"):
            texts.append(rec["description"])
        texts += rec.get("notes") or []
        for text in texts:
            for loc in find_locations(text, locs):
                acts.add(LOC_ACTS[loc])
                hits.append(loc)
        if acts:
            out[name] = {"acts": sorted(acts, key=ACT_ORDER.index),
                         "source": "location", "hits": sorted(set(hits))}
        else:
            out[name] = {"acts": [], "source": "unknown"}
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    unknown = [n for n, v in out.items() if not v["acts"] and v["source"] != "excluded"]
    excluded = [n for n, v in out.items() if v["source"] == "excluded"]
    print(f"wrote {OUT}: {len(out)} items")
    print(f"excluded: {len(excluded)} -> {excluded}")
    print(f"unknown acts: {len(unknown)} -> {unknown}")


if __name__ == "__main__":
    main()