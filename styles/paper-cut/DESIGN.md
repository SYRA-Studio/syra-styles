---
id: paper-cut
name: Paper cut
kind: primitive
family: Paper and craft
tags: [handmade, layered, warm, storytelling, shadow-box]
look: Layers of coloured card cut by hand and stacked in a shadow box, with real depth between them.
suits: Warm stories, education, culture, nature, and anything that should feel human and friendly.
made_with: code
mixes: []
---

# Paper cut

## Feel
A shadow box made at a kitchen table. Warm, patient and handmade, with a sense of real depth: you could reach in and lift
a layer. It makes a topic feel human and gives it the tone of a good picture book without being childish.

## Colours by job
Colour goes from dark at the back to light at the front, which is what creates the depth.
- **Back sheet (the ground):** deep teal `#12394A`.
- **Middle layers, back to front:** `#1E6072`, then `#2F8C8C`.
- **Front layer and text strips:** cream `#F2E3C6`.
- **Accent:** burnt orange `#F0683A`, one shape at a time, under 15% of the frame (a sun, a key object). It may sit at any
  depth; behind the city, it adds distance.
- **Text:** dark `#12394A` on cream, or cream on the dark layers.

To recolour, keep the dark-to-light order from back to front and keep one accent.

## Type
Words are printed on a cut strip of cream card, or cut out of it. Montserrat 800 for titles (about 90 px) and numbers
(about 210 px), Montserrat 600 for secondary English (about 58 px, Arabic about 66 px). IBM Plex Sans Arabic 700 for Arabic titles, 500 for secondary. Set
whole words or lines on their strip and move the strip, like a label placed by hand.

## Materials and texture
Everything is flat card. Three things sell it, and all three are needed:
- **Shadows between layers:** one tight and one soft on every piece, for example `0 2px 2px rgba(0,0,0,.28)` and
  `0 16px 26px rgba(0,0,0,.30)`. Pieces further forward cast longer, softer shadows. Light comes from above. Black shadows barely show on the dark back
  layers, so give those pieces more shadow or keep them well separated.
- **Hand-cut edges:** shapes are built from slightly uneven points and short curves, never perfect circles or
  ruler-straight lines. Even a "circle" sun is a little off.
- **Paper fibre:** a very faint grain over the card, at about 5–8% opacity.

No outlines, no colour gradients. The only shading is the shadow a piece casts.

## Layout
Think in depth: 4–6 layers from back to front. Big simple shapes, cut boldly, with detail in the silhouette rather than on
the surface. Often the nearest layer frames the picture, like the opening of a box; keep that frame thin enough that cream doesn't take over. Keep a calm area for the text strip, at
least 120 px from the edges.

## Motion
Pieces slide into place from outside the frame, or rise from behind another layer, as if pushed in by hand: 0.6–0.8 s,
`back.out(1.4)`. Layers arrive from back to front with about 0.1 s between them. Nearer layers travel further than far
ones, which adds parallax. Exits are quicker, 0.4–0.5 s with `power2.in`. Text strips overshoot less than scene pieces (`back.out(1.1)`), so they don't
cover their neighbours. A full-width layer should rise from below or drop from above rather than cross the whole width: at
this speed it would blur, and splitting it in two leaves a visible seam. Pieces can settle with a small rotation of about 2°. While resting, front pieces keep a very
slow sway of about 0.6°, as if hanging on thread. Between ideas, layers slide out and the next ones rise into place, so
a new scene is found inside the box.

## How it shows things
- **Numbers:** a big figure on its own cream card, placed in front of the scene.
- **Comparison:** two paper stacks of different heights side by side, in the same colours.
- **Process:** a strip sliding through a slit in the top layer, one step showing at a time.
- **Change over time:** a shape rising from behind a cut horizon, like the sun or a chart's edge.
- **A term or quote:** a strip of card that slides in and settles at a slight angle.

## How to make it
Each layer is an SVG `path` or HTML element with its own CSS `filter: drop-shadow(...)`, so the shadow follows the cut
shape; a `box-shadow` only follows a rectangle. Place the points by hand, with 1–3 px of irregularity; a small seeded script may add it, but the source holds the finished paths. Paper fibre: an
SVG `feTurbulence` with a fixed `seed`, in a full-frame layer at low opacity with `mix-blend-mode: multiply`, fixed in
place. Animate only `transform`.

## Arabic and English
Arabic and English sit on the same strip or on two strips of equal size, tall enough for the Arabic, with Arabic on top in
Arabic-first videos. Arabic text moves as a whole strip, never letter by letter. The
hand-cut rule applies to strips, not to the letters.

## Landscape and vertical
Landscape: wide horizons and layers that slide in from the sides. Vertical: tall layers that rise from the bottom, with the
text strip in the upper third.

## What would break it
Flat pieces with no shadow. One shadow for all layers. Perfect vector circles and straight edges. Outlines. Colour
gradients. A light front layer behind a dark one for no reason. Lots of small pieces. Smooth 3D rotation. Pieces fading in
rather than being placed.
