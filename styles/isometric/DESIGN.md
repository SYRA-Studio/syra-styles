---
id: isometric
name: Isometric
kind: primitive
family: Depth and 3D
tags: [3d, miniature, systems, technical, clean]
look: A tiny world of solid blocks seen from above at a fixed angle, with no perspective.
suits: Explaining systems, cities, technology, logistics and how parts fit together.
made_with: code
mixes: []
---

# Isometric

## Feel
A clever model on a table. Calm, tidy and a little playful: you look down on a small world and understand how it works at
a glance. It feels engineered rather than decorated, and it makes complicated things look manageable.

## Colours by job
- **Ground:** deep indigo `#141B34`. The whole background, flat, and most of the frame.
- **Main, in three tones:** a block's top is the lightest `#8FB3FF`, its left face the middle `#4F7BE0`, its right face
  the darkest `#3559B0`. Light always comes from the upper left, for every object, so the tones never swap.
- **Base tile:** top `#232C52`, one step lighter than the ground; left side `#1C2445`, right side `#181F3C`. Its front
  edges may carry a thin lighter strip `#2F3A69`. Roads are flat, in the ground colour.
- **Accent:** warm yellow, in three tones like the main colour (top `#FFC24B`, left `#E8A52A`, right `#C4861A`), under 10%
  of the frame. It means energy, life or "look here": lit windows, a sun, the
  key block. Never for large surfaces.
- **Text:** `#F4F6FF`; secondary text `#8E98C2`.

To recolour, change the three tones together: same hue, top lightest, right darkest.

## Type
Montserrat 800 for titles (about 96 px) and numbers (about 200 px), with the unit in the same weight and size as the
number. Montserrat 500 for the words that explain a number (about 54 px) and small labels (about 34 px). IBM Plex Sans Arabic 700
for Arabic titles, 500 for the rest, about 15% larger than the English beside it.
Headlines stay flat and upright so they read instantly. Only small labels may lie on the ground, using the same isometric
angle as everything else.

## Materials and texture
Clean matte solids: flat colour on each face, no gradients, no noise, no outlines. Under each object sits a flat contact
shadow, a ground-plane shape in black at about 20% opacity, offset to the lower right, with no blur. Small details
(windows, trees as little pyramids or cubes) follow the same three-tone rule at a smaller size. Unlit windows are one tone
darker than their face. Keep them few enough to read as one texture.

## Layout
One diorama per idea, built on one base tile and filling about 55–60% of the frame's width, on one side or centred. Text takes the
remaining side with generous margins (at least 120 px). The world sits on one shared grid: everything snaps to it. Hold
back on detail: five well-placed things beat fifty. With a number on screen, the eye goes to the number, then the accent.

## Motion
Things move only along the three axes: up and down, or along either ground direction. Blocks grow up out of the ground
with a stagger of 0.05–0.08 s, about 0.5 s each, `back.out(1.2)` or `expo.out`. Leaving, they sink back, or the camera
slides along an axis to the next part of the world. Between ideas, keep the same world and change what is happening in it.
Something small always stays alive: windows lighting, a dot travelling along a road. The camera may drift very slowly along
an axis and never rotates.

## How it shows things
- **Numbers:** a large upright figure beside a column or row of blocks that shows the amount. For "40% less", 4 of 10
  blocks sink and leave empty sockets, so it reads at a glance.
- **Comparison:** two towers on the same tile, same footprint, different height.
- **Process:** a path of tiles with something moving along it, stopping at each station.
- **Change over time:** blocks being added or removed in a row, one per step.
- **Parts of a whole:** the object lifts apart in layers along the vertical axis.

## How to make it
Draw with inline SVG polygons. Project a point with `sx = (x - y) * cos(30°)` and `sy = (x + y) * sin(30°) - z`, multiplied
by the unit size, so parallel lines stay parallel forever. A box is three polygons: top, left, right. Draw from back to
front; when footprints differ in size, compare them in pairs rather than trusting `x + y` alone. To grow a block, tween its height value and redraw the polygons from that value in
`onUpdate`; don't use `scaleY`, which shears the top. Windows are small polygons on the same face planes, projected the
same way.

## Arabic and English
Arabic and English stay upright as two separate lines of equal importance, right-aligned for Arabic-first videos, with the
blocks beside them. Never put a long Arabic line on the isometric plane: short labels only, whole words. Numbers use
Western digits unless told otherwise.

## Landscape and vertical
Landscape: diorama on one side, text on the other. Vertical: diorama below, text above, and let the diorama bleed slightly
off both edges.

## What would break it
Perspective or vanishing points. Rotating the camera. A second viewing angle. Soft 3D lighting, gradients or blurred
shadows. Top, left and right tones swapped on any object. Movement that isn't along an axis. Too many tiny details. Accent
yellow used everywhere.
