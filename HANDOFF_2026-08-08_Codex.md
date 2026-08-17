# CFM Corner — Session Handoff for Codex
**Date:** 2026-08-08 · **Prepared by:** Claude (Opus 4.8) · **For:** Codex (next session), Kymber back Monday

This is a complete picture of where CFM Corner stands after this session so you can pick up cold. Read the **Safety Rules** (bottom) before touching any week content.

---

## 0. TL;DR (one paragraph)
This session built and heavily polished a new study-library article ("Reading Job as a Poem"), ran a grammar/proofreading pass across the staged Weeks 32/33/34 study guides + insights + resources, mirrored those fixes back into the Obsidian vault source, fixed a real bug in the Hugo converter (numbered lists were rendering "1. 1. 1."), generated + wired hero/icon images for two poetry articles via the Learning Inspired "Prompt Studio" pipeline, and backed up the two articles into Obsidian. Everything is committed and pushed on the **`claude/week-34` staging branch** (and `main` for the tools repo). Nothing has been **published to production** — that waits for Kymber's explicit go-ahead.

---

## 1. Repos, branches, worktrees (the mental model — read first)
Three git checkouts, two share one `.git` (worktrees):

| Path | Branch | Role |
|---|---|---|
| `~/Developer/cfm-corner-site` | `claude/babylon-calendar-section-03zl57` | Main repo checkout. Currently on the **field-guide / babylon** branch (a *different, parallel* effort — see §8). Has **uncommitted** changes that belong to another session — **do not commit or clean it without asking.** |
| `~/Developer/cfm-week34` | `claude/week-34` | **The CFM staging worktree.** All this session's CFM content work lives here. This is where you work on Weeks 32/33/34 + articles. |
| `~/Developer/cfm-corner-tools` | `main` | Separate repo (github.com/KymBrock/cfm-corner-tools). Converters + video-tracker tooling. **Run via `.venv/bin/python`**, never bare `python3`. |

- **Publish model:** the site publishes from `main` on `cfm-corner-site`. Staged week/article work is done on `claude/week-34` and **cherry-picked to `main`** when Kymber says go. GitHub Actions auto-deploys `main` to `www.cfmcorner.com`.
- `cfm-week34` and `cfm-corner-site` **share the same `.git`**. A past incident wiped the `cfm-week34/.git` link; if worktrees look broken, `git worktree repair` + `git reset --hard HEAD` fixed it. **Always `git push origin claude/week-34` after commits** as off-machine backup.

---

## 2. Staging / preview platforms

### Hugo preview servers (local)
Defined in `~/Developer/cfm-corner-site/.claude/launch.json`. Start via the preview tool, not raw Bash.

| Name | Port | Source | Notes |
|---|---|---|---|
| `hugo-week34-staging` | **1327** | `cfm-week34` (`-D` drafts) | **The one to use** — serves the staged Weeks 32/33/34 + articles |
| `hugo-weekly-preview` | 1314 | `cfm-corner-site` | other session |
| `hugo-drafts-preview` | 1315 | `cfm-corner-site` | other session |

- **CRITICAL:** Hugo caches `static/` files at build time. **After editing anything in `static/content/` or adding images to `static/images/`, restart the server** (stop + start `hugo-week34-staging`) or the change won't show. `content/*.md` changes hot-reload fine.
- Verify article images actually serve with `curl -s -o /dev/null -w "%{http_code}" http://localhost:1327/images/articles/<slug>/icon-<slug>.png` (expect 200).

### Learning Inspired Studios (image/prompt tooling, on Tailscale)
Canonical doc: **`~/Developer/li-vectorizer/STUDIOS.md`** (read it). Mac Studio, Tailnet IP **100.110.3.21**.

