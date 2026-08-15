# CFM Corner — Weekly Lesson Protocol

This is the step-by-step workflow for preparing and publishing each week's lesson. Everything starts in Obsidian and ends with a live lesson page + email to subscribers.

---

## Overview

```
Obsidian (write/research) → Hugo (build site) → GitHub (deploy) → Mailchimp (email)
```

**Obsidian vault:** `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/`
**Hugo site:** `/Users/kymberbrockbank/Developer/cfm-corner-site/`
**Scripts:** `cfm-corner-site/scripts/`

---

## Phase 1: Content Creation (Obsidian)

**Location:** `OT_2026/WeeklyLessons/Week_NN_*/`

### 1.1 Study Guide (folder: `03_Study_Guide/`)
Write or review these files:
- [ ] `01_Week_Overview.md` — Theme, scripture scope, key concepts
- [ ] `02_Historical_Cultural_Context.md` — Ancient world context
- [ ] `03_Key_Passages_Study.md` — Verse-by-verse insights
- [ ] `04_Word_Studies.md` — Hebrew/Greek word studies
- [ ] `05_Teaching_Applications.md` — Teaching ideas for 7 settings
- [ ] `06_Study_Questions.md` — Discussion/reflection questions
- [ ] `07_Jewish_Perspective.md` — Jewish interpretive insights with LDS connections (Section 5 in study guide)
- [ ] All Hebrew/Greek terms in body text have lexicon links (not just word studies)
- [ ] Each word study has a Cross-Language Connections table (Greek/Latin/English)

### 1.2 Weekly Insights (folder: `02_Weekly_Insights/`)
- [ ] `Weekly_Insights_WeekNN.md` — Narrative synthesis of the week

### 1.3 Video Resources (folder: `Video_Resources/`)
1. Run the video collector:
   ```bash
   cd /Users/kymberbrockbank/Developer/cfm-corner-tools
   rm -rf ingesters/.cache/
   .venv/bin/python3 ingesters/collect_and_distill_videos.py --week N --collect-only
   ```
2. Manually add any missing URLs the collector didn't find
3. Pre-fill static channels (Scripture Gems 2022, Messages of Christ) if not already done:
   ```bash
   python3 /Users/kymberbrockbank/.openclaw/workspace/scripts/prefill-static-channels.py
   ```
4. Verify `academic_resources_urls.json` has the current week's slug:
   ```
   cfm-corner-tools/generators/weekly_resources/academic_resources_urls.json
   ```
5. The **cron job** handles ongoing backfill automatically (Wed–Sat, 10am & 6pm MST)
- [ ] Verify all links are live and correct
- [ ] Add summaries in `Distilled/` folder if needed

### 1.4 Interactive Charts (folder: `HTML/` or `Working/`)
- [ ] Build any week-specific charts (comparison tables, Hebrew charts, etc.)

### 1.5 Update Progress Tracker
- [ ] Update `Week_NN_Progress_Tracker.md` status for each item

### 1.6 Culture & Study Library Content (as needed)

These sections are **not per-week tasks** — they're published independently as the content is ready. See the dedicated specs for full details.

