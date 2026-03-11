# Resources HTML Specification

The definitive format reference for `static/content/weekNN/resources.html`. Week 11 is the canonical example. Every future week must match this structure.

---

## Document Structure

```
<!DOCTYPE html><html lang="en"><head>...</head><body><div data-pagefind-body>

1. <style> block (responsive CSS)
2. Header Box (title, scripture, dates, quote)
3. Quick Links (CFM Manual + Scripture Helps buttons)
4. ── Official Church Resources ──
   a. OFFICIAL CHURCH RESOURCES (accordion, collapsed)
   b. CHURCH MEDIA FOR FAMILIES (accordion, collapsed)
5. ── hr separator ──
6. ── Video Commentary ──
   a. Video Commentary (accordion, EXPANDED by default)
7. ── Specialized Audiences ──
   a. Women's Perspectives (accordion, collapsed)
   b. Family & Children's Resources (accordion, collapsed)
8. ── hr separator ──
9. ── Reference & Study Materials ──
   a. Academic hero cards (Scripture Central, Interpreter, Bible Project)
   b. Expand All / Collapse All buttons
   c. BIBLE PROJECT VIDEOS THIS WEEK (accordion, collapsed)
   d. ACADEMIC & SCHOLARLY SITES (accordion, collapsed)
   e. MAPS & BIBLICAL LOCATIONS (accordion, collapsed)
   f. JEWISH & SCHOLARLY RESOURCES (accordion, collapsed)
10. <script> block (accordion JS)

</div></body></html>
```

---

## Style Block

Minified on one line in production. Key rules:

```css
body { font-family: Georgia, serif; max-width: 900px; margin: 0 auto; padding: 0; background: transparent; color: #1f2937; line-height: 1.6; }
@media (max-width: 768px) {
    .video-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 10px !important; }
    .section-header { font-size: 1em !important; padding: 12px 16px !important; }
}
@media (max-width: 480px) {
    .video-grid { grid-template-columns: 1fr !important; gap: 8px !important; }
    h1 { font-size: 1.5em !important; } h2 { font-size: 1.1em !important; }
    table { font-size: 0.85em !important; } td { padding: 6px 8px !important; }
    .section-header { font-size: 0.95em !important; padding: 10px 14px !important; }
}
```

---

## Header Box

```html
<div style="background: linear-gradient(135deg, #e8ede9 0%, #d1ddd4 100%); border: 2px solid #7c9885; border-radius: 12px; padding: 30px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <h1 style="font-family: Georgia, serif; color: #5a6d5f; font-size: 2.2em; margin-bottom: 10px; font-weight: normal;">Weekly Resources: Week NN</h1>
    <p style="color: #7c9885; font-size: 1.3em; font-style: italic; margin-bottom: 15px;">Scripture Reference</p>
    <p style="color: #5a6d5f; font-size: 1em; margin-bottom: 10px;">Date Range</p>
    <p style="color: #666; font-size: 1em; font-style: italic; margin: 0;">&ldquo;Quote&rdquo;</p>
    <p style="color: #888; font-size: 0.85em; margin-top: 8px;">&mdash; Attribution</p>
</div>
```

---

## Quick Links Buttons

Two sage-green buttons centered below the header box:

```html
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-bottom: 25px;">
    <a href="https://www.churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/NN?lang=eng" target="_blank" style="background: #7c9885; color: white; padding: 10px 16px; text-decoration: none; border-radius: 8px; font-size: 0.9em; font-weight: 600; display: inline-block; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Come Follow Me Manual</a>
    <a href="https://www.churchofjesuschrist.org/study/manual/scripture-helps-old-testament?lang=eng" target="_blank" style="background: #7c9885; color: white; padding: 10px 16px; text-decoration: none; border-radius: 8px; font-size: 0.9em; font-weight: 600; display: inline-block; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Scripture Helps</a>
</div>
```

The CFM Manual URL changes per week (`/NN?lang=eng`). The Scripture Helps URL is static.

---

## Accordion Section Pattern

Every collapsible section follows this exact pattern:

