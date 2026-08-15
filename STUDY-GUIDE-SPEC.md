# Study Guide HTML Specification

Complete format specification for CFM Corner weekly study guides. Canonical example: **Week 09** (`static/content/week09/study-guide.html`).

---

## Overview

Each study guide is a single HTML file embedded via Hugo into the site layout. It contains inline `<style>`, a header section, quick links, expand/collapse buttons, and 7 major accordion sections. No external CSS file — all styles are self-contained in the HTML.

---

## Page Structure

```
<style>...</style>
<div class="container">
  <!-- Header Section -->
  <div class="header-section">
    <p class="week-label">Week N</p>
    <h1>Book Chapter–Chapter</h1>
    <div class="subtitle">"Week Theme Title"</div>
    <div class="date-location">Month Day – Month Day, Year</div>
  </div>

  <!-- Quick Links -->
  <div class="quick-links">
    <a href="CFM_MANUAL_URL" target="_blank" class="quick-link">CFM Manual</a>
  </div>

  <!-- Expand/Collapse Buttons -->
  <div class="button-container">
    <button class="expand-button" onclick="expandAll()">⊞ Expand All</button>
    <button class="expand-button" onclick="collapseAll()">⊟ Collapse All</button>
  </div>

  <!-- SECTION 1–7: Major Accordion Sections -->
  ...
</div>
```

---

## Major Accordion Sections (7 total)

Each major section uses this pattern:

```html
<div class="sg-accordion-section" onclick="toggleSection(this)">
  <span class="sg-section-title">N. Section Title</span>
  <span class="sg-section-actions">
    <button class="sg-action-btn" title="Expand all subsections"
            onclick="event.stopPropagation(); expandSection(this)">⊞</button>
    <button class="sg-action-btn" title="Collapse all subsections"
            onclick="event.stopPropagation(); collapseSection(this)">⊟</button>
  </span>
</div>
<div class="sg-panel" style="display: none;">
  <div class="panel-content">
    <!-- Sub-accordions go here -->
  </div>
</div>
```

### The 7 Sections

| # | Title Pattern | Contains |
|---|--------------|----------|
| 1 | `Book Chapter–Chapter` (e.g., "Genesis 18–23") | Week Overview sub-sections |
| 2 | `Week NN: Historical & Cultural Context` | ANE context, archaeology, tradition |
| 3 | `Week NN: Key Passages Study` | Verse-by-verse analysis per passage |
| 4 | `Week NN: Word Studies` | Hebrew word studies with cross-language tables |
| 5 | `Week NN: Jewish Perspective` | Ancient Jewish insights with LDS connections |
| 6 | `Week NN: Teaching Applications` | Per-setting teaching ideas |
| 7 | `Week NN: Study Questions` | Grouped by question type |

---

## Section 1: Week Overview

Contains these sub-accordions (all open by default with `style="display: block;"`):

1. **Week Information** — `info-table` with Week, Dates, Reading, CFM Manual link, Total Chapters, Approximate Verses
2. **Reading Summary** — Prose paragraphs summarizing each chapter, with inline scripture links
3. **Central Themes** — h3 per theme, with prose, bullet lists, scripture references, application questions
4. **Key Figures** — `info-table` with Person / Role / Significance columns
5. **Timeline Placement** — Historical period, dates, Abraham's age, relationship to adjacent weeks
6. **Connection to Restoration Scripture** — h3 sub-groups (Book of Mormon, D&C), bullet lists with links
7. **This Week's Key Doctrines** — Ordered list
8. **Temple Connections** — Bullet list
9. **CFM Manual Emphasis** — Manual focus summary + key questions
10. **Suggested Reading Approach** — Essential Reading + Deep Study lists
11. **For Further Study: Interpreter Foundation Resources** — External resource links
12. **Study Guide Files This Week** — `info-table` mapping file numbers to content focus

Each sub-accordion ends with `<hr>`.

---

## Section 2: Historical & Cultural Context

Sub-accordions per topic (e.g., "Ancient Near Eastern Setting", "The Akedah in Jewish and Christian Tradition"). Content is narrative prose with:
- `<h3>` sub-headings within each sub-panel
- Bullet lists for archaeological evidence, traditions
- Inline lexicon links for Hebrew terms
- Blockquotes for prophetic/scholarly quotes
- Scripture links (auto-detected by ScriptTagger + manual BLB links)

