# Session Continuity Note — Field Guides & Week 31

*Written 2026-07-23. Assume the next session knows nothing about the conversation that produced this.*

Branch: **`claude/eager-jang-5baf4c`** (pushed to `origin`, fully synced). This branch is **1 commit behind and 17 ahead of `origin/main`** — that is expected, see "Branch state" below.

---

## What this session was doing

Two threads, both about **cultural field guides** and **Week 31**:

1. Verifying, fixing, and publish-prepping the three unpublished ancient field guides (Achaemenid, Assyria, Babylon).
2. Drafting Week 31 (Ezra 1; 3–7; Nehemiah 2; 4–6; 8, "I Am Doing a Great Work").

---

## FINISHED

### Achaemenid field guide (`content/culture/ancient/achaemenid/`, 11 pages)
- Full content-verification pass done. ~14 corrections applied (dates, misattributed scripture, broken/wrong external links, one overclaim softened).
- **All 11 pages flipped to `draft: false`** — i.e. publish-ready.
- Interactive **era-map** added to `02-timeline-and-kings.md` (`data-start-era="500"`), verified rendering.
- ⚠️ **DO NOT MERGE THIS BRANCH TO `main` AS-IS.** Achaemenid cross-links 6 Babylon pages that are still `draft: true`. Kym's decision: **Achaemenid and Babylon ship together.** Publishing Achaemenid alone produces dead links.

### Assyria field guide (`content/culture/ancient/assyria/`, 12 pages)
Content-verification pass done (5 parallel agents). All findings applied:
- **12 broken Nahum links** — wrong Blue Letter Bible book code `nam/` (404) → `nah/`. Files 01, 02, 03, 04, 09, 10.
- **3 Livius URL fixes** — `place/assur-city/`→`place/assur/` (04); `place/nineveh/`→`place/nineveh-mosul/` (09, 10); `person/sennacherib/` (404) → `sources/content/anet/287-the-sennacherib-prism/` (08).
- **2 scripture misquotes** — 2 Kings 17:6 "unto"→"into" Assyria (09); 2 Kings 19:33 paraphrase → verbatim "by the way that he came, by the same shall he return" (08).
- **1 missing citation** — verbatim Isaiah 22:10 quote had no reference; link added (08).
- **Date consistency** — Esarhaddon `680`→`681` in two spots on page 02, to match the page's own prose.
- **1 overclaim removed** — Livius/Samaria link on page 07 claimed "translated excerpts of Sargon II's annals"; the linked page has none.
- **era-map added** to `02-timeline-and-empire.md` (`data-start-era="700"`), verified rendering.
- Agents confirmed clean: ~30 verbatim scripture quotes, all major historical claims, and the Genesis/Gilgamesh section (does not overclaim dependence either direction).
- **All 12 pages flipped to `draft: false`** — publish-ready.
- ⚠️ Assyria carries the **same Babylon dependency as Achaemenid**. It cross-links 3 still-draft Babylon pages:
  - `01-the-assyrian-heartland.md` → `babylon/01-the-land-between-the-rivers/`
  - `04-religion-and-the-god-ashur.md` → `babylon/04-religion-and-mythology/`
  - `09-assyria-and-the-bible.md` → `babylon/08-babylon-and-the-bible/`
  Publishing Assyria before Babylon produces 3 dead links.

### Other finished work
- **H6965 lexicon bug fixed** — `static/data/lexicon-popups.json`: the `original` field for H6965 was קוֹלָיָה (Kolaiah, which is H6964); corrected to קוּם (qum). The same fix was applied in the `cfm-corner-tools` repo (separate repo, see "Local-only" below).
- **`docs/field-guide-maps-and-images-sourcing.md`** — licensable maps/images sourcing guide (Wikimedia, Met CC0, AWMC, WHE), with a license cheat-sheet. Lives in `docs/`, so Hugo does not build it.
- **`content/weeks/31.md`** — drafted from the 30.md model. `current: false`.

---

## HALF-FINISHED / NOT STARTED

- **Babylon field guide** — Kym was editing this in a *different* session. This session deliberately did not touch Babylon content. Uncommitted Babylon work from that other session was committed here as a clearly-labelled WIP commit so it wouldn't be lost. All 13 pages still `draft: true`.
- **Babylon era-map** — requested but NOT added, to avoid colliding with Kym's other session. It is a 4-line insert; copy the block from `assyria/02-timeline-and-empire.md` and use `data-start-era="600"`.
- **`site-map-widget`** for the guides' "Major Sites" pages — **BLOCKED.** Needs one high-resolution regional base map image per guide, which does not exist yet. Hotspot coordinates are `%`-based and must be calibrated against that image. See `docs/field-guide-maps-and-images-sourcing.md` §A — needs a human pick.
- **Assyria publish-prep** — not done on purpose (see above).
- **Week 31** — `content/weeks/31.md` exists, but the `static/content/week31/` HTML fragments do **not**. Hugo needs BOTH to serve a week page. Week 31 is not servable yet.

---

## Where every artifact lives

