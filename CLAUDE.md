# Claude Code Safety Rules for cfm-corner-site

## ⚠️ Project scope & firewall — CFM Corner ≠ The Parable of Music

This repo is **CFM Corner** (free, mainstream Come-Follow-Me scripture study, cfmcorner.com).
**The Parable of Music / Alphabet Book** is a **separate, exploratory, premium** project — its
master map is `~/Developer/alphabet-music-study/WHERE-EVERYTHING-IS.md` (read it before any POM
work). Do **NOT** import POM thesis material into CFM: the letter↔constellation mapping, the
`4-1-5-2-6-3-7` pattern, ChromaKeys / the color-key system, the banded "readings," or the
**Parable of Music name/brand** (CFM→POM is *total silence* — no funnel, no credit). Shared
*attested* infrastructure only (Translation Hub dictionaries, standard etymologies,
Proto-Sinaitic script facts, core music theory). Devotional music *metaphor* is author's
discretion; *recovery/origin* claims are not.

⛔ CRITICAL SAFETY RULES — DO NOT VIOLATE ⛔

1. NEVER batch-regenerate weekly lesson HTML files. The files in
   `static/content/week01/` through `week52/` contain hand-crafted content
   that CANNOT be reproduced by any converter or script.

2. NEVER run a converter script against multiple weeks at once.

3. Only make targeted, single-file edits. One file at a time.

4. ALWAYS run `git diff` and show the output BEFORE committing.

5. NEVER commit changes to more than 3 week content files in a
   single commit without explicit approval from Kymber.

6. If a script or tool would modify multiple week files, STOP and
   ask Kymber before proceeding.

**What these rules protect (clarified 2026-08-04):** the danger is overwriting
hand-crafted content that is **already published live**. These rules are NOT a ban
on the normal content pipeline. For a **staged, unpublished week** (`draft: true`,
not yet on the live site), the CORRECT workflow is **source-first**: edit the vault
markdown source (e.g. `…/WeeklyLessons/Week_NN_…/02_Weekly_Insights/*.md`,
`03_Study_Guide/*.md`), regenerate **that one week's** fragments with the converter
(`--week NN --type study-guide|insights|resources`), `git diff`-review, and verify
in the local preview before committing to the week's branch. That keeps the vault
source (the true source of truth) and the generated fragment in sync — hand-editing
a generated fragment silently diverges it from its source, so do it only for a tiny
surgical fix. **Still forbidden:** regenerating to fix/edit an *already-published
(live)* week's fragment (use a surgical anchor edit instead — see the lexicon-
collision note below), and running the converter across multiple weeks at once.

## Published lessons — the linking rule (RULED 2026-08-15)

**Never `--fix` or regenerate a PUBLISHED fragment.** Surgical anchor replacement only —
rewrite the wrong `<a>` and leave every surrounding byte alone. **Staged or unpublished:
`--fix` is fine, scoped to one week** (`--fix --week weekNN`), then scan the rendered page.

*Ruled by Kymber 2026-08-15 (HUB-056), from her own 2026-08-04 line: "Regeneration is fine
— Week 33 isn't published yet." `LEXICON-POPUP-SPEC.md` told sessions the opposite for four
months and was referenced from no CLAUDE.md, so nothing corrected it. `link-audit.py` now
refuses `--fix` on any week present on live `main`; this is the rule the tool enforces.*

**And do not chase zero.** A fully linked week is *not* zero BARE HEBREW — the intentional
divine-name and rabbinic residual is expected. The audit is not a publication gate.

## Violation History

On 2026-02-21, commit `905fdfa` mass-regenerated all weeks 1–9 HTML,
destroying hand-crafted content. This required an emergency revert
(commit `2cfc1a0`). This must never happen again.

## Pre-Commit Hook

A git pre-commit hook blocks any commit touching more than 5 week
content files. Use `--no-verify` ONLY with Kymber's explicit approval.

## Recovery

If disaster strikes, the tag `stable-2026-02-21` marks a known-good state.

---

## Deployment Checklist

When deploying a new week, follow these steps in order:

