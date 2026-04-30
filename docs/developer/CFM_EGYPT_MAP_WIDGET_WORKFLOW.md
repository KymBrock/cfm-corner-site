# Map Widget Workflow

This note captures the workflow we used to build the Ancient Egypt interactive map so it can be reused for other cultures and geographies later in the year.

## Related References
- Developer docs index: `/Users/kymberbrockbank/Developer/cfm-corner-site/docs/developer/README.md`
- Developer tools index: `/Users/kymberbrockbank/Obsidian/K Master Vault/Tools/TOOLS_MASTER_INDEX.md`
- Master Brain: `/Users/kymberbrockbank/Obsidian/K Master Vault/00_Dashboard/MASTER_BRAIN.md`
- Original project note: `/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Culture/Egypt/images/Maps widget/MAP_WIDGET_WORKFLOW.md`

## Core Principle
Separate `geography` from `style`.

- Keep the map geometry and hotspot coordinates accurate.
- Treat the icons and visual treatment as a separate overlay layer.
- Never trust AI-generated artwork for geographic placement.
- Use generated/edited PNG landmark assets only as clickable visual markers.

## Best Overall Workflow
1. Start with an accurate base map.
2. Build the interactive widget with coded hotspot coordinates.
3. Generate or refine landmark icons separately.
4. Clean the icons and remove transparent waste space.
5. Place icons near the correct city/site labels without covering text.
6. Link each icon to a detail panel with images and explanatory text.
7. Do placement QA visually in-browser.
8. Only after layout is stable, polish the surrounding UI.

## What Worked Best For The Icon Style
The winning direction was:
- flat 2D
- silhouette-first
- transparent background
- dusty historical palette
- low contrast
- matte finish
- broad geometric forms
- very little interior detail
- readable at very small map size

The icon should read like a `tiny map landmark`, not a polished illustration, logo, sticker, badge, or app icon.

## Palette Direction That Worked
Use a subdued limestone / sandstone palette:
- dark dusty brown for shadow planes
- muted limestone or sandstone tan for the main form
- soft beige-tan only if absolutely needed
- low contrast only

Avoid:
- bright yellow-gold
- bright cream
- orange glow
- red cast
- saturated warm tones
- glossy shading

## Prompt Formula For New Landmark Icons
Use this structure:

```text
Create a transparent-background map landmark asset of [SITE NAME].

Subject:
[a very short description of the landmark's most recognizable outer shape]

Purpose:
this will be a tiny landmark icon placed on an illustrated historical map, so it must read clearly at very small size

Style:
- same style family as the approved map icons
- flat 2D
- silhouette-first
- simple historical map landmark
- not a logo
- not an app icon
- not a badge
- not a poster
- not a realistic illustration

Color family:
- dark dusty brown for shadow planes
- muted limestone/sandstone tan for the main forms
- soft beige-tan only if absolutely needed
- low contrast
- matte finish
- subdued historical stone feel

Important:
- no bright yellow-gold
- no bright cream
- no saturated colors
- no orange glow
- no glossy shading
- no modern icon look

Requirements:
- transparent background only
- no sky
- no people
- no text
- no glow
- no vignette
- no texture background
- no realistic stone texture
- no fine carved detail

Design rules:
- [list 2-4 silhouette rules specific to the site]
- broad clean shapes only
- very little interior detail
- readable at very small map size
- should feel like a landmark cutout for a historical map

If it looks too detailed, too realistic, too modern, or too much like a full scene, it is wrong.
```

## Prompt Formula For Simplifying An Icon
This was needed often and should be reused.

```text
Revise this image to be much simpler.

The current version is too detailed for a tiny map landmark.

Required correction:
- remove most texture
- remove most repeated small detail
- remove most surface variation
- simplify the image into broad clean shapes
- keep only the minimum forms needed to read as [SITE NAME]

Keep only:
1. [main shape block]
2. [secondary recognition feature]
3. [doorway/statue/column group if essential]
4. 2 or 3 tonal planes maximum

Style:
- flat 2D
- transparent background only
- same dusty limestone palette as the other Egypt icons
- low contrast
- matte finish
- historical map landmark
- not a realistic rendering
- not a detailed drawing
- not a modern icon

Important:
- no background
- no glow
- no vignette
- no texture
- no fine lines
- no small repeated details
- no realistic rendering

Design rule:
this should read at map size.
It should feel like a simplified cut-paper symbol, not a scene or illustration.

If there is visible texture or too much detail, it is wrong.
```

## Visual Category Mistakes To Avoid In Prompts
If the model gets stuck, explicitly forbid these:
- logo style
- app icon style
- badge style
- sticker style
- poster composition
- polished icon-pack look
- realistic rendering
- photographic cutout
- scene illustration
- parchment background
- dramatic lighting
- glow
- vignette
- textured background

## Site-Type Heuristics For Choosing An Icon Subject
Use the most recognizable outer shape, not the most historically complete one.

