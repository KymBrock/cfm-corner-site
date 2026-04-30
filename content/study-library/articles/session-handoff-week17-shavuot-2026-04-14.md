---
title: "Session Handoff: Week 17 & Shavuot Article"
description: "Session Handoff: Week 17 & Shavuot Article"
related_weeks: ["17"]
draft: true
---

**Date:** 2026-04-14
**Session span:** 2026-04-10 through 2026-04-14

---

## What Was Completed

### Week 16 (Exodus 14-17) — PUBLISHED
- Weekly Insights written, generated to HTML, deployed to Hugo site
- Glossary terms + flashcards added (6 terms)
- Home page updated (current: true on Week 16)
- Committed and pushed: `bebc323`
- Facebook announcement drafted

### Week 17 Study Guide Enhancements — IN VAULT (not yet on site)
- **Word Studies (04)** — Full rewrite with 6 terms (Qadash, Segullah, Kohen, Yare, Torah, Edut), cross-language tables, BLB links
- **Jewish Perspective (05)** — Expanded to 9 traditions with Sefaria links (added Aseret HaDibrot, Torah offered to all nations, Na'aseh v'Nishma)
- **Key Passages (03)** — Enhanced Hebrew analysis for Exodus 19:5-6 (three identity markers) and Exodus 20:2 (anokhi, Hiphil hotzeiticha, treaty pattern)
- **Overview (01)** — Header fix ("Big Idea" → lesson title)
- Location: `OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/`

### Shavuot / Pentecost Feast Day Article — DRAFT (committed, not published)
- Full interactive page at `cfm-corner-site/content/culture/jewish/moedim/shavuot.md`
- Commit: `bc01deb` (marked as draft)
- Hero images in `static/images/culture/jewish-festivals/shavuot/`

---

## What the Shavuot Article Contains

1. **Header** with Shavuot wheat field hero image + feast icon
2. **TOC** with jump links to all sections
3. **Spring Feast Timeline** (Shavuot highlighted)
4. **Biblical Foundation** — feast names, pilgrimage, two leavened loaves
5. **The First Shavuot: Sinai** — timing, theophany, Moses as mesites, rabbinic traditions in dropdowns
6. **Pentecost (Acts 2)** — Sinai-to-Pentecost fulfillment table
7. **JST Exodus 34 Higher Law Framework** — the second tablets were identical; the difference is interpretation, not text. Telestial/Terrestrial/Celestial layers with D&C 130:20-21
8. **10 Interactive Commandment Cards** — JS-powered expandable cards, each with 4 rows (Telestial, Terrestrial, Celestial, Blessing)
9. **Four Mountains Temple Progression** — Sinai, Galilee, Jerusalem/Temple Mount, Bountiful. Hero images, mountain cards, escalating proximity table
10. **Psalm 119 / Beatitudes** — ashrei language table (Hebrew→Greek→Latin→English), octave structure, doubled ashrei at Bountiful
11. **Bountiful as Shavuot** — Nephites and Law of Moses (5 scripture refs), typological pattern table, 5 post-resurrection changes in comparison cards
12. **Wheat Harvest in Restoration Scripture** — D&C 4:4, Alma 26:5, D&C 31:5, wheat and tares, Shavuot/Restoration parallel table
13. **Traditional Recipes** — 12 cards across Ashkenazi, Sephardic/Middle Eastern, and other traditions
14. **Abinadi's Shavuot Discourse** — Mosiah 12-13 as a possible Shavuot confrontation
15. **Restoration Feast Day Correlations** — 3 confirmed (Yom Teruah/plates, Passover eve/dedication, Passover/D&C 110) with Ricks (1983) citation
16. **Collapsible navigation** — deep sections in `<details>` dropdowns

---

## What Still Needs Work on the Shavuot Article

### Content to Add
- [ ] **Psalm 119 / Beatitudes side-by-side interactive** — show Ps 119:1-2 next to Matt 5:3-10 next to 3 Ne 12:1-12 with ashrei highlighted
- [ ] **Book of Ruth expanded section** — currently in a dropdown; deserves its own section with ruth-gleaning.jpg, connections to gathering/wheat/conversion
- [ ] **Family Shavuot activities** — how LDS families can observe Shavuot themes (all-night study, make cheesecake, read Ruth, discuss the three layers)
- [ ] **NT Events by Feast Day chart** — reference doc saved to vault (`Moedim/NT_Events_by_Feast_Day_Reference.md`); could become a standalone article or be excerpted into Shavuot

### Visual Improvements
- [ ] **Sinai hero image** — currently using wheat field for Sinai card; need a fire/mountain image from Illustrator file
- [ ] **Recipe images** — food cards need photos (stock or generated)
- [ ] **Individual icons** from Illustrator — still need to be sliced and exported (user has 4 artboards with icons ready)
- [ ] **Section divider images** from Illustrator

### Structural
- [ ] **Link audit** — run link-audit.py on the Shavuot page once content is finalized
- [ ] **Week 17 charts entry** — need to add Shavuot to `content/weeks/17.md` charts section
- [ ] **Moedim index page** — update `_index.md` to include Shavuot card (currently has placeholder)

---

## Week 17 Remaining Deliverables (from original handoff)

- [ ] Weekly Insights for Week 17 (not yet started)
- [ ] Hebrew Lesson 13 (definite article or construct state)
- [ ] Glossary terms for Week 17
- [ ] `content/weeks/17.md` charts entries
- [ ] Video resource processing (check for new Faith Insights episode)
- [ ] Generate HTML and deploy

---

## Key Files

### Shavuot Article
- Hugo page: `cfm-corner-site/content/culture/jewish/moedim/shavuot.md`
- Working draft: `Week_17_Exodus_18-20/Working/DRAFT_Shavuot_Article.md` (older version — Hugo page is canonical)
- Hero images: `cfm-corner-site/static/images/culture/jewish-festivals/shavuot/`
- Illustrator source: `/Volumes/Learning Inspired/Perforce/kymber_workspace/Shavuot/`

### Research
- NT feast day reference: `OT_2026/Moedim/NT_Events_by_Feast_Day_Reference.md`
- Deep Analysis (Sinai/Sermon/Bountiful): `Research Library/IF_Lesson16_Easter/DEEP_ANALYSIS_Sinai_Sermon_Bountiful_2026-03-25.md`
- Shavuot index: `OT_2026/Moedim/MOEDIM_Shavuot_Pentecost_Index.md`

### Week 17 Study Guide
- Enhanced files: `Week_17_Exodus_18-20/03_Study_Guide/` (all 7 files)
- Original handoff: `Week_17_Exodus_18-20/Working/OPUS_STUDY_GUIDE_REVIEW_HANDOFF.md`

### Memory
- Faith Insights playlist tracking: `~/.claude/projects/-Users-kymberbrockbank/memory/reference_faith_insights_playlist.md`

---

## Git Status

- **cfm-corner-site** — `main` branch, pushed through `bc01deb`. Shavuot committed but not deployed to production (draft: false in frontmatter — change to `draft: true` if you want it hidden, or leave as-is since it's accessible but not linked from navigation due to `hide_nav: true`).
- **Obsidian vault** — Week 17 study guide enhancements and research docs are local only (not in a git repo).

---

*Session handoff prepared 2026-04-14*