---

## Section 3: Key Passages Study

Sub-accordions per passage (e.g., "Passage 1: The Theophany at Mamre (Genesis 18:1–15)").

Each passage contains:

```html
<button class="sg-sub-accordion"><span>Passage N: Title (Verse Range)</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">

<h3>Text Focus</h3>
<blockquote><p><em>Key verse quotation...</em></p></blockquote>

<h3>Analysis</h3>
<ul>
  <li>Verse-by-verse commentary points</li>
  <li><strong>Bold principle:</strong> Explanation</li>
</ul>

<h3>Cross-References</h3>
<ul>
  <li><a href="BLB_URL" target="_blank">Verse</a> — description</li>
</ul>

<h3>Prophetic Witness</h3>
<blockquote>
  <p>"Quote from General Authority or scholar."</p>
  <p>— <strong>Speaker Name</strong>, "<a href="URL" target="_blank">Talk Title</a>", Conference</p>
</blockquote>

<hr>
</div>
</div>
```

---

## Section 4: Word Studies

This is the most structured section. Each word study follows this exact pattern:

```html
<button class="sg-sub-accordion"><span>Word Study N: HEBREW (<em>transliteration</em>) — "English Meaning"</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">

<p><strong>Root:</strong> ROOT_LETTERS (Letter-Letter-Letter)</p>

<p><strong>Appears:</strong> Verse — "quote with <a href="https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/"
   target="_blank"
   data-lexicon="brief definition"
   data-strongs="HNNNN"
   data-translit="word"
   data-original="HEBREW"
   data-lang="hebrew"
   data-verse="Verse"><em>transliterated_word</em></a>"</p>

<h3>Meaning</h3>
<p>Narrative explaining the root and its semantic range...</p>

<h3>Related Forms</h3>
<table class="info-table">
<tr><th>Form</th><th>Meaning</th><th>Example</th></tr>
<tr>
  <td>HEBREW (<a href="https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/"
     target="_blank"
     data-lexicon="definition"
     data-strongs="HNNNN"
     data-translit="word"
     data-original="HEBREW"
     data-lang="hebrew"
     data-verse="Verse"><em>word</em></a>)</td>
  <td>English meaning</td>
  <td>Verse — "quote"</td>
</tr>
</table>

<h3>Theological Significance</h3>
<p>Narrative connecting to doctrine, application...</p>

<h3>LDS Application</h3>
<ul>
  <li><a href="SCRIPTURE_URL" target="_blank">Verse</a>: "quote"</li>
</ul>

<h3>Cross-Language Connections</h3>
<table class="info-table">
<tr><th>Language</th><th>Word</th><th>Meaning</th><th>Reference</th></tr>
<tr>
  <td><strong>Greek (LXX)</strong></td>
  <td><a href="https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/"
     target="_blank"
     data-lexicon="definition"
     data-strongs="GNNNN"
     data-translit="transliteration"
     data-original="GREEK_CHARS"
     data-lang="greek"
     data-verse="LXX verse ref">GREEK_WORD</a> (transliteration)</td>
  <td>English meaning</td>
  <td>LXX verse reference</td>
</tr>
<tr>
  <td><strong>Latin (Vulgate)</strong></td>
  <td><a href="https://logeion.uchicago.edu/LATIN_WORD" target="_blank">latin_word</a></td>
  <td>English meaning</td>
  <td>Vulgate verse reference</td>
</tr>
<tr>
  <td><strong>English</strong></td>
  <td><a href="https://www.merriam-webster.com/dictionary/WORD" target="_blank">word</a>
     (<a href="https://webstersdictionary1828.com/Dictionary/WORD" target="_blank">1828</a>),
     <a href="https://www.merriam-webster.com/dictionary/WORD2" target="_blank">word2</a>
     (<a href="https://webstersdictionary1828.com/Dictionary/WORD2" target="_blank">1828</a>)</td>
  <td>Etymology connection explanation</td>
  <td>—</td>
</tr>
</table>

<hr>
</div>
</div>
```

### Key Rules for Word Studies

