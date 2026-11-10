---
id: neon-glow
name: Neon glow
kind: primitive
family: Screen and digital
tags: [neon, night, signage, glow, nightlife]
look: Everything is a glass tube of light on a nearly black wall, with a bright white-hot core and a soft coloured halo.
suits: Night cities, nightlife, tech launches, music, gaming, bold announcements and anything that should feel switched on.
made_with: code-with-care
mixes: []
---

# Neon glow

## Feel
A sign switched on after dark. The room is almost black, so the only things you see are things that are lit: electric,
a little dangerous, and sure of itself. It is not soft or dreamy. A neon tube is a single thin line of light, bent by hand,
so everything here is a line, a ring or a letter made of tube, never a filled shape. Light has to be earned: things
start dark, flicker, catch and then hold. Switching off is as dramatic as switching on.

## Colours by job
- **Ground:** `#07050F`, a blue-black with a trace of violet. About 85% of the frame, and never pure black, so the glow
  has something to bloom into. An ambient wash is allowed on top of it: cyan `#0FB4E0` at 7% opacity rising from the bottom
  edge, and magenta `#D0138A` at 5% in one upper corner. Nothing stronger.
- **Unlit glass:** `#2B2447` for a tube that is off, with a 1 px lighter edge `#3A3260` along its top. Every tube exists
  as unlit glass before it is lit and after it goes out, so the shape of the sign is always readable. It never glows.
- **Main, cyan, in three tones:** core `#E6FDFF` (the white-hot centre line), body `#3DF0FF` (the visible tube),
  halo `#0FB4E0` (the glow, always blurred and translucent). Cyan carries structure: outlines, rings, headlines. It is most
  of the lit area.
- **Accent, magenta, in three tones:** core `#FFE4F5`, body `#FF3FB4`, halo `#D0138A`. Under 10% of the lit area. It means
  "this one matters": the number, the moving spark, a few lit windows. Never for outlines of big shapes and never for
  paragraphs of text.
- **Text:** `#F2FBFF` for the lead words, `#A9C4F0` for the second language and anything quieter.

To recolour, change the whole trio together: the core stays almost white with a faint tint of the hue, the body is the
saturated colour, the halo is a darker step of the same hue. Keep exactly two hues lit at once. Never add a third.

## Type
Urbanist for Latin, IBM Plex Sans Arabic for Arabic, JetBrains Mono only for tiny status labels. Weights stay at 500 or
above, because a thin stroke loses its core in the blur.

| Level | Latin | Arabic (about 15% larger) |
|---|---|---|
| Title | Urbanist 600, 128 px | Plex Sans Arabic 600, 148 px |
| Number (hero) | Urbanist 800, 200 px, the unit the same size and weight | Western digits, same |
| Words that explain a number | Urbanist 600, 108 px | Plex Sans Arabic 600, 124 px |
| Second line, supporting | Urbanist 500, 64 px | Plex Sans Arabic 500, 74 px |
| Small label | JetBrains Mono 500, 28 px, uppercase, 0.12em spacing | not used; write the Arabic at the supporting size |

Line height 1.1 for Latin and at least 1.4 for Arabic. English may be set in capitals only for small labels; titles keep
their case. The words that explain a number are lead text, not captions: they sit beside the number at over half its
visual weight. Text is lit with a stacked `text-shadow`: tight 0 0 4px core colour at 90%, 0 0 18px halo at 70%, 0 0 46px
halo at 45%. Small sizes get only the first two layers so letters stay open.

## Materials and texture
Light only. A lit tube is three stacked strokes of the same path: a wide halo stroke (about 36 px, blurred 14–22 px, 50%
opacity), a body stroke (about 12 px, blurred 2 px), and a core stroke (about 4 px, sharp). Ends are round. The unlit tube
under it is a single 7 px stroke of the glass colour. Nothing has a fill, a solid shadow, an outline or a gradient inside
it. There is no grain and no scanline; the dark ground is clean so the bloom is the only texture. Where a lit tube is near
unlit glass, only the lit one lights its surroundings, and the halo never covers text.

