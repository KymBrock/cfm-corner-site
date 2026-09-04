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

## ⚖️ WHERE THE POPUP DATA COMES FROM — AND WHAT MAY NOT BE USED

**Moved here 2026-09-03 at Kymber's instruction.** This reasoning was recorded in full in commit
`49d2001` (2026-08-24) and **four lanes re-derived it anyway** — `INSTRUCTIONS_FOR_CLAUDE` records
that failure by name, and a fifth lane repeated it on 2026-09-03. **A commit message is not a
findable home for a standing rule.** Read `git log -1 49d2001` for the full context.

### ⚖️ THE GOVERNING PRINCIPLE — READ THIS BEFORE MARKING ANYTHING RESTRICTED

**Kymber, 2026-09-03, correcting an over-restriction in the first draft of this very section:**

> *"I have been told so many things about what we can use and what we can't use, and much of it we
> can use. And it has been marked that we can't use it because someone didn't read the print closely
> enough or the scope was narrowed. The biggest thing that has come through this is that **facts are
> not copyrightable. It's only glosses that are copyrightable.** So we can use information to help us
> reference what we need… Our glosses are not coming verbatim from copyrighted sources, but the facts
> are still the facts. **We can still parse specific words. We can still identify how different words
> are translated in different Bibles and different languages.** We have also been able to trace the
> sources for licensed materials to find that the licensed materials were directly quoting public
> domain sources."*

**⇒ COPYRIGHT PROTECTS EXPRESSION AND ARRANGEMENT. IT DOES NOT PROTECT FACTS.**

| ✅ FACTS — usable regardless of where you first saw them | ⛔ EXPRESSION — not reproducible verbatim |
|---|---|
| A word's **parsing / morphology** — stem, tense, person, gender, number | Someone's **definition or gloss**, copied as written |
| **Which Greek word renders which Hebrew word** in a given verse | A curated **essay, note, or commentary** |
| **How different Bibles and languages translate a word** | An editor's **arrangement** of an entry, reproduced wholesale |
| **Verse references, occurrence counts, cross-references** | |
| A word's **Strong's number** and the text it appears in | |

**Two working rules that follow:**

1. **WRITE OUR OWN GLOSS.** The fact of a word's meaning is not owned; one scholar's *phrasing* of it
   is. **Our glosses are ours.**
2. **TRACE THE PROVENANCE BEFORE ACCEPTING A RESTRICTION.** Licensed compilations frequently quote
   **public-domain** sources. A restriction on the compilation is not a restriction on what it
   quotes. **Read the fine print; do not inherit someone else's summary of it.**

> **⚠ THE FAILURE THIS BLOCK EXISTS TO PREVENT is over-restriction — a lane narrowing the scope or
> skim-reading a licence, marking usable material as forbidden, and blocking work that was always
> permitted. That has happened repeatedly, and the first draft of this section did it again.**

### ⚠️ SOURCES WITH ACTUAL CONSTRAINTS — and what the constraint really is

| source | the real constraint |
|---|---|
| **CATSS / CCATS** | **Its licence requires a signed declaration, so we do not distribute or build from THEIR FILE.** ⚠ **This is NOT a bar on the alignment facts themselves.** Which Greek word renders which Hebrew word in a verse **is a fact** and is obtained from open sources — Rahlfs LXX + OSHB — which is exactly what was done. **Kymber, 2026-08-24:** *"this is a matter of fact, not copyright. That is what appears in the Septuagint, and that can be verified, with or without the CCATS."* |
| **LSJ (`lsj_senses.json`)** | **Not a licensing bar at all — a CORRECTNESS bar.** Properly structured **and semantically wrong for a Bible reader**: classical *ktizō* is "found, build"; biblical is "create". **A structured source that is wrong is more dangerous than an unstructured one, because it looks like an upgrade.** |
| **`Sacred_Texts/RESTRICTED/`** | Copyrighted **expression** — use for sourcing and verification; **quoting into published lessons is Kymber's decision.** Facts drawn from it remain facts. |

### ✅ THE CLEAN SOURCES

