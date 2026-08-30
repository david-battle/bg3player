# BG3 Magic Item Knowledge Base

A machine-curated, plain-text reference for the **magic equipment** of
*Baldur's Gate 3* (Prologue through Act Three), built for use by an AI
assistant that helps with gear selection and "where do I get X" questions.

Covers **740 obtainable items** (plus a short list of items that are not
obtainable in the current game). This includes items the wiki's own per-act
list pages miss (e.g. Balduran's Giantslayer, Helldusk set, Markoheshkir).

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

## Scope and caveats

- Covers **magic equipment** (weapons, armour, shields, helmets, gloves, boots,
  cloaks, amulets, rings, instruments, clothing). **Not** covered yet:
  consumables (potions, scrolls, elixirs, arrows, coatings, grenades) and
  non-magic gear.
- bg3.wiki's per-act "List of magic items" pages are **incomplete**; items they
  miss were recovered from the wiki's full item catalog (category cross-check)
  and their acts assigned from each item page's "Where to find" text, so there
  is a small risk of act mis-assignment on those items.
- Data reflects the wiki as of **30 Aug 2026**. Patches can change merchant
  stock and item stats; re-extract to refresh (see below).
- Merchant stock is **partially random**; fixed/unique-named items are listed.

## Source and licensing

All data was extracted from **bg3.wiki** (https://bg3.wiki):

- "List of magic items in Act One/Two/Three" pages (per-act item/location tables)
- Individual item pages (effects, properties, acquisition, notes, bugs)
- Equipment-type and rarity categories (used to cross-check completeness)

bg3.wiki content is dual-licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This project
reproduces that content for personal reference use; keep attribution if you
redistribute. Item names and mechanical text are from Larian Studios' game.

## Regeneration

```
python3 scripts/fetch_act_lists.py      # base lists from per-act pages
python3 scripts/fetch_item_pages.py     # raw HTML cache for each item page
python3 scripts/parse_item_pages.py     # parse cache -> data/items_raw/
python3 scripts/classify_missing.py     # act assignment for all items
python3 scripts/build_knowledge_base.py # render markdown + data/items.json
```

Fetches are cached in `data/raw_html/` and `data/items_raw/`; re-running only
downloads what is missing. The wiki's MediaWiki API is rate-limited by a small
delay in the fetch script. Note: `fetch_act_lists.py` needs to run before
`classify_missing.py` if you change the act pages.