1. **Every Hebrew term** gets full `data-lexicon` popup attributes on BLB links
2. **Cross-Language Connections table is MANDATORY** for every word study — no exceptions. The `link-audit.py` script checks for this automatically (`MISSING CROSS-LANG` issue type).
3. **Greek (LXX) row** — BLB link with `data-lexicon` popup attributes (`data-lang="greek"`)
4. **Latin (Vulgate) row** — Plain link to `logeion.uchicago.edu/WORD` (no popup attributes)
5. **English row** — Each English word gets MW link + `(1828)` link in parentheses; multiple words separated by commas
6. **English Reference column** — Always `—` (dash)
7. **`<hr>` separator** between word studies (after the closing `</table>`)
8. **Sub-headings** within word studies use `<h3>` (Meaning, Related Forms, Theological Significance, LDS Application, Cross-Language Connections)

---

## Section 5: Jewish Perspective

Sub-accordions per insight topic (e.g., "Isaac's Evening Devotion", "Twelve Stones Becoming One"). Each insight follows this pattern:

```html
<button class="sg-sub-accordion"><span>Example N: Insight Title</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">

<h3>The Biblical Text</h3>
<blockquote><p><em>Key verse quotation (KJV)...</em></p></blockquote>

<h3>The Jewish Insight</h3>
<p><strong>Source Name</strong> (e.g., Targum Onkelos, Midrash Rabbah, Pirke de-Rabbi Eliezer):</p>
<blockquote><p>Quote or paraphrase from the Jewish source...</p></blockquote>
<p>Explanation of the tradition and its significance...</p>

<h3>Why This Matters for LDS Readers</h3>
<p><strong>Connection to LDS Practice/Theology:</strong></p>
<p>How this insight connects to Latter-day Saint beliefs, practices, or scripture...</p>
<ul>
  <li>Specific LDS scripture connections</li>
  <li>Practical applications</li>
</ul>

<h3>Discussion Questions</h3>
<ul>
  <li>Question connecting the insight to personal application...</li>
</ul>

<hr>
</div>
</div>
```

### Content Guidelines for Section 5

1. **Introduction sub-accordion** — Brief explanation of why Jewish sources matter for OT study, with a respectful framing note
2. **3–6 insight examples** per week — Each presenting a specific Jewish interpretive tradition with:
   - The biblical text it illuminates
   - The Jewish source and its insight
   - A clear connection to LDS theology or practice
   - Discussion questions for personal/class study
3. **Conclusion sub-accordion** — Summary and encouragement to respectfully engage with these traditions
4. **Source attribution** — Always name the specific Jewish source (Targum Onkelos, Talmud Bavli tractate/page, Midrash Rabbah section, etc.)
5. **Respectful framing** — Present as "enriching context," not as competing with or superseding LDS doctrine
6. **Cross-links** — Link to relevant Culture section articles (e.g., Jewish Texts Primer, PaRDeS Model) where appropriate

### Source File Convention

Jewish Perspective content for each week should be authored in the Obsidian vault at:
```
WeeklyLessons/Week_NN_.../03_Study_Guide/07_Jewish_Perspective.md
```

---

## Section 6: Teaching Applications

Sub-accordions per teaching context:

```html
<button class="sg-sub-accordion"><span>Teaching Setting Title</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">
<h3>Activity/Approach Title</h3>
<p>Description...</p>
<ul><li>Steps or discussion points</li></ul>
<hr>
</div>
</div>
```

---

## Section 7: Study Questions

Sub-accordions grouped by question type (e.g., "Comprehension Questions", "Analysis Questions", "Application Questions", "Synthesis Questions"):

```html
<button class="sg-sub-accordion"><span>Question Type (N questions)</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">
<ol>
  <li>Question text with scripture references...</li>
</ol>
<hr>
</div>
</div>
```

---

## Linking System

### 1. Scripture References (Auto-detected)
BLB ScriptTagger auto-detects plain-text scripture references (e.g., "Genesis 18:14") and converts them to hoverable links. **No manual markup needed** for standard references.

For explicit BLB scripture links (used in lists, specific formatting):
```html
<a href="https://www.blueletterbible.org/kjv/gen/18/14/s_18014" target="_blank">Genesis 18:14</a>
```

