# HANDOFF — First Temple & Divided Kingdom Field Guides

Resuming on a new machine / new Claude session? Start here. (The chat transcript does not
sync — it's too large — so this note + `git log` carry the context.)

## You are on branch `feature/first-temple-divided-kingdom`
```bash
git fetch origin
git checkout feature/first-temple-divided-kingdom && git pull
hugo server -D          # -D shows drafts locally (port 1313)
```
Tip: also `cd ~/Obsidian/Translation\ Hub && git pull` for the synced `memory/` + this note's twin
in `.claude-sync/HANDOFF-field-guides.md`.

## Draft previews from anywhere (Cloudflare Pages)
Branch pushes build draft previews on Cloudflare Pages (`scripts/cf-pages-build.sh`; drafts ON
for non-main branches, noindexed, analytics off). Preview URL:
`https://feature-first-temple-divided-kingdom.<project>.pages.dev`. Production hosting is
UNCHANGED — GitHub Pages from `main` (deploy.yml); Cloudflare is previews only.

## Publish state — IMPORTANT (do not publish the Divided Kingdom yet)
- The site **deploys from `main` only**. Pushing this feature branch publishes nothing.
- **Solomon's Temple guide = already published** (live on `main`, `draft = false`). Leave as-is.
- **Divided Kingdom guide = `draft = true` on every page = NOT published.** Keep it that way until
  Kymber says go. Publishing = flip its pages to `draft = false`, then merge to `main`.

## Status
- **Divided Kingdom** (10 pages): publish-ready in substance. Audit clean — 104 scripture refs
  all valid vs. the vault ScriptureDatabase, no broken links, all scholars in Sources, mobile OK.
  Interactives: regnal scorecard, dynasty+prophets strip, six two-readings toggles, calf-map
  overlay (Dan/Bethel), 5-panel story-strip, Holy Land Site markers. Images: author photos
  (Knossos throne room, Snake Goddess), Beth Alpha mosaic (PD), 5 Moedim storyboard panels, DK map.

## Open items (in priority order)
1. **Kuntillet Pithos A illustration** — ✅ DONE (2026-07-08): Moedim raster
   `kuntillet-pithos-a.jpg` (from Kymber's ChatGPT reimagining; not a copy of Beck's drawing)
   embedded in the "YHWH and His Asherah" section of `the-lady-of-the-temple.md`, caption points
   to Beck 2002 in Sources; crude `kuntillet-tree.svg` placeholder deleted.
2. **Term-refs** — `elijah-and-elisha.md` and `why-it-matters.md` have none; optionally add a few
   (Baal, bamah/high place, still small voice) for consistency with the other pages.
3. **Publish** when ready — flip Divided Kingdom pages to `draft = false`, merge to `main`.
4. **Future guides to prep** — Assyrian, Babylonian, Greek: the scattering of the 12 tribes, the
   destruction of the First Temple, and Achaemenid–Greece history.
5. **Hugo deprecation cleanup (low priority)** — Hugo v0.164.0 (laptop; newer than desktop's)
   prints two deprecation warnings: `languageCode` → `locale` in site config, and
   `.Site.Data` → `hugo.Data` in templates. Harmless for now; fix when convenient.

## Conventions / guardrails
- Scripture verified against the local ScriptureDatabase JSON (LDS/KJV), never from memory.
- Images are CFM-original, author's-own photos, or public domain — no unlicensed third-party art.
- Shared-file edits are intentional: `baseof.html` (BLB scripture hover, additive) and
  `tabernacle.css` (home card-grid). Kymber chose NOT to revert the tabernacle change.
- **Do not commit** `content/weeks/*` or `static/content/week*/` — a pre-commit hook guards them
  (there are stale week 26–28 edits left uncommitted on purpose; not part of this work).
