---
id: kinetic-type
name: Kinetic type
kind: primitive
family: Type-led
tags: [typography, bold, rhythmic, poster, punchy]
look: Huge heavy words that arrive, slam, slide and leave on a near-black ground, with hot orange and one lime flash.
suits: Announcements, statements, headline numbers, city and business stories, anything where the words are the message.
made_with: code
mixes: []
---

# Kinetic type

## Feel
A title sequence for the news. Loud, quick and confident: every word has weight and arrives like a beat in a drum
pattern, then holds still long enough to be read. There is no picture to hide behind, so the words are the picture, and
the pauses between hits matter as much as the hits. The mood is energetic but controlled, never messy.

## Colours by job
- **Ground:** warm ink `#0D0D0B`. The whole background, flat, about 70% of the frame.
- **Text:** bone white `#F3EFE4`. The main words and all Arabic headlines. About 15% of the frame.
- **Main, in three tones:** hot orange `#FF4B1F` for English headlines and the one "lit" lane on each structure;
  lighter `#FF7A52` only for a brief flash as something lands; deeper `#B8300F` for anything that must sit behind or
  under the main tone (a shadow slab, a struck-out word).
- **Accent, in two tones:** acid lime `#D4FF3B` for the number and the single thing that changed; deeper `#9FBF1F` for
  its small supporting marks. Under 8% of the frame. Never for ordinary headlines.
- **Structure fills:** raised ink `#171611` for large quiet shapes, and dim text `#6E6A5F` (3:1 on raised ink, so it textures without competing) for words that only texture
  a shape. Secondary text `#8C877A`.

To recolour, keep the pattern: a near-black ground, one hot main tone with a light and a deep step, and one accent
that is much brighter than anything else. Dark text goes on orange or lime bars; it is the ground colour.

## Type
- **Latin headlines:** Montserrat 900, uppercase, about 150 px, tight (`letter-spacing: -0.02em`), line-height 0.95.
- **Numbers:** Montserrat 900 at 400–460 px, with the unit in the same weight and size. Tabular figures, so counting
  does not wobble.
- **Words that explain a number:** these are not captions. English in Montserrat 800 at about 76 px; Arabic in IBM Plex
  Sans Arabic 700 at about 140 px, which is roughly 15% larger than the Latin beside it at equal visual weight.
- **Arabic headlines:** IBM Plex Sans Arabic 700 at about 200 px, `line-height` 1.4 or more. Arabic in the same
  box as Latin is always larger and always above.
- **Texture words:** Montserrat 800, uppercase, 30 px, only as pattern inside a shape, never to be read.
- Headline English is uppercase. Arabic has no case and is never faked with weight tricks, outlines or stretching.

## Materials and texture
Flat ink and flat colour. No gradients, no glow, no blur, no shadow, no outline text. Shapes have hard square edges. The
only "material" is the text itself: structures are made of repeated words in rows, so a mass of type reads as a
surface. A thin hard bar (6–10 px) in a main or accent tone underlines, divides or marks a change.

## Layout
Poster logic: one statement at a time, and it takes over the screen. A headline fills about 60–75% of the width, with
a margin of at least 110 px. Arabic sits above English, both centred when they are a title, so the eye reads one block. A
number takes the larger half, its explaining words the other half with a bar between. Large empty ink is deliberate:
never fill it. A band of text-built shapes may anchor the bottom third and bleed off the bottom edge; nothing sits behind
a headline, so headlines never overlap anything.

## Motion
Fast in, hold, fast out. Moves are about 0.6–0.8 s with `expo.out` or `power4.out`, so words arrive hard and settle
softly; exits are about 0.35–0.45 s with `power3.in`, quicker than entrances. Text appears through a mask: it rises from a hidden
line (a clipped box) and leaves the same way, upward, so nothing fades. English headlines move letter by letter with a
stagger of 0.03–0.05 s; numbers count up from zero over about a second, easing out. One idea leaves while the next
is already starting, with a small overlap, so the beat never stalls. Large structures rise from the bottom edge with a
stagger of 0.05–0.07 s and sink back when they are the thing that changes. Hold the final state still for the last half second.

## How it shows things
- **Numbers:** the figure is the hero, set huge and counting up, in the accent colour. Its words sit beside it at a
  readable size. The change itself is shown in the structure: some parts sink and take the accent.
- **Comparison:** two words or numbers at the same size, one in white, one in main; the winner is bigger.
- **Process:** one word per step, each replacing the last in the same spot, with a bar that grows between steps.
- **Change over time:** a repeating word or number whose value changes in place, with the old value leaving upward.
- **A term or quote:** the words fill the frame with the key word alone in main orange; the rest in white or dim.
- **The subject (a city):** never drawn. Suggest it with towers of text, a skyline of columns built from repeated
  words of different heights, one lit lane at the top of each.

## How to make it
Plain HTML and CSS with GSAP, no canvas. Every moving word sits in a mask: a box with `overflow: hidden` and about 0.2 em of
padding top and bottom (Arabic marks need it), inside it a child that tweens `yPercent` from 105 to 0 and out to -105.
English letters are one `span` each with `display: inline-block`. Structures are tall boxes of stacked uppercase
words, clipped by a container that ends at the bottom of the stage; raise one by tweening `y` from its height to 0, sink
it with `y` to a fraction of its height. The first line of each is a solid bar in the main tone with ground-coloured
text. Count numbers with a tween on a plain object whose `onUpdate` writes `Math.round(value)` into the element.

## Arabic and English
Arabic first and above, always larger by about 15% or more. Arabic joins letters, so it is **never** split into letters,
staggered by letter, letter-spaced, scaled per letter or masked in slices. All Arabic motion works on **the whole word or the
whole line**: a line rises through its mask as one piece, a pair of words enters as two pieces with a delay of about 0.08 s
(right word first), and a line may scale up very slightly (up to 4%) or slide. The English line below may use the letter-by-letter
stagger, which gives the pair a typographic rhythm without touching the Arabic. Mixed lines keep each language in its own
element. Numbers and `%` stay in a left-to-right element and use Western digits.

## Landscape and vertical
Landscape: headline centred in the upper two thirds, structures along the bottom, a number to the left and its words to the right.
Vertical: stack everything. Arabic and English headline lines each get the full width at about 80% of the landscape size, with the number on top and its
words below, and the text-built structures as a narrower band at the bottom.

## What would break it
Fading or blurred text. Letter-by-letter motion on Arabic, or letter-spacing it. Several statements competing on screen.
Drop shadows, glow, gradients or outlines. Any picture, icon or illustration instead of type. Orange or lime used as
backgrounds or everywhere. Slow, floaty easing. Small captions beside a huge number. Text sitting over the skyline or any
other text. A cluttered frame with no empty ink.