### 2. Hebrew Lexicon Links (BLB — Hover Popup)
```html
<a href="https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/"
   target="_blank"
   data-lexicon="brief definition"
   data-strongs="HNNNN"
   data-translit="transliteration"
   data-original="HEBREW_CHARS"
   data-lang="hebrew"
   data-verse="Book Ch:Vs"><em>word</em></a>
```
- **Behavior:** Hover shows popup with definition, original, Strong's, verse; click is prevented on the link; popup has "Full entry at BLB →" link
- **Styling:** `cursor: help`, sage-green with dotted underline

### 3. Greek Lexicon Links (BLB — Hover Popup)
```html
<a href="https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/"
   target="_blank"
   data-lexicon="brief definition"
   data-strongs="GNNNN"
   data-translit="transliteration"
   data-original="GREEK_CHARS"
   data-lang="greek"
   data-verse="LXX verse ref">GREEK_WORD</a>
```
- Same popup system as Hebrew, `data-lang="greek"`

### 4. Latin Dictionary (Logeion — Regular Link)
```html
<a href="https://logeion.uchicago.edu/WORD" target="_blank">latin_word</a>
```
- Opens new tab, no popup

### 5. English Dictionary (Merriam-Webster — Regular Link)
```html
<a href="https://www.merriam-webster.com/dictionary/WORD" target="_blank">word</a>
```

### 6. English Dictionary (Webster's 1828 — Regular Link)
```html
(<a href="https://webstersdictionary1828.com/Dictionary/WORD" target="_blank">1828</a>)
```
- Always in parentheses, always immediately after the MW link for the same word

### 7. Google Maps Satellite Links
```html
<a href="https://www.google.com/maps/place/COORDS&t=k" target="_blank">Place Name</a>
```
- `&t=k` parameter for satellite view

### 8. Content-Area Links (General)
- Styled via CSS `.panel-content a` and `.sg-sub-panel-content a` — sage-brown (`#8B7355`), hover underline

---

## CSS Classes Reference

| Class | Purpose |
|-------|---------|
| `.container` | Main content wrapper, max-width 1000px |
| `.header-section` | Brown gradient header with week title |
| `.quick-links` / `.quick-link` | CFM Manual button links |
| `.expand-button` | Expand/Collapse All buttons |
| `.sg-accordion-section` | Major section header (brown, clickable) |
| `.sg-panel` | Major section content panel |
| `.panel-content` | Padding wrapper inside `.sg-panel` |
| `.sg-sub-accordion` | Sub-section header (cream/tan, clickable) |
| `.sg-sub-panel` | Sub-section content panel |
| `.sg-sub-panel-content` | Padding wrapper inside `.sg-sub-panel` |
| `.sg-section-title` | Title text span inside major section |
| `.sg-section-actions` | Per-section expand/collapse button container |
| `.sg-action-btn` | Per-section expand/collapse buttons |
| `.info-table` | Data tables — bordered, alternating rows |
| `.nq` | Nikud/dagesh red highlighting (`#c0392b`) |
| `.BLBScriptRef` | ScriptTagger auto-generated scripture links |
| `.sg-section-heading` | Left-bordered sub-heading within panels |

---

## Table Pattern

All data tables use `.info-table`:

```html
<table class="info-table">
<tr><th>Column 1</th><th>Column 2</th><th>Column 3</th></tr>
<tr><td>data</td><td>data</td><td>data</td></tr>
<tr><td>data</td><td>data</td><td>data</td></tr>
</table>
```

**Styling:**
- Headers: cream background (`#f5f0e8`), brown text (`#6B5344`), bold
- Borders: `1px solid #d4c4a8`
- Alternating rows: even rows get `#faf8f5`
- Padding: 12px
- Full width

---

## Blockquote Pattern

```html
<blockquote>
<p><em>Quote text...</em></p>
</blockquote>
```

Or with attribution:
```html
<blockquote>
<p>"Quote text."</p>
<p>— <strong>Speaker Name</strong>, "<a href="URL" target="_blank">Source Title</a>", Context</p>
</blockquote>
```

**Styling:** Left border `4px solid #8B7355`, cream background (`#faf8f5`), italic text, rounded right corners.

---

## JavaScript Functions

