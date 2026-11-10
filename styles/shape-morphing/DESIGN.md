---
id: shape-morphing
name: Shape morphing
kind: primitive
family: Motion-led
tags: [morph, fluid, bold, transformation, flat]
look: One bold flat shape keeps turning into the next, trailing thin echo outlines while it changes, so the movement is the idea.
suits: Showing transformation, growth, change of state, before-and-after, and any story where one thing becomes another.
made_with: code
mixes: []
---

# Shape morphing

## Feel
Alive and confident, like a magician's one trick done well. A single piece of paint-bright colour never stops becoming
something else, and the viewer follows it the way they follow a ball in a rally. The calm comes from restraint: one hero
shape at a time, a dark quiet ground, and holds where the shape is simply what it is. The movement is elastic but never
wobbly: it starts slowly, rushes through the middle and settles.

## Colours by job
- **Ground:** midnight violet `#17112E`. The whole background, flat, about 70% of the frame.
- **Main shape:** coral `#FF5C47`, with its deep tone `#C8372B` for the offset shadow. The hero shape is coral most of the time
  and takes about 15-20% of the frame.
- **Second tone:** saffron `#FFC247`, deep `#D9941C`. It marks the "other" thing: a stage of the change, or a piece that
  leaves the whole. Used by one shape at a time, under 8% of the frame.
- **Third tone:** aqua `#35D6C4`, deep `#1E9C8F`. Only for the small satellite shapes (each under 60 px across), never the
  hero: aqua and coral blend to a muddy grey while the hero changes, whereas coral and saffron blend to a clean orange. The
  hero therefore alternates between coral and saffron from one form to the next.
- **Echo and guide lines:** lilac `#8F7FE0` for the trailing echoes (stroke only, up to 55% opacity) and the ghost outline of
  a whole `#3D3070`. Lines, never fills.
- **Text:** warm white `#FFF6EA`; secondary text `#B9AEE3`. A big figure may take saffron when it names the saffron piece of
  the shape beside it; the words that explain it stay warm white.
Never fill large areas with aqua or saffron. Never put coral behind text. To recolour, keep the pairing of each tone with
its deep version, and keep one main plus two minor colours.

## Type
Montserrat 800 for titles (about 120 px) and numbers (about 300 px, with the % sign at the same size and weight).
Words that explain a number are big: Montserrat 600 at about 64 px. IBM Plex Sans Arabic 700 for Arabic titles (about
140 px, 15% bigger than the English), 600 for the Arabic that explains a number (about 100 px). Arabic always has line height 1.5 or more.
Text is set flat and upright, aligned to the text side (right for Arabic-first), always in warm white; the secondary
colour only for small labels (about 36 px). Text never morphs; the shapes do.

## Materials and texture
Flat matte colour with no gradients, no grain and no blur. Under the hero shape sits a solid deep-tone copy of itself,
offset about 14 px right and 18 px down, which gives a cut-paper weight without softness. While the shape changes, two
thin lilac outlines of where it was a moment ago (about 0.09 s and 0.18 s behind) follow it, 3 px stroke. They fade out
as the shape comes to rest, so a held shape is clean. Corners are sharp where the shape has them; curves are true curves.

## Layout
One hero shape on one side, about 500-560 px across, centred on the shape side with at least 120 px of margin; text
fills the other side and is centred vertically. Never more than one hero. Two or three small satellite shapes drift in the
corners of the shape side and change form on their own schedule, never competing with the hero. Empty ground is part of
the design. The eye goes to the hero first, then to the number or title.

## Motion
The morph is the main verb. Every change takes 0.5-0.7 s with `power3.inOut` or `expo.inOut`, then the shape holds for at
least 0.3 s so each form can be read. Colour changes in step with the shape. The first appearance is the shape growing from
nothing with `back.out(1.4)`. Text enters by rising out of an invisible line (a mask), 0.5 s with `power3.out`, lines
staggered 0.12 s, and leaves by rising out the top, 0.3 s `power2.in`, overlapping the next idea's entry. An idea changes
into the next by the hero morphing, not by cutting. Satellites keep drifting gently so the frame never freezes. The last
half second is still.

## How it shows things
- **Numbers:** a whole shape that is cut. For "40% less", a full disc turns into a disc with a 40% wedge pulled out in
  saffron, while the figure counts up. The wedge is the amount, the remaining 60% is what stays.
- **Comparison:** the same shape in two forms, one morphing into the other with the echoes showing the distance travelled.
- **Process:** each step is one form of the same shape; the shape is the object travelling through the process.
- **Change over time:** the shape's form is the state; its colour is the period.
- **A term or quote:** the shape settles into a simple form beside it and stays quiet.

## How to make it
No plugin: morph by hand. Describe every form as a closed outline, sample it into the same number of points (for example 160,
equally spaced along the length of the outline, starting at the same place, in the same direction). Then the point at index
`i` of one form moves to the point at index `i` of the next. Draw a `<path>` as `M ... L ... Z` from the interpolated points.
Drive everything from one tweened `time` value and compute the shape purely from it (which pair of forms, how far through
the 0-1 change, with the easing applied to that 0-1), never from the order of earlier updates, because frames render in any
order. Choose each form's starting point so the points travel the short way; a shape with a hole or a piece pulled out is a
separate path. The echoes are the same function called with an earlier `time`. Fade them by how far the points moved
between the two times. Sectors, pies and arcs are polylines of 1-degree steps, resampled like any other form.

## Arabic and English
Arabic above English, right-aligned, equal importance, with the shape on the left in Arabic-first videos. Arabic is always
whole words in its own `dir="rtl"` element, never animated letter by letter, and the mask reveal moves the whole line.
Numbers are Western digits in a `dir="ltr"` element, with the `%` after the digits.

## Landscape and vertical
Landscape: shape on the left, text on the right. Vertical: shape in the upper 55% with text below; keep the hero at about 70%
of the frame width, with satellites in the upper corners.

## What would break it
A shape that cuts to the next without travelling. Two or more heroes at once. Forms with different point counts or starting
places, which twist and tangle. Echoes that stay on a resting shape. Gradients, blur or glow. More than three colours on the
screen at once. Morphing the text. Making the movement bouncy or wobbly: it should be a smooth, confident rush. Holds
so short that no form can be recognised.
