"""Normalize existing headshot cutouts so they align on the roster cards.

For every screens/assets/headshots/*.png (400x400 transparent PNG):
  - trim stray low-alpha halo/speck pixels left over from background removal
  - scale the figure so it spans exactly from the shared headroom line (32px)
    to the bottom of the frame -> every head-top aligns AND every figure sits
    flush on the card's bottom edge (the roster CSS bottom-anchors the photo)
  - center the person horizontally on the frame

Run: python align_headshots.py
"""
import glob
import os
from PIL import Image

HEADSHOTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "screens", "assets", "headshots"))
SIZE = 400
HEADROOM = 32
SPECK_ALPHA = 8    # alpha below this is residue from background removal
BBOX_ALPHA = 24    # figure measured on solidly visible pixels only


def solid_bbox(im):
    return im.split()[-1].point(lambda v: 255 if v > BBOX_ALPHA else 0).getbbox()


for path in sorted(glob.glob(os.path.join(HEADSHOTS, "*.png"))):
    img = Image.open(path).convert("RGBA")

    # trim faint halo/speck residue
    r, g, b, a = img.split()
    a = a.point(lambda v: 0 if v < SPECK_ALPHA else v)
    img = Image.merge("RGBA", (r, g, b, a))

    bbox = solid_bbox(img)
    if not bbox:
        print("skip (empty):", path)
        continue
    x0, y0, x1, y1 = bbox

    # scale so the figure fills headroom line -> frame bottom exactly
    scale = (SIZE - HEADROOM) / (y1 - y0)
    if abs(scale - 1.0) > 0.002:
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    x0, y0, x1, y1 = solid_bbox(img)

    dx = round(SIZE / 2 - (x0 + x1) / 2)   # center horizontally
    dy = SIZE - y1                          # figure bottom flush with frame bottom

    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    canvas.paste(img, (dx, dy))            # no mask: exact pixel copy, alpha included
    canvas.save(path)

    nb = solid_bbox(canvas)
    print(f"{os.path.basename(path):26s} scale={scale:.3f}  bbox={nb}  center={(nb[0]+nb[2])/2}  top={nb[1]}  bottom={nb[3]}")