```html
<div class="cfm-resources-section" style="border: 2px solid #c6d4c8; border-radius: 8px; margin-bottom: 15px; overflow: hidden;">
    <div class="section-header" onclick="toggleResourcesSection(this)" style="background: linear-gradient(135deg, #7c9885 0%, #5a6d5f 100%); color: white; padding: 14px 20px; cursor: pointer; font-family: Georgia, serif; font-size: 1.1em; font-weight: 600; display: flex; justify-content: space-between; align-items: center; letter-spacing: 0.5px;">
        <span>SECTION TITLE</span>
        <span class="arrow" style="font-size: 1em; transition: transform 0.3s ease;">&#9654;</span>
    </div>
    <div class="section-content" style="max-height: 0; overflow: hidden; transition: max-height 0.5s ease; background: transparent;">
        <div style="padding: 15px;">
            <!-- content here -->
        </div>
    </div>
</div>
```

**Collapsed** (default): `max-height: 0`, arrow `&#9654;` (right triangle)
**Expanded** (Video Commentary only): `max-height: none`, arrow `&#9660;` (down triangle), add `data-expanded="true"`

---

## Video Card Pattern (WITH thumbnail)

Used for: Video Commentary, Women's Perspectives, Family/Children, Bible Project, Church Media for Families.

**Every video with a YouTube URL MUST use the thumbnail card format.** Never use plain text link boxes.

```html
<div style="background: white; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <a href="https://www.youtube.com/watch?v=VIDEO_ID" target="_blank" style="text-decoration: none;">
        <img src="https://img.youtube.com/vi/VIDEO_ID/mqdefault.jpg" alt="Title" style="width: 100%; height: auto; display: block;">
        <div style="padding: 8px 10px; text-align: center;">
            <span style="color: #7c9885; font-weight: 600; font-size: 0.8em;">Channel/Video Title</span>
        </div>
        <div style="padding: 4px 10px 8px; font-size: 0.72em; color: #4a5568; line-height: 1.4;">Brief description of the video content.</div>
    </a>
</div>
```

### Thumbnail URL formula
```
https://img.youtube.com/vi/{VIDEO_ID}/mqdefault.jpg
```

### Grid layout
- **Video Commentary:** `grid-template-columns: repeat(3, 1fr)` — 3 columns
- **Bible Project:** `grid-template-columns: repeat(2, 1fr)` — 2 columns
- **Church Media for Families:** `grid-template-columns: repeat(3, 1fr)` — 3 columns

---

## Church Media for Families Card Pattern

For Church website videos (not YouTube), use the Church CDN thumbnail:

```html
<div style="background: white; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <a href="https://www.churchofjesuschrist.org/media/video/VIDEO-SLUG?lang=eng" target="_blank" style="text-decoration: none; display: block;">
        <img src="https://media.ldscdn.org/images/videos/scripture-and-lesson-support/old-testament-stories/VIDEO-SLUG-3840x2160-thumb-master.jpg" alt="Title" style="width: 100%; height: auto; display: block;">
        <div style="padding: 10px; text-align: center;">
            <span style="color: #7c9885; font-weight: 600; font-size: 0.8em; display: block;">Video Title</span>
            <span style="color: #9ca3af; font-size: 0.65em;">Old Testament Stories</span>
        </div>
    </a>
</div>
```

### Collection link cards (no thumbnail)

For "All OT Stories", "All Come Learn With Me", "Church Video Library":

```html
<div style="background: white; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <a href="COLLECTION_URL" target="_blank" style="text-decoration: none; display: block;">
        <div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); padding: 25px 15px; text-align: center;">
            <div style="color: white; font-size: 0.7em; margin-top: 5px; opacity: 0.9;">Full Collection</div>
        </div>
        <div style="padding: 10px; text-align: center;">
            <span style="color: #7c9885; font-weight: 600; font-size: 0.8em; display: block;">Collection Name</span>
            <span style="color: #9ca3af; font-size: 0.65em;">Subtitle</span>
        </div>
    </a>
</div>
```

> **No emojis.** The collection card uses only text ("Full Collection" / "Full Library"). The previous `&#128218;` emoji has been removed to match the site-wide design rule.

