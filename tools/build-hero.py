#!/usr/bin/env python3
"""Build hero derivatives from the supplied AI images (masters in source-images/hero-ai/, not deployed).
Landscape 1672x941 -> public/images/semi-hero-landscape-{640,960,1280,1672}.webp (tablet and desktop)
Portrait 1024x1536 -> public/images/semi-hero-portrait-{480,720,960,1024}.webp (phones)
No cropping (the page frames them with CSS), no upscaling. Run from the project root."""
import os
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SRC=os.path.join(ROOT,"source-images","hero-ai"); OUT=os.path.join(ROOT,"public","images")
for name,widths in (("landscape",(640,960,1280,1672)),("portrait",(480,720,960,1024))):
    im=Image.open(os.path.join(SRC,f"semi-hero-{name}-master.png")).convert("RGB"); w,h=im.size
    for t in widths:
        if t>w: continue
        o=im if t==w else im.resize((t,round(h*t/w)),Image.LANCZOS)
        p=os.path.join(OUT,f"semi-hero-{name}-{t}.webp"); o.save(p,"WEBP",quality=80,method=6); print(os.path.basename(p),o.size,os.path.getsize(p)//1024,"KB")
