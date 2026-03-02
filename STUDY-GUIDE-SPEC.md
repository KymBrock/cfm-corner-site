# Study Guide HTML Specification

Complete format specification for CFM Corner weekly study guides. Canonical example: **Week 09** (`static/content/week09/study-guide.html`).

---

## Overview

Each study guide is a single HTML file embedded via Hugo into the site layout. It contains inline `<style>`, a header section, quick links, expand/collapse buttons, and 7 major accordion sections. No external CSS file — all styles are self-contained in the HTML. The `<style>` block is generated automatically by `hugo_converter.py` (stored as `SG_STYLE_BLOCK` class constant).

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

| # | Title Pattern | Source File | Contains |
|---|--------------|------------|----------|
| 1 | `Book Chapter–Chapter` (e.g., "Genesis 24–33") | `01_Week_Overview.md` | Week Overview sub-sections |
| 2 | `Week NN: Historical & Cultural Context` | `02_Historical_Cultural_Context.md` | ANE context, archaeology, tradition |
| 3 | `Week NN: Key Passages Study` | `03_Key_Passages_Study.md` | Verse-by-verse analysis per passage |
| 4 | `Week NN: Word Studies` | `04_Word_Studies.md` | Hebrew word studies with cross-language tables |
| 5 | `Jewish Perspective: Book Chapter–Chapter` | `05_Jewish_Perspective.md` | Jewish interpretive traditions with LDS connections |
| 6 | `Week NN: Teaching Applications` | `06_Teaching_Applications.md` | Per-setting teaching ideas |
| 7 | `Week NN: Study Questions` | `07_Study_Questions.md` | Grouped by question type |

**Section numbering:** The converter (`hugo_converter.py`) numbers sections dynamically based on the alphabetical sort order of `*.md` files in `03_Study_Guide/`. Adding or removing files automatically renumbers all sections.

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
- Inline lexicon links for Hebrew terms (every Hebrew/Greek Unicode character must be linked)
- Blockquotes for prophetic/scholarly quotes
- Scripture links (auto-detected by ScriptTagger + manual BLB links)
- Location links with multi-source map resources (Key Locations sub-section)

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
2. **Greek (LXX) row** — BLB link with `data-lexicon` popup attributes (`data-lang="greek"`)
3. **Latin (Vulgate) row** — Plain link to `logeion.uchicago.edu/WORD` (no popup attributes)
4. **English row** — Each English word gets MW link + `(1828)` link in parentheses; multiple words separated by commas
5. **English Reference column** — Always `—` (dash)
6. **`<hr>` separator** between word studies (after the closing `</table>`)
7. **Sub-headings** within word studies use `<h3>` (Meaning, Related Forms, Theological Significance, LDS Application, Cross-Language Connections)

---

## Section 5: Jewish Perspective

Sub-accordions per topic, exploring how Jewish interpretive traditions illuminate the week's reading. Content respectfully engages Jewish sources while maintaining an LDS theological framework.

**Source file:** `05_Jewish_Perspective.md`

**Required sub-sections (minimum):**
1. **Introduction: Why Jewish Sources Matter** — Brief framing of the value of Jewish interpretive traditions for LDS readers
2. **3–5 topical sub-accordions** — Each examines a specific passage or theme through Jewish lenses (Targumim, Midrash, Talmud, medieval commentators like Rashi, Ramban, etc.)
3. **Each topical section includes:**
   - Jewish source citation and explanation
   - LDS doctrinal connection or parallel
   - Practical application for modern covenant-keeping
4. **Reflection Questions** — Closing questions that bridge Jewish and LDS perspectives