### Week Front Matter (`content/weeks/NN.md`)
- [ ] Set `current: true` on the **new** week's `.md`
- [ ] Set `current: false` on the **previous** week's `.md`
- [ ] Verify all `charts:` entries match their actual article titles and descriptions
  — title and description must come from the article's own front matter, not be invented
- [ ] Verify chart `url:` paths resolve correctly (e.g., `study-library/articles/slug/`)

### Static Content (`static/content/weekNN/`)
- [ ] Run `link-audit.py` on all three files (study-guide, insights, resources) — zero issues
- [ ] Verify no emojis in any HTML files (monochromatic icons only)
- [ ] Verify all video cards use thumbnail format (never plain text links)
- [ ] Verify every discovered weekly `watch?v=` URL renders as a thumbnail card; channel-homepage fallbacks are only acceptable when no week-specific video was found
- [ ] Use `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Planning/Content_Maps/Church_Media_Video_Map.md` as the authoritative Week-to-Church-Media mapping when OT Stories / Come Learn With Me cards are missing or shifted
- [ ] If the week's `Video_Resources/VIDEO_URL_TRACKER.md` includes a Bible Project section, make the generated Bible Project accordion match that documented weekly list rather than a reduced generator default

### Scripture & Term Link Contract
- Every scripture citation in a touched file must include the full book name and chapter. Never leave bare references like `(3:11)` or partial references like `Nephi 11:4`.
- Every scripture link must include a normalized `data-ref` with the full reference, e.g. `data-ref="Exodus 3:14"` or `data-ref="3 Nephi 11:1-17"`.
- If linking to Church or BLB scripture pages, always add `data-ref` so the popup system can resolve the reference.
- For chapter-only references such as `Exodus 3`, use the full book + chapter in `data-ref`; do not rely on shorthand.
- Do not invent glossary/term links. If a term is not in the approved glossary data, leave it plain or flag it for glossary expansion rather than fabricating a popup.
- Plain transliterations that function as term notes or glosses should not be left floating when a source link exists nearby. Link them either to the verified lexicon/source entry or to the specific source passage being discussed.
- **Link the transliteration, never the pointed Hebrew script.** The lexicon auto-linker attaches the popup to the *transliteration* (e.g. `torah`), leaving the vocalized script (תּוֹרָה) bare so niqqud stays legible. Many "bare Hebrew" audit hits are therefore correct, not defects.
- **Lexicon collisions & mislinks.** Several Strong's entries can normalize to the same transliteration key (e.g. `torah` → H8451 "law" vs ṭōraḥ H2960 "burden"). The converter now resolves these to the plain-ASCII lemma automatically (`hugo_converter._translit_quality`). If a transliteration still links to the wrong homonym: (1) add/fix an entry in `cfm-corner-tools/data/translit-aliases.json` (`"translit": "H####"`), then (2) for an **already-published** fragment do a **surgical anchor replace** — rewrite only that `<a data-strongs=…>`'s attributes, preserving the inner text. **NEVER regenerate a published fragment to fix a link** (that risks the hand-crafted-content loss in §1). Verify the sense in context first — some collisions are legitimately the other word (e.g. `ba'al` as verb/owner, not the deity).
- Every direct quote from a prophet or apostle in a touched file must link to a verified source. If the exact source cannot be verified, remove the quotation marks and flag it as `[QUOTE SOURCE PENDING VERIFICATION]` rather than leaving an unlinked quote.
- Word studies in touched files must include linked Greek, Latin, and English cognates or close parallels where the format calls for them. Do not leave the Hebrew alone if the word-study pattern expects cross-language parallels.

