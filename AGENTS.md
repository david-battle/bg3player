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
```

- `data/raw_html/` and `data/items_raw/` are gitignored regenerable caches;
  `data/items.json`, `data/items_base.json`, `data/item_acts.json` are tracked.
- Fetches are rate-limited; re-running only downloads what is missing.

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