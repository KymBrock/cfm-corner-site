# Study Library Section Specification

Format and structure specification for the CFM Corner Study Library section.

---

## Overview

The Study Library houses in-depth articles, thematic studies, and scholarly explorations that supplement the weekly Come Follow Me lessons. Content is Hugo markdown rendered through custom section templates.

**Navigation:** `Home | About | Weekly Lessons | Hebrew | Culture | Study Library | Resources`

---

## Directory Structure

```
content/study-library/
├── _index.md                           # Study Library landing page
└── articles/
    ├── _index.md                       # Articles subsection landing
    ├── seven-sermons.md                # Individual article pages
    ├── purim-hidden-providence.md
    └── (additional articles)
```

Future subsections may include `themes/`, `types-shadows/`, etc.

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
related_weeks: ["10"]        # Links to related weekly lessons (array of week numbers)
---
```

---

## Layout Templates

Located at `themes/cfm/layouts/study-library/`:

### `list.html`
- Hero section with title and description
- Body content from `_index.md`
- Child section cards (`.library-section-card`) showing subsections with article counts
- Article cards (`.library-article-card`) for regular pages
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
| `.library-landing` | Landing page wrapper |
| `.library-hero` | Hero section with title/subtitle |
| `.library-intro` | Body content section |
| `.library-sections` | Grid container for section cards |
| `.library-section-card` | Subsection card (clickable) |
| `.library-articles` | Grid container for article cards |
| `.library-article-card` | Article card with slate left border |
| `.library-article-page` | Single article page wrapper |
| `.library-article-header` | Article header with back link, title, description |
| `.library-article-content` | Article body content area |
| `.library-article-nav` | Prev/Next navigation |

---

## Content Guidelines

### Converting Articles from Obsidian

Source files are typically in `OT_2026/WeeklyLessons/Week_NN_*/02_Weekly_Insights/`.

Conversion steps:
1. Add Hugo front matter (title, description, weight, related_weeks)
2. **Strip End Matter** — Remove fact-check checklists, interpretive notes, alternate titles, and teaser paragraphs (internal editorial content)
3. Keep Sources/Further Reading sections
4. Verify all markdown renders correctly (tables, blockquotes, bold/italic)
5. Add cross-links to related articles using Hugo relative URLs (e.g., `/study-library/articles/other-article/`)

### Article Structure

Articles should generally include:
- Clear introduction establishing the topic
- Organized sections with `##` headings
- Scripture references (auto-detected by BLB ScriptTagger when deployed)
- Cross-references to related articles and Culture section pages
- Sources/Further Reading section at the end

### General Rules
- Use `related_weeks` to connect articles to weekly lessons
- Cross-link between Study Library and Culture sections where relevant
- Articles can be any length — the layout handles long-form content well
- Hebrew/Greek text can be included inline
- Tables, blockquotes, and lists all render within `.library-article-content`

---

## Design Notes

- Article cards have a slate (`var(--slate-blue)`) left border accent
- Section cards show article count from child pages
- Responsive: cards stack to single column below 768px
- Article content area has comfortable reading width with proper paragraph spacing
- Typography follows the site's serif/Georgia font stack
- Links within articles styled sage-green with hover underline

---

*Version 1.0 — 2026-02-27*