### Approved Source Locations Before Drafting Quotes or Word Studies
- Sacred Texts vault root: `/Users/kymberbrockbank/Obsidian/Sacred Texts/`
- LDS canon source files for scripture text and verse verification: `/Users/kymberbrockbank/Obsidian/Sacred Texts/01_LDS_Canon/`
- Jewish perspective source lanes: `/Users/kymberbrockbank/Obsidian/Sacred Texts/03_Talmud/Bavli/`, `/Users/kymberbrockbank/Obsidian/Sacred Texts/04_Midrash/Midrash_Rabbah/`, `/Users/kymberbrockbank/Obsidian/Sacred Texts/05_Targumim/`
- Conference talks / prophetic quote source lane: `/Users/kymberbrockbank/Obsidian/Sacred Texts/RESTRICTED/Conference_Talks/`
- OT 2026 lesson markdown source lane: `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/`
- IF research lane: `/Users/kymberbrockbank/Obsidian/K Master Vault/Research Library/Interpreter_Foundation_OT_2026/`
- Video distillation lane: check the week's `Video_Resources/Overviews/` or `Video_Distilled/` material before summarizing videos
### Hugo Preview
- [ ] **Restart the Hugo server** after editing any file in `static/content/` — Hugo's
  `readFile` function caches at build time, so changes to static HTML files are NOT
  visible until the server is restarted
- [ ] Check all tabs load (Study Guide, Insights, Resources, Charts)
- [ ] Check lesson image displays
- [ ] Verify charts are interactive

### Git & Deploy
- [ ] Run `git diff` and review before committing
- [ ] Commit with message format: `Week NN: Scripture Reference`
- [ ] Push to main — GitHub Actions auto-deploys
- [ ] Verify live site at `www.cfmcorner.com/weeks/NN/`

---

## ⛔ CONTENT INTEGRITY — ABSOLUTE RULE ⛔

**NOTHING in any CFM Corner lesson, insight, study guide, or resource may be
fabricated, assumed, inferred, or written from general knowledge.**

Every claim, description, summary, or characterization of content MUST be
sourced from one of the following:

1. **Scripture text** — direct reference to the biblical passage
2. **Vault source files** — study guides, overviews, word studies, or
   other documents in the K Master Vault that Kymber has written or approved
3. **Processed video transcripts** — distilled content in `Video_Distilled/`
   that has been processed through Knowlchemy
4. **Conference talk text** — verified against the actual published talk
   at ChurchofJesusChrist.org before being cited or described
5. **Explicit user instruction** — Kymber has directly provided or
   confirmed the information in the current session
6. **Approved Hebrew grammar references** — the following textbooks are
   approved sources for Hebrew grammatical claims, linguistic terminology,
   and grammatical classifications. When citing, reference the author,
   chapter/section, and page number:

   - **Gesenius' Hebrew Grammar (GKC)** — H.F.W. Gesenius, ed. E. Kautzsch,
     trans. A.E. Cowley. Oxford: Clarendon Press, 2nd English ed. 1910.
     *The universal standard reference grammar for Biblical Hebrew.*
     Vault: `Books/EPUB/Gesenius_Hebrew_Grammar_GKC.pdf`

   - **A Practical Grammar for Classical Hebrew** — J. Weingreen.
     Oxford University Press, 2nd ed. 1959.
     *The standard grammar used in Jewish studies programs and seminaries.*
     Vault: `Books/EPUB/Weingreen_Practical_Grammar_Classical_Hebrew.pdf`

   - **A Grammar for Biblical Hebrew** — William D. Barrick & Irvin A.
     Busenitz. The Master's Seminary, rev. July 2004.
     *Seminary-level grammar with exegetical insights per chapter.*
     Vault: `Books/EPUB/B_B_Hebrew_Grammar_2005.pdf`

   - **Simplified Hebrew Grammar** — Justin T. Alfred. Blue Letter Bible.
     *Accessible introduction hosted by BLB; covers conjunction,
     consecutive, prepositions, article, and verb tenses.*
     Vault: `Books/EPUB/BLB_Simplified_Hebrew_Grammar_Alfred.pdf`

   - **Blue Letter Bible online tools** — blueletterbible.org.
     Lexicon entries, interlinear, and grammar pages are approved sources.

