---
title: "Week 17 Study Guide Review — Opus Prompt"
description: "I need you to review and enhance the Week 17 (Exodus 18-20) study guide for CFM Corner, then draft two new content pieces. Read these files in order:"
related_weeks: ["17"]
draft: true
---

**Copy everything below this line and paste into a new Claude session.**

---

I need you to review and enhance the Week 17 (Exodus 18-20) study guide for CFM Corner, then draft two new content pieces. Read these files in order:

1. **Handoff with full instructions:** `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/Working/OPUS_STUDY_GUIDE_REVIEW_HANDOFF.md`

2. **Research brief (734 lines of primary sources):** `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/Working/RESEARCH_BRIEF_Week17_Exodus_18-20_2026-03-27.md`

3. **All 7 study guide files:**
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/01_Week_Overview.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/02_Historical_Cultural_Context.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/03_Key_Passages_Study.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/04_Word_Studies.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/05_Jewish_Perspective.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/06_Teaching_Applications.md`
   - `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_17_Exodus_18-20/03_Study_Guide/07_Study_Questions.md`

4. **Week 16 word studies (format reference — match this quality):** `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/WeeklyLessons/Week_16_Exodus_14-17/03_Study_Guide/04_Word_Studies.md`

5. **Existing Moedim articles (format reference for Shavuot):**
   - `/Users/kymberbrockbank/Developer/cfm-corner-site/content/culture/jewish/moedim/bikkurim.md`
   - `/Users/kymberbrockbank/Developer/cfm-corner-site/content/culture/jewish/moedim/matzot.md`

6. **Operational rules:** `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Templates/INSTRUCTIONS_FOR_CLAUDE.md` (read the first 100 lines for safety rules and content integrity standards)

After reading all files, do the following **in order**:

### Task 1: Fix the Overview h2
In `01_Week_Overview.md`, change `## Big Idea` to `## "All That the Lord Hath Spoken We Will Do"` (the lesson title, not a generic heading). This was a bug in Week 16 we already fixed.

### Task 2: Enhance Word Studies
Rewrite `04_Word_Studies.md` to match Week 16's format. Each word study needs:
- Cross-language table: Hebrew (with BLB lexicon link) → Greek LXX (with BLB link) → Latin Vulgate (with Logeion link) → English (with Merriam-Webster, Webster 1828, Etymonline links)
- Strong's number
- Root and derivatives section
- Semantic range
- Key passage with Hebrew analysis
- LDS/Christological connection
- Cross-language connections table (duplicate of the opening table with expanded English cognates)

Current terms (enhance all 4):
1. Qadash (קָדַשׁ) H6942 — sanctify
2. Segullah (סְגֻלָּה) H5459 — peculiar treasure
3. Kohen (כֹּהֵן) H3548 — priest
4. Yare (יָרֵא) H3372 — fear/reverence

Add 2 new studies:
5. Torah (תּוֹרָה) H8451 — instruction/law/teaching
6. Edut (עֵדוּת) H5715 — testimony/witness (the tablets are "tablets of testimony")

### Task 3: Expand Jewish Perspective
Enhance `05_Jewish_Perspective.md` from 4 traditions to at least 8-10. Add with Sefaria links where possible:
- God offered Torah to all nations (they declined; Israel accepted)
- Souls of all future generations present at Sinai
- "Ten Words" (Aseret HaDibrot) — not commandments but declarations
- Whether commandments were given individually or all at once
- Reading Ezekiel 1 (chariot vision) on Shavuot
- The tradition of standing during Torah reading (because Israel stood at Sinai)
- Jethro as a righteous convert — the ger tzedek tradition

### Task 4: Draft Shavuot Article
Create a new article at: `/Users/kymberbrockbank/Developer/cfm-corner-site/content/culture/jewish/moedim/shavuot.md`

Follow the format of `bikkurim.md` and `matzot.md`. Cover:
- Biblical foundation (Exodus 23:16, 34:22, Deuteronomy 16:9-12)
- Counting the Omer (Leviticus 23:15-16)
- Sinai connection: Torah given on Shavuot
- Book of Ruth on Shavuot (and why)
- Dairy foods tradition
- Tikkun Leil Shavuot (all-night Torah study)
- Pentecost connection (Acts 2 — Spirit descends on Shavuot)
- LDS resonance: temple endowment parallels, covenant renewal
- Include frontmatter with `related_weeks: ["17"]`

### Task 5: Provide Glossary Terms
List the Week 17 glossary terms in this format (for `cfm-glossary.json`):
```json
{"strongs": "H6942", "translit": "qadash", "original": "קָדַשׁ", "lang": "hebrew", "meaning": "to sanctify, set apart"}
```
Include all 6 word study terms plus any additional key terms from the week.

### Task 6: Recommend Charts Entries
Provide the YAML for the `charts:` section of `content/weeks/17.md`, including:
- The Shavuot article
- Hebrew Lesson 13 (if you draft it) or a placeholder
- Any other articles that should appear

---

**Critical rules:**
- Every claim must be sourced from scripture, the research brief, or approved references
- Every Hebrew term needs a BLB lexicon link: `https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/`
- Every Greek term needs a BLB link: `https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/`
- Latin terms link to Logeion: `https://logeion.uchicago.edu/TERM`
- No emojis in any output
- Do not fabricate quotes, traditions, or linguistic claims
- If uncertain about a source, flag it as `[PENDING VERIFICATION]`

Start by reading all the files, then confirm what you found before making changes.
