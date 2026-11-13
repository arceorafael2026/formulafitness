#!/usr/bin/env python3
"""Rebuild web derivatives of the group-coaching photos (run from project root).
Masters: source-images/semi-masters/ (never deployed). Output: public/images/<master>-<width>.webp
Rules: EXIF applied, no upscaling, no cropping, no retouching, metadata stripped. Masters are 1200x1200."""
import os
from PIL import Image, ImageOps
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(ROOT,"source-images","semi-masters"); OUT=os.path.join(ROOT,"public","images")
USED=["semi-group-slam-ball-sq","semi-group-knee-raise-sq","semi-group-kettlebell-swing-sq","semi-coach-deadlift-pair-sq"]
for n in USED:
    im=ImageOps.exif_transpose(Image.open(os.path.join(SRC,n+".jpg"))).convert("RGB"); w,h=im.size
    for t in (480,720,960,1200):
        if t>w: continue
        o=im.resize((t,round(h*t/w)),Image.LANCZOS); p=os.path.join(OUT,f"{n}-{t}.webp"); o.save(p,"WEBP",quality=80,method=6); print(os.path.basename(p),o.size)
