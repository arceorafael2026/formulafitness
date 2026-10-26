#!/usr/bin/env python3
"""Rebuild the web derivatives of the coaching photos.

Run from the project root:  python3 tools/build-images.py
Masters live in source-images/coaching-masters/ (never deployed).
Derivatives go to public/images/ as WebP, named <master>-<width>.webp.
Rules: EXIF orientation applied, no upscaling, no cropping, no retouching, metadata stripped.
"""
import os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source-images", "coaching-masters")
OUT = os.path.join(ROOT, "public", "images")
USED = ["pt-coach-dumbbell-curl", "pt-coach-guided-deadlift", "pt-coach-guided-movement", "pt-assisted-floor-movement"]
WIDTHS = [640, 960, 1280, 1600, 1920]  # long-edge cap is 1920
QUALITY = 78

for name in USED:
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, name + ".jpg"))).convert("RGB")
    w, h = im.size
    cap_w = min(w, round(w * 1920 / max(w, h)))  # long edge <= 1920 (portrait images are capped by height)
    widths = sorted({t for t in WIDTHS if t <= cap_w} | ({cap_w} if cap_w not in WIDTHS and cap_w < 1920 else set()))
    for target in widths:
        if target > w:  # never upscale
            continue
        nh = round(h * target / w)
        if max(target, nh) > 1920:  # long-edge cap (portrait photos)
            continue
        out = im.resize((target, nh), Image.LANCZOS)
        path = os.path.join(OUT, f"{name}-{target}.webp")
        out.save(path, "WEBP", quality=QUALITY, method=6)
        print(f"{os.path.basename(path)}  {target}x{nh}  {os.path.getsize(path)//1024} KB")
