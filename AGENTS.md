# BG3 Magic Item Knowledge Base

A machine-curated reference for Baldur's Gate 3 magic equipment, built from
bg3.wiki data for use by an AI assistant. See `README.md` for scope, file
guide, and how the AI should use it.

## Start here

- The markdown in `knowledge_base/` is **generated output**. Edit the source
  data or the scripts, then regenerate — never hand-edit the generated files.
- Data provenance and licensing: `README.md` (Source and licensing). All
  content derives from **bg3.wiki** (dual-licensed CC BY-NC-SA 4.0 /
  CC BY-SA 4.0); keep attribution if redistributing.

## Regeneration pipeline

```
python3 scripts/fetch_act_lists.py      # base lists from per-act pages
python3 scripts/fetch_item_pages.py     # raw HTML cache (data/raw_html/)
python3 scripts/parse_item_pages.py     # parse cache -> data/items_raw/
python3 scripts/classify_missing.py     # act assignment -> data/item_acts.json
python3 scripts/build_knowledge_base.py # render markdown + data/items.json

python3 scripts/fetch_consumables.py    # consumable base + page cache
python3 scripts/parse_consumables.py    # parse cache -> data/consumables_raw/
python3 scripts/build_alchemy.py        # alchemy/ingredient data + alchemy.md
python3 scripts/build_consumables.py    # consumables markdown + data/consumables.json

python3 scripts/fetch_reference.py      # reference page cache (feats/conditions/companions/buffs)
python3 scripts/build_feats.py          # feats.md + data/feats.json
python3 scripts/build_conditions.py     # conditions.md + data/conditions.json
python3 scripts/build_permanent_buffs.py # permanent_buffs.md + data/permanent_buffs.json
python3 scripts/build_companions.py     # companions.md + data/companions.json
```

- `data/raw_html/` (equipment), `data/raw_html_cons/` (consumables),
  `data/raw_html_ref/` (reference), `data/items_raw/` and
  `data/consumables_raw/` are gitignored regenerable caches; the tracked JSON
  masters and rendered markdown are the deliverables. Keep the three cache
  trees separate so the pipelines never cross-contaminate.
- Fetches are rate-limited; re-running only downloads what is missing.
- Consumable acts come from vendor/location mentions in item text via
  `scripts/locations.py` (reuses the item pipeline's location->act map; its
  `CONS_EXTRA_LOCS` overrides like "High Hall"->Act Three are consumables-only
  and do not affect the equipment KB).
- The character reference (`scripts/reference_data.py`) has a **curated**
  conditions list and a `ACT_OVERRIDES` map in `build_companions.py`; treat
  both as authoritative manual decisions. It also reads
  `data/condition_seed.json` (written by `fetch_reference.py`) to know which
  condition pages to build.

## Always preserve

- **Accuracy over coverage.** Where the wiki lacks data, keep the item but mark
  it (Act: unknown / "acquisition not documented") rather than guessing.
- bg3.wiki's per-act lists are **incomplete**; `classify_missing.py` recovers
  missing items from the wiki catalog and assigns acts from item-page text.
  Treat its `override` entries as authoritative manual decisions; revise the
  `OVERRIDES` / `STOCK` / `EXCLUDED` sets in that file rather than hardcoding
  acts in the builder.
- Do not commit secrets, API keys, or local-only files. Gitignore, never track
  them.

## Handoff procedure

1. Validate the pipeline end-to-end (see `README.md`); run
   `git diff --check`.
2. Stage only intended files; commit with a concise message.
3. The user pushes manually (do not push).
4. Update `HANDOFF.md` with the verified state and next actions.