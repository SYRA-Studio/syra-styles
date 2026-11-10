---
id: pixel-art
name: Pixel art
kind: primitive
family: Screen and digital
tags: [retro, game, pixels, night, nostalgic]
look: Everything built from big square pixels on one hidden grid, with a few flat colours, hard stepped shadows and no smoothing.
suits: Games, apps, tech history, cities and systems, playful or nostalgic explainers, anything about "levels", scores and progress.
made_with: code
mixes: []
---

# Pixel art

## Feel
A game level at night. Cosy, bright and a little nostalgic: small chunky things in a few strong colours, lit like a
handheld screen. It is playful but disciplined, because nothing is allowed to be finer than the grid. Everything is
counted in squares, so even a city feels like something you could hold and replay.

## Colours by job
Few colours, each with a fixed job. Never a gradient: shading is made by stepping between tones, and soft transitions
by a checkerboard of two tones (dither).
- **Ground (sky):** a stack of flat bands from deep to glowing, top to bottom: `#120E2B`, `#1A1440`, `#261B55`, `#36256B`,
  `#5A3A8F`, `#8A4A9A` (only a sliver at the horizon). Bands meet with two rows of checkerboard dither. About 55% of the
  frame at night.
- **Main, two families, three to four tones each.** Blue: body `#2E3A7A`, lit left edge `#4A5CB0`, shaded right edge
  `#222B5E`, roof line `#7F96E6`, unlit window `#1B2150`. Teal: body `#1F5F73`, lit edge `#2F8AA0`, shade `#17475A`, roof
  `#6AD0DC`, unlit window `#123846`. Light always comes from the left. Neighbouring objects alternate families.
- **Far layer:** body `#231B4F`, top edge `#3A2D72`, windows `#4D3B8F`. Always darker than anything in front, never lit.
- **Light (accent 1):** yellow `#FFD34D` with a lower row of `#FF9F3A`. It means life and activity: lit windows, small
  highlights. Under 4% of the frame.
- **Good (accent 2):** green `#5CF29A`, shade `#1E8F5A`. It means saved, gained, correct, and is used for the key
  number and its meter, never for scenery.
- **Spark:** pink `#FF5C8A` for one small moving thing (a car, a pickup) and red `#FF4A4A` for a blinking warning light.
  Together under 1%.
- **Panel and text:** panel fill `#0E0A24`, border and text `#FFF6E0` (cream), inner line and text shadow `#3A2D72`,
  hard shadow `#05030F`, corner studs yellow. Moon is cream with craters `#C4B793` and `#D9CDB0`.
- Never pure white, never pure black, never a colour outside this list at full strength. To recolour, replace each
  family as a set of same-hue tones (light edge, body, shade, roof) and keep the sky darker than the objects.

## Type
There is no pixel font in the toolkit, so text works in two ways:

- **Latin and digits are drawn on the same pixel grid as the picture**, from a hand-made 5-wide, 7-tall bitmap alphabet
  (descenders drop two more rows). They are made of the same squares as everything else, never typed in a font. Draw
  only the letters needed and keep every square aligned with the picture's grid.
- **Arabic is set in a real font and is the one smooth thing in the frame.** Use IBM Plex Sans Arabic 700 with its
  letters left joined and whole; never rebuild Arabic from squares, never pixelate or letter-space it. It sits on a solid
  panel (below) with a hard shadow, which ties it to the pixel world.

Sizes at 1920x1080, where one picture pixel is 8 screen pixels:
- **Title, Latin:** grid scale 2 (16 px squares): letters 112 px tall (descenders 144 px). Cream, with a 1-pixel
  shadow in `#3A2D72` down and right.
- **Title, Arabic:** IBM Plex Sans Arabic 700 at 120 px (the Latin cap height is 112 px; Arabic runs a little larger so
  the two read as equals), line-height 1.4, cream, text-shadow `6px 6px 0 #3A2D72`, no blur.
- **Number:** grid scale 4 (32 px squares): 224 px tall, `%` or any unit in the same size and colour as the digits.
  Green with a 2-pixel shade `#1E8F5A`. Never smaller than half the frame's panel height.
- **Words that explain a number:** same size as the title (Latin scale 2, Arabic 120 px), cream. They are not captions.
- **Small labels** (if needed): grid scale 1 (8 px squares): 56 px cap height, only for things like "LV 2", never for
  meaning.
- Latin is lower case with a capital at the start of names. No all-caps strings longer than six letters. Numbers use
  Western digits. A line of Arabic and a line of Latin stay in separate elements.

## Materials and texture
Flat squares of colour. No outlines, no antialiasing, no blur, no transparency: every pixel is exactly one palette
colour. Edges are made by a one-pixel lighter row on the lit side and a two-pixel darker column on the shaded side.
Roofs get a one-pixel bright line. Shadows are hard offsets (3 pixels down and right) in `#05030F`, never soft. Texture
comes only from dither: a two-row checkerboard where sky bands meet, a ring of single dots around the moon, stars as
single pixels (the brightest as a plus of five pixels). The picture is drawn at 240x135 and scaled by 8 with
nearest-neighbour, so nothing can ever land between pixels.

