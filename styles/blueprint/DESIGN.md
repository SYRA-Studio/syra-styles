---
id: blueprint
name: Blueprint
kind: primitive
family: Line and hand-drawn
tags: [technical, cyanotype, plans, drafting, precise]
look: White drafting lines on deep cyanotype blue, with a fine grid, dimension arrows and one small redline mark.
suits: Plans, infrastructure, engineering, cities, systems and any idea that should feel designed, measured and trustworthy.
made_with: code
mixes: []
---

# Blueprint

## Feel
A drawing someone has checked twice. Calm, exact and a little proud: the idea is not decorated, it is drawn to scale, with the
measurements left visible. It feels like the moment before something gets built, so numbers feel earned and plans feel
possible. The drawing draws itself, line by line, as if an invisible pen is working.

## Colours by job
- **Ground:** cyanotype blue `#0F3D73`, flat and nearly the whole frame. The corners fall away to a deeper `#0A2D58` in a
  soft vignette, like an aged sheet under a lamp.
- **Grid:** two tones of lighter blue, drawn as lines. Minor lines every 48 px `#1A4F8C` at 1 px, major lines every 240 px
  `#2A66A8` at 1.5 px. The grid is felt, never the subject.
- **Line, in three tones:** main drawing line chalk white `#EAF4FF` at 3 px; secondary line (windows, hatching, extension
  lines, dimensions) `#9CC4EE` at 1.5-2 px; faint line (centre lines, construction, the sheet border) `#5E92CC` at 1.5 px.
- **Fill:** a shape is almost never filled. When something must read as solid or lit, use `#EAF4FF` at 20% opacity, never opaque.
- **Redline accent:** coral `#FF6B57`, under 6% of the frame. It is the reviewer's pen: it marks what changed or what the
  video wants you to look at (the part that goes away, a key measurement). One accent mark per idea. Never for text or large areas.
- **Text:** `#F2F8FF`; secondary text `#A9CBEE`.

To recolour, keep the idea: one hue for ground, grid and lines in three or four steps (light lines on a dark ground, or the
reverse), and one contrasting pen colour.

## Type
- **Titles:** Montserrat 700 at 112 px (Latin). Arabic titles IBM Plex Sans Arabic 700 at 132 px.
- **Numbers:** Montserrat 700 at 280 px, tabular, with the unit (%) in the same weight and size.
- **Words that explain a number:** Montserrat 600 at 72 px in `#F2F8FF`; Arabic IBM Plex Sans Arabic 600 at 92 px. They are
  never captions: they are the second most important thing on screen.
- **Annotations:** JetBrains Mono 400 at 22 px, upper case, letter-spacing 0.08em, in `#9CC4EE`. Used only for drawing
  labels (dimensions, scale, sheet info). They decorate and never carry the message, so Arabic is never set in them.
- Text is upright and flat, aligned to one column edge, never centred.

## Materials and texture
Only line. Strokes have round caps and miter joins, constant width, no gradients, no glow, no drop shadow. Surfaces are
suggested by hatching (45° lines, 8 px apart, 1.5 px, secondary tone) on the ground and on anything cut or removed. Windows
and details are thin outlines; "lit" things take the 20% fill. The only paper feel is the vignette. No noise, no texture images.

## Layout
A sheet: a thin faint border inset 48 px with small corner ticks, a grid inside it. The drawing takes the left 55% of the
frame; a faint vertical rule separates it from a text column at the right edge, right-aligned for Arabic-first videos, at
least 90 px from the border. The drawing sits on one ground line and every measurement refers to it. A small title block
(mono) sits in a bottom corner, clear of the text. Show at most one drawing and one text group at a time; empty blue is part
of the design. The eye goes to the drawing as it draws itself, then to the big text beside it.

## Motion
Everything is drawn or revealed, never popped. Lines draw on (stroke-dashoffset from full to zero) in 0.5-0.7 s with
`power2.inOut`, staggered 0.08-0.12 s: ground line first, then outlines, then details, then dimensions. Fine details (windows,
hatching) fade in over 0.25 s in short staggers. Text is written on by a wipe along its reading direction (Arabic from the
right, English from the left) in about 0.5 s, `power3.out`. Numbers count up in 0.9-1.0 s with `power2.out`. Leaving, text
lifts 16 px while fading in 0.25 s; drawn parts do not erase, they dim to 40-50% so the world persists while the next idea
takes the foreground. Between ideas the same drawing stays and gets annotated or marked in redline. The grid drifts slowly,
and the last half second is still.

## How it shows things
- **Numbers:** a huge figure beside the drawing, and a scale bar of ten equal cells under the drawing. Solid cells are what
  remains; hatched redline cells are the amount (for 40%, four of ten). A dimension line with end ticks sits under the figure.
- **Comparison:** two elevations on one ground line at the same scale, each with a vertical dimension.
- **Process:** numbered circles joined by thin dashed lines, each stage drawn on in turn.
- **Change over time:** the same drawing with a revision tag (REV A, REV B) and the changed part in redline.
- **Parts of a whole:** an exploded view with extension lines and small leader callouts.
- **A term or quote:** inside a thin title-block frame, the term large and a mono reference tag.

## How to make it
Inline SVG. Give every drawn path `pathLength="1"`, `stroke-dasharray="1"` and tween `stroke-dashoffset` from 1 to 0; this
draws any shape without measuring it. The grid is two sets of SVG lines under everything, drifting up to 24 px over the
video. Dimension lines: a line, a 45° tick at each end (about 8 px), a mono label sitting on a ground-coloured gap in the middle,
and dotted extension lines to the thing measured. Hatching: a `<pattern>` of 45° lines. Windows are generated in a loop in rows
and columns from the building's measurements, using a fixed formula (not random) to choose which are lit. Vignette: one
radial gradient over the ground.

## Arabic and English
Arabic goes first and above, in its own `dir="rtl"` element, right-aligned and about 15% larger than the English. The English
line follows below, right-aligned, with equal importance. Numbers use Western digits and `40%` sits in a `dir="ltr"` element.
Mono annotations stay Latin. Arabic is never letter-spaced, uppercased, sloped or placed inside the drawing, and its wipe
reveals from the right so letters appear in reading order.

## Landscape and vertical
Landscape: drawing left, text right. Vertical: the sheet border stays, the drawing sits in the lower half (ground line about
60% down) and the text group above it, right-aligned; the grid keeps its 48 px cells.

## What would break it
Solid fills and colour blocks. Gradients on lines, glow or shadows. Perspective or 3D. Wobbly hand-drawn lines (this is ruled
and exact). More than one accent mark per idea, or coral used for text. Lines that pop in instead of being drawn. A grid so
bright it competes with the drawing. Centred text. Mono type used for message text. Pure black or pure white.
