# Moedim raster prompts — First Temple & Divided Kingdom (Track 2)

For the **atmospheric raster track** (ChatGPT / OpenAI image-gen + Moedim Animation Studio). These produce the fully painterly bases/assets that match the Tabernacle guide's look (e.g. `static/images/tabernacle/tabernacle-floorplan-clean.png`). The in-repo SVGs are the provenance-clean fallback / immediate version; drop a generated raster in as the base `image` when ready (the hotspot data + x/y in `data/first-temple/hotspots.yaml` stay valid as long as the new base keeps the same top-down layout and proportions).

**House style — paste verbatim into every prompt** (from `OT_2026/Culture/.../Visual_Style/CFM_MOEDIM_IMAGE_PROMPTS.md`):

> CFM Corner Moedim animation style: clean 2D hand-painted animation look, layered paper-cut forms, warm parchment whites, deep navy text, muted terracotta, olive, antique gold, slate blue, soft desert greens, gentle dimensional shadows, refined devotional educational illustration, modern but ancient Near Eastern in tone. Not photorealistic, not medieval engraving, not fantasy, not cluttered.

**Rules (learned):** say *"Moedim animation style, not realistic"* early and repeatedly · for compositing assets say *"ONLY a standalone asset"* + *"fully transparent PNG"* + *"no scene"* · **no baked-in text labels** (labels/hotspots are added in Hugo/design) · any Hebrew = *"decorative Hebrew-style scribal marks, not readable scripture."* · **provenance:** end every prompt with *"original composition; do not reproduce any specific copyrighted reconstruction."*

---

## 1. Temple floor-plan base (PRIMARY — top-down, matches the Tabernacle map)

```text
CFM Corner Moedim animation style, not realistic. A top-down (bird's-eye) floor-plan
illustration of Solomon's First Temple and its courtyard, in the same clean 2D
hand-painted, layered paper-cut look as a warm desert sanctuary map: warm sandy
parchment ground, soft dimensional shadows, muted terracotta, olive, antique gold,
slate blue, soft desert greens.

Layout (long axis horizontal; entrance faces EAST at the RIGHT, the inner sanctuary
at the far LEFT/WEST; north at top):
- A rectangular stone temple building, three chambers in a row. From right to left:
  a shallow PORCH; a long MAIN HALL with gold-toned cedar-paneled walls; and at the
  far left a smaller perfect-square INNER ROOM rendered in rich antique gold.
- Two free-standing bronze pillars flanking the porch entrance (one north, one south),
  with decorative lily-and-pomegranate capitals.
- Three stories of small side chambers wrapping the north, west, and south outer walls.
- In the courtyard before the porch: a large square bronze ALTAR with a gentle flame;
  a very large round bronze basin ("molten sea") resting on twelve oxen (three facing
  each compass direction), placed toward the south-east; and ten small wheeled bronze
  basins, five along the north and five along the south.
- A few stylized palm trees and desert rocks at the edges of the sandy court.

Proportions to honor (do not print numbers on the image): porch 20 wide × 10 deep;
main hall 40 long × 20 wide; inner room a 20 × 20 square; the whole house twice as
long as the hall-plus-inner-room is wide.

NO text, no labels, no numbers, no compass letters anywhere in the image (added later
in design). Not photorealistic, not an engraving, not fantasy, not cluttered.
Original composition; do not reproduce any specific copyrighted reconstruction.
Output a high-resolution image with a warm sandy background (not transparent).
```
*After generating:* save as `static/images/culture/first-temple/temple-floorplan.png`, set it as the page `image` (keep the SVG as the vector fallback), and re-check the 11 hotspot x/y against it.

## 2. Temple furnishing map-icons (standalone, transparent — for hotspot markers)

Match the existing `static/images/tabernacle/mapicon-*.png` set. **Reusable as-is from the Tabernacle set** (same furnishings): ark, menorah/lampstand, table of showbread, laver, brazen altar. **Generate new** for the Temple-specific pieces:

