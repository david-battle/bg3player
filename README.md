# BG3 Knowledge Base

A machine-curated, plain-text reference for **magic equipment**, **consumables**
(potions, elixirs, scrolls, special arrows, coatings, grenades, alchemy, camp
supplies) and **build & character reference** (feats, conditions, companions,
permanent buffs, classes, races, backgrounds, illithid powers) of *Baldur's Gate
3* (Prologue through Act Three), built for use by an AI assistant that helps
with gear selection, consumable choices, build advice, and "where do I get X"
questions.

Covers **739 obtainable magic items** (plus a short list that are not
obtainable in the current game), **305 consumables** plus the full alchemy
recipe set, and a character reference (41 feats, 135 conditions, 11
companions + 12 hirelings, 30 permanent buffs, 12 classes + 58 subclasses,
31 race/subrace entries, 12 backgrounds, 39 illithid powers). This includes
items the wiki's own per-act list pages miss (e.g. Balduran's Giantslayer,
Helldusk set, Markoheshkir).

## Files

| File | Purpose |
| --- | --- |
| `knowledge_base/magic_items_by_slot.md` | **Browse index.** Every item grouped by gear slot (weapon, armour, helmet, gloves, boots, cloak, amulet, ring, shield, instrument), then by act. One entry per item with compact effect + how to get. Use this to answer "what \<slot\> helps \<build\> in Act N?" |
| `knowledge_base/magic_items_act_one.md` | Full detail for Act One items, sorted by in-game location, with X/Y map coordinates, full effect text, every acquisition method, notes, and known bugs. Each act file also ends with an "Additional items" section for items the wiki's list page misses. |
| `knowledge_base/magic_items_act_two.md` | Same, Act Two. |
| `knowledge_base/magic_items_act_three.md` | Same, Act Three. |
| `knowledge_base/magic_items_merchant_stock.md` | Generic enchanted +1/+2 weapons/armour/shields sold by traders across acts (not fixed-location items). |
| `knowledge_base/magic_items_undocumented.md` | Items whose acquisition is **not documented** on bg3.wiki (Act: unknown - do not invent locations), and items **not obtainable** in the current game (Early Access-only / inaccessible / conjured). |
| `data/items.json` | Merged machine-readable master (one record per item with all fields, act(s), and acquisition rows). |
| `knowledge_base/consumables/potions_elixirs.md` | All potions and elixirs (mundane included), with effects, duration, and where to get them. |
| `knowledge_base/consumables/scrolls.md` | All spell scrolls with the spell effect and where to get them. |
| `knowledge_base/consumables/arrows_coatings_grenades.md` | Special arrows, weapon coatings, and throwable grenades/bombs. |
| `knowledge_base/consumables/alchemy.md` | Alchemy crafting: every ingredient -> extract, the first vendor that sells each ingredient (earliest-act), and all potion/elixir/grenade/coating recipes (specific extract + generic family + craft/trade levels). |
| `knowledge_base/consumables/camp_supplies.md` | Earliest/convenient camp-supply vendors per town-like area. |
| `data/consumables.json` | Machine-readable master for all 305 consumables. |
| `data/alchemy_recipes.json`, `data/ingredients.json` | Machine-readable recipes and ingredient/vendor data. |
| `knowledge_base/reference/feats.md` | Every feat (41) with its effects, per-power breakdown, and notes. |
| `knowledge_base/reference/conditions.md` | Core gameplay conditions (135) with effects, sources, and notes. |
| `knowledge_base/reference/permanent_buffs.md` | Permanent/lasting character rewards (Ethel's Hair, Mirror of Loss, Awakened, etc.) by act, with how to unlock each. |
| `knowledge_base/reference/companions.md` | The 11 party companions (stats, class, personal quest, recruitment, leaving conditions, romance) + the 12 hirelings and permanent-removal notes. |
| `knowledge_base/reference/classes_subclasses.md` | All 12 classes (hit points, key abilities, starting/multiclass proficiencies) with every subclass and what distinguishes it. |
| `knowledge_base/reference/races.md` | All playable races + subraces from the wiki's comparison table: base speed, proficiencies, features (incl. darkvision, spells). |
| `knowledge_base/reference/backgrounds.md` | The 12 backgrounds: the two skill proficiencies each grants, plus who starts with each. |
| `knowledge_base/reference/illithid_powers.md` | The full tadpole power tree (base, Act Three elite, full-ceremorphosis, story) with type, effect, recharge and prerequisites. |
| `data/feats.json`, `data/conditions.json`, `data/permanent_buffs.json`, `data/companions.json`, `data/classes.json`, `data/races.json`, `data/backgrounds.json`, `data/illithid_powers.json` | Machine-readable masters for the character reference. |

## How an AI should use it

- **Gear-set questions:** search `magic_items_by_slot.md` by slot + act + effect
  keywords. Effects are written out in plain language (e.g. "Advantage on
  Sleight of Hand Checks", "Spell Save DC +1"), so the AI can find candidates
  without knowing item names.
- **Acquisition questions:** the act files give every known way to obtain an
  item, including alternative routes (e.g. stealing vs buying vs reward).
  `magic_items_merchant_stock.md` and `magic_items_undocumented.md` cover the
  edge cases.
- **Coordinates** (X, Y) are in-game map coordinates.
- **Rarity** is one of: Story Item, Legendary, Very Rare, Rare, Uncommon, Common
  (as displayed on bg3.wiki).
- An item can be obtainable in **multiple acts** (listed in the by-slot file).
- Items marked **Act: unknown** in the by-slot index have no documented
  acquisition on the wiki - do not guess a location for them.
- Items in the "Not obtainable" section (Early Access-only, inaccessible,
  conjured) should not be recommended to a player.
- **Consumables:** search the consumables files by type + act + effect keyword
  (e.g. "elixir", "strength", "Act 1"). Elixirs overwrite each other when drunk
  and last until a long rest. For crafting questions use `alchemy.md` (it tells
you the exact ingredient + generic extract family + the earliest vendor).
   Scrolls are usable by any class; Wizards can learn the spell from a scroll.
- **Character reference:** for build advice use `feats.md` (what a feat grants),
   `conditions.md` (what a condition does and what applies it), `companions.md`
   (default class/stats and how/when to recruit each companion),
   `permanent_buffs.md` (permanent character rewards and how to unlock them),
   `classes_subclasses.md` (class role/hit points/proficiencies + what each
   subclass does), `races.md` (speed, proficiencies, features per race/subrace;
   note ability bonuses are a free +2/+1, not fixed per race),
   `backgrounds.md` (skills + who starts with each) and `illithid_powers.md`
   (tadpole power tree and prerequisites).
   The conditions glossary is a curated core set, not the wiki's full 1,500+
   condition pages; conditions with no dedicated wiki page (e.g. Blessed,
   Weakened, Deafened) are omitted rather than guessed.

## Using it as a playthrough adviser

`ADVISER.md` is the instruction set for running this repo as a live playthrough
adviser (opencode pointed at this directory). Two extra pieces make that work:

- `scripts/kb_lookup.py` — precise queries over the JSON masters, so the AI
  answers with grounded facts instead of eyeballing markdown:
  `python3 scripts/kb_lookup.py item --slot gloves --act 2 --effect "spell save"`
  (see the script header for all commands).
- A per-playthrough **state file** the AI maintains (party, act, decisions,
  gear, open missables) so advice is continuous across sessions. The state file
  is a local file, not part of the repo.

The KB itself is static reference; the state file is what makes the adviser
remember where you are.

## Scope and caveats

- Magic equipment covers weapons, armour, shields, helmets, gloves, boots,
  cloaks, amulets, rings, instruments, clothing. Consumables cover potions,
  elixirs, scrolls, special arrows, coatings, grenades, alchemy, and camp
  supplies. The character reference covers feats, conditions, companions,
  permanent buffs, classes and subclasses, races, backgrounds, and illithid
  powers. **Not** covered: dyes, toolkits, quest items, barrels,
  non-magic mundane gear, and the quest index (planned, deferred).
  (planned).
- bg3.wiki's per-act "List of magic items" pages are **incomplete**; items they
  miss were recovered from the wiki's full item catalog (category cross-check)
  and their acts assigned from each item page's "Where to find" text, so there
  is a small risk of act mis-assignment on those items.
- Consumable **acts** are derived from vendor/location mentions in each item's
  "Where to find" text. Many consumables are sold throughout the game with no
  fixed vendor, so they are marked **Act: unknown** (often correct - they
  appear across acts as random loot or generic trader stock).
- Alchemy ingredients marked "First vendor: not documented on bg3.wiki" have no
  vendor listed on the wiki (world-loot only); do not guess one.
- Data reflects the wiki as of **30 Aug 2026**. Patches can change merchant
  stock and item stats; re-extract to refresh (see below).
- Merchant stock is **partially random**; fixed/unique-named items are listed.

## Source and licensing

All data was extracted from **bg3.wiki** (https://bg3.wiki):

- "List of magic items in Act One/Two/Three" pages (per-act item/location tables)
- Individual item pages (effects, properties, acquisition, notes, bugs)
- Equipment-type and rarity categories (used to cross-check completeness)
- Consumable categories (Potions, Elixirs, Scrolls, Arrows, Coatings,
  Grenades, Alchemical ingredients/extracts) for the consumables masters
- The **Alchemy** page (all recipe tables + ingredient/extract families)
- The **Feats**, **Conditions**, **Companions** and **Permanent bonuses** pages,
  plus each companion's page (stats, quest, recruitment, romance) and each
  condition's page (effects, sources), for the character reference

bg3.wiki content is dual-licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This project
reproduces that content for personal reference use; keep attribution if you
redistribute. Item names and mechanical text are from Larian Studios' game.

## Regeneration

```
python3 scripts/fetch_act_lists.py         # base lists from per-act pages
python3 scripts/fetch_item_pages.py        # raw HTML cache for each item page
python3 scripts/parse_item_pages.py        # parse cache -> data/items_raw/
python3 scripts/classify_missing.py        # act assignment for all items
python3 scripts/build_knowledge_base.py    # render markdown + data/items.json

python3 scripts/fetch_consumables.py       # consumable base + page cache
python3 scripts/parse_consumables.py       # parse cache -> data/consumables_raw/
python3 scripts/build_alchemy.py           # alchemy + ingredient/vendor data
python3 scripts/build_consumables.py       # consumables markdown + masters

python3 scripts/fetch_reference.py         # reference page cache (feats, conditions, companions, buffs, classes, races, backgrounds, illithid)
python3 scripts/build_feats.py             # feats markdown + data/feats.json
python3 scripts/build_conditions.py        # conditions glossary + data/conditions.json
python3 scripts/build_permanent_buffs.py   # permanent buffs + data/permanent_buffs.json
python3 scripts/build_companions.py        # companions + data/companions.json
python3 scripts/build_classes.py           # classes + subclasses + data/classes.json
python3 scripts/build_races.py             # races + data/races.json
python3 scripts/build_backgrounds.py       # backgrounds + data/backgrounds.json
python3 scripts/build_illithid.py          # illithid powers + data/illithid_powers.json
```

Fetches are cached in `data/raw_html/` (equipment), `data/raw_html_cons/`
(consumables) and `data/raw_html_ref/` (reference), and parsed in
`data/items_raw/` / `data/consumables_raw/`; re-running only downloads what is
missing. The wiki's MediaWiki API is rate-limited by a small delay in the fetch
scripts. Note: `fetch_act_lists.py` needs to run before `classify_missing.py`
if you change the act pages.