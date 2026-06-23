# Handoff — First Temple & Divided Kingdom visuals → main project integration

**Paste this into the integration/Codex session.** The visual-build lane (Claude Code) has produced and committed the Week 26–27 visuals. This is the rejoin point: pull them into the Hugo site and publish. Nothing below requires re-deriving facts — geometry, verdicts, and hotspot copy are already verified.

## Repo / branch
- Repo: `~/Developer/cfm-corner-site` (the live Hugo site).
- Branch: **`feature/first-temple-divided-kingdom`** (all work committed here; do not start a new branch).
- Unrelated WIP on `main` (baseof.html, link-audit.py, etc.) is untouched — leave it.

## What's committed (ready to wire)
| File | What it is | State |
|---|---|---|
| `static/images/culture/first-temple/temple-floorplan.svg` | Flagship floor-plan base (Moedim style, verified cubit geometry) | Done |
| `data/first-temple/hotspots.yaml` | 11 hotspots, copy **verbatim** from the verified vault draft; `x/y` set to the SVG | Done |
| `content/culture/ancient/first-temple/explore-the-floor-plan.md` | Preview stub, `draft = true`, `layout="tabernacle"`, `hotspotKey="first-temple"`, `dataNamespace="first-temple"` | Stub — finalize |
| `static/previews/first-temple-floorplan-preview.html` | Build-lane QA harness (not for production) | Reference only |
| `static/images/culture/divided-kingdom/divided-kingdom-map.svg` | Divided-kingdom map (geographic, Moedim) — Dan/Bethel calves vs. Jerusalem | Done (see "pending" re: painterly version) |
| `static/images/culture/divided-kingdom/regnal-timeline.svg` | Regnal-evaluation timeline (generated) | Done |
| `scripts/build_regnal_timeline.py` | Regenerates the timeline from kings.json | Done |
| `data/divided-kingdom/kings.json` | Verified regnal data (verdicts quoted; BCE dates null) | Done |
| `static/images/culture/divided-kingdom/divided-kingdom-map.blueprint.png` | PNG blueprint for the Track-2 painterly map | Reference |
| `INTEGRATION_NOTES_first-temple-divided-kingdom.md` | **Detailed integration spec — read this** | — |
| `MOEDIM_RASTER_PROMPTS_first-temple-divided-kingdom.md` | Track-2 ChatGPT/Moedim prompts | — |

## Integration tasks (Codex / Hugo lane)
Full detail in `INTEGRATION_NOTES_first-temple-divided-kingdom.md`; the essentials:

1. **Generalize the hotspot data lookup (one theme change).** `themes/cfm/layouts/culture/tabernacle.html` hardcodes `index site.Data.tabernacle.hotspots .`. Make it honor the page's **`dataNamespace`** param (already set to `first-temple` on the stub) so `hotspotKey="first-temple"` resolves against `data/first-temple/hotspots.yaml`. (Or add a parallel layout/partial.) Without this the flagship won't render.
2. **Register the section + nav.** Create `content/culture/ancient/first-temple/_index.md` (+ overview/home pages as the content lane delivers them), add First Temple to the culture nav, then flip `draft = false` on the floor-plan page. The shared layout's `field-guide-nav` currently hardcodes the four Tabernacle pages — parametrize per guide.
3. **Wire popups/links.** Hotspot `copy`/`deep_dive` carry scripture refs (e.g. *1 Kings 6:20*) and cross-refs ("see Dedication A6"); wire per `LEXICON-POPUP-SPEC.md`. Hebrew terms are in each hotspot's `translit`/`hebrew` — add `data/first-temple/term_popups.yaml` if term popups are wanted (content lane supplies definitions).
4. **Embed map + timeline on Guide B pages** (split / sin-of-Jeroboam / how-Kings-was-written) via the normal converter/shortcode flow. Both are plain `<img>`-able SVGs.
5. **CSS** reuses `static/css/tabernacle.css` tokens; SVGs are self-styled, no extra CSS needed.
6. **Provenance framing** (guardrail): SVGs already footnote the Kings-vs-Chronicles tensions and the "no remains excavated / reconstruction" note; ensure page prose leads "deepens, not debunks" and labels contested claims.

## Pending (not yet in repo — coming from Kymber)
- **Divided-kingdom map, publish version.** Kymber is building a higher-fidelity map in Illustrator over **LDS Bible Map 1 (Physical Map of the Holy Land), used by permission (calling-related)** — and/or via the Track-2 painterly prompt. When delivered, it replaces/augments `divided-kingdom-map.svg` as the page image. The current SVG stays the accurate fallback. Raw licensed base + working traces live in git-ignored `_source-maps/` (do **not** commit/publish the raw LDS map).
  - **The published derivative must carry the credit line the permission grant specifies** (e.g. "© Intellectual Reserve, Inc.").
- **Floor-plan + timeline publish polish** (via Claude Design or direct tweaks) may land before integration — re-pull before wiring.

## Lane boundaries
- Build lane owns the SVGs + data + the generator script. Integration lane owns the Hugo wiring (layout, sections, nav, popups, converter, deploy) — don't rewrite the SVGs/data except to wire them.
- Don't batch-regenerate existing lesson HTML. Commit checkpoints on the feature branch.

## Definition of done (per the build plan)
Both guides live, scoped lean, cross-linked (A↔B + Tabernacle back-link), flagship interactive working, **zero open `<!-- VERIFY -->`**, Kymber voice + doctrinal pass, deployed, live-checked.
