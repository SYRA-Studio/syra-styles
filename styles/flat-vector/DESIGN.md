---
id: flat-vector
name: Flat vector
kind: primitive
family: Flat and graphic
tags: [flat, shapes, friendly, bright, illustration]
look: Bright, simple shapes in a few solid colours on a warm cream ground, with no outlines, gradients or shadows.
suits: Friendly explainers about cities, energy, money, health, apps and everyday ideas for a wide audience.
made_with: code
mixes: []
---

# Flat vector

## Feel
A good children's-book poster, grown up. Sunny, open and optimistic: everything is a simple shape with soft corners, and the
whole picture reads in one second. It feels warm and welcoming rather than technical, and it makes a serious subject
feel easy to like. It is light, never dark.

## Colours by job
- **Ground:** warm cream `#F6EFE2`. The whole background and about 45% of the frame. It is the only light ground; never
  pure white, never grey.
- **Ink:** deep green-black `#14323A`. All text, and the odd small detail (a door, a trunk). Never a large surface.
- **Main, in four tones (teal):** pale `#CFE9E4` (hills far away, rings' empty track, clouds sit on it), light `#6CC5BC`,
  middle `#1F8A8A`, deep `#0F5C63`. About 35% of the frame. Things further away use the paler tone; things in front
  use the deeper one. Neighbouring shapes always differ by one tone step so they separate without any outline.
- **Accent, in two tones (coral):** bright `#FF6B4A` for shapes, deep `#D9472B` for coloured text and thin parts, which
  need the extra contrast on cream. Under 12% of the frame. It means "the point": the one building, the one number, the
  share that changed. Never for backgrounds or for more than one idea at a time.
- **Spark:** sun yellow `#FFC93C`, under 4%. Light and energy only: the sun, lit windows, a bolt. Never text on cream.
- **White:** `#FFFFFF`, only for clouds, tiny highlights and shapes that must lift off cream.

To recolour, keep the jobs: swap the teal for another hue in the same four steps (pale to deep) and the coral for a
contrasting hue; the ground stays a warm light tint of whatever you choose.

## Type
Urbanist for English, IBM Plex Sans Arabic for Arabic. Sizes at 1920×1080:

| Level | English | Arabic |
|---|---|---|
| Title | Urbanist 800, 128 px | Plex Arabic 700, 148 px |
| Number | Urbanist 800, 300 px, `-0.02em`, line-height 0.95 | same figure, Western digits |
| Words that explain a number | Urbanist 700, 84 px | Plex Arabic 700, 96 px |
| Secondary line | Urbanist 600, 56 px | Plex Arabic 500, 64 px |
| Label | Urbanist 600, 36 px | Plex Arabic 500, 42 px |

Arabic runs about 15% larger than English at its level and has line-height 1.4 or more. Titles and explaining words are
ink; the number is deep coral. The `%` or unit is the same weight and size as the digits. Words that explain a number
are never small captions: they are the second biggest thing on screen. Text is always upright, on the cream ground or
inside a solid shape, never over busy art.

## Materials and texture
Pure flat colour. Shapes have rounded corners (about 6–12% of their short side), perfect circles and straight edges.
No outlines, no gradients, no blur, no shadows, no grain, no highlights drawn as glows. Depth comes only from overlap,
size, and stepping through the teal tones. Detail is one extra shape in another tone (a window, a roof, a door), not
texture. Windows are rounded rectangles, unlit in a deeper tone of their wall, lit in spark yellow. Keep the count of
shapes low enough that each one is still readable.

## Layout
Think in layers across the frame: sky (cream), far hills (pale), buildings or objects (middle tones), ground band (deep
teal) along the bottom. A scene is either one wide picture under a centred title, or a picture on one side with the words
on the other. Margins are at least 120 px. The eye goes first to the biggest text or number, then to the single coral
shape. Leave real cream empty around the text. Round numbers and shapes sit on a shared baseline (the ground line) so
the picture feels settled.

## Motion
Friendly and springy, never slow. Shapes arrive by popping: scale from 0 at their own base point (buildings grow up from the
ground line, circles from their centre) with `back.out(1.5)` over 0.45–0.6 s and a stagger of 0.05–0.09 s. Text rises
about 40 px with a small scale from 0.9 to 1, `back.out(1.4)`, 0.55 s, Arabic first and English 0.15 s later. Exits are
faster than entrances: 0.3 s, `power2.in`, shapes shrink to their base, text lifts away and fades. Between ideas, keep the
same world and move it: the ground slides down, some elements change colour, a ring draws itself. Counting numbers run
`power2.out` and finish with a small pop. Something gentle always drifts (clouds, a slow sun ring); the last half second of
a short video is still apart from that.

## How it shows things
- **Numbers:** a huge figure with a solid donut or bar that shows the same share; the changed part is coral, the rest deep teal.
- **Comparison:** two plain shapes of the same kind side by side on one baseline, one taller, the larger one in coral.
- **Process:** round stations joined by a thick rounded line, a circle travelling along it, each station popping on arrival.
- **Change over time:** a row of shapes that shift tone or height one after another.
- **Term or quote:** the words large on cream, with one simple symbol in a solid circle beside them.

## How to make it
Inline SVG with `<rect rx>`, `<circle>`, `<path>` and `<polygon>`, filled with solid colours; no `stroke` except for rings
(`stroke-width` 60–80, `stroke-linecap: butt`, drawn with `stroke-dasharray`, rotated -90°). Group a scene into layers
(`<g id>`) so each layer can move on its own. Scale shapes with GSAP `svgOrigin` set to their base point so they grow
from the ground. Generate repeated shapes (windows) from fixed numbers in a short loop, never random. Text lives in HTML
elements over the SVG. For a count, tween a plain number and write `Math.round(n)` into the text in `onUpdate`.

## Arabic and English
Arabic first, above English, each in its own element, both centred under a wide picture or both right-aligned beside a
picture. Arabic is `dir="rtl"`, never split or letter-spaced, never put on a coloured shape in a size under its level.
The number is `dir="ltr"` Western digits. When a picture sits beside text in an Arabic-first video, the picture goes on
the left and the words on the right.

## Landscape and vertical
Landscape: wide layered picture along the bottom with words above, or picture and words side by side. Vertical: the
picture takes the lower half as a stack of layers, the words sit in the upper half, and the number can grow to 360 px.
Sizes of text stay the same or grow; shapes crop at the edges rather than shrink.

## What would break it
Outlines around shapes. Gradients, drop shadows, glows, textures or any 3D look. Pure white or dark grounds. More than the
listed colours, or a coral that appears everywhere. Sharp corners on friendly objects. Thin, tiny details that need
squinting. Slow, linear or floaty motion. Text smaller than its level, or set over busy art. Arabic split, cramped or
smaller than the English beside it.
