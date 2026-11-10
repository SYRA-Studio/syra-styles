---
id: glass-panels
name: Glass panels
kind: primitive
family: Depth and 3D
tags: [glass, frosted, translucent, layered, modern]
look: Frosted, see-through panels floating in front of a soft glowing colour field, each one blurring what lies behind it.
suits: Technology, apps, finance, city and energy topics, product launches, and anything meant to feel clean, premium and calm.
made_with: code
mixes: []
---

# Glass panels

## Feel
Looking through a clean window at a city lit up at dusk. Quiet, expensive and weightless: nothing is solid, everything is a
sheet of light-catching glass hovering at its own depth. The colour is not on the panels but behind them, so each panel
borrows a different tint from what sits underneath. It feels like a modern operating system or a high-end product page, and
it makes even a plain subject look refined.

## Colours by job
- **Ground:** deep night blue `#080B1C`. Never pure black. It is only visible at the edges and between the glows.
- **Glow field (the colour behind the glass):** three soft blurred blobs, 500 to 800 px wide, 55 to 75% opacity: violet
  `#6D4CFF`, cyan `#1FD1F0` and rose `#FF5B8D`. Together they take about 45% of the frame, always overlapping, never
  touching the text directly. They are the only large saturated areas in the frame.
- **Glass body:** white at 9% opacity, so about `rgba(255,255,255,0.09)`, on top of a blur of what is behind it. The
  upper-left corner of a panel may be 5% brighter than the lower-right, giving a faint sheen.
- **Glass edge:** a 1.5 px line, white at 30% opacity, brightest along the top and left (up to 55%) and faintest along the
  bottom and right (12%). Light always comes from the upper left.
- **Panel shadow:** a soft, wide shadow `rgba(3,5,20,0.5)`, blur 60 px, dropped 24 px below. It is the only dark thing on a
  panel.
- **Light (accent):** warm amber `#FFC15E`, with a hotter core `#FFE2A8`. It means energy, power, "this is what matters".
  Under 5% of the frame. Used for one glowing thing at a time, never for text or panel bodies.
- **Text:** `#F7F9FF` for titles and numbers; secondary text `#C3CBEA` for words that explain, never dimmer than that.

To recolour, keep the shape of the scheme: three hues in the glow field that sit well next to each other, one warm contrasting
accent, white glass. Text stays near-white.

## Type
Montserrat for English and numbers, IBM Plex Sans Arabic for Arabic. Light weights vanish on glass, so use medium to heavy.
Arabic is about 12% larger than the English at the same level and sits above it.

| Level | English (Montserrat) | Arabic (IBM Plex Sans Arabic) |
|---|---|---|
| Title | 700, 104 px | 700, 184 px |
| Big number | 800, 360 px, `%` the same weight at 60% of the size | n/a, digits stay Western |
| Words that explain a number | 600, 80 px | 700, 140 px |
| Label | 500, 38 px | 500, 44 px |

Titles are centred on their panel. Beside a number, the explaining words are set big and in `#F7F9FF`, as the second
half of the sentence, not as a caption. Letter-spacing 0 for Arabic; -0.01em at most for Montserrat. Add a faint text
shadow `0 2px 24px rgba(8,11,28,0.55)` so text stays crisp when a glow sits behind the panel.

## Materials and texture
Everything is one material: thin frosted glass. A panel is a rounded rectangle (radius 36 to 56 px, always one radius
family) with a blur behind it (backdrop blur about 28 px, plus a slight 140% saturation boost so the colours behind it get
richer, not muddier), the body tint, the lit edge and the soft shadow. Nothing is opaque except the ground. No solid fills,
no hard outlines, no flat shapes. Optionally a very fine noise at 3% opacity across the whole frame to stop the glows
banding. Glass can overlap glass: the overlap gets visibly brighter and blurrier, which is what sells the depth.
Light things (the amber glow) sit under or inside glass and are softened by it.

## Layout
Few, large panels: one to three per idea, 40 to 70% of the frame in total. Panels are staggered in depth: a back layer that
is smaller, dimmer, blurrier, and a front layer that carries the words. Margins at least 140 px. Text always sits inside a
panel, centred or aligned to its reading edge with 64 px or more of padding, so it always has a calm frosted background. The
eye goes to the front panel's biggest text first, then to the glow behind it. Leave real space around the panels so the
glow field shows between them.