```html
<button class="sg-sub-accordion"><span>Introduction: Why Jewish Sources Matter</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">
<p>Framing paragraph on the value of Jewish interpretive traditions...</p>
<p><strong>A Word About Approach:</strong></p>
<ul>
<li>We respect these as <strong>Jewish interpretive traditions</strong>, not LDS scripture</li>
<li>We look for <strong>genuine parallels</strong> rather than forced comparisons</li>
<li>We let Jewish voices speak in their own terms before connecting to our framework</li>
</ul>
<hr>
</div>
</div>

<button class="sg-sub-accordion"><span>Topic Title (e.g., "The Birthright in Jewish Tradition")</span></button>
<div class="sg-sub-panel" style="display: block;">
<div class="sg-sub-panel-content">
<h3>Jewish Source</h3>
<p>Citation and explanation from Targum, Midrash, or commentary...</p>
<h3>LDS Connection</h3>
<p>How this illuminates LDS doctrine or practice...</p>
<h3>Application</h3>
<p>Practical takeaway for covenant living...</p>
<hr>
</div>
</div>
```

### Guidelines for Jewish Perspective Content
- **Always cite sources** by name: Targum Onkelos, Midrash Rabbah, Rashi, Ramban, etc.
- **Respect Jewish tradition** — present interpretations in their own terms before drawing LDS parallels
- **Avoid forced comparisons** — genuine connections are more valuable than superficial similarities
- **Mark non-LDS sources clearly** — readers should always know when they're reading Jewish vs. LDS interpretation
- **Focus on enrichment** — this section adds depth, not replacement, to LDS scriptural understanding

### ⛔ Sourcing & Verification Requirements (Anti-Hallucination)

**NEVER fabricate, paraphrase from memory, or improvise rabbinic quotes.** Every claim attributed to a Jewish source MUST be verified against actual text in the Sacred Texts vault before inclusion.

**Sacred Texts vault:** `/Users/kymberbrockbank/Obsidian/Sacred Texts/`

**Required workflow:**
1. **Search** the Sacred Texts vault for commentary on the week's chapters:
   - Midrash Rabbah: `04_Midrash/Midrash_Rabbah/` (Genesis Rabbah for Genesis weeks, etc.)
   - Talmud Bavli: `03_Talmud/Bavli/` (34 tractates)
   - Targumim: `05_Targumim/` (Onkelos, Jonathan, Pseudo-Jonathan)
   - Mishnah: `03_Talmud/Mishnah/`
   - Additional: `04_Midrash/Tanchuma/`, `04_Midrash/Pirke_deRabbi_Eliezer/`, `06_Mystical/Zohar/`
2. **Extract** relevant passages verbatim from vault files; record the file path for traceability
3. **Cite** each source with verification status:
   - `✓ Vault` — text found and confirmed in Sacred Texts vault
   - `⚠ External` — general scholarly knowledge not verified against vault text; mark as `[UNVERIFIED — needs manual confirmation]`
4. **Kymber reviews** all Jewish Perspective content before publication — this section is never auto-deployed

**What counts as verified:**
- ✅ Text found in Sacred Texts vault file and quoted/paraphrased from it
- ✅ Tractate/chapter reference confirmed against vault file contents
- ⚠ General knowledge about a commentator's position without vault text → mark External
- ⛔ "Rashi says..." from AI memory with no vault search → **NEVER acceptable**

See `INSTRUCTIONS_FOR_CLAUDE.md` → "Jewish Perspective Sourcing Protocol" for full details, vault path table, and search examples.

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

### 7. Location Map Links (Multi-Source)

Each biblical location in the Key Locations sub-section gets compact inline links to up to three map sources:

```html
<li><strong>Bethel (Luz)</strong> — Jacob's ladder vision (Gen. 28:10-22)
  <span style="font-size: 0.85em; white-space: nowrap;">&#x1F5FA;&#xFE0E;
    <a href="https://www.holylandsite.com/bethel" target="_blank"
       style="color: #8B7355;" title="Holy Land Site: Bethel">HLS</a> ·
    <a href="https://bibleatlas.org/bethel.htm" target="_blank"
       style="color: #8B7355;" title="Bible Atlas: Bethel">Atlas</a> ·
    <a href="https://scriptures.byu.edu/mapscrip/" target="_blank"
       style="color: #8B7355;" title="BYU Scriptures Mapped">BYU</a>
  </span>
</li>
```