7. **Approved rabbinic primary sources for letter symbolism** — the
   following texts are approved sources for claims about the Jewish
   tradition of finding meaning in Hebrew letter forms. These are
   *midrashic* sources (homily and meditation), NOT grammar references.
   Never conflate them with linguistic analysis.

   - **Babylonian Talmud, Shabbat 104a** — The children's alphabet
     homily. Young students derive moral and symbolic lessons from the
     names, forms, and sequences of the Hebrew letters.
     Sefaria (bilingual): https://www.sefaria.org/Shabbat.104a
     Vault: `Books/EPUB/Shabbat_104a_Letter_Symbolism_Sefaria.md`

   - **Otiyot de-Rabbi Akiva (Alphabet of Rabbi Akiva)** — Post-Talmudic
     midrashic text building extended homilies around each letter. Version 1
     features the letters petitioning God to begin creation.
     Sefaria (Version 1): https://www.sefaria.org/Otzar_Midrashim,_Midrashim_of_Rabbi_Akiba,_Aleph_Bet_of_Rabbi_Akiba_(Version_1)
     Sefaria (Version 2): https://www.sefaria.org/Otzar_Midrashim,_Midrashim_of_Rabbi_Akiba,_Aleph_Bet_of_Rabbi_Akiba_(Version_2)
     Vault: `Books/EPUB/Otiyot_de_Rabbi_Akiva_Sefaria.md`

### What this means in practice:

- **Video descriptions** — NEVER describe what a video "covers" or
  "focuses on" unless the transcript has been processed and is in
  `Video_Distilled/`. If no distillation exists, list the title only
  and direct readers to the Resources tab.

- **Conference talk quotes** — NEVER paraphrase or characterize a talk
  without verifying the actual text. If uncertain, link to the talk
  and let readers read it themselves.

- **Hebrew/Greek claims** — NEVER assert a linguistic meaning, root, or
  connection that is not sourced from BLB, an approved grammar reference,
  a vault word study, or Kymber's direct instruction.

- **Pictographic claims** — The connection between ancient pictographic
  letter forms and grammatical function is Kymber's personal mnemonic
  approach. It is NOT conventional grammar pedagogy. Always present
  pictographic connections as memory aids, never as scholarly consensus.
  The grammar itself (sourced from approved references) is what matters.

- **Historical/cultural claims** — NEVER add "enriching" context that
  comes from training data alone. Source it from vault files or flag it
  as needing verification.

### When in doubt:

Leave a placeholder and flag it explicitly, e.g.:
`[VIDEO SUMMARY PENDING — awaiting Knowlchemy distillation]`
`[QUOTE PENDING VERIFICATION]`

**It is always better to publish less and be accurate than to publish
more and be wrong. Kymber's readers trust this content for scripture
study. That trust must never be violated.**


---

## ⚠️ Known Issues & Hard-Won Lessons (Updated 2026-03-14)

### 1. Worktree Orphan Problem
Claude Code creates `.claude/worktrees/<name>/` directories when using
isolated agents. Content created in these worktrees does NOT automatically
merge to the main working directory. **Before shipping any week, run:**
```bash
# Check all worktrees for content not in main
for wt in .claude/worktrees/*/; do
  name=$(basename "$wt")
  diff -rq "$wt/content/" content/ 2>/dev/null | grep "^Only in $wt"
  diff -rq "$wt/static/" static/ 2>/dev/null | grep "^Only in $wt"
done
```
**History:** On 2026-03-14, the Passover Seder guide (15 pages + images),
Four Cups article, Alma 5 Nephite Seder article, and Hebrew Lesson 11
were all stranded in the `nice-leakey` worktree. Week 12 almost shipped
without them.

### 2. Desktop Commander `read_file` Returns Metadata
The `mcp__desktop-commander__read_file` tool intermittently returns JSON
metadata (`{"fileName":"...","filePath":"...","fileType":"text"}`) instead
of file content. **Workaround:** Always use `cat` via
`mcp__desktop-commander__start_process` for reliable file reads.

### 3. Every New Week MUST Have Both Pieces
Hugo requires TWO things to serve a week page:
- `content/weeks/NN.md` — the Hugo content page with frontmatter
- `static/content/weekNN/` — the generated HTML fragments (study-guide,
  resources, insights)

Missing the `.md` file → 404. Missing the static HTML → empty tabs.

### 4. The `charts:` Section Is NOT Optional
Every `content/weeks/NN.md` must include a `charts:` YAML list linking to
that week's articles, Hebrew lesson, and cultural guides. Without it, the
article cards don't appear on the week page. **Always populate charts from
the actual articles that exist for that week.**