Examples:
- Giza: pyramids + Sphinx silhouette
- Saqqara: Step Pyramid tiers
- Heliopolis: obelisk
- Avaris/Goshen: mudbrick settlement with palms
- Karnak: two pylon towers, tiny hint of avenue if needed
- Luxor: temple entrance with seated colossi
- Valley of the Kings: layered desert ridges + tomb cutouts
- Hatshepsut: stacked terraces
- Abu Simbel: four seated colossi + central doorway
- Philae: twin pylon temple silhouette
- Elephantine/Satet: compact island temple
- Beni Hasan: cliff with a few tomb doorways
- Serabit el-Khadim: desert shrine + standing stelae
- Amarna: planned sacred city / temple complex silhouette

## File/Asset Workflow That Worked
1. Generate PNG icon.
2. Check whether the file still has baked-in background, glow, or transparent waste space.
3. Remove white/opaque background if present.
4. Crop transparent padding where possible.
5. Copy cleaned asset into the site repo:
   - `static/images/culture/egypt/map-icons/`
6. Wire it into CSS using a site-specific class.
7. Tune size using `--smw-dot-size`.
8. Tune placement in the content file, not by editing the asset itself.

## Coding Architecture We Landed On
The stable architecture is:
- one accurate full SVG map as the base
- hotspot positions stored in content as percentages
- PNG landmark assets rendered as marker glyphs on top
- marker selection + description box controlled in JS
- map labels like Mount Sinai / Wadi El-Hol rendered as overlay text, not baked into the SVG

## Important Files
- `content/culture/ancient/egypt/08-major-sites.md`
- `static/css/site-map-widget.css`
- `static/js/site-map-widget.js`
- `static/images/culture/egypt/08-egypt-sites-map.svg`
- `static/images/culture/egypt/map-icons/*`

## Placement Rules That Worked
- Keep icons near the relevant city/site label.
- Do not cover map text.
- In crowded areas, prioritize readability over exact proximity.
- Use open desert/off-river space when necessary.
- West-bank Luxor sites can be pushed into open desert without losing meaning.
- Delta sites need extra spacing because labels cluster tightly.
- The visual icon can sit slightly away from the exact point if the detail panel makes the site explicit.

## Scaling Rules That Helped
- Some icons need to be larger than expected to read well at map size.
- Icons with simpler silhouettes can often be larger.
- Icons with many columns or repeated shapes usually need simplification before scaling.
- Scale visually in-browser, not by intuition.

## Hover / Hitbox Lesson
Do **not** solve crowded hover problems by changing map geometry.

Safe approach:
- keep marker positions and sizes unchanged
- keep the visible icon unchanged
- tighten only the hover/click target using a separate centered hit area
- do this per-problem marker or per-cluster, not globally unless necessary

Unsafe approaches that caused problems:
- changing the map viewport geometry
- changing the SVG geometry/viewBox to crop it
- changing marker box anchoring in a way that alters visual alignment

## Cropping Lesson
Do **not** crop the SVG map itself after positions are already tuned.
That changed the rendering geometry and shifted placements.

Safe approach:
- keep the full map geometry
- if extra bottom area needs to disappear, use a purely visual mask/overlay
- do not let the mask alter marker math

## Layout Lesson For The Bottom Area
Once the Kush tail was visually hidden, the empty area below the visible map felt awkward.
The better solution was:
- keep the full map geometry intact
- use a visual bottom mask
- overlap the selector ribbon and description card upward into that space
- adjust the selector ribbon separately from the description card

## UI Lessons
- The selector ribbon can float between the map and the description card.
- The description card can overlap upward to bridge empty masked space.
- Move the ribbon and description card independently.
- Micro-adjustment language like `up 15 pixels`, `left 8 pixels` was very effective for final placement work.

## Label Overlay Lessons
Custom map labels (Mount Sinai, Mount Horub, Wadi El-Hol) worked best when:
- the font matched the map's narrow label style
- the labels were overlay elements, not SVG edits
- a tiny red dot was included as a site marker
- text and dot stayed together as one movable unit

## Process For Future Culture Maps
1. Choose an accurate reference map.
2. Build the widget first with placeholders.
3. Identify all required sites.
4. Decide the strongest landmark subject for each site.
5. Generate icons with the shared prompt formula.
6. Simplify icons aggressively until they read at map scale.
7. Clean/crop assets.
8. Wire icons into CSS.
9. Place markers in content.
10. Add detail-panel content and images.
11. Do iterative browser QA for spacing, scale, labels, and hover behavior.
12. Only then do final layout polish.

## Suggested Checklist For The Next Culture
- accurate base map chosen
- all required sites listed
- each site has a landmark concept
- prompt written
- icon generated
- icon simplified
- icon background removed
- transparent padding cropped
- asset copied into repo
- CSS class added
- marker placed
- description added
- hover tested
- mobile tested
- final UI overlap polished

## Recommended Naming Conventions
- use short stable slugs for icon classes and filenames
- keep location names human-readable in the detail panel
- prefer filenames like:
  - `karnak-map.png`
  - `satet-elephantine-map.png`
  - `valley-of-kings-map.png`
  - `hanging-church-map.png`

## Final Takeaway
The most successful formula was:
- accurate coded map
- handcrafted or AI-assisted but heavily simplified landmark assets
- disciplined palette consistency
- aggressive texture removal
- careful in-browser placement tuning
- never letting visual cleanup alter coordinate geometry
