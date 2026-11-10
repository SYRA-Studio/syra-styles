# SYRA styles

The style library of SYRA Studio: looks for motion-graphics videos, each one a reference the agent designs from, never a
template. SYRA Studio downloads them from here.

```
index.json          the styles and their files (made by tools/build_index.py)
styles/<id>/
  DESIGN.md         the look in words, with its info card on top
  preview.mp4       the small sample the Styles page plays
  thumbnail.jpg     one picture
  sample.mp4        the full sample, downloaded when a style is opened
  source/           the sample as HTML, to learn how an effect is made
  CREDITS.txt       picture licences, where a style uses pictures by others
```

## Adding or changing a style

1. Put the style's folder in `styles/` (see the app's `library/DESIGN-TEMPLATE.md` for DESIGN.md). Make its preview with
   `python -X utf8 tools/previews.py styles`.
2. Run `python -X utf8 tools/build_index.py`.
3. Commit and push. Installed apps pick it up at their next check (a few minutes after they start, then every few hours).

Styles listed in `held.txt` stay out of this repo until their picture licences are checked.