## Layout
Generous darkness. At most one lit sign and one small set of supporting marks per idea. Keep 140 px of margin to every
edge. The eye goes first to the brightest, most saturated thing, so put the key number or title there and keep everything
else at least a step dimmer. Space between lit things should be bigger than the halo of either one, so halos never merge
into a smear. A skyline or other scenery sits low and wide, and text takes the open dark above it or beside it.

## Motion
Everything switches on and off like gas in glass. **Ignite:** from dark, flicker through 4 or 5 sudden steps in 0.2 to 0.3
seconds (for example 0, 90%, 10%, 100%, 30%, 100%), landing on full. The steps are abrupt, no easing between them. **Draw:**
a tube that is a path lights along its length, 0.4 to 0.8 s, `power2.inOut`, with a small bright dot (a "spark") leading the
tip. **Leave:** a short double flicker, then the core and body go out at once and the halo is already gone, so the glass
is left dark. Numbers count up under a clock that is shared with the thing they measure. Between ideas, switch the old
sign off and leave its glass in place, dim, as scenery for the next one. Staggers between neighbouring tubes are 0.05 to
0.12 s, deliberately uneven. Nothing slides, bounces or scales; light does not move, it switches. Something may hum: halo
opacity swaying by 10 to 15% over about half a second. The last half second stays still.

## How it shows things
- **Numbers:** a ring of tube with the figure lit in the accent in its middle. For a drop such as "40% less", the whole ring
  starts lit and 40% of its length goes out, sweeping clockwise from the top, a spark running at the front of the dark.
  The number counts up in step with the tube going out. The remaining 60% stays lit, and the unlit arc stays visible as
  glass, so the missing part is shown as missing.
- **Comparison:** two parallel tubes of the same length, one lit fully, the other lit to its share.
- **Process:** a tube path with a spark travelling along it and lighting each station as it passes.
- **Change over time:** a tube line plotted point by point, lit as it is drawn, with the old part dimming to body-only.
- **A term or quote:** the words themselves are the sign, centred, one language per tube colour step, with a thin frame tube.

## How to make it
Inline SVG for tubes, DOM text with `text-shadow` for words.
- Build each tube once in a script from a list of path strings and make the layers from it: a glass copy, then a halo copy, a
  body copy and a core copy. Put all halos in one group with `filter: blur()` so the filter runs once, and the body copies in
  a second group with a 2 px blur. Core copies are unfiltered.
- Give each path `pathLength="1"` and animate `stroke-dashoffset` from 1 to 0 on all layers together to draw it. Use
  `stroke-linecap: round`.
- For a ring that goes dark in part, keep a single dash on the circle and redraw `stroke-dasharray` and `stroke-dashoffset`
  from a tweened value in `onUpdate`; place the spark by computing the angle from the same value.
- A flicker is a run of `set` calls at fixed times, not a tween. Random-looking timing comes from a small fixed table or a
  hash of the element's index, never `Math.random()`.
- Windows and small details are short horizontal round-capped dashes, each with its own tiny halo copy.
- Keep the blur radii the same across the frame so the glow reads as one lighting system.

## Arabic and English
Arabic goes above English, centred or right-aligned, as two tubes of equal importance. Arabic is lit in the main cyan and
English beneath it in the same cyan at a lower brightness, so neither fights the accent. Join the letters: never split
Arabic into pieces to animate it, and never letter-space it. Ignite a whole line at once. The Arabic font carries a glow
well from weight 500 up; do not use 300 or 400. Numbers are Western digits in the accent, left to right, beside the
Arabic, which is right-aligned.

## Landscape and vertical
Landscape: scenery low and wide, title above; or a ring on one side and words on the other, words right-aligned for Arabic.
Vertical: the ring or number above, words below, scenery behind at the bottom, and shrink the halo radii by a quarter so
they do not eat the narrower frame.

## What would break it
A light or mid-tone background. Filled shapes, solid colour blocks or gradients inside the tubes. A glow that is a flat
drop shadow, with no hot core. Halos so big that text turns to mush, or so small that it looks like a thin outline. More
than two lit hues, or a rainbow. Pastel or desaturated colours. Things that slide, scale, bounce or fade in smoothly
instead of flickering on. Everything lit all the time, with no unlit glass left to show the shape. Bloom over body text. Grain,
scanlines or glitch (those are other styles). Magenta used for big areas.