## Motion
Smooth and slow-ish, like glass settling. Panels enter by sliding 60 to 120 px up (or sideways) from slightly lower, while
their opacity goes from 0 and their blur eases in from heavier to normal, 0.8 to 1.0 s, `power3.out` or `expo.out`. Never
bounce. Staggers 0.1 to 0.15 s, back layer first, so the front panel arrives last and lands on top. Text arrives 0.15 s after
its panel, rising 24 px with a fade. Leaving, a panel keeps drifting the direction it came, fades and slips away in 0.5 to
0.7 s, `power2.in`, or sinks back to the back layer (smaller, dimmer, lower). The glows drift slowly and constantly
(30 to 60 px over the whole video) so the glass always has something moving behind it, and a panel's tint slowly changes as
it crosses a glow. One panel at a time may tilt a few degrees at most, with perspective only on that tilt.

## How it shows things
- **Numbers:** the figure is big on a front panel. The amount is shown with light through glass: a glass trough or
  tube, with amber light inside it. The part that goes away leaves behind empty, only-frosted glass of the same size, edged with a thin dashed line and a hairline marking the cut, so the
  eye reads full, then 60%, as the gap. The figure counts as the light drains. This is the look's own way: no rows of
  dots, and no pies.
- **Comparison:** two panels of the same size at different depths, or one panel with an amber glow inside against one with
  none.
- **Process:** a row of panels at the same height, each lighting up in turn from left to right (the amber glow moves
  from one to the next through the glass).
- **Change over time:** panels stack or shift behind each other, with the oldest at the back, smallest and blurriest.
- **A term or quote:** one wide panel with the words, very little else.
- **Parts of a whole:** a stack of separate sheets, spread apart and offset slightly, each one carrying a part.

## How to make it
HTML `div`s with `backdrop-filter: blur(28px) saturate(140%)`, `background: linear-gradient(135deg, rgba(255,255,255,.14),
rgba(255,255,255,.05))`, `border: 1.5px solid` with `border-color: rgba(255,255,255,.5) rgba(255,255,255,.14)
rgba(255,255,255,.1) rgba(255,255,255,.4)`, a large `border-radius` and a wide soft `box-shadow`. The glow field is
absolutely positioned circles with `filter: blur(90px)` (or a radial-gradient) behind everything. The sheen is an extra
inner `::before` with a diagonal white-to-transparent gradient. Animate `y`, `scale`, `opacity` and a `blur`
variable through GSAP; the backdrop blur itself is best left constant and only the panel's opacity animated. An amber
glow is a pill with a gradient fill (`#FFE2A8` to `#FFC15E`) and a `box-shadow: 0 0 60px rgba(255,193,94,.7)`. For a
drain, tween the pill's width from a value and redraw from that value. Glass must sit above the glow in z-order, or it has
nothing to blur. Check that backdrop blur works in the render and check a frame early, since a panel with nothing behind it
turns into a flat grey box.

## Arabic and English
Two separate lines on the same panel, Arabic first (above), both centred or both aligned to the same edge, with 12 to 20 px
between them. Arabic gets the bigger size and the heavier weight, and its own `dir="rtl"` element. Do not put Arabic on the
sheen or the edge; the panel's flat middle is its home. The same panel layout is kept for both, only mirrored if everything
else is. Numbers stay Western, in a `dir="ltr"` element so `40%` never reads as `%40`.

## Landscape and vertical
Landscape: a wide front panel with a back layer offset behind it, the glows spread across the width. Vertical: panels stack
from top to bottom with the front panel in the middle third, narrower (80% of the width), and the glow blobs moved to the
top and bottom. Text sizes can stay the same, as there is more height to share.

## What would break it
Opaque or flat-coloured panels. Glass with nothing coloured behind it, so it turns into a grey card. Heavy dark
shadows or hard black outlines. Panels that are fully transparent with no blur, so the text fights the background. Text
placed straight onto the glow field without a panel. Thin or light weights. Too many glows, or all three colours at full
strength fighting each other. Amber used as a general accent colour instead of for light. Bouncy or snappy motion. Mixing in
solid flat shapes, grain-heavy textures or 3D blocks. Neon outlines (that is a different style: glowing lines).
