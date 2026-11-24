#!/usr/bin/env python3
"""Permanently blur every face in the three results composites (both BEFORE and AFTER panels).
Usage: python3 tools/blur-faces.py <folder-with-unblurred-originals>
The originals are NOT stored in this project (keep them private, never in public/).
Only the elliptical face regions below are changed (strong Gaussian blur, feathered edge); everything else,
including bodies, backgrounds and the BEFORE/AFTER labels, stays pixel-identical. Output: public/images/client-result-0N.webp.
Face regions are in the 1080x1080 pixel space of the originals: (centre x, centre y, radius x, radius y)."""
import os, sys, glob
from PIL import Image, ImageDraw, ImageFilter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=os.path.join(ROOT,"public","images")
FACES={
 "client-result-01":[(300,175,64,82),(785,163,66,84)],    # supplied 22389831
 "client-result-02":[(310,226,70,108),(790,216,62,88)],   # supplied 7764d0a5
 "client-result-03":[(268,150,62,76),(762,160,62,76)],    # supplied 76d5fb68
}
RADIUS=26; FEATHER=7
def blur_regions(im,boxes):
    out=im.copy()
    for cx,cy,rx,ry in boxes:
        pad=RADIUS*3
        box=(cx-rx-pad,cy-ry-pad,cx+rx+pad,cy+ry+pad)
        crop=im.crop(box)
        b=crop.filter(ImageFilter.GaussianBlur(RADIUS)).filter(ImageFilter.GaussianBlur(RADIUS))  # strong, two passes
        m=Image.new("L",crop.size,0); d=ImageDraw.Draw(m)
        d.ellipse((pad,pad,pad+2*rx,pad+2*ry),fill=255)
        m=m.filter(ImageFilter.GaussianBlur(FEATHER))
        out.paste(b,box[:2],m)
    return out
if __name__=="__main__":
    src=sys.argv[1]
    for name,boxes in FACES.items():
        f=glob.glob(os.path.join(src,name+"*.png"))[0]
        im=Image.open(f).convert("RGB")
        blur_regions(im,boxes).save(os.path.join(OUT,name+".webp"),"WEBP",quality=88,method=6)
        print("blurred",name,len(boxes),"faces")