---

## Church Media for Families — Week-Specific Videos

Select relevant videos from these Church collections for each week:

### Old Testament Stories (2021 series)
| Slug | Title | Relevant Weeks |
|------|-------|----------------|
| `2021-11-1080-abraham-and-sarah` | Abraham and Sarah | 08 |
| `2021-11-1090-hagar` | Hagar | 08, 09 |
| `2021-11-1100-abraham-and-isaac` | Abraham and Isaac | 09 |
| `2021-11-1110-jacob-and-esau` | Jacob and Esau | 10 |
| `2021-11-1120-jacob-and-his-family` | Jacob and His Family | 11 |
| `2021-11-1130-josephs-inspired-dreams` | Joseph's Inspired Dreams | 12 |
| `2021-11-1140-joseph-in-egypt` | Joseph in Egypt | 12, 13 |
| `2021-11-1150-joseph-and-the-famine` | Joseph and the Famine | 13 |
| `2021-11-1160-baby-moses` | Baby Moses | 14 |
| `2021-11-1170-moses-the-prophet` | Moses the Prophet | 14, 15 |
| `2021-11-1180-the-plagues-of-egypt` | The Plagues of Egypt | 15 |
| `2021-11-1190-the-passover` | The Passover | 16 |
| `2021-11-1200-the-israelites-in-the-wilderness` | The Israelites in the Wilderness | 17 |
| `2021-11-1210-moses-on-mount-sinai` | Moses on Mount Sinai | 18 |

Thumbnail formula: `https://media.ldscdn.org/images/videos/scripture-and-lesson-support/old-testament-stories/{SLUG}-3840x2160-thumb-master.jpg`

### Come Learn with Me (2025 series)
| Slug | Title | Relevant Weeks |
|------|-------|----------------|
| `2025-10-i-can-be-a-peacemaker-genesis-13` | I Can Be a Peacemaker | 08 |
| `2025-09-trusting-god-genesis-17-21` | Trusting God | 09 |

Thumbnails: fetch from page source (`assets.churchofjesuschrist.org/...`)

### Always include these three collection links:
1. All OT Stories → `churchofjesuschrist.org/media/collection/primary-old-testament-stories-children`
2. All Come Learn With Me → `churchofjesuschrist.org/media/collection/come-learn-with-me-old-testament`
3. Church Video Library → `churchofjesuschrist.org/media/video`

---

## Table Pattern (for reference lists)

Used in: Official Church Resources, Academic Sites, Maps, Jewish Resources.

```html
<table style="width: 100%; border-collapse: collapse;">
    <tr>
        <td style="padding: 6px 12px; background: linear-gradient(135deg, #e8ede9 0%, #d1ddd4 100%); font-weight: 600; color: #4a5d4f; font-size: 0.9em;" colspan="2">Section Header</td>
    </tr>
    <tr>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f0f0; text-align: left; font-size: 0.9em;">Resource Name</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f0f0; text-align: right; width: 60px;">
            <a href="URL" target="_blank" style="color: #7c9885; text-decoration: none; font-size: 0.9em;">View</a>
        </td>
    </tr>
</table>
```

---

## Academic Hero Cards

Three cards in a 3-column grid before the expand/collapse buttons:

1. **Scripture Central** — dark blue gradient `#1a365d → #2d4a6f`, white logo box, week-specific URL
2. **Interpreter Foundation** — brown gradient `#2c1810 → #4a2c20`, logo on dark bg, week-specific URL
3. **Bible Project** — white card with YouTube thumbnail overlay, green gradient text overlay at bottom

All three have hover lift effect (`translateY(-3px)` + shadow increase).

### URL patterns
- Scripture Central: `https://scripturecentral.org/come-follow-me/old-testament-sunday-school-2026/{scripture-slug}`
- Interpreter: `https://interpreterfoundation.org/come-follow-me/old-testament-2026/{scripture-slug}`
- Bible Project: link to most relevant overview video

---

## Bible Project Videos

### Standard set (include every week unless clearly irrelevant)

