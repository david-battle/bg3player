# Handoff

## Verified State

- Branch `main`; upstream is set to `origin` (https://github.com/david-battle/bg3player,
  public), so the user's `push` script (plain `git push` per repo) works — the
  user runs it, not the assistant.
- Worktree is clean. All Phase 1-3 pipeline work, the adviser scaffolding
  (ADVISER.md + kb_lookup.py), and the adviser-mode AGENTS.md note are committed
  on `main`. Nothing pending to stage.

## Completed Work (2026-08-30)

Built the knowledge base in two parts, from **bg3.wiki** data in
`/home/dlbattle/bg3player`.

### Part 1 — Magic equipment (739 items)
- **739 obtainable items** covered (plus 18 not obtainable in the current
  game), including items bg3.wiki's own per-act lists miss (e.g. Balduran's
  Giantslayer, the Helldusk set, Markoheshkir, Helm of Balduran, Orphic Hammer).
- Pipeline: `fetch_act_lists.py` -> base per-act lists (588 rows);
  `fetch_item_pages.py` -> raw HTML cache; `parse_item_pages.py` -> structured
  records; `classify_missing.py` -> act assignment; `build_knowledge_base.py`
  -> markdown + `data/items.json`.
- Deliverables: `knowledge_base/magic_items_by_slot.md` (browse by slot + act),
  per-act detail files with coordinates/acquisition/notes/bugs,
  `magic_items_merchant_stock.md`, `magic_items_undocumented.md`.

### Part 2 — Consumables + alchemy (305 items)
- **305 consumables**: all potions (mundane included), all elixirs, all 137
  scrolls, special arrows, coatings, grenades.
- **Alchemy**: 64 recipes (potions/elixirs/grenades/coatings) from the wiki's
  Alchemy page; all 68 ingredients mapped to their extract; first (earliest-act)
  vendor per ingredient from the pages' "Sold by" text; 64 extract families.
- Pipeline additions: `fetch_consumables.py` (category members + page cache),
  `parse_consumables.py` (structured records), `build_alchemy.py`,
  `build_consumables.py`; shared `locations.py` act map (reuses the item
  LOC_ACTS + consumables-only overrides such as High Hall -> Act Three).
- Deliverables: `knowledge_base/consumables/` -> `potions_elixirs.md`,
  `scrolls.md`, `arrows_coatings_grenades.md`, `alchemy.md`, `camp_supplies.md`;
  masters in `data/consumables.json`, `data/alchemy_recipes.json`,
  `data/ingredients.json`.
- Design goal met in both parts: an AI can browse by slot/type/act/effect
  keywords without knowing item names.

### Part 3 — Character reference (Phase 2 first tranche)
- **Feats** (41, the full wiki list): description, per-power breakdown, notes.
- **Conditions glossary** (135 curated core): effects, sources (what applies
  the condition), notes. Curated set in `scripts/reference_data.py`
  (`CURATED_CONDITIONS`); seed resolved against the wiki Conditions category
  into `data/condition_seed.json`. Two page layouts handled (effects table vs
  tooltip box); stack tables filtered to the condition itself.
- **Permanent buffs** (30 across Acts One/Two/Three): effect + how to unlock,
  parsed from the wiki's Permanent bonuses page.
- **Companions** (11): role, race/subrace, class/subclass, background, hometown,
  starting stats, personal quest, recruitment (act + text), leaving conditions,
  romance summary; plus the 12 hirelings and permanent-removal notes.
  `ACT_OVERRIDES` covers Karlach (page omits the act; unambiguous Act One).
- Pipeline: `fetch_reference.py` (page cache in `data/raw_html_ref/`),
  `build_feats.py`, `build_conditions.py`, `build_permanent_buffs.py`,
  `build_companions.py`; shared `reference_data.py`. Deliverables:
  `knowledge_base/reference/` -> `feats.md`, `conditions.md`,
  `permanent_buffs.md`, `companions.md`; masters in `data/feats.json`,
  `data/conditions.json`, `data/permanent_buffs.json`, `data/companions.json`.

### Part 4 — Phase 2 remainder (classes, races, backgrounds, illithid powers)
- **Classes + subclasses** (12 classes, 58 subclasses): per-class role, hit
  points, key abilities, starting/multiclass proficiencies, starting equipment,
  and a one-line "what sets it apart" per subclass (subclass page intro, with
  the "X is one of the subclasses of Y." boilerplate and `[url N]` refs
  stripped). Parent class comes from a curated `SUBCLASS_OF` map.
- **Races** (31 race/subrace entries) parsed from the wiki's Races comparison
  table: base speed (Standard/Fast/Slow), proficiencies and features per race
  and subrace, race-level traits inherited by subraces; the wiki's "+2 any /
  +1 any other" free allocation note and the curated size note (only Halfling
  and Gnome are Small). Dragonborn colours each restate Draconic Ancestry, so
  the per-colour trait replaces the race-level one rather than duplicating it.
- **Backgrounds** (12): the two skill proficiencies each grants plus the page
  intro naming which companions/hirelings start with each background.
- **Illithid powers** (39 in 4 tiers): base power tree (16), Act Three elite
  powers (10), full ceremorphosis (11), other/story powers (2, incl. Awakened);
  each with type, effect and prerequisite (the "Requires" column doubles as act
  availability). Spellcasting-ability note captured.
- New builders: `build_classes.py`, `build_races.py`, `build_backgrounds.py`,
  `build_illithid.py`; shared helpers `heading_html/parse_dl/first_paragraph`
  added to `reference_data.py` (companions builder refactored to use the shared
  `heading_block`; its output is byte-identical). Deliverables in
  `knowledge_base/reference/` and masters `data/{classes,races,backgrounds,illithid_powers}.json`.
