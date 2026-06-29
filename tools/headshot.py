"""Remove the background from a member headshot and crop to head+shoulders.

Usage: python headshot.py <input_image> <output-slug>
Outputs: vanguard/screens/assets/headshots/<output-slug>.png  (transparent PNG, 400x400)
"""
import os
import sys
from rembg import remove
from PIL import Image

infile = sys.argv[1]
slug = sys.argv[2]
outdir = os.path.join(os.path.dirname(__file__), "..", "screens", "assets", "headshots")
outdir = os.path.abspath(outdir)
os.makedirs(outdir, exist_ok=True)

img = Image.open(infile).convert("RGBA")
cut = remove(img)  # AI background removal -> transparent background

# Bounding box of the person (non-transparent pixels)
bbox = cut.split()[-1].getbbox()
x0, y0, x1, y1 = bbox
pw = x1 - x0
cx = (x0 + x1) // 2

# Square crop framing head + shoulders, with a little headroom above
side = int(pw * 1.0)
top = int(y0 - side * 0.08)
left = int(cx - side / 2)
crop = cut.crop((left, top, left + side, top + side))  # out-of-bounds pads transparent

out = os.path.join(outdir, slug + ".png")
crop.resize((400, 400), Image.LANCZOS).save(out)
print("saved", out, "| person bbox", bbox, "| crop side", side)