| source | licence | note |
|---|---|---|
| **Kymber's own dictionary** | **Thayer's 1889, public domain by age**, plus her and her son's edits | **Carries no critical apparatus, so nothing needs stripping.** Entries tagged `thayers-1889-kymber` are hers — **a bulk sync must not overwrite them.** |
| **OSHB** (Open Scriptures Hebrew Bible) | **CC BY 4.0** | Source of the Hebrew side of the LXX correspondence, and of per-word morphology. |
| **Rahlfs LXX** | Open Scriptures | `text_accented` + `final_Strongs`. |
| **STEPBible TBESG / TBESH / TFLSJ** | **CC BY 4.0 — ATTRIBUTION REQUIRED** | Attribution is live site-wide in `baseof.html`: *"STEPBible TFLSJ, CC BY 4.0; citations preserved."* **Do not remove it.** |

**Kymber, 2026-08-24, on why the LXX↔Hebrew correspondence is legitimate without CATSS:**

> *"This is a matter of fact, not copyright. That is what appears in the Septuagint, and that can be
> verified, with or without the CCATS."*

Copyright protects expression and arrangement, **not the reading of two ancient texts.** A pair is
linked only where a real verse carries both the Greek number and the Hebrew number.

### ⚠️ THREE FIXES ALREADY TRIED ON THE STEPBible DUMP — ALL FAILED. DO NOT RETRY.

    splitting on ';'    left a manuscript siglum as charis's OPENING definition — 3 of 4 broken
    lsj_senses.json     structured but semantically wrong (see above)
    token-stripping     left "(1Es, l.with)" and ate verse refs — 1Co.11:9 became Co.11:9

**The fix that worked was SWAPPING THE SOURCE, not cleaning the dump.** Sense splits are
**hand-authored** — eleven entries, read one at a time, because a wrong split changes a sense.

### ⚠️ DO NOT MERGE FLAT GREEK SENSES

Running the STEPBible builder for Greek yields 5,431 entries with `senses` and **zero nested ones** —
the headword as sense 1, an LXX note as sense 2. Measured once already: **11,428 flat lists were
produced, found redundant with `definition`, and dropped.** They also took a file loaded on **every
page** from **2.98 MB to 11.06 MB.**

### ⚠️ RESOLVE BY EVIDENCE, NEVER BY SPELLING

Matching Hebrew words to Strong's numbers **by consonants was wrong 3 times in 9.** The worst:
*padah* → **H3301 *Iphdeiah***, a proper name in Chronicles. **Requiring co-occurrence in a real verse
kills all three without special-casing.**

    padah  -> H6299   37 verses      (not H3301 Iphdeiah)
    yatsar -> H3335    4 verses      (not H3334 "be distressed")
    qanah  -> H7069    4 verses      (not H7066, Aramaic)

**One word stays UNLINKED** — *pidyom* under *lytron*, absent from OSHB's lemma index. It renders as
plain Hebrew. **Unlinked and right beats linked and wrong.**