The study guide relies on these JS functions (defined in the site's base template or inline):

| Function | Trigger | Behavior |
|----------|---------|----------|
| `toggleSection(el)` | Click on `.sg-accordion-section` | Toggle `.sg-panel` visibility |
| `expandAll()` | Expand All button | Open all panels and sub-panels |
| `collapseAll()` | Collapse All button | Close all panels and sub-panels |
| `expandSection(btn)` | Per-section ⊞ button | Expand all sub-panels in that section |
| `collapseSection(btn)` | Per-section ⊟ button | Collapse all sub-panels in that section |

Sub-accordion toggle is handled by click event listeners that toggle `.active` class and `display` style.

---

## Color Palette (Study Guide)

| Color | Hex | Usage |
|-------|-----|-------|
| Brown (primary) | `#8B7355` | Headers, accordion sections, links, accents |
| Dark brown | `#6B5344` | Hover states, h3/h4 headings, bold text |
| Deep brown | `#5a4a3a` | Body text emphasis, h4 |
| Cream | `#f5f0e8` | Sub-accordion backgrounds, table headers |
| Light cream | `#faf8f5` | Blockquote backgrounds, alternating rows |
| Border tan | `#d4c4a8` | Table borders, sub-panel borders |
| Warm hover | `#e8e0d4` | Sub-accordion hover |
| Sage-green accent | `#8B9D77` | Section heading left border |
| Sage heading text | `#5a6b4f` | `.sg-section-heading` text |
| Nikud red | `#c0392b` | `.nq` class for Hebrew diacritics |

---

## Weekly Study Guide Checklist

### Content Creation
- [ ] Create `static/content/weekNN/study-guide.html`
- [ ] Header section: week number, reading range, theme title, dates
- [ ] Quick link to CFM Manual lesson

### Section 1: Week Overview
- [ ] Week Information table
- [ ] Reading Summary (paragraph per chapter)
- [ ] Central Themes (3–5 themes with h3 headings)
- [ ] Key Figures table
- [ ] Timeline Placement
- [ ] Restoration Scripture Connections (BofM, D&C)
- [ ] Key Doctrines list
- [ ] Temple Connections
- [ ] CFM Manual Emphasis
- [ ] Suggested Reading Approach

### Section 2: Historical & Cultural Context
- [ ] ANE setting and cultural background
- [ ] Archaeological evidence where relevant
- [ ] Jewish/Christian tradition context
- [ ] Geographic references with maps where helpful

### Section 3: Key Passages Study
- [ ] 3–6 key passages identified
- [ ] Each has: Text Focus blockquote, Analysis, Cross-References
- [ ] Prophetic Witness quotes where available

### Section 4: Word Studies
- [ ] 4–6 Hebrew words selected
- [ ] Each has: Root, Appears, Meaning, Related Forms table
- [ ] Each has: Theological Significance, LDS Application
- [ ] Each has: Cross-Language Connections table (Greek/Latin/English)
- [ ] All Hebrew links have `data-lexicon` popup attributes
- [ ] Greek links in Cross-Language table have popup attributes
- [ ] Latin links point to Logeion (regular links)
- [ ] English links: MW + (1828) for each word
- [ ] `<hr>` separator between word studies
- [ ] New terms added to `lexicon-popups.json`

### Section 5: Jewish Perspective
- [ ] Introduction with respectful framing note
- [ ] 3–6 insight examples from Jewish sources
- [ ] Each has: Biblical Text, Jewish Insight, LDS Connection, Discussion Questions
- [ ] Sources properly attributed (specific text, tractate, chapter)
- [ ] Cross-links to Culture section articles where relevant
- [ ] Conclusion with summary

### Section 6: Teaching Applications
- [ ] 3–5 teaching settings/activities
- [ ] Practical, actionable suggestions

### Section 7: Study Questions
- [ ] Grouped by type (Comprehension, Analysis, Application, Synthesis)
- [ ] 20+ questions total
- [ ] Scripture references in questions

### Final Checks
- [ ] All sub-panels have `style="display: block;"` (open by default)
- [ ] All sections end with `<hr>` before closing tags
- [ ] File status footer at end of Section 1
- [ ] Test expand/collapse functionality
- [ ] Test lexicon hover popups
- [ ] Test ScriptTagger scripture detection
- [ ] Verify all external links open in new tab (`target="_blank"`)
- [ ] Run `link-audit.py --type study-guide` — zero BARE HEBREW, BARE ROOT, BARE BLB LINK, and MISSING CROSS-LANG issues
- [ ] If issues found, run `link-audit.py --fix --week weekNN` to auto-link bare terms (Cross-Language tables require manual creation)

---

*Version 1.1 — 2026-03-01*
*Canonical Example: Week 09 (`static/content/week09/study-guide.html`)*

---

> **Brought to `main` 2026-08-15.** This section was written 2026-08-13 and lived only on
> `claude/week-34`, so it postdated weeks 30–33 and was invisible to any session working
> from `main` — which is where lessons are built. The Fable audit (K2) measured its effect
> when it WAS applied: week 34's insights-prose overlap fell **275 → 52** of 2,939 shingles,
> and the Key Passages section went **199 → 0**. Verbatim; nothing rewritten.

## Division of labour: the study guide vs Weekly Insights

**This is the rule that stops the two files converging. Read it before writing either.**

The study guide and the Weekly Insights essay cover the same passages. Left alone, they drift into
saying the same things about them — because they are organised on the same axis. This has recurred
for several weeks running and it is structural, not carelessness.

| | Weekly Insights | Study Guide |
|---|---|---|
| Answers | **What does it mean for me?** | **How do we know?** |
| Voice | devotional, second person, lands a point | instructional, shows the working |
| Carries | the conclusion | the mechanism, the Hebrew, the counts, the method |
| Reader arrives | wanting to be moved | wanting to check, or to learn the skill |

**The real rule: show the mechanism and stop.**

The study guide points at a feature of the text and says how a reader could find it. It does **not**
then say what the feature means. That last step is the essay's, and doing it in both places is what
makes a lesson read as preachy — the second telling implies the reader did not get it the first
time, which is condescending whether or not the wording is new.

Concretely, on Psalm 46:

| | |
|---|---|
| ✅ study guide | "*'eretz*, 'earth', sounds five times: vv. 2, 6, 8, 9, 10. Mark those, then note which verse sits between the last two." |
| ❌ study guide | "…so 'be still' sits inside a frame of the whole shaking earth." |
| ✅ Insights | owns the meaning of that, and already says it better |

The second version is not wrong — it is *already said*. Handing the reader the count and letting
them see it lands harder than telling them twice.

**Beware of paraphrase.** Rewriting the essay's sentence in different words does not fix redundancy;
it only hides it from a word-overlap check. The 2026-08-13 revision initially kept "the alphabet is
a handrail" and the whole shaking-earth conclusion while scoring well on overlap. **Redundancy is a
question about concepts, not vocabulary.** Read the two files side by side and ask whether the
reader learns a second thing — not whether the sentences differ.

**The paste test still applies as a backstop.** If a study-guide paragraph could be pasted into
Insights and nobody would notice, it belongs to Insights.

**What the study guide should carry instead**, in order of value:

1. **Structure a reader can find themselves** — a frame, a turn, a refrain, a pronoun shift. Say
   which verse, and say how to spot the same move elsewhere.
2. **Where the Hebrew adds something English cannot** — and be specific about what is lost.
3. **Counts, with their method attached.** Never print a number without saying *what* was counted
   and *in which language*. Psalm 24 is the standing example: the root *nasa'* appears six times in
   Hebrew but "lift up" appears four times in the KJV, and a reader who counts in English will
   conclude the Hebrew count is wrong.
4. **How a claim was verified** — the acrostic check, the manuscript question, the lemma-level
   comparison. A reader who can repeat the check does not have to take our word for anything.
5. **Honest limits.** Where a sense is lost (*al-alamoth*), where a reading is disputed
   (Psalm 22:16), where a tool was silent for a mechanical reason rather than a real one.

**Correct duplication exists.** Both files quote the same scripture, and both name the same psalms.
Shared *verses* are fine. Shared *explanation* is the defect.

**A word-overlap check is a smoke alarm, not the standard.** Comparing 8-word runs between the two
rendered files will catch copy-paste — Week 34 ran 9.2%, rose to 11.6% when a passage was written by
reusing the essay's prose, and fell to 5.7% after rewriting. Useful, and it caught a real problem.
But it passed a draft that still repeated every concept in fresh words. **Use it to catch the
careless case; use the reading test above to catch the real one.**

---

## Section 3: Key Passages Study
