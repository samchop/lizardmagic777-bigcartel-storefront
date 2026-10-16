"""Make the Elixir pouch image and its traced double outline.

Usage: python3 tools/elixir-rings.py pouch.png assets/photos/elixir.webp assets/photos/elixir-rings.png preview.png
Needs Pillow, numpy and scipy. The rings PNG is a mask; theme.css fills it with --acc.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src, out_img, out_rings, preview = sys.argv[1:5]
im = Image.open(src).convert('RGBA')
im = im.crop(im.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox())
POUCH_W = 752                     # pouch width at 2x (376px on screen)
PAD = 54                          # canvas margin at 2x, room for the outer ring
R_IN, R_OUT = 16, 38              # ring distance from the pouch at 2x (8px / 19px on screen)
h = round(im.height * POUCH_W / im.width)
im = im.resize((POUCH_W, h), Image.LANCZOS)
W, H = POUCH_W + 2 * PAD, h + 2 * PAD
canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0)); canvas.paste(im, (PAD, PAD), im)
# smooth silhouette so the outline follows the shape, not every crimp
a = np.asarray(canvas.getchannel('A'), dtype=float) / 255
a = ndimage.gaussian_filter(a, 9)
mask = a > .5
yy, xx = np.mgrid[-22:23, -22:23]
mask = ndimage.binary_closing(np.pad(mask, 30), structure=(xx**2 + yy**2) <= 22**2)[30:-30, 30:-30]  # fill notches/dents
yy, xx = np.mgrid[-14:15, -14:15]
mask = ndimage.binary_opening(mask, structure=(xx**2 + yy**2) <= 14**2)  # drop specks/bumps on the edge
d = ndimage.gaussian_filter(ndimage.distance_transform_edt(~mask), 7)  # soften small steps in the outline
ring = lambda r, op: np.clip(1.5 - np.abs(d - r), 0, 1) * op
alpha = np.maximum(ring(R_IN, .4), ring(R_OUT, 1.0))
rings = Image.fromarray((alpha * 255).astype('uint8'), 'L')
rgba = Image.new('RGBA', (W, H), (255, 255, 255, 0)); rgba.putalpha(rings)
rgba.save(out_rings, optimize=True)
canvas.save(out_img, 'WEBP', quality=88, method=6)
# preview: blue rings + pouch on the store background
bg = Image.new('RGBA', (W, H), (0x26, 0x18, 0x1d, 255))
blue = Image.new('RGBA', (W, H), (0x42, 0x71, 0xff, 255)); blue.putalpha(rings)
bg.alpha_composite(blue); bg.alpha_composite(canvas); bg.convert('RGB').save(preview)
print('canvas', W, H, '-> on screen', W // 2, H // 2)
