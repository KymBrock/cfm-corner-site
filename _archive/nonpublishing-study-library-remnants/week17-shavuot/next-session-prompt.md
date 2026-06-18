---
title: "Session Opener: Week 17 Deployment"
description: "Copy and paste everything below the line into Claude Code to start the next session:"
related_weeks: ["17"]
draft: true
---

**Updated:** 2026-04-15

Copy and paste everything below the line into Claude Code to start the next session:

---

Please review the following handoff summary:

Read the full handoff at `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/Working/SESSION_HANDOFF_Week17_2026-04-15.md`

## Where We Left Off

Most Week 17 content is built. The Shavuot article has 5 new major sections (Beatitudes interactive, Book of Ruth, recipe images, Family Activities, scholarly links). Hebrew Lesson 13 (Verbless Sentences) is written. All 7 study guide files are enhanced with verified citations and Hebrew terms. 12 video transcripts are distilled.

## Priority Tasks for This Session

### 1. Process Lynne Hilton Wilson video
URL: `https://www.youtube.com/watch?v=sH3ZuERg9zQ` — "Exodus 19-34 | AT THE FOOT OF SINAI | Handmaidens, Harems and Heroines"
Needs: yt-dlp transcript → clean → distill. Update VIDEO_URL_TRACKER.md.

### 2. Collect remaining weekly video drops
Week 17 (Exodus 18-20, Apr 20-26) — check if these have released:
- Faith Insights 2026 (Scripture Central — Tyler Griffin)
- Follow Him 2026 episode (not the 2022 Belnap episodes already processed)
- Finding Christ, Don't Miss This, Scripture Insights, Talking Scripture, Scriptures Are Real
- Grounded, Our Mothers Knew It
- Latter Day Kids, Scripture Explorers, Thumb Follow Me
- Manual lookup: Unshaken, Line Upon Line, Messages of Christ

Tracker: `Week_17.../01_Weekly_Resources/VIDEO_URL_TRACKER.md`
Distilled output: `Week_17.../Video_Resources/Distilled/`
Use yt-dlp for transcripts (no API needed). Verify video IDs via oembed API.

### 3. Write Weekly Insights for Week 17
Not yet started. Source from distilled videos + study guide material.

### 4. Create `content/weeks/17.md`
Hugo week page with frontmatter and `charts:` entries for Shavuot article and Hebrew Lesson 13. Use Week 16 (`content/weeks/16.md`) as template.

### 5. Generate HTML and deploy
Convert study guide, insights, resources → HTML via converter. Run link-audit.py. Commit and push.

### 6. Glossary terms for Week 17
6 terms from word studies: qadash, segullah, kohen, yare, torah, edut

## Key Rules
- Links on transliterations, never on Hebrew with niqqud
- Every prophet/apostle attribution must have a verified linked citation
- Never batch-regenerate weekly HTML (see cfm-corner-site CLAUDE.md)
- Content integrity — source from scripture, vault, or processed transcripts only

## Uncommitted Changes
- **cfm-corner-site** (main branch): Shavuot article updates, Hebrew Lesson 13, 11 recipe images
- **Obsidian vault**: Study guide enhancements, 12 video transcripts + distillations

Start by reading the full handoff, then let's tackle them in priority order.
