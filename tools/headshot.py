"""Remove the background from a member headshot and crop to head+shoulders.

Usage: python headshot.py <input_image> <output-slug>
Outputs: vanguard/screens/assets/headshots/<output-slug>.png  (transparent PNG, 400x400)

Pipeline (keeps every roster card framed identically):
1. detect the face (YuNet, tools/yunet.onnx) and frame a square crop so the
   face is 38% of the frame height with its center at (50%, 37%)
2. re-run background removal on the crop at working resolution — full-frame
   photos give the model too little hair detail and leave halos around curls
3. solidify + defringe the matte, resize to 400, anchor bottom-flush
"""
import os
import sys
import cv2
import numpy as np
from rembg import new_session, remove
from PIL import Image, ImageFilter, ImageOps

FACE_H = 0.38   # face height as a fraction of the frame
FACE_CY = 0.37  # face center y as a fraction of the frame

infile = sys.argv[1]
slug = sys.argv[2]
tooldir = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.abspath(os.path.join(tooldir, "..", "screens", "assets", "headshots"))
os.makedirs(outdir, exist_ok=True)

# u2net_human_seg segments portraits much more cleanly than the default u2net
session = new_session("u2net_human_seg")
det = cv2.FaceDetectorYN_create(os.path.join(tooldir, "yunet.onnx"), "", (320, 320))

img = ImageOps.exif_transpose(Image.open(infile)).convert("RGB")
W, H = img.size

# face detection on a bounded copy; retry smaller if the face fills the frame
face = None
for target in (1600, 1000, 640):
    scale = min(target / max(W, H), 1.0)
    small = img.resize((int(W * scale), int(H * scale)), Image.LANCZOS) if scale < 1 else img
    bgr = cv2.cvtColor(np.asarray(small), cv2.COLOR_RGB2BGR)
    det.setInputSize((bgr.shape[1], bgr.shape[0]))
    _, faces = det.detect(bgr)
    if faces is not None and len(faces):
        face = [v / scale for v in max(faces, key=lambda b: b[2] * b[3])[:4]]
        break
if face is None:
    sys.exit("no face detected in " + infile)
x, y, w, h = face

# square crop framed off the face; shift up if it would run past the bottom
side = min(h / FACE_H, H)
left = (x + w / 2) - side / 2
top = (y + h / 2) - FACE_CY * side
if top + side > H:
    top = H - side
crop = img.crop((int(left), int(top), int(left + side), int(top + side)))
crop = crop.resize((800, 800), Image.LANCZOS)

cut = remove(crop, session=session).convert("RGBA")

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

out = cut.resize((400, 400), Image.LANCZOS)

# bottom-flush: cards anchor the photo to the card bottom
a = np.asarray(out)[:, :, 3]
rows = np.where(a.max(axis=1) > 8)[0]
if len(rows) and rows.max() < 399 - 1:
    shifted = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    shifted.paste(out, (0, 399 - rows.max()))
    out = shifted

dest = os.path.join(outdir, slug + ".png")
out.save(dest)
print("saved", dest, "| face", (int(x), int(y), int(w), int(h)), "| crop side", int(side))