| Artifact | Location |
|---|---|
| Achaemenid guide | `content/culture/ancient/achaemenid/` (11 pages, `draft: false`) |
| Assyria guide | `content/culture/ancient/assyria/` (12 pages, `draft: true`) |
| Babylon guide | `content/culture/ancient/babylon/` (13 pages, `draft: true`) |
| Week 31 page | `content/weeks/31.md` |
| Maps/images sourcing guide | `docs/field-guide-maps-and-images-sourcing.md` |
| Lexicon data (H6965 fix) | `static/data/lexicon-popups.json` |
| era-map widget | `static/css/era-map-widget.css`, `static/js/era-map-widget.js`, maps at `static/images/culture/egypt/maps/ane-XXXXbc.svg` |
| Verification helper scripts | `scripts/verification/` (rescued from a temp dir this session) |
| Week 30 (DONE, live) | already on `origin/main` and deployed |

### era-map embed snippet
```html
<link rel="stylesheet" href="/css/era-map-widget.css">
<div class="era-map-widget" data-start-era="700"></div>
<script src="/js/era-map-widget.js"></script>
```
Era values: `500` = Persia, `600` = Babylon, `700` = Assyria.

---

## Branch state — read before merging

- `claude/eager-jang-5baf4c` is **1 behind / 17 ahead** of `origin/main`.
- The one commit `main` has that this branch lacks is the **Week 30 deploy**, which was pushed to `main` from a *different* clean worktree. The local `content/weeks/30.md`, `content/weeks/29.md`, and `static/content/week30/` files are **byte-identical to `origin/main`** — they are safe there, and were intentionally left uncommitted on this branch. Expect them to keep showing as untracked/modified in `git status`; that is not lost work.
- **Deploy trigger:** `.github/workflows/deploy.yml` fires only on push to `main`. Pushing this branch publishes nothing.
- Merging this branch to `main` **would publish BOTH the Achaemenid and Assyria guides** (all `draft: false`) while Babylon is still `draft: true`. Both guides cross-link Babylon pages, so merging early produces **9 dead links** (6 from Achaemenid, 3 from Assyria). **Babylon is the gate: nothing merges to `main` until Babylon is finished and un-drafted.**

---

## Deliberately NOT committed

- `static/data/lexicon-popups.json.bak-h6965` — a backup artifact of the lexicon fix. Safe to delete once the fix is confirmed good.
- `static/abtest/` — 37 audio A/B-test MP3s belonging to the narration system, which Kym is developing in a separate session. Binaries; do not put in git. They remain on disk.
- `content/weeks/30.md`, `content/weeks/29.md`, `static/content/week30/` — identical to `origin/main`, already safe there.

---

## Staging pipeline (branch `claude/staging-pipeline`)

A 4-stage production pipeline was added so weeks and guides can be built weeks ahead.
Full write-up: **`docs/staging-pipeline.md`**. Short version:

- `draft:` is the hard public gate; `stage:` is the pipeline position
  (`drafting` → `review` → `ready` → `live`). No `stage` = `live`, so existing content is unaffected.
- `/pipeline/` is a staging-only dashboard listing everything in flight with its blockers.
- Verified: a production build emits **0 pages and 0 sitemap entries** for all three staged
  guides and no `/pipeline/`; the staging build shows everything.

**This also fixed a real leak.** Achaemenid and Assyria had been set `draft: false`, which
rendered **22 pages at public URLs and added them to `sitemap.xml`** even though their listing
cards were hidden. *Hiding a card does not hide a page.* Both are now `draft: true` at
`stage: ready`. They go `draft: false` only when all three guides ship together.

### ⚠️ Cloudflare previews are NOT actually set up
`scripts/deploy-preview.sh` and `scripts/cf-pages-build.sh` exist and are correct, but the
Cloudflare side was never stood up: `wrangler` is not installed, there is no auth state, and
both `cfm-corner-previews.pages.dev` and the branch alias return **404**. Until someone runs
the one-time interactive `npx wrangler login` and creates the Pages project, the only staging
surface is **local** (`hugo server -D`). Everything in the pipeline still works locally.

### Two active branches
- `claude/eager-jang-5baf4c` — field-guide verification work (Achaemenid, Assyria, Week 31)
- `claude/staging-pipeline` — branched from the above; adds the staging system **and** the
  draft-leak fix. This is the newer branch and contains everything.

---

## Narration script location — CONVENTION (decided 2026-07-26)

Narration scripts live in **both** places, kept in sync:
- **Vault** (canonical): `~/Obsidian/K Master Vault/.../Culture/<Guide>/_narration/<slug>.script.md`
- **Repo**: `docs/narration/<guide>/<slug>.script.md`