### 5. Do NOT Mutate Previous Weeks Without Permission
The `current: true/false` flag on week pages controls which week shows as
"this week" on the site. **NEVER change a previous week's frontmatter
unless Kymber explicitly asks.** The deployment checklist says to flip
`current`, but that is a DEPLOYMENT step — not a content-generation step.
Only flip flags when actually deploying to production.

### 5a. The directory PROVES third-party — it does not prove original

**Ruled by Kymber 2026-08-15 (CFM-020).** See: `mc-intelligence/locate.py CFM-020`
**The implication runs one way only.** Read both lines:

    <topic>/sourced/ /photos/ /maps/   THIRD-PARTY, ALWAYS — CREDIT sidecar REQUIRED
                                       sound: 0 of 90 are on the NAS

    <topic>/*  (top level)             MOSTLY hers — but NOT proof of origin
                                       435 of 497 are on the NAS; the other 62 are not,
                                       and 10 of those are CC BY-SA or public domain

A `sourced/` path is **sufficient to require** a credit. A top-level path is **not
sufficient to skip** one — `first-temple/cypriot-laver-stand.jpg` sits at top level and is
CC BY-SA 3.0 (Marcus Cyron). **No NAS copy is the flag that a human must look**; 31
top-level images are in that state today with no sidecar.

**TWO sidecar naming conventions exist.** Pre-existing files use `<stem>.CREDIT.txt`;
`backfill_image_credits.py` writes `<filename>.CREDIT.txt`. **Check both** — checking one
undercounts coverage and reports credited images as bare.

Kymber declared the sourced images are mostly AI-sourced and mostly from **Wikimedia
Commons**. That is a **lead for finding each file's source page, not an attribution.**
Commons carries both public-domain and CC-BY-SA works, and CC-BY-SA requires naming the
author and the licence. Writing "Wikimedia Commons" into a credit line would be a
fabricated attribution that happens to look plausible.

### 6. Hugo Static File Caching
Hugo's `readFile` function caches static files at build time. After
editing any file in `static/content/`, you MUST restart the Hugo server
to see changes. Live reload does NOT pick up static file changes.

### 7. macOS Dark Mode vs Tkinter (RESOLVED 2026-07-29)
Fixed and launch-tested — the GUI renders legibly in macOS dark mode
(cfm-corner-tools commit `11cc697`). The root cause was **global ttk style
overrides**:
- `style.configure(".", ...)` — overrides ALL widget colors, causes invisibility
- `style.map(".", ...)` — same problem
- `tk_setPalette()` — no effect on ttk, confuses widget rendering

The fix in `hugo_gui.py`:
- Forces the `clam` theme (`s.theme_use('clam')`) — macOS `aqua` ignores ttk
  background colors and goes unreadable in dark mode; `clam` respects them.
- Uses ONLY named styles (`CFM.TFrame`, `CFM.TLabel`, `CFM.TButton`, …) plus a
  hardcoded CFM palette — NEVER the global `style.configure(".", ...)`.
- Adds a custom `MacButton` canvas widget for colored, legible action buttons.

⚠️ Do NOT reintroduce a global `style.configure(".", ...)` / `style.map(".", ...)`
/ `tk_setPalette()` — that is exactly what broke the six prior attempts. The GUI
is now the recommended way to generate content.

---

## 🖼 IMAGE CREDIT — capture it when you take the image, not later

**When you pull an image from a Church source, record the credit the Church
publishes with it, in the same commit.**

Church materials — the Come, Follow Me manual, the Gospel Media Library, the
Gospel Library app — list the artist and title alongside their images. That
information is available at the moment you take the file and is expensive to
reconstruct afterwards. **Capture it then.**

    artist:   the credited artist, exactly as the Church lists them
    title:    the work's title as given
    source:   which Church resource it came from, with the URL
    retrieved: the date

Record it in the page's front matter or the accompanying sources file, next to
the image reference.

**Why this rule exists.** Textual sources have been cited carefully — see
`data/tabernacle/tabernacle_sources.yaml`, which records author, work, citation,
tier and status per claim. Images have had no equivalent, and Church-sourced
images across the site carry no attribution at all. Kymber flagged this on
2026-08-15: *"we have not been on the ball about crediting the sources we get
from the church… They have those sources listed with the images that we pull."*

**This is a credit obligation, not a licensing one.** The Church permits
non-commercial use and CFM Corner is free, so the right to use the image is not
in question. What is missing is naming the artist — and an artist named on the
Church's own page and unnamed on ours is a gap we introduced.

**Do not retro-fit by guessing.** If an existing image's origin is unknown, mark
it unknown and leave it for the provenance audit. A confidently wrong attribution
is worse than an absent one.

> **RESCUED TO main 2026-08-22.** This section was committed on 2026-08-15 as `58c91e2` and
> lived on `claude/babylon-calendar-section-03zl57` and nowhere else — `git branch --contains`
> returned only that branch. A squash-merge or a branch deletion would have taken it, and it is
> the governing rule for a 59-file image-credit queue that fieldguide is holding. Found by
> fieldguide on 2026-08-22 when it was woken and read its own standing rules.
>
> **It is the other half of §5a above.** Both were ruled by Kymber on 2026-08-15: §5a (CFM-020)
> says WHEN a credit is required — the directory proves third-party. This says HOW and WHEN to
> capture it, and not to guess. One day's ruling, split across a branch boundary, with half of
> it invisible to every session working on main for a week.

## Weekly Content Generation Workflow

### Step-by-step for each new week:

1. **Generate content** — the GUI (`python3 converters/hugo_gui.py`) now renders
   correctly in dark mode (fixed 2026-07-29, see §7) and is the recommended path.
   The CLI is equivalent:
   ```bash
   cd /path/to/cfm-corner-tools
   python3 -m converters.hugo_converter --week NN --type resources
   python3 -m converters.hugo_converter --week NN --type study-guide
   python3 -m converters.hugo_converter --week NN --type insights
   ```

2. **Audit worktrees** for any orphaned content (see §1 above)

3. **Create `content/weeks/NN.md`** with:
   - Full frontmatter (title, scripture, dates, week_num, weight, etc.)
   - `charts:` section linking all articles, Hebrew lessons, cultural guides
   - `current: true`

4. **Verify in Hugo dev server:**
   ```bash
   hugo server --port 1326
   # Check http://localhost:1326/weeks/NN/
   # NOTE: Port 1326 matches HUGO_PORT in hugo_gui.py (line 32)
   # Verify all tabs, article cards, images load
   ```

5. **Run link audit** on all generated HTML files

6. **Only when deploying to production:** flip previous week's `current`
   flag to `false` and commit everything together

---

## Staging & Deployment Surfaces

Two surfaces serve this site. Canonical detail lives in `docs/staging-pipeline.md`
(the staging flag model) and `docs/working-remotely.md` (Cloudflare previews +
Hugo version pinning). This section is the quick map that ties them together.

### Production — GitHub Pages (NOT Cloudflare)
- Built + deployed by `.github/workflows/deploy.yml` on every push to **`main`**
  (and `workflow_dispatch`). Build: `hugo --minify --baseURL "https://www.cfmcorner.com/"`
  → `./public`, then a Pagefind search index. Hugo pinned to **0.156.0**.
- Live URL: **https://www.cfmcorner.com/** (custom domain via `static/CNAME`).
- Pre-build guard `scripts/check-staging.sh` **fails CI** if any non-live page is
  missing `draft: true` — a half-finished week cannot leak to production.
- **Only `main` deploys to production.** Never commit staged/in-progress week
  content straight to `main`; work on a branch (worktree convention below).

### Previews — Cloudflare Pages (staging only, never production)
- Project **`cfm-corner-previews`**, Git-connected through the Cloudflare
  dashboard. There is **no `wrangler.toml` in the repo** — the project config is
  dashboard-only. Dashboard build command: `sh scripts/cf-pages-build.sh`,
  output `public`, `HUGO_VERSION = 0.156.0`.
- Every branch push auto-builds a preview at
  **`https://<branch-alias>.cfm-corner-previews.pages.dev/`**
  (branch-alias = branch name lowercased, `/` and `_` → `-`, capped 28 chars).
- `cf-pages-build.sh` builds **with drafts** (`hugo -D --config hugo.toml,config-preview.toml`)
  for any non-`main` branch, and a **draft-free production mirror** for `main`
  (smoke test). Every `*.pages.dev` build is **noindexed** (robots + `X-Robots-Tag`).
- Manual one-off preview: `sh scripts/deploy-preview.sh` (wraps
  `npx wrangler pages deploy public --project-name cfm-corner-previews --branch <branch>`;
  needs a one-time `npx wrangler login`).

### Local preview (`.claude/launch.json`)
- **1314** — `hugo-weekly-preview` (no drafts, production-like).
- **1315** — `hugo-drafts-preview` (`hugo server -D`; shows drafts + stage badges
  + `/pipeline/`). **Use this to review a staged week.**
- **1326** — `hugo-gui-converter` (matches `HUGO_PORT` in `hugo_gui.py`).
- Reminder (§6): restart the server after editing any `static/content/` file —
  Hugo's `readFile` caches those at build time and live-reload won't pick them up.

### Staging flags — two gates (full detail in `docs/staging-pipeline.md`)
- `draft:` is the **hard gate**: `draft: true` = not built for production at all.
  This is the only flag that actually keeps a page off the live site.
- `stage:` is **pipeline position** only (`drafting → review → ready → live`) —
  drives badges, the `/pipeline/` dashboard, and staging-surface visibility, but
  does NOT hide a page by itself. A page with **no** `stage:` defaults to `live`.
- **Live** = `stage: live` AND `draft: false`. Shipping a week flips both and
  merges its branch to `main`.

### Worktree-per-week convention
- Each in-progress week gets its own worktree + `claude/week-NN` branch:
  `cfm-week31 → claude/week-31`, `cfm-week32 → claude/week-32`,
  `cfm-week34 → claude/week-34`. Each carries weeks 01–29 plus that one staged
  week's `content/weeks/NN.md` (`draft: true`, `stage: review`).
- Push the branch → Cloudflare builds its preview automatically. Merge to `main`
  only when shipping (a deliberate desktop step, per `docs/working-remotely.md`).
- `.claude/worktrees/` and `.session-checkpoints/` are gitignored — never commit
  them (a past incident committed them as gitlinks and broke Cloudflare clones).

## ✂️ THE PASTE TEST — study guide vs Weekly Insights

**Insights owns MEANING. The study guide owns METHOD.**

> **If a study-guide paragraph could be pasted into Insights unnoticed, it belongs to
> Insights.**

The study guide points at a feature of the text and says how a reader could find it. It does
**not** then say what the feature means — that step is the essay's. Doing it in both places
is what makes a lesson read as preachy: the second telling implies the reader missed it the
first time.

⚠️ **Paraphrase hides redundancy from word-overlap checks but not from readers.** A rewritten
sentence saying the same thing still fails the test.

*Ruled by the 2026-08-13 rewrite (`43e1be0`, `b7b312e`). Measured: week 34's insights-prose
overlap fell 275 → 52 of 2,939 shingles; Key Passages went 199 → 0. The full rule is in
`STUDY-GUIDE-SPEC.md` § Division of labour — which lived only on a branch until 2026-08-15,
which is why weeks 30–33 never had it.*

## 🔬 K4 — LABEL EVERY STRUCTURAL CLAIM

**Label every structural claim `verified` or `candidate`, and name the text it was checked
against.**

A count that does not say which text it counted is not checkable. Qualify them — *"stated as
**Hebrew** counts"* — and explain the versification offset where one exists.

*Week 34's poetry analyser reported **1 verified against 96 candidates** across 20 psalms and
DECLINED to certify a Psalm 31 acrostic — logged as "the guardrail working, not a finding."
That discipline then reached the reader in Passage 5: "A detector that only matched a clean
A-to-Z would fail this psalm. Reproducing the irregularities is the test that the method
works." No rule required it. This line is the rule. (Fable audit K4.)*

## 🛡 K6 — A HEDGE IN ONE SECTION BINDS THE OTHERS

**When a claim is hedged or attributed in one section, propagate it to every section that
states the same thing.** A guide that hedges in §09 and over-claims in §03 is inconsistent
with itself, and the reader meets the over-claim first.

Hedge at **drafting time**, not as a cleanup pass. The evidence: Canaan's first draft already
carried **25 hedge-phrases across 7 of 11 files**; Achaemenid needed **a dozen commits** to
reach 8. The later pass was catching up to a standard the earlier guide had from day one.

*Includes retracting numeric over-claims — "seven English months honor a god" became "four
certainly… three more debated". Interpretation calls go to Kymber (queue class C), not to a
session. (Fable audit K6; `CULTURE-SPEC.md` contains none of this.)*

## 🎙 K7 — NARRATION SCRIPTS LIVE IN TWO PLACES, KEPT IN SYNC

**Convention decided 2026-07-26, rescued to `main` 2026-08-15** — it was committed in
`2ed6617`, which is not an ancestor of `main`, so the rule has been invisible where lessons
are built.

    Vault (canonical)  ~/Obsidian/K Master Vault/.../Culture/<Guide>/_narration/<slug>.script.md
    Repo               docs/narration/<guide>/<slug>.script.md

The vault is what the Narration Studio run reads; the repo copy is for easy find/edit
(github.dev from a phone). **Edit one, update the other.**

**A guide is a SYSTEM — prose, widget JSON, and audio must agree with each other.** When text
changes, announce the audio re-gen in the same commit ("Script synced; §04 queued for
re-gen") and close the loop from the other side when it lands ("Text-only; narration already
matched"). A stepper reading 734 BC against prose saying 733 is a defect in the guide, not in
one file.

*Ruled 2026-08-15 (HUB-058): the lane may create an episode; Kymber approves before it ships.*

## Where things are — read this before searching

**`~/Obsidian/Translation Hub/mc-intelligence/locations.json`** declares where everything
is: repos, worktrees, the 20 dictionary builds, data files, the NAS, services and ports.

```bash
python3 mc-intelligence/locate.py <thing>    # where is it, with the caveats
python3 mc-intelligence/locate.py --traps    # why your search will lie to you
python3 mc-intelligence/locate.py --verify   # is every declared path still real
```

Conversation histories are declared separately in `scriptorium/session_archives.json`.

**Absence is a claim that needs evidence.** On 2026-08-15 three things were reported
missing that were not missing — the ChatGPT export, the memory-intake adapters, and four
dictionary build directories. Each was a *correct search of the wrong place*, which
returns "not found" with total confidence. Two of them reached Kymber as a false claim.

If it is not in the registry, say **"the registry does not declare it"** — not "it does
not exist."


---

## Before researching or writing ANY CFM week — the canonical files

**`INSTRUCTIONS_FOR_CLAUDE.md` is canonical.** 1,775 lines, and it says of itself: *"If any
other document contradicts this one, this file wins."* It carries REQUIRED READING, the
SOURCE PRIORITY MODEL, and the RULINGS IN FORCE.

    K Master Vault/.../CFM Corner/OT_2026/Templates/INSTRUCTIONS_FOR_CLAUDE.md

**Three more, and the work is already in them — do not search the web first:**

| file | what it already holds |
|---|---|
| `Research Library/00_MASTER_RESOURCE_HUB.md` | ~47,000 indexed files across six vaults — Sacred Texts ~25,000 (Talmud 5,035, Midrash 369, Targumim 567), Knowlchemy ~2,260, **529 Interpreter articles filed BY LESSON** |
| `OT_2026/Resources/00_RESOURCE_LOCATION_INDEX.md` | every research source, declared since 2026-01-04 |
| `OT_2026/WeeklyLessons/Week_NN_*/[01_Weekly_Resources\|Video_Resources]/VIDEO_URL_TRACKER.md` | **the week's own work** — found videos, per-video reasoning, the completion checklist |

Also: `cfm-corner-tools/data/static_resource_map.json` resolves Unshaken, Line Upon Line,
Scripture Gems and the Church series for **49 of 52 weeks**. It is a lookup. Never re-search
those — they cover the whole year and never move.

**Why this is here:** on 2026-08-15 a session spent hours sweeping videos and still missed
sources sitting in the vault all year. The preflight gate in `hugo_converter` catches this
at GENERATION — but that session never generated anything, so it never fired. This block
loads whether or not anyone remembers, which is the only thing that has ever worked.
