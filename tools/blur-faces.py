#!/usr/bin/env python3
"""Permanently blur every face in the three Semi-Private results composites (both BEFORE and AFTER panels).
Usage: python3 tools/blur-faces.py <folder-with-unblurred-originals>
The originals are NOT stored in this project (keep them private, never in public/).
Only the elliptical face regions below are changed (strong Gaussian blur, feathered edge); everything else,
including bodies, backgrounds and the BEFORE/AFTER labels, stays pixel-identical. Output: public/images/client-result-0N.webp.
Face regions are in the 1080x1080 pixel space of the originals: (centre x, centre y, radius x, radius y)."""
import os, sys, glob
from PIL import Image, ImageDraw, ImageFilter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=os.path.join(ROOT,"public","images")
FACES={
 "client-result-04":[(293,238,64,92),(788,215,60,78)],   # supplied ac287212-image.jpg
 "client-result-05":[(295,246,60,72),(790,262,64,68)],   # supplied 8d46a509-image.jpg
 "client-result-06":[(290,298,64,80),(766,315,54,66)],   # supplied bfa4772a-image.png
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
        f=glob.glob(os.path.join(src,"semi-result-"+name[-2:]+"-master-*.png"))[0]
        im=Image.open(f).convert("RGB")
        blur_regions(im,boxes).save(os.path.join(OUT,name+".webp"),"WEBP",quality=88,method=6)
        print("blurred",name,len(boxes),"faces")
