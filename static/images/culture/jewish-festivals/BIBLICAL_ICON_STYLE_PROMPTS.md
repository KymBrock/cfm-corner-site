# Biblical Icon Style Prompts

> Reusable prompt system for festival icons, animal flashcards, and related symbolic image sets
> Intended for the CFM Corner visual system

## Core Style Prompt

Use this as the base prompt for any new icon in this series.

```text
Create an original icon for a biblical teaching resource.

Format:
- beveled square tile
- softly clipped corners
- 512x512 PNG

Visual treatment:
- layered paper-cut shapes
- matte paper texture
- subtle depth between layers
- clean silhouettes
- minimal internal detail
- muted earth-tone palette
- calm, reverent, handcrafted feeling
- simple centered composition
- elegant and symbolic rather than realistic

Avoid:
- copying any existing artwork
- referencing any named artist or named style
- cartoon effects
- glossy effects
- gradients
- exaggerated cute style
- playful modern tech illustration
- app icon look

Important:
- make this a completely new original icon
- keep the composition readable at small size
- favor dignity, clarity, and warmth over complexity
```

## Botanical / Festival Variant

Use this for seven-species icons or other feast-symbol imagery.

```text
Create an original botanical icon for a biblical harvest page.

Format:
- beveled square tile
- softly clipped corners
- 512x512 PNG

Visual treatment:
- layered paper-cut shapes
- matte paper texture
- subtle depth between layers
- clean silhouettes
- minimal internal detail
- muted earth-tone palette
- calm, reverent, handcrafted feeling
- simple centered composition
- elegant and symbolic rather than realistic

Avoid:
- copying any existing artwork
- referencing any named artist or named style
- cartoon effects
- glossy effects
- gradients
- playful modern tech illustration
- app icon look

Subject:
[INSERT BOTANICAL SUBJECT]

Tile color:
[INSERT HEX COLOR]

Accent colors:
[INSERT COLORS]

Make this a completely new original icon.
```

## Animal Flashcard Variant — LOCKED v2

> ⚠️ Updated March 2026. This replaces the previous animal variant.
> The old prompt caused ChatGPT/DALL-E to add a white stroke border (sticker look).
> The correct edge treatment is a soft drop shadow only — NO white border.
> See "Session Workflow" section below for how to anchor new sessions with a reference image.

Use this for Noah animals, Bible animals, or child-recognizable flashcards.

```text
Create an original animal icon for a biblical teaching flashcard.

FORMAT (NON-NEGOTIABLE):
- Square canvas, white background
- A single rounded-square tile filling most of the canvas
- Corner radius approximately 18% of total width (similar to an iOS app icon)
- NO white border, NO stroke, NO frame, NO outline around the tile
- The tile color extends fully to the rounded edge with no inset or frame
- The ONLY edge treatment is a very soft, low-opacity drop shadow outside the tile
- Shadow is subtle — the card should look resting on a surface, not floating

TILE BACKGROUND:
- Single flat color: [INSERT HEX]
- Subtle matte paper/fabric texture across the entire tile
- No gradients, no lighting, no vignette, no center glow

ILLUSTRATION STYLE:
- Layered paper-cut construction
- Each body part is a separate cut shape with its own matte surface
- Shapes have subtle tonal variation between layers (like different paper colors)
- Organic, slightly imperfect edges — not perfect vector curves
- No painted shading, no smooth blending, no airbrush
- No outlines or strokes on shapes — color contrast defines edges
- No cast shadows within the tile (none at all is acceptable)

ANIMAL DETAIL:
- 3–6 layered shapes for major body forms
- Markings, fur texture, or patterns built from separate cut shapes (not printed texture)
- Face: calm, neutral expression
- Eye: small, matte, no gloss or catchlight
- No cartoon smile, no exaggerated proportions

COMPOSITION:
- Animal centered horizontally, slightly above vertical center
- Clean margin on all sides
- Animal faces right or is in profile

ANIMAL: [INSERT ANIMAL NAME AND POSE]
TILE COLOR: [INSERT HEX]
ACCENT COLORS: [INSERT 2–3 HEX VALUES from the palette below]

APPROVED PALETTE:
#dbc3a4 · #be8b55 · #c88143 · #923a23
#7a5c6e · #5f4656 · #3f6438 · #466758 · #536b83

DO NOT:
- Add any white stroke, border, or frame around the tile
- Add any inner border or inset frame
- Use gradients anywhere
- Use glossy or shiny effects
- Use realistic rendering or 3D shading
- Reference any named artist or existing artwork
- Use exaggerated cute or cartoon style

This must be a completely original image.
```

## Session Workflow (How to Avoid Style Drift)

DALL-E has no memory between sessions. Follow this workflow every time you open a new ChatGPT conversation:

**Step 1 — Upload a reference image first.**
Use the pig (`B2AA9824`) or the owl (`F56DB9BB`) from the Animals folder. These are the cleanest examples of the target style.

**Step 2 — Paste this opener before your prompt:**

```text
Generate a new animal in this exact visual style — same tile shape, same paper-cut illustration technique, same shadow treatment. No white border of any kind. The soft shadow you see around the tile is the only edge effect. Use the detailed prompt below for all specifications.
```

**Step 3 — Paste the full locked prompt above** with ANIMAL, TILE COLOR, and ACCENT COLORS filled in.

**Why the sticker border happened:**
The phrase "white border" in correction attempts caused DALL-E to draw a literal stroke. The correct description is "no border — only a soft outer drop shadow." The old phrases "beveled square tile" and "softly clipped corners" were also ambiguous and have been replaced with the explicit corner radius description.

## Suggested Shared Palette

### Tile Colors
- `#d4a53e` — Golden Ochre
- `#be8b55` — Warm Caramel
- `#466758` — Deep Sage
- `#3f6438` — Forest Moss
- `#923a23` — Rusted Brick
- `#536b83` — Dusk Slate
- `#c88143` — Burnished Copper
- `#634130` — Deep Umber

### Accent Colors
- `#dbbb87` — Honey Wheat
- `#edc25a` — Sunlit Amber
- `#dbc3a4` — Pale Driftwood
- `#b1542f` — Ember Clay
- `#634130` — Deep Umber
- `#3f6438` — Forest Moss
- `#466758` — Deep Sage

## Prompting Rules

1. Do not say "match this image" or "same style as existing artwork."
2. Describe the visual characteristics directly.
3. Do not reference named artists or copyrighted works.
4. Ask for a completely new original icon each time.
5. Keep one subject per tile.
6. Keep the composition centered and simple.
7. Prefer symbolic clarity over decorative detail.

## Best Uses

- Seven species / festival icons
- Noah flashcard animals
- Bible animals
- symbolic feast imagery
- educational visual tiles for children or lesson pages

## Output Convention

- PNG
- 512x512
- single subject
- one tile per file
- transparent outside tile only if needed by the tool
