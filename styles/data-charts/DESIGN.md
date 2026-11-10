---
id: data-charts
name: Data charts
kind: primitive
family: Data and diagrams
tags: [charts, data, journalism, editorial, evidence]
look: A printed-page chart on warm paper, where bars, lines and gaps are the picture and one red mark makes the point.
suits: Statistics, results, trends, before and after, any claim that should be proved by showing the numbers.
made_with: code
mixes: []
---

# Data charts

## Feel
Data journalism: a good newspaper graphic that has learned to move. Sober, exact and a little confident. Nothing is
decoration, every mark is a measurement, and the viewer should feel they are being shown evidence, not sold something. It
is calm and quick: marks arrive already knowing where they belong, then one of them is singled out.

## Colours by job
- **Ground:** warm paper `#F5F0E6`. The whole background, flat, about 70% of the frame.
- **Ink:** deep navy-black `#16202E`. Headlines, the line itself, the top rule, axis baselines. Never for large fills.
- **Data, in two tones:** main blue `#2F5D8A` for the marks that matter in the context (the tallest or leading bars, the dots
  on a line), and soft blue `#A9BDD3` for the rest of the marks. A chart uses both at once, so it reads in tiers.
- **Signal:** vermilion `#E4472B`, under 10% of the frame, plus its wash `#E4472B` at 16% opacity for an area. It marks
  the one thing the video is saying: the gap, the change, the number. Never for ordinary data, never on more than one idea at
  a time.
- **Rules and grid:** `#D8D0BE` for gridlines (2 px) and `#C2B9A4` for tick marks.
- **Secondary text:** `#6B6A63` for axis labels and chart captions.
- **Text:** ink `#16202E`; the key number takes signal vermilion.

To recolour, keep the roles: one dark ink, two tones of one data hue, one loud signal colour on a quiet ground.

## Type
- **Titles:** Montserrat 800 at 80 px for English and IBM Plex Sans Arabic 700 at 120 px for Arabic (about 50% larger in
  size, since Arabic reads smaller at the same px). Tight leading for English (1.05), 1.4 for Arabic.
- **The number:** Montserrat 800 at 250 px, signal colour, with the `%` in the same weight and size. Digits are tabular so
  a counting number does not jitter.
- **Words that explain a number:** Arabic IBM Plex Sans Arabic 600 at 88 px, English Montserrat 600 at 60 px. These are
  the meaning of the figure, so they are large and in ink, never small captions.
- **Chart labels:** JetBrains Mono 500 at 28 px in secondary text, uppercase for captions, for ticks and the chart's own
  caption. They are quiet furniture; no message lives in them.

## Materials and texture
Printed paper, no screen effects. Flat solid fills, square corners (a 3 px radius at most), no gradients, no shadows, no
glow, no outlines on bars. Gridlines are hairlines. The ink rule across the top is 6 px thick, like a newspaper's
masthead rule. A faint wash under a line (the signal colour at 16%) is the only transparent fill.

## Layout
A chart is the picture and takes about 55% of the frame's width, on one side, anchored on a shared baseline with gridlines
behind it. Words take the other side, right-aligned, with at least 120 px of margin. The top rule runs between the
margins. One chart on screen at a time, with 12 marks or fewer. The eye goes to the signal colour first, then the
number, then the rest.

## Motion
Marks come from the baseline: bars grow up from zero with a 0.05 s stagger, 0.6 s each, `expo.out`; lines are drawn
along their path with `power2.inOut`. Text slides up 40 px and fades in over 0.7 s with `expo.out`, and leaves by
fading and lifting 30 px in 0.3 s. Between ideas the same marks become the next chart: bars narrow into the dots of a line
and their tops slide to the new values, so the chart is one object that answers a new question. Nothing bounces, spins or
overshoots. End on a rest: nothing moves in the last half second.

## How it shows things
- **Numbers (a percentage change):** show it as a gap. Draw the starting level as a dashed reference line, draw the
  line falling away from it, and measure the distance between them with a vertical bracket in the signal colour. The
  bracket grows as the line is drawn and the figure beside it counts up with the bracket's length, so the number is the
  measured gap, not a count of things.
- **Comparison:** two bars on one baseline, the one that matters in main blue, the other in soft blue, with the
  difference marked.
- **Process:** a single line chart or step chart whose stages are labelled points.
- **Change over time:** a line drawn left to right, the latest point emphasised with a ring.
- **Parts of a whole:** one horizontal stacked bar split into labelled segments, or a ring, with the highlighted part in
  signal colour.
- **A place or subject:** appears through data, such as a skyline built from bars of its districts.

## How to make it
Plain SVG over a paper background. Compute every mark from numbers: a bar is a `rect` whose `y` and `height` come from
`value * scale`, and a line is a `path` or `polyline` built from the same points. To change between charts, tween one
progress value and redraw all marks from it in `onUpdate` (lerp each bar's top between its two values while its width
shrinks to a dot). Draw a line by revealing the points up to a tweened index and interpolating the last
segment. Gridlines are `line` elements at fixed value steps with mono tick labels. For counting numbers, tween a number and
write `Math.round(v)` into a `dir="ltr"` element with `font-variant-numeric: tabular-nums`.

## Arabic and English
Arabic goes first and above, English below, both right-aligned in the same column, with Arabic about 50% larger in pixels
for titles and 45% for explanatory lines, since Arabic looks smaller at the same size. Chart labels are English or digits
only, because they are furniture. Numbers use Western digits, set left-to-right in their own element even in an Arabic
sentence.

## Landscape and vertical
Landscape: chart on the left, words on the right. Vertical: words on top, chart below filling the width, and no more than
8 marks so each stays readable.

## What would break it
Decoration in place of measurement: icons, 3D bars, shadows, gradients or glow. Signal colour used for ordinary bars.
More than one chart or more than one point on screen. Showing a percentage as a row of things dimming instead of a
measured gap. Bouncy or overshooting motion. Small captions for the words that explain the number. A neon, dark, dashboard-like
look instead of printed paper.
