# Claude Code Safety Rules for cfm-corner-site

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
- [ ] Verify the homepage "This Week's Study" bar points to the new current week after the front-matter handoff
- [ ] Verify all `charts:` entries match their actual article titles and descriptions
  — title and description must come from the article's own front matter, not be invented
- [ ] Verify chart `url:` paths resolve correctly (e.g., `study-library/articles/slug/`)

### Static Content (`static/content/weekNN/`)
- [ ] Run `link-audit.py` on all three files (study-guide, insights, resources) — zero issues
- [ ] Run `python3 scripts/check_popup_links.py <touched files>` on every touched lesson/article file
- [ ] Fix every flagged bare verse reference such as `(3:11)` or missing numeric prefix such as `Nephi 11:4` before handoff
- [ ] If the week introduces new Hebrew/Greek terms, update the glossary data and verify the Hebrew landing page / glossary section reflects the new entries
- [ ] Verify `rg -n 'churchofjesuschrist\\.org/study/scriptures/(ot|nt)' content/culture static/content/weekNN` returns **zero** results for the active published set
- [ ] Verify non-Bible scripture or deuterocanonical references that are outside the Bible popup cache use an approved external source such as Sefaria and include `data-popup-text` when a hover preview is expected
- [ ] Verify no emojis in any HTML files (monochromatic icons only)
- [ ] Verify all video cards use thumbnail format (never plain text links)
- [ ] Verify every discovered weekly `watch?v=` URL renders as a thumbnail card; channel-homepage fallbacks are only acceptable when no week-specific video was found
- [ ] Use `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Planning/Content_Maps/Church_Media_Video_Map.md` as the authoritative Week-to-Church-Media mapping when OT Stories / Come Learn With Me cards are missing or shifted
- [ ] If the week's `Video_Resources/VIDEO_URL_TRACKER.md` includes a Bible Project section, make the generated Bible Project accordion match that documented weekly list rather than a reduced generator default
- [ ] If new scripture popup behavior is expected, verify the touched pages against the published popup data files in `static/data/`, especially `scripture-verses.json`
- [ ] If a touched page references new images, verify those assets exist in the site repo and are included in the publish set
- [ ] After deploy, test at least one live Bible hover, one live lexicon hover, and one non-Bible fallback hover before calling the week stable

### Scripture & Term Link Contract
- All OT/NT Bible scripture links in touched or published lesson/culture surfaces must go to **Blue Letter Bible**, not the Church scripture site.
- Church scripture URLs are only acceptable for non-Bible works that BLB does not cover, and even then only when that source is intentionally approved.
- Every scripture citation in a touched file must include the full book name and chapter. Never leave bare references like `(3:11)` or partial references like `Nephi 11:4`.
- Every scripture link must include a normalized `data-ref` with the full reference, e.g. `data-ref="Exodus 3:14"` or `data-ref="3 Nephi 11:1-17"`.
- If linking to Church or BLB scripture pages, always add `data-ref` so the popup system can resolve the reference.
- For chapter-only references such as `Exodus 3`, use the full book + chapter in `data-ref`; do not rely on shorthand.
- Do not expect `scripture-verses.json` to resolve deuterocanonical or non-Bible references automatically. For Maccabees, Sirach, Judith, or similar sources, use an approved source such as Sefaria and provide `data-popup-text` if hover preview text is required.
- Do not invent glossary/term links. If a term is not in the approved glossary data, leave it plain or flag it for glossary expansion rather than fabricating a popup.
- Plain transliterations that function as term notes or glosses should not be left floating when a source link exists nearby. Link them either to the verified lexicon/source entry or to the specific source passage being discussed.
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
- [ ] Check key new pages on mobile before publish (especially harmony charts, maps, and custom calendar/card layouts)

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

### 0. Week 13 Publish Failures (Added 2026-03-23)
- BLB is the required destination for OT/NT Bible scripture links in published lesson and culture surfaces. Do not ship Church OT/NT scripture URLs in those active pages.
- Hover previews depend on both the link markup **and** the published popup data files. A correct BLB link can still show `Preview unavailable` if `static/data/scripture-verses.json` on `main` is stale.
- Non-Bible references outside the Bible verse cache, such as `1–2 Maccabees`, must use an approved source such as Sefaria plus explicit `data-popup-text` when hover text is expected.
- `main` can drift from the working branch on site-critical files. Before publish, verify that `themes/cfm/layouts/_default/baseof.html`, `static/data/scripture-verses.json`, `layouts/shortcodes/rawhtml.html`, and any newly referenced assets are actually present on the publish branch.
- Live verification is mandatory after deploy. Before calling a release stable, test one Bible hover, one lexicon hover, one fallback hover, and one mobile page on the live site.

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

### 6. Hugo Static File Caching
Hugo's `readFile` function caches static files at build time. After
editing any file in `static/content/`, you MUST restart the Hugo server
to see changes. Live reload does NOT pick up static file changes.

### 7. macOS Dark Mode vs Tkinter (DIAGNOSED — NOT YET FIXED)
Six styling attempts failed, but the root cause is NOT "macOS dark mode
vs Tkinter" in general. The root cause is **global ttk style overrides**:
- `style.configure(".", ...)` — overrides ALL widget colors, causes invisibility
- `style.map(".", ...)` — same problem
- `tk_setPalette()` — no effect on ttk, confuses widget rendering

The current `hugo_gui.py` (restored from commit `dc55dd0`) has ZERO
styling code and should render with default ttk appearance.

**Next session approach (test-first, minimal fix):**
1. Run a single diagnostic test (bare ttk widgets, no styling) to confirm
   default rendering works
2. Launch the current GUI as-is (it has no styling)
3. Only then add CFM branding using ONLY named styles (`CFM.TButton`, etc.)
4. NEVER use `style.configure(".", ...)` — this is what broke everything
5. Add `--no-style` flag for future debugging

See `Session_Handoffs/2026-03-14_Week12_Session_Handoff.md` §4 for
full strategy with code examples.

---

## Weekly Content Generation Workflow

### Step-by-step for each new week:

1. **Generate content via CLI** (not the GUI until dark mode is fixed):
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
