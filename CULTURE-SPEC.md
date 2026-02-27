# Culture Section Specification

Format and structure specification for the CFM Corner Culture section.

---

## Overview

The Culture section provides cultural context for Old Testament study — Jewish traditions, feast days, interpretive frameworks, and historical perspectives. Content is Hugo markdown rendered through custom section templates.

**Navigation:** `Home | About | Weekly Lessons | Hebrew | Culture | Study Library | Resources`

---

## Directory Structure

```
content/culture/
├── _index.md                           # Culture landing page
└── jewish/
    ├── _index.md                       # Jewish Culture & Tradition landing
    ├── moedim/
    │   ├── _index.md                   # Moedim (Feast Days) landing
    │   ├── purim.md                    # Individual feast day pages
    │   ├── passover.md
    │   └── (additional holidays)
    └── perspective/
        ├── _index.md                   # Cultural Perspective landing
        ├── jewish-texts-primer.md      # Reference articles
        └── pardes-model.md
```

---

## Front Matter

### Landing Pages (`_index.md`)

```yaml
---
title: "Section Title"
description: "One-sentence description shown as subtitle."
---

Optional introductory paragraph rendered as body content.
```

### Article Pages

```yaml
---
title: "Article Title"
description: "1-2 sentence description for card display and meta tags."
weight: 1                    # Controls sort order within section
related_weeks: ["10"]        # Links to related weekly lessons
---
```

---

## Layout Templates

Located at `themes/cfm/layouts/culture/`:

### `list.html`
- Hero section with title and description
- Body content from `_index.md`
- Child section cards (`.culture-section-card`) showing subsections with topic counts
- Article cards (`.culture-article-card`) for regular pages
- Back navigation link to parent section

### `single.html`
- Back link to parent section
- Title, description, related weeks links
- Full article content
- Prev/Next navigation within section

---

## CSS Classes

All styles are in `static/css/style.css`:

| Class | Purpose |
|-------|---------|
| `.culture-landing` | Landing page wrapper |
| `.culture-hero` | Hero section with title/subtitle |
| `.culture-intro` | Body content section |
| `.culture-sections` | Grid container for section cards |
| `.culture-section-card` | Subsection card (clickable) |
| `.culture-articles` | Grid container for article cards |
| `.culture-article-card` | Article card with gold left border |
| `.culture-article-page` | Single article page wrapper |
| `.culture-article-header` | Article header with back link, title, description |
| `.culture-article-content` | Article body content area |
| `.culture-article-nav` | Prev/Next navigation |

---

## Content Guidelines

### Moedim (Feast Day) Pages
Each feast day page should include:
- **Overview** section with Hebrew name, date, biblical basis, key themes
- **The Story in Brief** — narrative summary of the biblical/historical event
- **How [Holiday] Is Observed** — traditional observance practices
- **Why [Holiday] Matters for Latter-day Saints** — LDS theological connections
- **Cross-links** to related Study Library articles

### Perspective (Reference) Pages
- Educational/reference content about Jewish interpretive traditions
- Respectful framing — present as context enrichment, not competing doctrine
- Quick reference tables for key terms
- Glossary where applicable
- Source citations

### General Rules
- Use `related_weeks` to connect content to weekly lessons
- Cross-link between Culture and Study Library sections where relevant
- Hebrew text renders correctly inline (no special handling needed)
- All content should be accessible to an LDS audience unfamiliar with Jewish tradition

---

## Design Notes

- Section cards use the existing sage/gold/slate design palette
- Article cards have a gold (`var(--gold)`) left border accent
- Section cards show topic count from child pages
- Responsive: cards stack to single column below 768px
- Typography follows the site's serif/Georgia font stack

---

*Version 1.0 — 2026-02-27*
