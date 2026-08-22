# Lexicon Popup Specification

Inline hover popups for Hebrew/Greek dictionary links, parallel to BLB ScriptTagger for scripture references.

> **Read this before the checklist. Corrected 2026-08-15.**
>
> This document was written 2026-03-01 and **was not updated when the publishing rules
> changed in late July**. For four months its checklist told sessions to run
> `link-audit.py --fix` on published weeks, which is the exact mass-edit the collision
> discipline forbids — and sessions followed it, because it was the instruction they
> found. It is referenced from **no** `CLAUDE.md`, so nothing corrected it either.
>
> The rule it was missing: **a published fragment is never auto-fixed or regenerated.**
> Surgical anchor replacement only. Staged weeks are unaffected.
>
> `link-audit.py` now refuses `--fix` on any week present on live `main`, so the tool no
> longer depends on this document being read correctly.
>
> Related: `blb-scraping-prohibited` and `lexicon-popups-authority` in Translation Hub
> `scriptorium/decisions.json`. The popup data is no longer sourced from Blue Letter
> Bible — it is built from STEPBible, Strong's 1890 and Hitchcock 1869, all public domain.

---

## How It Works

Any `<a>` tag with a `data-lexicon` attribute triggers a hover popup instead of navigating away. The popup displays the original word, transliteration, Strong's number, definition, key verse, and a link to the full BLB entry.

The system is loaded site-wide in `baseof.html` (after ScriptTagger).

---

## Required Data Attributes

| Attribute | Required | Example | Description |
|-----------|----------|---------|-------------|
| `data-lexicon` | ✅ | `"to be wonderful, extraordinary"` | Brief definition (also serves as the feature flag) |
| `data-strongs` | ✅ | `"H6381"` or `"G2298"` | Strong's number (H = Hebrew, G = Greek) |
| `data-translit` | ✅ | `"pala"` | Transliteration |
| `data-original` | ✅ | `"פָּלָא"` or `"θαυμαστός"` | Original script characters |
| `data-lang` | ✅ | `"hebrew"` or `"greek"` | Language (controls font rendering) |
| `data-verse` | Optional | `"Genesis 18:14"` | Key verse reference |

---

## HTML Pattern

### Hebrew Example
```html
<a href="https://www.blueletterbible.org/lexicon/h6381/kjv/wlc/0-1/"
   target="_blank"
   data-lexicon="to be wonderful, surpassing, extraordinary"
   data-strongs="H6381"
   data-translit="pala"
   data-original="פָּלָא"
   data-lang="hebrew"
   data-verse="Genesis 18:14"><em>pala</em></a>
```

### Greek Example (in Cross-Language tables)
```html
<a href="https://www.blueletterbible.org/lexicon/g2298/kjv/tr/0-1/"
   target="_blank"
   data-lexicon="wonderful, marvelous"
   data-strongs="G2298"
   data-translit="thaumastos"
   data-original="θαυμαστός"
   data-lang="greek"
   data-verse="Psalm 118:23">θαυμαστός</a>
```

---

## BLB URL Patterns

- **Hebrew:** `https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/`
- **Greek:** `https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/`

The `h` or `g` prefix in the URL determines Hebrew vs Greek.

---

## Popup Behavior

- **Hover:** Shows popup below the link with definition, original script, transliteration, Strong's number, verse reference
- **Click:** Prevented on the link itself — popup contains "Full entry at Blue Letter Bible →" link for those who want the full page
- **Mouse-out:** Popup fades after 200ms (allows moving cursor into popup)
- **Mobile:** Falls back to click-to-show (touch events)

---

## Styling

- Links with `data-lexicon` get `cursor: help`
- Existing sage-green dotted underline styling (from inline styles or CSS) is preserved
- Popup uses site brand colors: sage-dark border, 8px rounded corners, light shadow

---

## Where Lexicon Links Appear

