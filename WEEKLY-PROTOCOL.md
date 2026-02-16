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

### 1.2 Weekly Insights (folder: `02_Weekly_Insights/`)
- [ ] `Weekly_Insights_WeekNN.md` — Narrative synthesis of the week

### 1.3 Video Resources (folder: `Video_Resources/`)
- [ ] Update `VIDEO_URL_TRACKER.md` with this week's video URLs
- [ ] Verify all links are live and correct
- [ ] Add summaries in `Distilled/` folder if needed

### 1.4 Interactive Charts (folder: `HTML/` or `Working/`)
- [ ] Build any week-specific charts (comparison tables, Hebrew charts, etc.)

### 1.5 Update Progress Tracker
- [ ] Update `Week_NN_Progress_Tracker.md` status for each item

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
Convert Obsidian content to HTML and place in:
- [ ] `study-guide.html` — from Study Guide markdown files
- [ ] `insights.html` — from Weekly Insights markdown
- [ ] `resources.html` — from Video Resources / VIDEO_URL_TRACKER
- [ ] Any chart HTML files referenced in front matter

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
hugo server --noHTTPCache --disableFastRender --renderToMemory
```
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

### Mailchimp Image URLs (fill in once, reuse weekly)
- **Header (CFMClogo.jpg):** `________________`
- **Footer (CFMbannet.jpg):** `________________`

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

---

## Future Automation (TODO)

- [ ] **Obsidian → Hugo converter**: Auto-convert study guide markdown files to `study-guide.html`
- [ ] **Video URL auto-update**: Pull from `VIDEO_URL_TRACKER.md` into `resources.html`
- [ ] **Mailchimp API integration**: Auto-create campaign from generated HTML
- [ ] **One-command publish**: Single script that does Phase 2–4 in sequence
- [ ] **Mailchimp saved template**: Upload header/footer once, use template ID for campaigns

---

*Last updated: 2026-02-15*
