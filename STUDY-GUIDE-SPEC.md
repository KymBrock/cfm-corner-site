# Study Guide HTML Specification

Complete format specification for CFM Corner weekly study guides. Canonical example: **Week 09** (`static/content/week09/study-guide.html`).

---

## Overview

Each study guide is a single HTML file embedded via Hugo into the site layout. It contains inline `<style>`, a header section, quick links, expand/collapse buttons, and 6 major accordion sections. No external CSS file — all styles are self-contained in the HTML.

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

  <!-- SECTION 1–6: Major Accordion Sections -->
  ...
</div>
```

---

## Major Accordion Sections (6 total)

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

### The 6 Sections

| # | Title Pattern | Contains |
|---|--------------|----------|
| 1 | `Book Chapter–Chapter` (e.g., "Genesis 18–23") | Week Overview sub-sections |
| 2 | `Week NN: Historical & Cultural Context` | ANE context, archaeology, tradition |
| 3 | `Week NN: Key Passages Study` | Verse-by-verse analysis per passage |
| 4 | `Week NN: Word Studies` | Hebrew word studies with cross-language tables |
| 5 | `Week NN: Teaching Applications` | Per-setting teaching ideas |
| 6 | `Week NN: Study Questions` | Grouped by question type |

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
2. **Greek (LXX) row** — BLB link with `data-lexicon` popup attributes (`data-lang="greek"`)
3. **Latin (Vulgate) row** — Plain link to `logeion.uchicago.edu/WORD` (no popup attributes)
4. **English row** — Each English word gets MW link + `(1828)` link in parentheses; multiple words separated by commas
5. **English Reference column** — Always `—` (dash)
6. **`<hr>` separator** between word studies (after the closing `</table>`)
7. **Sub-headings** within word studies use `<h3>` (Meaning, Related Forms, Theological Significance, LDS Application, Cross-Language Connections)

---

## Section 5: Teaching Applications

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

## Section 6: Study Questions

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

### Section 5: Teaching Applications
- [ ] 3–5 teaching settings/activities
- [ ] Practical, actionable suggestions

### Section 6: Study Questions
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

---

*Version 1.0 — 2026-02-19*
*Canonical Example: Week 09 (`static/content/week09/study-guide.html`)*
