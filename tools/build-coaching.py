#!/usr/bin/env python3
"""Build the Build Strength section image from the supplied AI-enhanced derivative of the real photo
(source-images/semi-masters/semi-build-strength-enhanced.png, 1254x1254) -> public/images/semi-build-strength-{480,720,960,1200}.webp.
Not an untouched original. The knee-raise enhanced image is held back (see docs/held-for-review/)."""
import os
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=os.path.join(ROOT,"public","images")
im=Image.open(os.path.join(ROOT,"source-images","semi-masters","semi-build-strength-enhanced.png")).convert("RGB")
for t in (480,720,960,1200):
    o=im.resize((t,t),Image.LANCZOS); p=os.path.join(OUT,f"semi-build-strength-{t}.webp"); o.save(p,"WEBP",quality=82,method=6); print(os.path.basename(p),os.path.getsize(p)//1024,"KB")
