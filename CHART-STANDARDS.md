# Chart HTML Standards

Standards for all standalone chart HTML files in `static/charts/` and embedded chart content in `static/content/weekNN/`.

---

## Logo Header Pattern

Every chart with a header uses the CFM Corner tree logo. The standard responsive pattern:

```html
<header>
    <div class="header-flex" style="display: flex; align-items: center; justify-content: center; gap: 20px; margin-bottom: 10px;">
        <div class="header-logo" style="width: 50px; height: 50px; border-radius: 50%; background: white; padding: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); flex-shrink: 0;">
            <img src="../images/tree-logo.png" alt="CFM Corner" style="width: 100%; height: 100%; border-radius: 50%; object-fit: contain;">
        </div>
        <div>
            <h1>Chart Title</h1>
            <p class="subtitle">Subtitle text</p>
        </div>
    </div>
</header>
```

### Critical Rules

| Rule | Correct | Wrong |
|------|---------|-------|
| Logo size | `50px × 50px` | `60px`, `70px` |
| Image fit | `object-fit: contain` | `object-fit: cover` (distorts — logo is 1807×1703, not square) |
| Flex shrink | `flex-shrink: 0` on logo div | Missing (logo gets squished) |
| Image path (charts/) | `../images/tree-logo.png` | Absolute paths |
| Image path (content/weekNN/) | `../../images/tree-logo.png` | Wrong depth |

### Required Mobile Breakpoint

Every chart with a logo header MUST include this CSS:

```css
@media (max-width: 600px) {
    .header-flex { flex-direction: column !important; gap: 10px !important; }
    .header-logo { margin: 0 auto; }
    header h1 { font-size: 1.4em !important; }
}
```

This stacks the logo above the title on mobile instead of overlapping.

---

## Chart Shortcode (Embedding)

Charts are embedded in lesson pages via Hugo shortcode:

```
{{</* chart "chart_name" */>}}
```

This renders as an iframe with "Open full chart in new tab" link below. The chart's internal CSS handles all responsive behavior.

---

## Places of Articulation — Region Color Map

Each articulatory region has a unique color used consistently across three elements:
1. **SVG overlay dot** (on the anatomical diagram)
2. **Letter cards** (background tint when region is selected)
3. **Classification table** (left border + text color)

| Region | Color | Hex | Card RGBA |
|--------|-------|-----|-----------|
| Bilabial | Gold | `#d5a93c` | `rgba(213,169,60,0.18)` |
| Labiodental | Slate | `#57899c` | `rgba(87,137,156,0.18)` |
| Dental/Alveolar | Plum | `#6a5983` | `rgba(106,89,131,0.18)` |
| Palatal | Sage | `#4a6b52` | `rgba(74,107,82,0.18)` |
| Velar | Soft Red | `#c0392b` | `rgba(192,57,43,0.18)` |
| Uvular | Copper | `#c37c3c` | `rgba(195,124,60,0.18)` |
| Pharyngeal | Teal | `#2a9d8f` | `rgba(42,157,143,0.18)` |
| Glottal | Deep Blue | `#264653` | `rgba(38,70,83,0.2)` |

### SVG Dot Opacity

Use higher opacity for dots that sit on the pink anatomical diagram (the background color washes them out):

- Standard: `opacity="0.35"` with `stroke-width="2"`
- On busy background: `opacity="0.6-0.7"` with `stroke-width="2.5"` and hex values instead of CSS vars

### CSS Variables Required in Chart `:root`

Charts are standalone HTML (loaded in iframes), so they need their own CSS variable definitions:

```css
:root {
    --sage-dark: #4a6b52;
    --sage-mid: #7c9885;
    --sage-pale: #dce8dd;
    --gold: #d5a93c;
    --gold-light: #f5e6b8;
    --slate: #57899c;
    --navy: #1e3a4f;
    --plum: #6a5983;
    --copper: #c37c3c;
    --terracotta: #c65528;
}
```

If you use a brand color in a chart, make sure it's defined in that chart's `:root` — site-wide `style.css` variables are NOT available inside iframes.

---

## Hebrew Lesson Navigation

Lessons use `weight` in front matter for sort order:

```yaml
---
title: "Lesson Title"
lesson_num: 1
weight: 1
---
```

Hugo's `.PrevInSection` (weight-sorted) returns the **next** lesson, and `.NextInSection` returns the **previous** — counterintuitive. The template swaps them:

```go
{{ with .NextInSection }}  ← Previous lesson (left)
{{ with .PrevInSection }}  → Next lesson (right)
```

---

## Mobile Responsive Checklist

For any new chart or content HTML:

- [ ] Logo: 50×50, `object-fit: contain`, `flex-shrink: 0`
- [ ] Mobile breakpoint: logo stacks above title at `max-width: 600px`
- [ ] Tables: `overflow-x: auto` wrapper for horizontal scroll
- [ ] Buttons: vertical margin (`margin: 5px 10px`) so stacked buttons have gaps
- [ ] Timeline/nav items: `flex-wrap: wrap` for graceful wrapping
- [ ] Fonts: use `clamp()` or breakpoint sizing for headings
- [ ] Test on phone before deploying

---

## Files with Logo Headers (as of 2026-02-19)

### Charts (`static/charts/`)
- `hebrew_alphabet_development_chart.html`
- `hebrew_dagesh_letter_classifications.html`
- `hebrew_vowels_chart.html`
- `hebrew_root_system.html`

### Week Content (`static/content/`)
- `week04/comparison.html`
- `week05/comparison.html`
- `week07/comparison.html`
- `week08/comparison.html`
- `week08/root-system.html`

### Charts WITHOUT Logo (no header fix needed)
- `hebrew_places_of_articulation.html` (no logo in header)
- `hebrew_parts_of_speech.html` (no logo in header)

---

*Version 1.0 — 2026-02-19*