**Theme Videos:**
| Title | Video ID |
|-------|----------|
| Covenant | `8ferLIsvlmI` |
| Temple | `wTnq6I3vUbU` |
| Sacrifice & Atonement | `G_OlRWGLdnw` |
| Holiness | `l9vn5UvsHvM` |
| Image of God | `YbipxLDtY8c` |
| The Messiah | `3dEh25pduQ8` |
| Tree of Life | `TJLan-pJzfQ` |

**Word Study Videos:**
| Title | Video ID |
|-------|----------|
| YHWH/LORD | `eLrGM26pmM0` |
| Shalom/Peace | `oLYORLZOaZE` |
| Khesed/Loyal Love | `dHKsqaM-IF4` |
| Nephesh/Soul | `g_igCcWAMAM` |
| Ruakh/Spirit | `gPjL_VFcqnM` |

**Book Overview Videos (add as relevant):**
| Title | Video ID | Relevant Weeks |
|-------|----------|----------------|
| Genesis 1-11 | `GQI72THyO5I` | 01–07 |
| Genesis Summary: Part 2 | `F4isSyennFo` | 08–13 |
| Exodus 1-18 | `jH_aojNJM3E` | 14–17 |
| Exodus 19-40 | `oNpTha80yyE` | 18–20 |

**Grid:** 2 columns (`repeat(2, 1fr)`)

---

## Official Church Resources — Standard Table Rows

These are the same every week (only the CFM Manual URL changes):

### Church Manuals
| Resource | URL Pattern |
|----------|-------------|
| Come Follow Me Manual | `churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/{NN}?lang=eng` |
| Scripture Helps: OT | (static) |
| OT Seminary Manual | (static) |
| OT Institute (Gen-2Sam) | (static) |
| Pearl of Great Price Manual | (static) |

### Scripture Reference
Bible Dictionary, Topical Guide, Guide to the Scriptures — all static.

### Church Media
Gospel for Kids (YouTube), Bible Videos — static.

### Church Publications & Library
Church Magazines, Gospel Library — static.

---

## JavaScript (same every week)

```javascript
function toggleResourcesSection(header) {
    const content = header.nextElementSibling;
    const arrow = header.querySelector('.arrow');
    const isCollapsed = content.style.maxHeight === '0px' || content.style.maxHeight === '';
    if (isCollapsed) {
        content.style.maxHeight = content.scrollHeight + 'px';
        arrow.innerHTML = '&#9660;';
        content.dataset.expanded = 'true';
        setTimeout(() => { if (content.dataset.expanded === 'true') content.style.maxHeight = 'none'; }, 500);
    } else {
        content.dataset.expanded = 'false';
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(() => { content.style.maxHeight = '0px'; }, 10);
        arrow.innerHTML = '&#9654;';
    }
}
function toggleAll(expand) {
    document.querySelectorAll('.cfm-resources-section .section-content').forEach(c => {
        if (expand) { c.style.maxHeight = 'none'; c.dataset.expanded = 'true'; }
        else { c.dataset.expanded = 'false'; c.style.maxHeight = '0px'; }
    });
    document.querySelectorAll('.cfm-resources-section .arrow').forEach(a => {
        a.innerHTML = expand ? '&#9660;' : '&#9654;';
    });
}
```

---

## Week-Variable Content Checklist

Only these things change per week:

- [ ] Header: title, scripture, dates, quote
- [ ] Quick Links: CFM Manual URL (week number)
- [ ] Official Church Resources: CFM Manual "View" link
- [ ] Church Media for Families: 2-3 week-specific videos from OT Stories / Come Learn With Me
- [ ] Video Commentary: all channel videos with thumbnails + descriptions
- [ ] Women's Perspectives: week-specific videos
- [ ] Family & Children's: week-specific videos
- [ ] Academic hero cards: Scripture Central + Interpreter URLs (scripture slug)
- [ ] Bible Project: book overview video (changes per book); theme + word study videos stay the same
- [ ] Bible Project hero card video + count

Everything else (static reference links, collection links, JS, CSS) is identical.

---

*Canonical example: `static/content/week11/resources.html`*
*Spec version: 1.1 — 2026-03-10*