**Culture Section** (`content/culture/`):
- Jewish tradition articles, feast days (mo'edim), interpretive frameworks
- See `CULTURE-SPEC.md` for front matter, layout, and content guidelines
- Canonical example: Purim mo'edim page

**Study Library** (`content/study-library/`):
- In-depth articles, thematic studies, deep dives
- See `STUDY-LIBRARY-SPEC.md` for article format and front matter
- Canonical example: Seven Sermons article

> **Tip:** If Culture or Study Library articles relate to the current week's scripture, mention them in the study guide's Teaching Applications section or link to them from relevant subsections.

---

## Phase 2: Hugo Site Content

### 2.1 Week Front Matter (`content/weeks/NN.md`)
Create or update the week's markdown file with front matter:

```yaml
---
title: "Week Title Here"
scripture: "Scripture Reference"
dates: "Month DD–DD, YYYY"
week_num: "NN"
weight: N
current: true          # set previous week to false
image: "images/weeks/weekNN.jpg"
image_alt: "Description of the lesson image"
description: "One-paragraph summary for study guide section."
quick_summary: "2-3 sentence overview for the email intro and page header."
charts:
  - title: "Chart Name"
    url: "content/weekNN/chart.html"
    description: "What this chart shows."
---
```

**Important:** The email generator reads these fields, so fill them all in.

### 2.2 Static Content Files (`static/content/weekNN/`)
Convert Obsidian content to HTML and deploy using **cfm-corner-tools**:

**Primary Command (generates ALL three + deploys to Hugo site):**
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-tools
.venv/bin/python3 cfm_cli.py generate --week NN --book ot --deploy
```
This generates `study-guide.html`, `insights.html`, and `resources.html` (with thumbnails + logo cards) and copies them directly to `cfm-corner-site/static/content/weekNN/`.

**Alternative: GUI Converter** (when you need more control):
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-tools/converters && ./run_converter_ui.sh
```

**Check status of all weeks:**
```bash
.venv/bin/python3 cfm_cli.py status --book ot
```

Verify outputs:
- [ ] `study-guide.html` — from Study Guide markdown files
- [ ] `insights.html` — from Weekly Insights markdown
- [ ] `resources.html` — from Video Resources / VIDEO_URL_TRACKER (**must match `RESOURCES-HTML-SPEC.md`**)
- [ ] Any chart HTML files referenced in front matter
- [ ] Run `link-audit.py` on **all three** files (study-guide, insights, resources) — zero issues
- [ ] If issues found, run `link-audit.py --fix --week weekNN` to auto-link bare terms
- [ ] All BLB lexicon links have `data-lexicon` popup attributes (no bare BLB links)
- [ ] Every word study has a Cross-Language Connections table (Greek/Latin/English)
- [ ] Key Locations section has multi-source map links (HLS, Atlas, BYU)

> **Important:** The resources HTML must follow the format in [`RESOURCES-HTML-SPEC.md`](RESOURCES-HTML-SPEC.md). Canonical example: `static/content/week08/resources.html`. Every week must include: Church Media for Families section, video thumbnail cards (never plain text links), Bible Project theme + word study videos, and all accordion sections.

> **Weekly video cards must use direct weekly video URLs whenever available.** Do not leave a discovered weekly item as a plain channel link if a `watch?v=` URL exists. If the tracker has a direct YouTube video URL, the generated card must render with a thumbnail rather than plain text.

> **Church Media for Families must use the OT planning map as source of truth.** When week sequencing around Easter/holidays causes drift, use `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Planning/Content_Maps/Church_Media_Video_Map.md` instead of inferred numbering.

> **Bible Project must use the weekly tracker as source of truth.** If the week's `Video_Resources/VIDEO_URL_TRACKER.md` contains a Bible Project section, the generated accordion must mirror that documented weekly list rather than a reduced fallback subset.

> **Hebrew/Greek lexicon links** must use hover popups per [`LEXICON-POPUP-SPEC.md`](LEXICON-POPUP-SPEC.md). **Every Hebrew/Greek Unicode character in body text** must be inside a lexicon `<a>` tag with all `data-*` attributes — not just first occurrences and not just in Word Studies. New terms must be added to `cfm-corner-tools/data/lexicon-popups.json`. The GUI converter handles this automatically for links in Obsidian markdown.

> **Cross-Language Connections** are mandatory for every word study — see [`LEXICON-POPUP-SPEC.md`](LEXICON-POPUP-SPEC.md) for the 3-row table pattern (Greek/Latin/English). The `link-audit.py` script checks for missing tables.

### 2.3 Lesson Image
- [ ] Add lesson image to `static/images/weeks/weekNN.jpg`
- [ ] Update front matter `image` and `image_alt` fields

### 2.4 Set Current Week
- [ ] Set `current: true` on new week's `.md`
- [ ] Set `current: false` on previous week's `.md`

---

## Phase 3: Build & Deploy

### 3.1 Local Preview
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-site
hugo server --noHTTPCache --disableFastRender --renderToMemory -p 1314
```
**⚠️ Must restart after major content edits** — `renderToMemory` can serve stale content.
- [ ] Check all 4 tabs load (Study Guide, Insights, Resources, Charts)
- [ ] Check lesson image displays
- [ ] Check mobile layout
- [ ] Verify charts are interactive

### 3.2 Push to GitHub
```bash
git add -A
git commit -m "Week NN: Scripture Reference"
git push
```
GitHub Actions will automatically build Hugo + Pagefind and deploy to GitHub Pages.
The post-commit hook will also auto-update `CODE_INDEX_AUTO.md` in Obsidian.

> **Full Git protocol** (commit conventions, repo overview, hook setup): `GIT-PROTOCOL.md`

### 3.3 Verify Live Site
- [ ] Check `www.cfmcorner.com/weeks/NN/` (or `kymbrock.github.io/cfm-corner-site/weeks/NN/`)
- [ ] Confirm all content loads correctly

---

## Phase 4: Email Newsletter

### 4.1 Generate Email
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-site
./scripts/generate-email.sh NN
```
Output: `~/Desktop/cfm-email-weekNN.html`

### 4.2 Preview & Customize
- [ ] Open the HTML file in browser to preview
- [ ] Make any edits to the generated content (add/remove bullet points, adjust wording)
- [ ] If you want a custom intro beyond the auto-generated one, edit the HTML directly

### 4.3 Send via Mailchimp
1. Log into Mailchimp
2. **Create Campaign → Email → Regular**
3. Choose audience (All Contacts)
4. Subject line: `This Week on CFM Corner: [Scripture Reference]`
5. **Design Email → Code your own → Paste in code**
6. Paste the generated HTML
7. Replace image `src` URLs:
   - `CFMClogo.jpg` → Mailchimp-hosted header URL (save this — it's the same every week)
   - `CFMbannet.jpg` → Mailchimp-hosted footer URL (same every week)
   - `lesson-image.jpg` → Upload this week's lesson image to Content Studio, use that URL
8. **Preview & Test** — send a test to yourself
9. **Send** (or schedule for Saturday/Sunday morning)

### Mailchimp Image URLs (reuse weekly)
- **Header (CFMClogo.jpg):** `https://mcusercontent.com/6074bb2e8a5b4a52150832446/images/5cf0c4cd-300b-66a8-bab1-2c326c39f2b3.jpg`
- **Footer (CFMbannet.jpg):** `https://mcusercontent.com/6074bb2e8a5b4a52150832446/images/0ae702ea-fca6-a65c-501c-5972c12aeaf7.jpg`
- **CAN-SPAM address:** 5725 S. Valley Blvd. Ste 5 PMB 266598, Las Vegas, NV 89118-3122

---

## Phase 5: Cleanup

- [ ] Update `Week_NN_Progress_Tracker.md` — mark everything complete
- [ ] Commit any final changes to Git
- [ ] Note anything to improve for next week in `memory/YYYY-MM-DD.md`

---

## Quick Reference: File Locations

| What | Where |
|------|-------|
| Obsidian weekly lessons | `OT_2026/WeeklyLessons/Week_NN_*/` |
| Hugo week content | `content/weeks/NN.md` |
| Static HTML content | `static/content/weekNN/` |
| Lesson images | `static/images/weeks/weekNN.jpg` |
| Email generator script | `scripts/generate-email.sh` |
| Generated emails | `~/Desktop/cfm-email-weekNN.html` |
| Master Resource Tracker | `OT_2026/Resources/MASTER_RESOURCE_TRACKER.md` |
| Video URL Trackers | `OT_2026/WeeklyLessons/Week_NN_*/Video_Resources/VIDEO_URL_TRACKER.md` |
| Culture section content | `content/culture/` |
| Study Library content | `content/study-library/` |
| Culture spec | `CULTURE-SPEC.md` |
| Study Library spec | `STUDY-LIBRARY-SPEC.md` |
| **cfm-corner-tools** | `/Users/kymberbrockbank/Developer/cfm-corner-tools/` |
| Tools config | `cfm-corner-tools/config.yaml` |
| Academic URLs config | `cfm-corner-tools/generators/weekly_resources/academic_resources_urls.json` |
| Static channel pre-fill | `/Users/kymberbrockbank/.openclaw/workspace/scripts/prefill-static-channels.py` |

---

## Future Automation (TODO)

- [x] **Obsidian → Hugo converter**: ✅ GUI converter (`cfm-corner-tools/converters/run_converter_ui.sh`) + CLI (`md_to_html_converter.py`)
- [x] **Video URL auto-update**: ✅ Video collector pipeline + resources HTML generator + cron automation
- [ ] **Mailchimp API integration**: Auto-create campaign from generated HTML
- [ ] **One-command publish**: Single script that does Phase 2–4 in sequence
- [ ] **Mailchimp saved template**: Upload header/footer once, use template ID for campaigns

---

*Last updated: 2026-03-01*

---

## 🗂 SOURCES LEDGER + INTAKE PIPELINE — run these BEFORE drafting

**Added 2026-08-15.** The Fable audit (K3) found this practice *written nowhere* — zero
mentions across this file, `STUDY-GUIDE-SPEC.md` and both `CLAUDE.md` files, with a positive
control confirming the zero was real. It exists only in weeks 32–34, which are the weeks the
audit rates as the best craft in the corpus.

    Week_NN_<slug>/Working/intake_A_interpreter.md
                            intake_B_conference_talks.md
                            intake_C_rabbinic.md
                            intake_D_church_manuals.md
                            intake_E_poetry_analyzer.md      (poetry weeks)

    Week_NN_<slug>/02_Weekly_Insights/_SOURCES_Weekly_Insights_WeekNN.md

**The intakes can be run MONTHS AHEAD.** Nothing in them depends on the week being current —
which makes this the future-planning pipeline, not just a drafting step.

**The sidecar is an editorial provenance ledger and is NOT published to readers.** It records
each quote's source, what it was verified against, and the licence — Sefaria's William
Davidson Talmud is CC BY-NC. Inline attribution appears at each quote in the text itself.

Its own stated discipline: *"the essay draws where the tradition speaks and does not
manufacture commentary where it is silent."*

**Label every structural claim `verified` or `candidate`, and name the text it was checked
against.** Week 34's poetry analyser reported 1 verified against 96 candidates and *declined*
to certify a Psalm 31 acrostic — recorded as "the guardrail working, not a finding."

Full spec: `OT_2026/Templates/SOURCES-AND-INTAKE-SPEC.md`
