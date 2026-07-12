"""Remove the background from a member headshot and crop to head+shoulders.

Usage: python headshot.py <input_image> <output-slug>
Outputs: vanguard/screens/assets/headshots/<output-slug>.png  (transparent PNG, 400x400)
"""
import os
import sys
import numpy as np
from rembg import new_session, remove
from PIL import Image, ImageFilter

infile = sys.argv[1]
slug = sys.argv[2]
outdir = os.path.join(os.path.dirname(__file__), "..", "screens", "assets", "headshots")
outdir = os.path.abspath(outdir)
os.makedirs(outdir, exist_ok=True)

img = Image.open(infile).convert("RGBA")
# u2net_human_seg segments portraits much more cleanly than the default u2net
cut = remove(img, session=new_session("u2net_human_seg"))

# Solidify the matte: rembg leaves the subject at ~alpha 230-250, which lets the
# card background bleed through. Smoothstep-remap alpha so the subject is fully
# opaque, haze drops to 0, and anti-aliased edges keep a short ramp.
LO, HI = 70, 200
arr = np.asarray(cut).copy()
t = np.clip((arr[:, :, 3].astype(np.float64) - LO) / (HI - LO), 0, 1)
t = t * t * (3 - 2 * t)
arr[:, :, 3] = np.round(t * 255).astype(np.uint8)
cut = Image.fromarray(arr, "RGBA")

# Defringe: the seg mask sits a few px outside the true silhouette, so erode
# ~4px (then soften) to drop the ring of background it would otherwise keep.
# Never grow the matte.
r_, g_, b_, a_ = cut.split()
a2 = a_.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(1.0))
a2 = Image.fromarray(np.minimum(np.asarray(a_), np.asarray(a2)))
cut = Image.merge("RGBA", (r_, g_, b_, a2))

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