1. **Study Guide** (`study-guide.html`) — ALL sections:
   - Section 1 (Week Overview): Reading Summary, Central Themes — any Hebrew/Greek terms
   - Section 2 (Historical & Cultural Context): ANE setting, archaeology, sacred geography
   - Section 3 (Key Passages Study): Analysis, cross-references — Hebrew terms in commentary
   - Section 4 (Word Studies): All occurrences, Related Forms tables, Cross-Language tables
   - Section 5 (Jewish Perspective): Hebrew terms in source citations and commentary
   - Section 6 (Teaching Applications): Any Hebrew/Greek terms that appear
   - Section 7 (Study Questions): Rarely, but link if present
2. **Weekly Insights** (`insights.html`)
   - Hebrew section spotlight terms
   - Any Hebrew/Greek terms in narrative text
3. **Resources** (`resources.html`) — any Hebrew/Greek terms in video descriptions or resource annotations
4. **Hebrew Lessons** (`/hebrew/` section) — future

---

## Obsidian Markdown Convention

In Obsidian source files, lexicon links use standard markdown with a special format that the converter can detect:

```markdown
[*pala*](https://www.blueletterbible.org/lexicon/h6381/kjv/wlc/0-1/ "H6381|פָּלָא|to be wonderful, extraordinary|Genesis 18:14")
```

The title attribute encodes: `Strong's|Original|Definition|Verse` (pipe-delimited).

If no title is provided, the converter extracts the Strong's number from the URL and looks it up in the lexicon data file.

---

## Lexicon Data File

A shared JSON lookup at `cfm-corner-tools/data/lexicon-popups.json`:

```json
{
  "H6381": {
    "translit": "pala",
    "original": "פָּלָא",
    "lang": "hebrew",
    "definition": "to be wonderful, surpassing, extraordinary",
    "verse": "Genesis 18:14"
  },
  "G2298": {
    "translit": "thaumastos",
    "original": "θαυμαστός",
    "lang": "greek",
    "definition": "wonderful, marvelous",
    "verse": "Psalm 118:23"
  }
}
```

This file grows as new terms are introduced each week. The converter reads it during HTML generation.

---

## Non-Lexicon Links (Do NOT Popup)

- **Logeion links** (`logeion.uchicago.edu`) — Latin dictionary, regular navigation
- **Merriam-Webster links** — English dictionary, regular navigation  
- **Scripture references** — Handled by BLB ScriptTagger (separate system)
- **Webster's 1828 links** (`webstersdictionary1828.com`) — Historical English dictionary, regular navigation, always paired with Merriam-Webster link in format: `word (1828)`
- **Any link without `data-lexicon`** — Normal behavior

---

## Comprehensive Coverage Rule

> **Every occurrence of Hebrew/Greek Unicode characters in body text must be inside a lexicon `<a>` tag with full `data-*` attributes.** The only exception is accordion `<button>` headings, where nesting `<a>` inside `<button>` causes click-handler conflicts.

This rule was established after Week 10 (March 2026), when 23 bare Hebrew terms were found across multiple study guide sections that the audit script had not been scanning.

---

## Checklist for Each Week

- [ ] Identify **every** Hebrew/Greek term across **all** study guide and insights sections
- [ ] Look up Strong's numbers via BLB for each term
- [ ] Add entries to `lexicon-popups.json` for any new terms
- [ ] **Every Hebrew/Greek Unicode character** in body text (outside `<button>` headings) has a lexicon link with all `data-*` attributes
- [ ] Word study sections link all occurrences
- [ ] Cross-Language tables include Greek lexicon links with popup attributes
- [ ] Run `link-audit.py` on **all three** files (study-guide, insights, resources)
- [ ] **Read the residual — do NOT chase zero.** A fully linked week is *not* zero BARE
      HEBREW. Intentionally bare script is required beside transliterations, and divine
      names and rabbinic terms stay bare on purpose. Week 26's correct residual is **14
      flags** — the forms Kymber specified herself (`לַה׳`, `ה׳`, `גֵּט`, `חִלּוּל`,
      `עֲגוּנָה`, `עֲגוּנוֹת`, `קְרִיעָה`). A session that drives this to zero will
      "fix" text that was already right.