| Studio | Port | What |
|---|---|---|
| Studios hub | 5090 | launcher (`http://100.110.3.21:5090`) |
| Prompt Studio | 5079 | compose/stage AI image prompts (read-only viewer of prompt docs) |
| Vexel Studio | 5077 | upscale (Real-ESRGAN) + vectorize (VTracer) art |
| Storyboard | 5080 / AppBoard 5081 / Narration 8770 | (other projects — **don't touch Narration**) |

- Studios **bind the Tailnet IP**, so `localhost:<port>` reads them as offline — always probe `http://100.110.3.21:<port>/`.
- **I restarted Prompt Studio this session** to watch the whole Moedim vault root (was scoped to `Moedim_Series/05_AI_Prompts`), so it now sees both Moedim and CFM prompt docs. Launch pattern:
  ```bash
  cd ~/Developer/li-vectorizer && caffeinate -s .venv/bin/python src/prompt_studio.py \
    -i "/Users/kymberbrockbank/Obsidian/Moedim Animation Studio" --host 100.110.3.21 --port 5079 --no-open
  ```

---

## 3. What was accomplished this session

### 3a. New article — "Reading Job as a Poem"
`cfm-week34/content/study-library/articles/reading-job-as-a-poem.md` (created + iterated in ~15 commits, `6237704`→`35e59ad`). A general-audience on-ramp to Hebrew poetry before the Psalms. Final shape:
- **Five numbered "skills," each named for its real device** (Kymber insisted on actual literary terms): **1 Parallelism** (two-beat line; synonymous/antithetic/synthetic), **2 Leitwort** (repeated key word — Job's "know"/*yada*), **3 Anaphora** (the whirlwind's repeated "Who…?"), **4 Antithesis** (Job 19 estrangement→Kinsman, with a "vs." figure), **5 Semantic field** (Job 13 courtroom vocabulary).
- **Hover term-definitions** via the site's popup layer (`data-ref` + `data-popup-kind="source"` + `data-popup-text`) on: prose, prologue, epilogue, lament, wisdom literature, parallelism, synonymous, antithetic, synthetic, Leitwort, anaphora, antithesis, semantic field.
- Interactive widget `<div class="poetry-map-widget" data-set="job">` — the `job` POEM_SET was added to `cfm-week34/static/js/poetry-map-widget.js` (English-line maps; a Hebrew per-word layer is **deferred** until Kymber exports OSHB tags from the TH scanner).
- All content-integrity-safe: KJV text, standard literary terms, **no hand-authored Hebrew from memory**. Removed all mentions of the (unpublished) "Scripture Poetry Analyzer."
- Companion article already existed: `how-hebrew-poems-are-built.md` (Psalms primer).

### 3b. Grammar / proofreading pass (staged Weeks 32/33/34)
Kymber flagged an agreement error and asked for a full pass **including the study guides**. Ran 7 read-only proofreader passes (one per file), applied only genuine fixes, **targeted edits only — never regenerated**, verified each byte-intact on scripture/Hebrew/links/refs. Fixes:
- **Week 32** (`d4dee2c`): "…its reading…**is**→**are** treated"; "What **does**→**do** her patience and timing teach". Insights: "Johnson **names**→**named**"; "they→**both** pray". Plus list-numbering fix (`4fbcd6c`, see 3d) and "friends turned prosecutor→**prosecutors**" (`4798fbd`).
- **Week 33** (`a612ed6`): "one tradition **attributes**→**attributed**"; "first-hand→**firsthand**".
- **Week 34** (`bac0119`): "roughly **half**→**a third** the Psalter is lament" — this one is **factual, not grammar** (three other spots said "a third"); I aligned the outlier. **Kymber still needs to confirm the correct figure against her source** — one-word revert if "half" was right.
- The Job article itself also got a grammar pass (`24224ac`), independently re-proofread clean.

### 3c. Vault source sync
The staged fixes were made to the generated `static/content/weekNN/*.html` fragments. I mirrored the same corrections back into the **vault Markdown source** so a future regeneration won't undo them:
`~/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_{32,33,34}_*/…` (Study_Guide + Weekly_Insights files). Vault edits are **not** committed anywhere (Obsidian syncs on its own).

### 3d. Converter bug fix (cfm-corner-tools, `5bcf2ea` on main, pushed)
`converters/hugo_converter.py` — both markdown parsers (`_md_to_html_block` for study guides, `_insights_body_html` for insights) closed the open list on **any blank line**, so a numbered list with blank lines between items produced a separate `<ol>` per item → every list restarted at "1." Fix: on a blank line inside a list, look past the blank run; if the next content line is a same-type list item, keep the list open ("loose list"). Unit-tested (loose/tight ol, loose ul, list+heading stays split, list+paragraph closes) + verified against the real Week 32 list. **This means regenerating any week no longer reintroduces the numbering bug.**

### 3e. Article images pipeline (LI Studios)
- **How article images work (no frontmatter):** the study-library card template (`themes/cfm/layouts/study-library/list.html`) auto-detects `static/images/articles/<slug>/icon-<slug>.png` via `fileExists`; the single template (`study-library/single.html`) uses `hero-<slug>.png`. Just drop the PNGs in and restart Hugo.
- **Prompt doc authored:** `~/Obsidian/Moedim Animation Studio/01_Projects/CFM_Corner_Assets/04_Prompts/Study_Library_Articles_Poetry_Pair_Hero_Icon_Prompts.md` — in the **current Prompt Studio parser format** (`## N. Title` + `` Slug: `slug` `` + `### Hero Prompt` / `### Icon Prompt`, plain text, no fences). Built on the **locked house style** (layered paper-cut; palette wheat-gold #d4a53e / clay #b1542f / cream #f5e6cc / sage #466758; no text/photorealism), grounded in each article's content.
  - NOTE: the older master plan `…/04_Prompts/Study_Library_Articles_Hero_Icon_Prompt_Plan.md` (10 already-imaged articles) uses the **pre-update `## Hero Prompt` headings**, so the current parser **skips it**. If regenerating any of those, bump its headings to `### Hero Prompt` / `### Icon Prompt`.
- **Images generated + wired (`35e59ad`):** hero + icon for **reading-job-as-a-poem** and **how-hebrew-poems-are-built**, placed in `cfm-week34/static/images/articles/<slug>/`, web-optimized (~960 KB each; full-res masters in Perforce). Verified: icons render on the Articles cards, heroes render on the article headers.

### 3f. Obsidian backups
Copied the two article `.md` files (reference/backup) to:
`~/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Study_Library_Articles/`
These are **Hugo-format** (front matter + inline HTML widgets). Snapshot only — re-copy if the repo versions change. Kymber may want the **other ~15 articles** backed up too (offered, not done).

---

## 4. Where everything lives (quick map, all under `cfm-week34/`)
- Week landing pages: `content/weeks/NN.md` (frontmatter + `charts:` list + `current`/`draft`/`stage`)
- Week fragments (hand-crafted, **never batch-regenerate**): `static/content/weekNN/{study-guide,insights,resources}.html`
- Study-library articles: `content/study-library/articles/<slug>.md`
- Article images: `static/images/articles/<slug>/{icon,hero}-<slug>.png`
- Poetry widget: `static/js/poetry-map-widget.js` (+ `static/css/poetry-map-widget.css`)
- Templates/theme: `themes/cfm/layouts/` (study-library, weeks, `_default/baseof.html`)
- Vault lesson source: `~/Obsidian/K Master Vault/…/CFM Corner/OT_2026/WeeklyLessons/Week_NN_*/`
- Prompt docs: `~/Obsidian/Moedim Animation Studio/01_Projects/CFM_Corner_Assets/04_Prompts/`
- Tools: `~/Developer/cfm-corner-tools/converters/hugo_converter.py`, `scripts/`, `ingesters/`

---

## 5. Policy / documentation / memory updates
- **`STUDIOS.md`** created (by a parallel session) at `~/Developer/li-vectorizer/STUDIOS.md`, committed `e520161` in li-vectorizer — canonical cross-session map of the LI Studios.
- **Project memory** (loads automatically for CFM sessions, at `~/.claude/projects/-Users-kymberbrockbank-Developer-cfm-corner-site/memory/`):
  - `learning-inspired-studios-suite` — the Studios (added by other session)
  - `cfm-study-library-article-images` — **added this session**: article-image filename convention, prompt-folder location, the `###`-heading parser gotcha, workflow.
- `CLAUDE.md` (repo root) — unchanged this session but **authoritative**; see Safety Rules below.

---

## 6. Field guides (parallel effort — context only, NOT touched this session)
There is a separate culture "field guide" effort on the **`claude/babylon-calendar-section` branch** (checked out in `~/Developer/cfm-corner-site`). From project memory (`cfm-culture-field-guides`, `cfm-narration-pipeline`, `between-testaments-guide-handoff`):
- Guides: Assyria / Babylon / Achaemenid, at `content/culture/ancient/{assyria,babylon,achaemenid}/` (+ images under `static/images/culture/…`, audio under `static/audio/culture/…`). **Babylon is the lead**; being upgraded with maps, licensed photos, and widgets (reusable `fg-gallery`, era-map/site-map).
- Narration: culture-guide audio is produced from vault `_narration/*.script.md` via local **Narration Studio (localhost:8770)**, NOT from the HTML. Guide **text** is on `babylon-calendar`; **audio** on `claude/staging-pipeline`.
- A "Between the Testaments" (Persia→Rome intertestamental) guide is in progress in a Comparative Mythologies session; handoff doc in vault `Culture/`.
- The `cfm-corner-site` working tree currently has **uncommitted** changes on this branch (`.claude/launch.json`, `docs/field-guide-maps-and-images-sourcing.md`, untracked `Learning-Inspired-Contractor-Docs/`) plus a **library image-optimization** that a parallel session did there (see §7). **Leave this branch to that session** unless Kymber says otherwise.

---

## 7. Open / pending items & decisions needed
1. **Week 33 (Job) publication** — staged and near-ready but **NOT published**. Publishing = cherry-pick week/article/image files to `main`, set `current: true` on Week 33 + `current: false` on the prior week, verify live. **Only on Kymber's explicit go-ahead.** (Weeks 32 and 34 are also staged/draft.)
2. **"half" vs "a third" Psalter-lament figure** — I changed it to "a third" (fragment + both Week 34 vault source files) for internal consistency; **Kymber to confirm the correct figure**. One-word revert if wrong.
3. **Library image optimization** (parallel session, on `cfm-corner-site`/babylon-calendar, **uncommitted**): 30 article PNGs optimized 82.9 MB→27.5 MB. That session asked Kymber to choose: (a) commit on babylon-calendar → flows to main via merge, (b) revert and re-run the `web_optimize` pass on `week-34` so it ships with Weeks 33/34, or (c) hold. **Kymber's call — not this session's branch.**
4. **Back up remaining ~15 study-library articles** into the vault `Study_Library_Articles/` folder (offered, not done).
5. **Hebrew per-word layer** for the Job poetry widget — deferred until Kymber exports OSHB tags from the TH scanner.
6. **Post-Aug-9 video re-collection** — Week 33 video tracker may have stragglers to re-collect + distill, then regenerate `week33/resources.html`. Week 34 `insights.html` + `resources.html` are **not yet generated** (only `study-guide.html` exists).
7. **Vault↔fragment divergence** — grammar fixes are synced now, but any future direct fragment edits should be mirrored back to the vault source (or made in the vault + regenerated).

---

## 8. How to resume (commands)
```bash
# Start/refresh the CFM staging preview (use the preview tool, not raw bash, in Claude)
#   name: hugo-week34-staging  → http://localhost:1327
# After ANY static/ change, RESTART it (stop+start), don't just reload.

# Run the tools repo under its venv (NEVER bare python3):
cd ~/Developer/cfm-corner-tools && .venv/bin/python -m converters.hugo_converter --help

# Confirm article images serve:
for s in reading-job-as-a-poem how-hebrew-poems-are-built; do for k in icon hero; do
  curl -s -o /dev/null -w "$k-$s %{http_code}\n" http://localhost:1327/images/articles/$s/$k-$s.png; done; done

# Prompt Studio (image prompts) — see §2 launch line; docs at :5079/docs, parse at :5079/doc?path=
```

---

## 9. ⛔ Safety rules (from CLAUDE.md — do not violate)
- **NEVER batch-regenerate weekly lesson HTML.** `static/content/weekNN/` files are hand-crafted. Targeted single-file edits only. A pre-commit hook blocks commits touching >5 week files; the manual rule is ≤3 week files/commit without explicit approval.
- **Content integrity is absolute:** nothing fabricated/inferred/from training data. Every claim sourced from scripture, approved vault files, processed transcripts, verified conference talks, or approved Hebrew-grammar references. Flag unverified with placeholders. **Never hand-author pointed Hebrew from memory.**
- **Writing voice:** accessible general-LDS, clear and concise, not academic. Explain Biblical/Jewish terms plainly. Link every scripture (with normalized `data-ref`) and every Hebrew term to its lexicon/source.
- **Never cite Wikipedia** — use it only to find the primary source, then link that.
- **Don't flip `current:` flags** except as a deliberate deployment step with Kymber's go.
- **Always `git diff` and review before committing; show the diff.** Push to origin after committing (backup).
- **POM ↔ CFM firewall:** keep the "Parable of Music" project entirely out of CFM.

*End of handoff.*
