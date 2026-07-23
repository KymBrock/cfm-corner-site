# Field-Guide Maps & Images — Licensable Sourcing Guide

*Working reference for the Achaemenid, Assyria, and Babylon field guides. Not a published page (lives in `docs/`, outside `content/`). Compiled 2026-07-22; entry-point URLs verified to resolve.*

## The one rule before you use anything
Each individual file must be checked on **its own page** for its license — Wikimedia Commons holds a mix of Public Domain, CC0, CC-BY, and CC-BY-SA. Never assume a category's contents share one license. Record, for every asset you pull: **(1) the source URL, (2) the exact license, (3) the author/attribution string, (4) the date pulled.**

## License cheat-sheet (what these mean for CFM Corner)
- **Public Domain / CC0** — use freely, no attribution legally required (but credit anyway). *Best choice.*
- **CC-BY** — free to use, must credit the author.
- **CC-BY-SA** — free to use, must credit **and** keep the same license on any derivative (fine for us; we just credit).
- **CC-BY-NC / CC-BY-NC-SA** — **non-commercial only.** CFM Corner is a free, non-monetized study site, so this is usable — but if the site ever runs ads or sells anything, these must be removed. World History Encyclopedia's images are **CC-BY-NC-SA 4.0**; the guides already cite WHE, so this is a known, accepted term. Flag it if the site's commercial status ever changes.
- **© All rights reserved** (most museum "collection" photos, stock sites) — do **not** use without written permission. The exceptions below (Met, some British Museum) explicitly opt into open licenses.

---

## A. Base maps (the keystone — needed for the `site-map-widget`)
The interactive site-map on each guide's "Major Sites" page needs **one high-resolution base map image** of the region, against which hotspot coordinates (`data-top` / `data-left`, as % of the image) are calibrated. This asset does not exist yet for Achaemenid/Assyria/Babylon and is the blocker for building those widgets.

| Source | License | Notes |
|---|---|---|
| [Wikimedia — Maps of the Achaemenid Empire](https://commons.wikimedia.org/wiki/Category:Maps_of_the_Achaemenid_Empire) | mixed (many PD / CC-BY-SA) | Several clean vector + raster maps of the empire's extent and the Royal Road. **Recommended starting point.** |
| [Wikimedia — Achaemenid Empire](https://commons.wikimedia.org/wiki/Category:Achaemenid_Empire) | mixed | Broader category; includes region maps. |
| [Wikimedia — Neo-Assyrian Empire](https://commons.wikimedia.org/wiki/Category:Neo-Assyrian_Empire) | mixed | For the **Assyria** guide's base map. |
| [Ancient World Mapping Center](https://awmc.unc.edu/) (UNC) | CC-BY-NC 3.0 | Scholarly, clean base maps of the ancient world; good for a custom Persia/Mesopotamia crop. (The old `/free-maps/` path 404s — start from the homepage.) |
| The site's **own** `era-map` SVGs (`/images/culture/egypt/maps/ane-0500bc.svg`) | owned by CFM Corner | Already in the repo. Could be re-styled into a static site-base, but they're whole-Near-East, not a sites-detail crop. |

> **Recommendation:** pick or crop one PD/CC-BY-SA regional map (Iran plateau + Mesopotamia + Anatolia to the Aegean), size it to a consistent aspect ratio, drop it at `/images/culture/achaemenid/maps/persian-empire-sites.jpg`, then the hotspot `%` coordinates for Persepolis/Susa/Pasargadae/Behistun/Ecbatana/Babylon/Sardis can be calibrated against it. Until that image exists and is placed, the site-map-widget scaffold can be written but not positioned.

---

## B. Site photos (for the site-map galleries)
All verified to resolve. Each gallery image still needs its individual license checked.

**Achaemenid / Persia:**
- **Persepolis** — [Wikimedia: Category:Persepolis](https://commons.wikimedia.org/wiki/Category:Persepolis) (abundant CC-BY-SA photos of the Apadana, the Gate of All Nations, the reliefs)
- **Pasargadae & the Tomb of Cyrus** — [Wikimedia: Category:Pasargadae](https://commons.wikimedia.org/wiki/Category:Pasargadae) · [Category:Tomb of Cyrus the Great](https://commons.wikimedia.org/wiki/Category:Tomb_of_Cyrus_the_Great)
- **Susa (Shushan)** — [Wikimedia: Category:Susa](https://commons.wikimedia.org/wiki/Category:Susa)
- **Behistun relief/inscription** — [Wikimedia: Category:Behistun Inscription](https://commons.wikimedia.org/wiki/Category:Behistun_Inscription)
- **Naqsh-e Rustam (royal tombs)** — Wikimedia Category:Naqsh-e Rostam
- General — [World History Encyclopedia image search: Achaemenid](https://www.worldhistory.org/image/?search=achaemenid) (CC-BY-NC-SA 4.0, credit "© <author>, World History Encyclopedia")

**Assyria (for that guide):**
- Wikimedia Categories: Nineveh, Nimrud, Khorsabad, Assyrian reliefs, Lamassu, Lachish reliefs (British Museum)
- The **Lachish reliefs** and **lamassu** are also in the British Museum's open-access collection (check per-object license).

---

## C. Key artifacts (open-access, high value)
- **Cyrus Cylinder** — [British Museum object W_1880-0617-1941](https://www.britishmuseum.org/collection/object/W_1880-0617-1941) (BM has an open-access image program — check the object's license) · also PD photos on Wikimedia.
- **The Metropolitan Museum of Art — Open Access (CC0)** — [Achaemenid open-access search](https://www.metmuseum.org/art/collection/search?q=achaemenid&showOnly=openAccess). Met CC0 images are the **cleanest legal option** for Persian gold, seals, rhytons, and Assyrian reliefs — no attribution legally required. (The search URL rate-limits scripts but works in a browser.)
- **Louvre** — some Persian/Assyrian pieces (the Susa glazed-brick archers, Khorsabad lamassu) are available; check `collections.louvre.fr` per-object terms.

---

## D. Attribution format to use on the page
Match the existing Egypt guide's caption style, e.g.:
`<em>Wikimedia Commons, CC BY-SA.</em>` or `<em>© Jane Doe, World History Encyclopedia (CC BY-NC-SA 4.0).</em>` or `<em>The Metropolitan Museum of Art (CC0).</em>`
Egypt's page 08 already models this — reuse it verbatim in structure.

---

## E. Status / next actions
1. **Base map** (blocker) — choose + place one regional map per guide (see §A recommendation). Human pick recommended so the styling matches.
2. Once the base map exists, calibrate hotspot `%` coordinates and build the `site-map-widget` (scaffold pattern is Egypt's `08-major-sites.md`).
3. Pull 2–4 gallery images per site from §B, logging license + attribution for each.
4. The **era-map widget** (a different, simpler interactive) needs **none** of this — it's already added to Achaemenid and works from the shared SVG maps.

*Compiled for CFM Corner field guides — Achaemenid / Assyria / Babylon.*