- [ ] **If issues found, the FIRST question is whether the week is PUBLISHED.**
  - **Published on live `main`** → **surgical anchor replacement only.** Rewrite the one
    wrong `<a>`; leave every surrounding byte alone. **Never `--fix`, never regenerate.**
    `link-audit.py --fix` refuses on a published week and exits non-zero — that guard
    exists because this line told sessions to do the opposite for four months.
  - **Staged / unpublished** → `link-audit.py --fix --week weekNN` is fine, scoped to the
    one week. Kymber, 2026-08-04: *"Regeneration is fine — Week 33 isn't published yet."*
- [ ] Verify any fix against the **live page**, with a positive control. Production
      minifies HTML and strips attribute quotes, which has silently defeated greps here.
- [ ] Test hover popups in local preview
- [ ] Check for BLB lexicon `<a>` tags missing `data-lexicon` attributes (the audit script catches these as BARE BLB LINK)

---

---

## Cross-Language Connections Table Pattern

> **MANDATORY:** Every word study MUST include a Cross-Language Connections table. The `link-audit.py` script enforces this (`MISSING CROSS-LANG` issue type). There are no exceptions.

Word studies include a 3-row cross-language table connecting Hebrew roots to Greek, Latin, and English cognates. Each row uses a different link type:

```html
<h3>Cross-Language Connections</h3>
<table class="info-table">
<tr><th>Language</th><th>Word</th><th>Meaning</th><th>Reference</th></tr>

<!-- Row 1: Greek (LXX) — BLB lexicon link WITH popup attributes -->
<tr>
  <td><strong>Greek (LXX)</strong></td>
  <td><a href="https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/"
     target="_blank"
     data-lexicon="definition"
     data-strongs="GNNNN"
     data-translit="transliteration"
     data-original="GREEK_CHARS"
     data-lang="greek"
     data-verse="LXX verse">GREEK_WORD</a> (transliteration)</td>
  <td>English meaning</td>
  <td>LXX verse reference</td>
</tr>

<!-- Row 2: Latin (Vulgate) — Logeion link, regular navigation, NO popup -->
<tr>
  <td><strong>Latin (Vulgate)</strong></td>
  <td><a href="https://logeion.uchicago.edu/LATIN_WORD" target="_blank">latin_word</a></td>
  <td>English meaning</td>
  <td>Vulgate verse reference</td>
</tr>

<!-- Row 3: English — MW link + (1828) link for each word -->
<tr>
  <td><strong>English</strong></td>
  <td><a href="https://www.merriam-webster.com/dictionary/WORD" target="_blank">word</a>
     (<a href="https://webstersdictionary1828.com/Dictionary/WORD" target="_blank">1828</a>),
     <a href="https://www.merriam-webster.com/dictionary/WORD2" target="_blank">word2</a>
     (<a href="https://webstersdictionary1828.com/Dictionary/WORD2" target="_blank">1828</a>)</td>
  <td>Etymology connection</td>
  <td>—</td>
</tr>
</table>
```

### Rules
- **Greek row:** Always includes full `data-lexicon` popup attributes (same system as Hebrew)
- **Latin row:** Plain `<a>` to Logeion — no popup attributes
- **English row:** Each English word gets two links: Merriam-Webster followed by `(1828)` in parentheses; multiple words separated by commas
- **English Reference column:** Always `—` (em dash)

---

## Dictionary URL Patterns

| Dictionary | URL Pattern | Link Type |
|-----------|-------------|-----------|
| BLB Hebrew Lexicon | `https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/` | Popup (via `data-lexicon`) |
| BLB Greek Lexicon | `https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/` | Popup (via `data-lexicon`) |
| Logeion (Latin) | `https://logeion.uchicago.edu/WORD` | Regular link |
| Merriam-Webster | `https://www.merriam-webster.com/dictionary/WORD` | Regular link |
| Webster's 1828 | `https://webstersdictionary1828.com/Dictionary/WORD` | Regular link (in parentheses after MW) |

**Notes:**
- `hNNNN` / `gNNNN` — Strong's number (e.g., `h6381`, `g2298`)
- Hebrew uses `/wlc/` (Westminster Leningrad Codex); Greek uses `/tr/` (Textus Receptus)
- Logeion WORD is the Latin dictionary form (e.g., `mirabilis`, `rideo`, `ligo`)
- MW and 1828 WORD is lowercase English (e.g., `miracle`, `provision`)

---

*Version 1.2 — 2026-03-01*
