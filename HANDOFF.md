# Handoff

## Verified State

- Branch `main`; pushed to `origin` (https://github.com/david-battle/bg3player,
  public). Upstream is set, so the user's `push` script (plain `git push` per
  repo) works — the user runs it, not the assistant.
- Worktree has uncommitted changes (Phase 2 first tranche: reference KB) — not
  yet committed as of this handoff's last write; commit + push when convenient.

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

## Validation

- Full pipeline re-run clean end-to-end (cached, no network needed).
- Equipment counts consistent: 225 / 162 / 201 act-file entries; 739 items in
  master; 18 excluded; 56 documented as "acquisition not documented".
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
- 56 equipment items are listed as "acquisition not documented" (bg3.wiki
  lacks the info); the user — an experienced player — may want to fill these in
  by hand. 29 alchemy ingredients have no documented vendor (world-loot only).
- Consumable acts derive from vendor/location text; many consumables are
  genuinely sold throughout the game, hence "Act: unknown".
- Not covered: dyes, toolkits, quest items, barrels, food items individually.
- bg3.wiki content is CC BY-NC-SA 4.0 / CC BY-SA 4.0 dual-licensed; attribution
  is in `README.md`.

## Natural Next Action

1. Commit the Phase 2 first tranche; the user then runs their `push` script.
2. Phase 2 remainder per `PLAN.md`: classes + subclasses (2b), races (2c),
   backgrounds (2e), illithid powers (2g).
3. Phase 3 (achievements, honour mode) — small.
4. Optionally fill in acts/acquisition for the 56 undocumented items
   (`classify_missing.py` `OVERRIDES`).