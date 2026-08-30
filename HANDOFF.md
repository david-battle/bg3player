# Handoff

## Verified State

- Branch `main`; local commits only. Remote `origin` is configured to
  `https://github.com/david-battle/bg3player.git` (added by the assistant); the
  user pushes manually with `git push -u origin main` — `push` is the user's
  script that pushes all their repos, do not run it for them.
- The worktree is clean after this session's commit.

## Completed Work (2026-08-30)

Built a machine-curated **magic equipment** knowledge base for Baldur's Gate 3
from **bg3.wiki** data, in `/home/dlbattle/bg3player`.

- **739 obtainable items** covered (plus 18 not obtainable in the current
  game), including items bg3.wiki's own per-act lists miss (e.g. Balduran's
  Giantslayer, the Helldusk set, Markoheshkir, Helm of Balduran, Orphic Hammer).
- Pipeline (all Python, in `scripts/`): `fetch_act_lists.py` -> base per-act
  lists (588 rows); `fetch_item_pages.py` -> raw HTML cache; `parse_item_pages.py`
  -> structured records; `classify_missing.py` -> act assignment;
  `build_knowledge_base.py` -> markdown + `data/items.json`.
- Deliverables: `knowledge_base/magic_items_by_slot.md` (browse index by gear
  slot + act), per-act detail files with coordinates/acquisition/notes/bugs,
  `magic_items_merchant_stock.md`, `magic_items_undocumented.md`.
- Design goal met: an AI can browse by slot/act/effect keywords without knowing
  item names.

## Validation

- Full pipeline re-run clean end-to-end (cached, no network needed).
- Counts consistent: 225 / 162 / 201 act-file entries; 739 items in master;
  18 excluded; 56 documented as "acquisition not documented".
- Spot-checked known items against game facts (Gloves of Thievery, Ring of
  Protection, Phalar Aluve, Helldusk set, etc.); curated `OVERRIDES`/`STOCK`/
  `EXCLUDED` sets for edge cases (EA-only items, pre-Patch-3 move of the Amulet
  of Elemental Torment, generic +1/+2 trader stock).
- `git diff --check` clean.

## Operational Caveats

- `knowledge_base/*.md` and `data/items.json` are **generated**; edit source
  data or scripts and re-run the pipeline, never hand-edit output.
- `data/raw_html/` and `data/items_raw/` are gitignored regenerable caches.
- 56 items are listed as "acquisition not documented" (bg3.wiki lacks the
  info); the user — an experienced player — may want to fill these in by hand.
- Consumables (potions/scrolls/arrows/elixirs) are **not** covered yet; that is
  the natural next phase.
- bg3.wiki content is CC BY-NC-SA 4.0 / CC BY-SA 4.0 dual-licensed; attribution
  is in `README.md`.

## Natural Next Action

1. The user runs `git push -u origin main` when ready.
2. Optionally fill in acts/acquisition for the 56 undocumented items
   (`classify_missing.py` `OVERRIDES`).
3. Next phase: consumables (potions, scrolls, elixirs, arrows, coatings,
   grenades) as a separate reference.