*(Independently re-derived 2026-09-03 as the* yāšar */* yāsar *collision — H3474 vs H3256 — by a lane
that did not know this was already recorded. **Join on the Strong's number, never the string.**)*

---

## Non-Lexicon Links (Do NOT Popup)

- **Logeion links** (`logeion.uchicago.edu`) — Latin dictionary, regular navigation
- **Merriam-Webster links** — English dictionary, regular navigation  
- **Scripture references** — Handled by BLB ScriptTagger (separate system)
- **Webster's 1828 links** (`webstersdictionary1828.com`) — Historical English dictionary, regular navigation, always paired with Merriam-Webster link in format: `word (1828)`
- **Any link without `data-lexicon`** — Normal behavior

---

## ⚖️ THE LINK GOES ON THE TRANSLITERATION — Kymber, 2026-08-21

> *"Links should always be added to the transliteration, not the Hebrew because I do not want
> the niqqud obstructed."*

**This governs, and it resolves an ambiguity that has been in this file for months.** Link
styling — underline, colour, hover state — sits directly on top of the vowel points, which are
the smallest marks on the page and the ones a reader most needs to see.

**CORRECT** — link on the transliteration, Hebrew bare beside it:

```html
<a href="…/h1254/…" data-lexicon data-strongs="H1254" data-translit="bārāʾ"
   data-original="בָּרָא" data-lang="hebrew"><em>bārāʾ</em></a> (בָּרָא)
```

**WRONG** — link wrapping the Hebrew, niqqud obstructed:

```html
<em>bārāʾ</em> (<a href="…/h1254/…" …>בָּרָא</a>)
```

### How this reconciles with the Comprehensive Coverage Rule below

The rule below says every Hebrew character in body text must sit inside a lexicon `<a>`. **Read
literally that contradicts this section, and it is the reason 13 Hebrew terms on week 35 shipped
with links on the script** — יְהוָה, אֱלֹהִים, נְגִינָה, מַשְׂכִּיל, סֶלָה.

**The reconciliation is already in this file**, in the "do NOT chase zero" bullet: *"Intentionally
bare script is required beside transliterations."*

So the coverage rule means: **every Hebrew term must be COVERED by a lexicon link — not that the
link must wrap the Hebrew itself.** Where a transliteration stands beside the Hebrew, the link
goes on the transliteration and the script stays bare. **A bare Hebrew word beside a linked
transliteration is correct and must not be "fixed."**

---

## ⚖️ MULTI-WORD PHRASES — every word gets its own link

**Kymber, 2026-08-21:** *"There should be a segment on how phrases need to be divided word for
word so every word is accounted for."*

A Hebrew phrase is not one lexicon entry. **Each word has its own Strong's number, its own
meaning, and its own popup** — and a reader who hovers a two-word phrase and gets one definition
has been told less than the text contains.

**CORRECT** — `ʾerek ʾappayim (אֶרֶךְ אַפַּיִם)`, "slow to anger," is **two words**:

```html
<a … data-strongs="H750" data-translit="ʾerek" data-original="אֶרֶךְ"><em>ʾerek</em></a>
<a … data-strongs="H639" data-translit="ʾappayim" data-original="אַפַּיִם"><em>ʾappayim</em></a>
(אֶרֶךְ אַפַּיִם)
```

**WRONG** — the phrase linked once, to whichever word the lookup happened to find:

```html
<a … data-strongs="H750">ʾerek ʾappayim</a> (אֶרֶךְ אַפַּיִם)
```

### Rules

1. **Split on the Hebrew word boundary, not on the English gloss.** *"Slow to anger"* is three
   English words and two Hebrew ones. **Follow the Hebrew.**
2. **Every word gets an entry**, including the ones that look unimportant — the definite
   article, the conjunction, the preposition. If a word is in the phrase it is in the text, and
   *"every word is accounted for."*
3. **The gloss belongs to the phrase; the definitions belong to the words.** Give the phrase's
   meaning in the prose — *"long of nostril"* — and let each popup carry its own word.
4. **A hyphenated compound is still two words** where Hebrew treats it as two:
   *halelû-yāh* is *halelû* (H1984) + *Yāh* (H3050).
5. **Where a word repeats in the phrase, link each occurrence.** A reader may hover either.
6. **If a word has no Strong's number** — some particles do not — say so rather than attaching a
   neighbouring number. A wrong Strong's number is worse than a missing link, because the popup
   will confidently show a different word.

### Worked examples from live weeks

| phrase | words | Strong's |
|---|---|---|
| *ʾerek ʾappayim* (אֶרֶךְ אַפַּיִם) | *ʾerek* · *ʾappayim* | H750 · H639 |
| *nishmat chayyim* (נִשְׁמַת חַיִּים) | *nishmat* · *chayyim* | H5397 · H2416 |
| *halelû-yāh* (הַלְלוּ־יָהּ) | *halelû* · *Yāh* | H1984 · H3050 |
| *lēb ṭāhôr* (לֵב טָהוֹר) | *lēb* · *ṭāhôr* | H3820 · H2889 |

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
