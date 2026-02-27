# CFM Corner — Content Specifications Index

All spec documents for the CFM Corner site content pipeline. Read these before creating or editing weekly content.

---

## Documents

| Document | What It Covers | Canonical Example |
|----------|---------------|-------------------|
| `WEEKLY-PROTOCOL.md` | End-to-end weekly workflow (Obsidian → Hugo → Deploy → Email) | — |
| `STUDY-GUIDE-SPEC.md` | Study guide HTML format, 7 accordion sections (incl. Jewish Perspective), word studies, linking system | Week 09 (Sections 1-4, 6-7); Week 10+ (all 7 sections) |
| `RESOURCES-HTML-SPEC.md` | Resources page HTML format, video cards, accordions | Week 08 |
| `LEXICON-POPUP-SPEC.md` | Hebrew/Greek hover popups, data attributes, dictionary linking patterns | — |
| `CHART-STANDARDS.md` | Chart HTML standards: logo pattern, mobile responsive, region colors, CSS vars | Week 09 charts |
| `CULTURE-SPEC.md` | Culture section structure, layout templates, content guidelines | Purim moedim page |
| `STUDY-LIBRARY-SPEC.md` | Study Library section structure, article format, front matter | Seven Sermons article |
| `CONTENT-SPECS-INDEX.md` | This file — master index and quick reference | — |

---

## Quick Reference

### Link Types (All Content Pages)

| # | Link Type | Behavior | URL Pattern |
|---|-----------|----------|-------------|
| 1 | Scripture references | Auto-detected by BLB ScriptTagger (no markup needed) | Plain text → auto-linked |
| 2 | Hebrew lexicon (BLB) | Hover popup via `data-lexicon` attributes; click prevented | `blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/` |
| 3 | Greek lexicon (BLB) | Hover popup via `data-lexicon` + `data-lang="greek"` | `blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/` |
| 4 | Latin dictionary (Logeion) | Regular link, opens new tab | `logeion.uchicago.edu/WORD` |
| 5 | English dictionary (MW) | Regular link, opens new tab | `merriam-webster.com/dictionary/WORD` |
| 6 | English dictionary (1828) | Regular link in parentheses after MW | `webstersdictionary1828.com/Dictionary/WORD` |
| 7 | Google Maps satellite | Regular link with `&t=k` param | `google.com/maps/place/...&t=k` |
| 8 | Content-area links | Sage-green with subtle border-bottom | Varies |

### Dictionary Sources

| Source | URL Pattern | Used For | Popup? |
|--------|-------------|----------|--------|
| BLB Hebrew | `https://www.blueletterbible.org/lexicon/hNNNN/kjv/wlc/0-1/` | Hebrew word studies | Yes |
| BLB Greek | `https://www.blueletterbible.org/lexicon/gNNNN/kjv/tr/0-1/` | Greek cross-language rows | Yes |
| Logeion | `https://logeion.uchicago.edu/WORD` | Latin (Vulgate) cross-language rows | No |
| Merriam-Webster | `https://www.merriam-webster.com/dictionary/WORD` | English etymology connections | No |
| Webster's 1828 | `https://webstersdictionary1828.com/Dictionary/WORD` | Historical English definitions | No |

### Key Paths

| Path | Description |
|------|-------------|
| `static/content/weekNN/` | Weekly content directory (study-guide.html, resources.html, insights.html) |
| `content/weeks/weekNN.md` | Hugo page for weekly content (front matter + shortcodes) |
| `content/culture/` | Culture section (Jewish tradition, feast days, interpretive frameworks) |
| `content/study-library/` | Study Library section (in-depth articles and thematic studies) |
| `themes/cfm/layouts/culture/` | Culture section Hugo templates (list.html, single.html) |
| `themes/cfm/layouts/study-library/` | Study Library Hugo templates (list.html, single.html) |
| `layouts/shortcodes/` | Hugo shortcodes for embedding content |
| `cfm-corner-tools/data/lexicon-popups.json` | Shared lexicon data for popup generation |
| `static/js/` | Site JavaScript (accordion, lexicon popup, ScriptTagger) |
| `static/css/` | Site CSS |

### Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Navy | `#1e3a4f` | — |
| Slate | `#57899c` | — |
| Sage | `#4a6b52` | Content links, accents |
| Gold | `#d5a93c` | Table hover, highlights |
| Plum | `#6a5983` | — |
| Copper | `#c37c3c` | — |
| Terracotta | `#c65528` | — |

**Study guide palette** uses a brown family (`#8B7355` primary, `#6B5344` dark, `#5a4a3a` deep) rather than the main site palette.

### Design Rules

- **No emojis** — monochromatic icons only (Unicode symbols like ⊞ ⊟)
- **Tables:** sage-dark headers, alternating rows, gold hover, rounded corners (site CSS); study guides use brown/cream variant
- **Nikud/dagesh:** soft red (`#c0392b`) via `.nq` class
- **Content links:** sage-green with subtle border-bottom
- **Hebrew lexicon links:** sage-green with dotted underline + hover popup
- **Scripture links:** handled by BLB ScriptTagger (dotted underline via `.BLBScriptRef` CSS)
- **Blockquotes:** left border accent, cream background, italic text, rounded right corners
- **`<hr>` separators:** between sub-sections and between word studies

---

*Version 1.0 — 2026-02-19*