- `kb_lookup.py` extended with `class`, `subclass`, `race`, `background`,
  `power` subcommands.

### Part 5 — Phase 3 (achievements, honour mode)
- **Achievements** (54, 29 hidden): name + unlock condition + hidden flag,
  parsed from the wiki's Achievements table. Act/missable flags are not
  invented; the description is the condition. Honour-only Foehammer and
  Tactician's Critical Hit are cross-referenced from `honour_mode.md`.
- **Difficulties / Honour Mode**: parsed from the wiki's Difficulty page
  (Honour Mode redirects there) — Explorer/Balanced/Tactician/Honour/Custom
  descriptions (Legendary Actions, single-save rules incl. the ALT+F4 case,
  death -> Custom-mode vs delete-save, once-only restoration pods, rewards),
  the full 20-setting custom-mode table with per-difficulty defaults
  (colspan-aware parse; setting names from image alt text), and the worked
  enemy-stat example. Mechanics only, no boss guides.
- New builders: `build_achievements.py`, `build_honour_mode.py`; the two pages
  added to `MASTER_PAGES` in `reference_data.py` so `fetch_reference.py` caches
  them. Deliverables: `knowledge_base/reference/achievements.md` +
  `honour_mode.md`; masters `data/achievements.json` + `data/honour_mode.json`.
- `kb_lookup.py` extended with `achievement` and `difficulty` subcommands.

## Validation

- Full pipeline re-run clean end-to-end (cached, no network needed).
- Equipment counts consistent: 225 / 162 / 201 act-file entries; 683 items in
  master; 74 excluded; 0 documented as "acquisition not documented".
- Consumable counts: 305 items in master (39 potions + 44 elixirs + 137 scrolls
  + 28 arrows + 21 coatings + 36 grenades; Elixir of Universal Resistance is
  dual-categorized, counted once). 116 have act(s) from vendor/location
  mentions; 189 marked Act: unknown (sold throughout the game / random loot).
- Alchemy: 64 recipes, 68 ingredients (39 with a first vendor; 29 vendor-free
  = world-loot only), 64 extract families.
- Reference counts: 41 feats, 135 conditions (all with effects), 30 permanent
  buffs, 11 companions + 12 hirelings. Companion stats spot-checked against
  known values (e.g. Astarion 8/17/14/13/13/10, Shadowheart 13/13/14/10/17/8);
  Minthara and The Dark Urge have no documented starting-stat table (omitted
  rather than guessed).
- Phase 2 remainder counts: 12 classes + 58 subclasses (all with descriptions),
  31 race/subrace entries, 12 backgrounds, 39 illithid powers (16 base / 10
  elite / 11 full-ceremorphosis / 2 other). Spot-checked: Barbarian hit points
  12+CON; Warlock spellcasting ability Charisma; Wood Elf speed Fast; Lolth-
  Sworn Drow has Drow Magic; Halfling speed Slow; Sage background -> Gale.
  The reference-pipeline refactor changed nothing in the existing outputs
  (feats/conditions/buffs/companions byte-identical).
- Phase 3 counts: 54 achievements (29 hidden, no dupes), 5 difficulty modes +
  20 custom settings (colspan-aware parse clean). Spot-checked: Foehammer
  "Complete the game in Honour mode."; Honour single-save includes the ALT+F4
  overwrite rule; Tactician grants the Critical Hit achievement; the custom
  settings table expands Ruleset/Single Save/Proficiency Bonus correctly across
  the four difficulty columns.
- Vendor-extraction edge cases handled: "such as/including" phrasing, trailing
  prepositional fragments, "1x –" prefixes, level-gated vendors ("after
  Level 6"), Bixa Root (renamed copy of Mergrass) mapping.
- Spot-checked against game facts: Elixir of Hill Giant Strength (vendors +
  recipe), Potion of Angelic Slumber (multi-act), Arrow of Fire, camp-supply
  merchants (Arron/Okta, Talli, Rivington vendors) verified via wiki List of
  Traders.
- `git diff --check` clean.

## Operational Caveats

- `knowledge_base/*.md`, `data/items.json` and `data/consumables*.json` are
  **generated**; edit source data or scripts and re-run the pipeline, never
  hand-edit output.
- `data/raw_html/` (equipment), `data/raw_html_cons/` (consumables),
  `data/raw_html_ref/` (reference), `data/items_raw/` and
  `data/consumables_raw/` are gitignored regenerable caches. The cache trees
  are kept separate so the pipelines never cross-contaminate.
- The former 56 "acquisition not documented" equipment items were reviewed with
  the user (an experienced player, who recognized none of them) and moved to
  `EXCLUDED` in `classify_missing.py` as not obtainable in the current game;
  bg3.wiki's own notes flag 14 of them as cut/unfinished/replaced content. 29
  alchemy ingredients still have no documented vendor (world-loot only).
- Consumable acts derive from vendor/location text; many consumables are
  genuinely sold throughout the game, hence "Act: unknown".
- Not covered: dyes, toolkits, quest items, barrels, food items individually.
- bg3.wiki content is CC BY-NC-SA 4.0 / CC BY-SA 4.0 dual-licensed; attribution
  is in `README.md`.

## Natural Next Action

1. All repo work is committed; the user runs their `push` script when convenient.
2. Phase 4 (merchant catalog, quest index) only if the source lists prove
   insufficient.