**Footer** at the end of the Key Locations section:
```html
<p style="font-size: 0.85em; color: #8B7355; margin-top: 10px;">
  <strong>Map Resources:</strong>
  <a href="https://www.holylandsite.com/all-biblical-sites" target="_blank" style="color: #8B7355;">Holy Land Site</a> ·
  <a href="https://bibleatlas.org/" target="_blank" style="color: #8B7355;">Bible Atlas</a> ·
  <a href="https://scriptures.byu.edu/mapscrip/" target="_blank" style="color: #8B7355;">BYU Scriptures Mapped</a>
</p>
```

**Rules:**
- **HLS** — include only when holylandsite.com has a page for that location (check `OT_Location_Map_by_Week.md`)
- **Atlas** — bibleatlas.org has most biblical locations; always include
- **BYU** — general tool (no per-location URLs); always include
- Use `&#x1F5FA;&#xFE0E;` (map icon with text variation selector) before link set
- Style links in section color (`#8B7355` for study guide)

### 8. Google Maps Satellite Links (Legacy)
```html
<a href="https://www.google.com/maps/place/COORDS&t=k" target="_blank">Place Name</a>
```
- `&t=k` parameter for satellite view
- For new content, prefer multi-source location maps (Link Type 7) instead

### 9. Content-Area Links (General)
- Styled via CSS `.panel-content a` and `.sg-sub-panel-content a` — sage-brown (`#8B7355`), hover underline

---

## Comprehensive Lexicon Coverage Rule

> **Every Hebrew/Greek Unicode character in body text must be inside a lexicon `<a>` tag with full `data-*` attributes.** The only exception is accordion `<button>` headings, where nesting `<a>` inside `<button>` causes click-handler conflicts. Run `link-audit.py` to verify zero bare terms before publishing.

This applies across ALL 7 study guide sections, not just Word Studies. Includes both contiguous Hebrew/Greek text AND dash-separated root consonants (e.g., ב-ר-כ). See `LEXICON-POPUP-SPEC.md` for the full list of sections where links are required.

**Auto-Linker:** The `hugo_converter.py` auto-linkers run automatically during generation, linking bare scriptures (`_auto_link_scriptures()`) and Hebrew/Greek terms including roots (`_auto_link_hebrew_greek()`). For post-hoc fixes: `python3 scripts/link-audit.py --fix --week weekNN`.

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
- [ ] Rabbinic commentary on key passages (Rashi, Ramban, Midrash)
- [ ] Jewish interpretive traditions relevant to the week's reading
- [ ] Connections to Jewish liturgy, practice, or holidays where applicable
- [ ] Cross-references between Jewish and Latter-day Saint insights
- [ ] Proper source citations for all rabbinic/scholarly quotes

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
- [ ] No backend metadata visible (File Status, Created, Last Updated, Next File)
- [ ] Test expand/collapse functionality
- [ ] Test lexicon hover popups
- [ ] Test ScriptTagger scripture detection
- [ ] Verify all external links open in new tab (`target="_blank"`)
- [ ] Run `link-audit.py` — zero BARE HEBREW, BARE ROOT, and BARE BLB LINK issues
- [ ] If issues found, run `link-audit.py --fix --week weekNN` to auto-link bare terms
- [ ] All Key Locations have multi-source map links (HLS where available, Atlas, BYU)
- [ ] Every Hebrew/Greek Unicode character in body text is inside a lexicon `<a>` tag

---

*Version 1.2 — 2026-03-01*
*Canonical Examples: Week 09 (`static/content/week09/study-guide.html`), Week 10 (`static/content/week10/study-guide.html`)*