```text
CFM Corner Moedim animation style, not realistic. Create ONLY a standalone asset on a
FULLY TRANSPARENT background — no scene, no ground, no shadow plate baked in.
Subject: a single free-standing bronze temple pillar seen from a gentle top-down 3/4
angle, with an ornate capital of lilies and two rows of pomegranates, antique-gold and
bronze tones, soft cel-shaded highlights, clean paper-cut edges.
No text. Not photorealistic, not an engraving. Original composition; do not reproduce
any specific copyrighted reconstruction. High-resolution transparent PNG icon.
```
Repeat for: **the molten sea** (large round bronze basin on twelve oxen, top-down) and **the pair of cherubim** (two gold winged guardian figures, wings touching, stylized). File-naming: `static/images/culture/first-temple/mapicon-jachin.png`, `…-boaz.png`, `…-molten-sea.png`, `…-cherubim.png`.

## 3. Divided-kingdom atmospheric scene (optional companion to the SVG map)

```text
CFM Corner Moedim animation style, not realistic. A warm illustrated scene of the
divided kingdom of ancient Israel: in the foreground a golden calf idol on a stone
pedestal at a hilltop shrine (muted terracotta, olive, antique gold, soft desert
greens, slate-blue sky), with two small worship platforms in the distant north and a
walled temple city on a southern hill far to the other side, a dividing valley between
them. Layered paper-cut forms, gentle dimensional shadows, deep navy shadows.
NO text or labels. Not photorealistic, not fantasy, not cluttered. Original
composition; do not reproduce any specific copyrighted reconstruction. High-resolution.
```
*Use as a section header/atmospheric image on Guide B; the SVG map stays the informational piece.*

## 4. Divided-kingdom MAP — painterly (to match the seven-nations Canaan map)

The way to get a map that is **both on-brand and geographically correct**: attach **two** reference images in ChatGPT —
- **STYLE reference:** `static/images/culture/canaan/03-seven-nations-map.png` (the reader-facing house map)
- **GEOGRAPHY / LAYOUT blueprint:** `static/images/culture/divided-kingdom/divided-kingdom-map.blueprint.png` (PNG export of our accurate SVG)

```text
Create a single illustrated historical map in the EXACT painterly style of the FIRST
attached image — a warm aged-parchment map with soft relief shading, hill and mountain
texturing, blue seas and rivers, a decorative compass rose and elegant serif labels.
CFM Corner Moedim style: hand-painted, not photorealistic, not a flat modern infographic,
not a video-game render, not fantasy.

Use the SECOND attached image as the GEOGRAPHY and LAYOUT blueprint: keep the same
coastline, the Jordan River flowing from the Sea of Galilee down to the Dead Sea, and
the same relative positions of every place.

Subject — the divided kingdom after Solomon (1 Kings 12):
- Two gently tinted, labeled territories: KINGDOM OF ISRAEL in the north (Galilee,
  Samaria, and Gilead east of the Jordan) and KINGDOM OF JUDAH in the south (the Judean
  hill country), with a soft dividing border running east–west just north of Jerusalem.
- A golden-calf shrine at DAN (far north) and at BETHEL (just north of the border).
- A small temple icon at JERUSALEM (just south of the border).
- Labeled city dots: Dan, Samaria, Shechem, Bethel, Jerusalem, Hebron, Beersheba.
- Faint neighbor labels at the edges: Phoenicia (NW), Aram-Damascus (NE), Philistia
  (SW coast), Ammon and Moab (east of the Jordan/Dead Sea), Edom (south).
- Labeled water: Mediterranean Sea, Sea of Galilee, Jordan River, Dead Sea.
- A compass rose and a simple scale bar. Title lettered at top: THE DIVIDED KINGDOM.

All labels spelled exactly as listed and clearly readable. Do NOT invent extra cities or
change the geography. Aged-parchment background (not transparent). Original composition;
do not reproduce any specific copyrighted reconstruction or basemap.
```
*After generating:* save as `static/images/culture/divided-kingdom/divided-kingdom-map.png`; use it as the page image and keep the SVG as the precise/interactive fallback. The kingdom-border line and "borders are approximate" caveat from the SVG should carry over.

---

**Note:** the regnal-evaluation **timeline** is a data-driven chart, not a raster candidate — it stays the script-generated SVG (`scripts/build_regnal_timeline.py`).
