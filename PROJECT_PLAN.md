# CFM Corner — Site Migration Project Plan
Created: 2026-02-14

## Overview
Migrate cfmcorner.com from Wix to a self-hosted static site (Hugo + GitHub Pages). Unify all content under one platform, add search, fix Hebrew rendering, improve SEO, reduce weekly publishing effort.

## Current State
- **Wix site** at cfmcorner.com — blog-style, 8 weekly OT 2026 posts, Resources pages, About, archived lessons from previous years (NT, BoM, D&C)
- **GitHub Pages** at kymbrock.github.io/cfm-ot-study — study guides, interactive Hebrew charts, comparison charts
- **200 email subscribers** on Wix
- **Prototype started** in this repo — Hugo scaffolding, Week 08 content ported, basic templates

## Brand Assets
- **Current banner**: `/Volumes/Learning Inspired/.../LOGO/CFMBG.jpg`
- **Updated tree (standalone)**: `/Volumes/Learning Inspired/.../LOGO/tree_animation_template.png`
- **Tree source (AI)**: `/Volumes/Learning Inspired/.../LOGO/logo_complete.ai`
- **Learning Inspired logo**: `/Volumes/Learning Inspired/.../Logo/Learning_Inspired_LOGO (1).png`
- **Color direction**: Migrate from flat sage grey-green to warmer Learning Inspired palette
  - Primary: Sage green (carry over)
  - Accent: Gold/amber (from LI logo)
  - Secondary: Slate blue (from LI logo)
  - Keep Georgia serif for headings

## Phase 1: Foundation (Next Session)
- [ ] Fix CSS loading issue in Hugo dev server
- [ ] Build proper color palette from Learning Inspired branding
- [ ] Create banner/header using updated tree + new colors
- [ ] Build and polish homepage layout
- [ ] Build week landing page with tabs (Resources / Insights / Study Guide / Charts)
- [ ] Verify Week 08 content renders correctly (Hebrew, video thumbnails, nesting)
- [ ] Test mobile responsive

### Lesson Artwork
- Each week uses the hero image from the CFM Manual page
- URL pattern: `https://www.churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/{WEEK_NUM}?lang=eng`
- Image served via: `https://www.churchofjesuschrist.org/imgs/{hash}/full/!{width},/0/default`
- Can scrape programmatically — grab first large image from each manual page
- Download and store in `static/images/weeks/` for each week
- Week 08 example: "Melchizedek laying his hands on Abram's head" (hash: `d43983a7907011ee8442eeeeac1e4df71aab14ec`)

## Phase 2: Content Migration — OT 2026 (Session After)
- [ ] Create content pages for Weeks 1-7 (port existing HTML)
- [ ] Run encoding fix on all HTML (Hebrew entities)
- [ ] Copy all charts to static site
- [ ] Verify all video links and thumbnails
- [ ] Build "All Weeks" grid page

## Phase 3: Site Pages & Features
- [ ] About page (with updated branding)
- [ ] Resources page + sub-pages (Digital Tools, Podcasts, Culture & Traditions, Language Learning, Printed Material, History)
- [ ] Search (Pagefind — client-side full-text search)
- [ ] Email subscribe integration (Buttondown, Mailchimp, or similar — migrate 200 subscribers)
- [ ] Print/PDF stylesheet
- [ ] SEO: meta tags, structured data, sitemap, Open Graph

## Phase 4: Archives
- [ ] Assess previous years' content (NT, BoM, D&C) — what exists, what's worth migrating
- [ ] Create archive section with category navigation
- [ ] Make all content searchable

## Phase 5: Launch
- [ ] Deploy to GitHub Pages (or Netlify/Cloudflare Pages)
- [ ] Point cfmcorner.com domain to new host
- [ ] Test everything live
- [ ] Keep Wix site as backup for 30 days
- [ ] Announce to email list

## Ongoing Workflow (Post-Launch)
Weekly publishing becomes:
1. Write content in Obsidian (same as now)
2. Run generator scripts (same as now)
3. Copy HTML to site content folder
4. `git push` — site auto-deploys
- No more Wix paste
- No more BiDi fixer
- No more split publishing

## Key Decisions Still Needed
1. **Email provider**: Buttondown (simple, free tier), Mailchimp (more features), or other?
2. **Hosting**: GitHub Pages (free, simple) vs Netlify (more features, still free tier)?
3. **Domain**: Keep cfmcorner.com? Update DNS only.
4. **Archive depth**: How much previous-year content to migrate?
5. **Login/members**: Add any member features, or keep it public-only?

## Files in This Repo
```
cfm-corner-site/
├── hugo.toml                    # Site config
├── content/
│   ├── weeks/08.md              # Week 08 content page
│   ├── about.md                 # About page
│   └── resources.md             # Resources page
├── static/
│   ├── content/week08/          # Week 08 HTML files
│   │   ├── resources.html
│   │   ├── insights.html
│   │   ├── study-guide.html
│   │   ├── comparison.html
│   │   └── root-system.html
│   ├── charts/                  # Shared Hebrew charts
│   └── images/                  # Logo/banner (need re-copy)
└── themes/cfm/                  # Custom theme
    ├── layouts/
    │   ├── _default/baseof.html # Base template
    │   ├── _default/single.html # Default page
    │   ├── index.html           # Homepage
    │   └── weeks/               # Week templates
    └── static/css/style.css     # Stylesheet
```
