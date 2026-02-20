# Lexicon Popup Specification

Inline hover popups for Hebrew/Greek dictionary links, parallel to BLB ScriptTagger for scripture references.

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

1. **Study Guide** (`study-guide.html`)
   - Inline in narrative text (first meaningful occurrence of each term)
   - Word Study sections (all occurrences)
   - Cross-Language Connections tables (Greek entries)
2. **Weekly Insights** (`insights.html`)
   - Hebrew section spotlight terms
3. **Hebrew Lessons** (`/hebrew/` section) — future

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

## Checklist for Each Week

- [ ] Identify all Hebrew terms that appear in word studies, key passages, and insights
- [ ] Look up Strong's numbers via BLB
- [ ] Add entries to `lexicon-popups.json` for any new terms
- [ ] First meaningful occurrence of each term gets a lexicon link
- [ ] Word study sections link all occurrences
- [ ] Cross-Language tables include Greek lexicon links
- [ ] Test hover popups in local preview

---

---

## Cross-Language Connections Table Pattern

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

*Version 1.1 — 2026-02-19*