The vault is where the Narration Studio run reads from; the repo copy is for easy find/edit
(e.g. github.dev from a phone). Edit one, update the other. 05b lives on the calendar branch
(PR #2) in the repo until that PR merges.

## Narration (added 2026-07-23)

**Babylon audio: 11 of 12 sections live.** Sections 06-10 were pulled from the
Narration Studio and wired in this session. Only `05b-the-calendar-and-the-names-of-time`
has no episode yet.

> **Encoding matters.** Studio exports are 160 kbps; the published files are
> **mono / 48 kHz / 64 kbps**. Always re-encode before installing:
> `ffmpeg -nostdin -v error -y -i <master>.mp3 -ac 1 -ar 48000 -b:a 64k -map_metadata -1 <dest>.mp3`
> The destination filename **must equal the page's markdown filename** — studio
> episode names are looser (e.g. `babylon-08-babylon-the-bible` -> `08-babylon-and-the-bible.mp3`).

**21 narration scripts drafted** for Achaemenid (10) and Assyria (11), matching the
Babylon format. They live in the **Obsidian vault**, not this repo:
`~/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Culture/<Guide>/_narration/`
Committed and pushed to the private `KymBrock/K_Master_Vault` repo.

**Not yet human-reviewed and not yet recorded.** To produce the audio, see
**`docs/narration-studio-run.md`** — it holds a ready-to-paste prompt for a new
Claude Code session **on the Mac** (the Studio is local-only), plus the outstanding
human-review items.

**Lexicon:** `~/Developer/narration-studio/lexicon.json` went 27 -> 154 entries with all
the Persian/Assyrian terms and KJV traps (`cieled` = "seeld"). Committed and pushed to
that repo's `origin/main`.

## Assyria guide artwork (added 2026-07-23)

**All 23 images complete** — 11 section heroes, 11 icons, and the guide banner, in
`static/images/culture/assyria/` (63 MB). Generated to prompts in
**`docs/assyria-image-prompts.md`**, which also documents the paper-cut style and the
Assyrian-vs-Babylonian accuracy notes.

Known cosmetic issues, all accepted rather than fixed:
- `02-hero` and `09-hero` show **blue glazed brick gates** — Ishtar Gate vocabulary,
  which is Babylonian, not Assyrian.
- `05-icon` renders photorealistically where the other ten icons are flat paper-cut.
- Style varies between flatter (01, 06, 08, 11) and denser (02-05) heroes.

**Assyria pages 02 and 03 have listen players pointing at audio that does not exist**
(404 on the preview). Deliberately left in place pending recording.

## Working files organized (2026-07-23)

The Perforce-workspace folder `.../Animation Studio References/To be named and Organized/`
went from 38 items to empty. Everything was filed into `CFM Corner Field Guides/`,
`Chroma-Keys repo communication/`, and `7 Moedim/Visual Assets/`, with every move logged
line-by-line in `ORGANIZED-LOG.txt` in that folder (format: `NEW PATH <<< ORIGINAL NAME`).
Two verified byte-identical duplicates are quarantined in
`_VERIFIED-DUPLICATES-safe-to-delete/` with a README naming each original — deletion left
to Kym.

## LOCAL-ONLY — exists only on this Mac, unreachable remotely

Nothing below is in git or on GitHub. Do not assume it is available from another machine.

| Thing | Location / port | Notes |
|---|---|---|
| Obsidian **K Master Vault** | `~/Obsidian/K Master Vault/` | All lesson source markdown, weekly research, planning maps |
| Obsidian **Sacred Texts** vault | `~/Obsidian/Sacred Texts/` | LDS canon, Talmud, Midrash, Targumim, conference talks |
| Scripture verification DB | `~/Developer/POM-Beta-Reader-main/data/scriptures_complete.json` | Used by `scripts/verification/verse.py` for verbatim checks |
| **Narration Studio** | `localhost:8770` (Python) | Kym's local voice-clone app. Running as of this note |
| **Ollama** | `localhost:11434` | Local model host, used for video distillation |
| Hugo drafts preview | `localhost:1315` (`hugo server -D`) | Only server that renders `draft: true` pages |
| Hugo normal preview | `localhost:1314` | Not running as of this note |
| `cfm-corner-tools` repo | `~/Developer/cfm-corner-tools` | **Separate repo**, own GitHub remote |
| `static/abtest/` | in this repo, untracked | 37 narration A/B-test MP3s. Binaries — keep out of git |
| A post-commit hook | writes to `~/Obsidian/K Master Vault/Tools/Developer/CODE_INDEX_AUTO.md` | Fires on every commit in these repos |

### `cfm-corner-tools` state
On `main`, synced with its remote. The H6965 lexicon fix **is committed and pushed** there.
**45 other entries remain uncommitted** in that repo — in-progress work from other sessions
(converters, ingesters, generators) plus generated artifacts (`public/`, `.hugo_build.lock`,
`*.bak-*`, `.session-checkpoints/`). They were deliberately left alone: they were not authored
or reviewed by this session, and Kym's standing preference for that repo is to commit only
her data files. They are safe on disk but are **not backed up to GitHub.**

---

## Published artifacts

This session published **no** artifacts. (Artifacts from other sessions exist on
claude.ai; to update any artifact later you must pass its URL, or a new one is minted.)

---

## Known constraints carried into this session

- **Never batch-regenerate week HTML** (see `CLAUDE.md`). Pre-commit hook blocks any commit touching >5 `content/week` files.
- **Content integrity:** nothing may be fabricated. Every claim needs a verified source; flag rather than invent.
- **Do not touch the narration system** — Kym is developing it separately.
- Weeks 24, 27, 28 `current:` flags must be left alone.
