# Integration notes — First Temple & Divided Kingdom visuals (v1)

**Branch:** `feature/first-temple-divided-kingdom`
**Lane:** built by the visual lane (Claude Code). Hugo wiring below is the **Codex lane** — these notes list exactly what is left to do. Nothing here touches `hugo_converter.py` or the existing lesson HTML.

## What shipped (provenance-clean, geometry/verdicts verified)

| Visual | Files |
|---|---|
| **A — Floor-plan hotspot map** (flagship) | `static/images/culture/first-temple/temple-floorplan.svg` · `data/first-temple/hotspots.yaml` (11 points) |
| **B — Divided-kingdom map** | `static/images/culture/divided-kingdom/divided-kingdom-map.svg` |
| **B — Regnal-evaluation timeline** | `static/images/culture/divided-kingdom/regnal-timeline.svg` (generated) · `scripts/build_regnal_timeline.py` · `data/divided-kingdom/kings.json` |
| Preview (build-lane only) | `static/previews/first-temple-floorplan-preview.html` · content stub `content/culture/ancient/first-temple/explore-the-floor-plan.md` (`draft = true`) |

Hotspot copy/deep_dive in `hotspots.yaml` is **verbatim** from the verified vault draft (`A_First_Temple/03_.../03-floor-plan-hotspots.DRAFT.md`). The build lane supplied only `id` + `x/y`. No open `<!-- VERIFY -->` markers.

## What Codex needs to wire

1. **Generalize the hotspot/term-popup data lookup (one theme change).**
   `themes/cfm/layouts/culture/tabernacle.html` hardcodes `index site.Data.tabernacle.hotspots .` and `site.Data.tabernacle.term_popups`. As-is, `hotspotKey = "first-temple"` resolves against `data/tabernacle/`, not `data/first-temple/`, so the flagship will not render. Honor the page param **`dataNamespace`** (already set to `first-temple` on the stub), e.g. `index (index site.Data .Params.dataNamespace) "hotspots"`, or factor the interactive into a shared partial. (Local SVG + position rendering is already verifiable via the preview harness without this change.)

2. **Register the section + nav.** Create `content/culture/ancient/first-temple/_index.md` (+ home/overview pages as the content lane delivers them) and add First Temple to the culture nav. The shared layout's `field-guide-nav` block currently hardcodes the four Tabernacle pages — parametrize or branch it per guide. Then flip `draft = false` on the floor-plan page.

3. **Popups / links / iframes inside hotspot copy.** The `copy`/`deep_dive` text carries scripture references (e.g. *1 Kings 6:20*) and cross-references (e.g. "see the Dedication section (A6)"). Wire these per `LEXICON-POPUP-SPEC.md` / the term-ref pattern. If Hebrew term popups are wanted (terms like *ulam*, *hekhal*, *devir* are in each hotspot's `translit`/`hebrew`), add `data/first-temple/term_popups.yaml` (content lane supplies definitions).

4. **Embed the map + timeline into Guide B pages.** Both are standalone SVGs under `static/images/culture/divided-kingdom/`. Place via the normal converter/shortcode flow on the Guide B sections (split / sin-of-Jeroboam / how-Kings-was-written). They are plain `<img>`-able; no JS required.

5. **CSS.** The layout loads `css/tabernacle.css`; First Temple reuses the same tokens (sage/gold/slate/terracotta). The SVGs are self-styled (inline `<style>`), so they need no extra CSS. Add a `first-temple.css` only if a distinct skin is wanted.

6. **Provenance framing in prose (guardrail).** The SVGs already footnote the Kings-vs-Chronicles tensions (pillars 18 vs 35; sea 2,000 vs 3,000; altar from 2 Chr 4:1; partition = doors + veil) and the "no remains excavated / reconstruction" note. Ensure the page prose also leads with "deepens, not debunks" and labels contested claims per the build-plan guardrails.

## Divided-kingdom map base (licensed)

The publish-quality divided-kingdom map is being built in Illustrator over **LDS Bible Map 1 — "Physical Map of the Holy Land"** (© Intellectual Reserve), used **by permission (calling-related)**. The raw source lives in the git-ignored `_source-maps/` (never committed/published — see `_source-maps/CREDIT.txt`). The **published derivative must carry the credit line the permission grant specifies.** The in-repo `divided-kingdom-map.svg` remains the accurate label/layout layer and the interactive/vector fallback.

## Regenerating the timeline

`python3 scripts/build_regnal_timeline.py` re-reads `data/divided-kingdom/kings.json` and rewrites the SVG. `dates_bce` are intentionally `null`; when a chronology (e.g. Thiele) is chosen and the dates are filled in, each cell auto-renders its BCE label — re-run the script, no code change.
