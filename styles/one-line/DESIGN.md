---
id: one-line
name: One-line drawing
kind: primitive
family: Line and hand-drawn
tags: [line, minimal, elegant, hand-drawn, continuous]
look: One unbroken pen line draws everything on an open page, with a single flat shape of colour.
suits: Ideas, stories, philosophy, brand films, and anything that should feel thoughtful and elegant.
made_with: code
mixes: []
---

# One-line drawing

## Feel
A confident hand that never lifts the pen. Quiet, elegant and clever, with a small moment of delight when you see the same
line become one thing after another. A lot of empty space makes it feel sure of itself.

## Colours by job
- **Ground:** warm paper `#F6F1E7`, flat, at least 70% of the frame even when a drawing is finished.
- **Line and text:** soft black `#1A1A1A`.
- **Accent:** vermilion `#E4572E`, used for one flat shape per idea, sitting behind the line, shifted about 16 px from
  it, like a misprinted colour. A number stays in the line colour, so it still reads on the shape.

To recolour, change the accent freely and keep ground and line far apart in lightness. A dark version simply swaps ground
and line.

## Type
Light and quiet, so the line stays the star. Urbanist 300 for English titles (about 84 px) and numbers (about 220 px, still
light), Urbanist 400 for
the words that explain a number (about 44 px). IBM Plex Sans Arabic 300 for Arabic titles (about 96 px), 400 for the rest (about 54 px).
Never bold.

## Materials and texture
Ink on paper. Line width 4–5 px at 1080p, constant, with round ends and round joins. No fills on the drawing and no
shadows. No texture on the paper beyond its colour.

## Layout
Asymmetric and open. One drawing per idea, with text beside or under it and margins of at least 140 px. The line comes in
from off-frame and leaves off-frame, so the drawing feels like one moment of a longer gesture. It can pass near the words,
underline them or loop around a number, which ties text and picture together.

## Motion
The line is the camera: it's always the thing moving. It draws at a nearly even pace, with only a soft start and finish, and never
fully stops until the final rest. Its tail can erase behind it, leaving only what's needed, so an old idea undraws as the
new one forms. Both ends finish off-frame, so the last picture has no loose end; the line may leave the frame and come back
between ideas, because that isn't a pen lift. Text appears once the pen has crossed its position across the frame, with a soft reveal in the direction the line is
travelling (0.4 s), and the accent shape pops in about 0.1 s after the line closes around it, then shrinks away as the line undraws. The next idea is drawn by the same line;
there are no cuts.

## How it shows things
- **Numbers:** a large, light figure with the line circling or underlining it.
- **Comparison:** the same line draws two versions of a thing at different sizes.
- **Process:** the line travels across the frame, making a small loop at each step.
- **Change over time:** the line itself becomes the chart, rising or falling as it goes.
- **A term or quote:** the line underlines it, then carries on.

## How to make it
Exactly one stroked SVG `path` for the whole video: a single long `d` from smooth cubic curves, with its points placed by hand (a small script may round corners and add
wobble, but the source holds the finished path), with loops
where the pen turns back on itself. Give it `pathLength="1"` and `stroke-dasharray`, then tween `stroke-dashoffset` to
draw. To erase behind the pen, tween the dash pattern so a moving window of line is visible. Accent shapes are separate
flat fills placed behind the line. Keep the drawing simple enough to recognise in the fewest strokes, with a slight natural
wobble instead of ruler-straight lines. Digits and words are real text, not drawn with the line.

## Arabic and English
In Arabic-first videos the line travels from right to left, so it leads the eye the way Arabic reads, and text reveals from
the right. Arabic is revealed as a whole with a mask, never letter by letter. Arabic and English stay on separate lines of
matching visual weight: Arabic light looks thinner, so step it up one weight if needed.

## Landscape and vertical
Landscape: the line sweeps across the width, and the empty space sits to one side. Vertical: the line falls from the top to
the bottom, with text in the open space it leaves.

## What would break it
A second line, or visible breaks and pen lifts. Line weight changing. Filled, shaded or very detailed drawings. Bold type.
Several colours. A full frame. Things appearing that the line hasn't reached. Text animated with bounce.