## Layout
One grid of 240x135 squares. Everything snaps to it: objects, text, panels, motion. Anchor an idea in a panel: a
dialogue box with a cream border, a dark fill, a violet inner line, a yellow stud at two opposite corners, cut corners
(one missing pixel) and a hard shadow. The panel takes the top 40% of the frame, 48 px from the top and at least 64 px
from the sides, and holds the words. The scene (a skyline, a level) takes the lower half. Text inside the panel is
right-aligned for Arabic-first videos, Arabic above Latin. A number sits at the right of the panel with its words at
its left (the order Arabic readers meet them), and the number is the largest thing. Keep three to five things in the
scene doing something at once; the rest is quiet.

## Motion
Everything moves in steps, never smoothly. Use stepped easing (`steps(n)`), with the number of steps showing in the
motion, between 4 and 10 per move. Things never move by fractions of a pixel.
- **Enter:** buildings and objects grow upward from the ground in 8 steps over 0.45 s, staggered by about 0.07 s. A
  panel pops from its centre in 5 steps over 0.3 s. Latin text is typed one letter at a time, about 0.05 s a letter,
  with the last letter appearing column by column. Arabic is revealed by a stepped wipe from its right edge (the way it
  begins), 10 steps over 0.3 s, so no letter is ever drawn in two parts that don't join. A number builds from its bottom
  row up in 7 steps, with a one-frame cream flash when complete.
- **Leave:** the reverse. Latin erases from the right letter by letter, Arabic wipes back to its right edge in 6 steps
  over 0.2 s. Between ideas the world stays and changes: the panel steps wider (6 steps, 0.45 s), the moon steps down
  behind the new panel's edge.
- **Always alive:** stars twinkle by changing tone every third of a second, a roof light blinks every half second, a
  vehicle crosses the road a pixel at a time, clouds drift one pixel per tick, a turbine turns in 15 degree jumps. Keep
  this small and slow so the eye stays on the words.
- Nothing eases in or out. Final rest: last half second only the twinkle and the vehicle move.

## How it shows things
- **Numbers:** the big digits plus a row of ten blocks (a health bar). For "40% less", four of the ten go dark, one by
  one from the right, while about 40% of the lit windows in the scene go dark with them.
- **Comparison:** two bars or two towers side by side on the same ground, stepped growth, the better one in green.
- **Process:** a path of tiles or road with a small character hopping from stop to stop in whole squares.
- **Change over time:** a level or score counter, or a row of blocks filling, one square at a time.
- **Parts of a whole:** the object split into labelled blocks, like inventory slots.
- **A term or quote:** the panel alone, dialogue-box style, typed letter by letter.

## How to make it
Use one `<canvas>` of 240x135 inside the 1920x1080 stage, `width: 1920px; height: 1080px; image-rendering: pixelated`,
and draw only with `fillRect` at integer coordinates. Write the picture as one function of time that redraws
everything (sky, stars, moon, far layer, near layer, street, panel, text), and drive it from one linear tween on the
paused timeline whose `onUpdate` calls it. Easing is a helper: `step(p, n) = floor(p*n)/n` over a clamped progress. Randomness comes from a small
integer hash of positions, never `Math.random`. Buildings are a rectangle plus edge rows and columns, windows are 2x3
squares on a 5x6 pitch with the same grid for every building; windows go lit/dark by comparing time with each window's
own on/off time. To make exactly 40% go dark, rank the lit windows by a hash and darken the first 40%. A bitmap letter
is an array of strings, one per row, with `#` as a filled square, drawn as squares of the chosen scale; to type it,
draw whole letters up to a count; to reveal it, draw only its first columns. Arabic is DOM text over the canvas, clipped
by `clip-path: inset(...)` computed from a number (use a fixed width for the box, don't measure it). Draw the panel
and its shadow in the canvas so it shares the grid.

## Arabic and English
Arabic first, above Latin, both right-aligned inside the same panel, with the same colour. Latin is the pixel text,
Arabic is the real font: say this once and keep it, since the clash is intended and the panel and shadow bridge it.
Arabic never goes inside the scene, on a building or in a sprite, because it cannot be drawn on the grid. If a label
must live in the scene, use Latin digits or a symbol. Arabic is revealed only as a whole word or phrase by wipe, never
letter by letter. Numbers use Western digits in the pixel font, even inside Arabic.

## Landscape and vertical
Landscape: panel on top, scene below as described. Vertical (1080x1920 at 135x240 grid): the panel moves to the top
third, text stacks Arabic above Latin, number goes under the words instead of beside them, and the skyline fills the
bottom 40% with its tallest buildings at the sides. Keep the 8-pixel scale and the 5x7 letters.

## What would break it
Smooth curves, gradients, soft shadows, blur or antialiasing anywhere in the scene. Things placed or moved between grid
squares, or scaled by non-whole numbers. Mixing pixel sizes in one object. A real font for Latin or digits (only Arabic
may use one). Arabic drawn from squares, letter-spaced, split or typed letter by letter. A colour outside the palette,
or more than two accents. Smooth easing or fades on pixel things. A busy scene where the words are not the loudest
thing. Panels without a hard shadow. Pure black or white.
