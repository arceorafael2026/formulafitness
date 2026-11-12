#!/usr/bin/env python3
"""Permanently blur every visible face in the 24 'Real People. Real Results.' comparison images (BEFORE and AFTER panels).
Usage: python3 tools/blur-booking-results.py <folder-with-unblurred-originals>   (files named comparison-NN.png|jpg)
The originals are NOT stored in this project (keep them private, never in public/).
Only the elliptical face/head regions below are changed (strong two-pass Gaussian blur, feathered edge). Everything else,
including bodies, backgrounds and the BEFORE/AFTER labels, is left as supplied. Output: public/images/results/result-NN.webp (1080x1080).
Regions are (centre x, centre y, radius x, radius y) in the 1080x1080 pixel space of the originals. No names are used anywhere."""
import os, sys, glob
from PIL import Image, ImageDraw, ImageFilter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=os.path.join(ROOT,"public","images","results")
FACES={
 "01":[(280,185,85,110),(820,200,95,100)],
 "02":[(250,236,95,108),(815,185,75,85)],
 "03":[(275,285,85,100),(818,258,85,112)],
 "04":[(302,150,62,82),(763,155,58,78)],
 "05":[(288,188,66,80),(784,172,62,78)],
 "06":[(290,215,88,104),(806,212,72,88)],
 "07":[(296,270,70,82),(796,262,88,100)],
 "08":[(308,245,72,95),(780,215,70,88)],
 "09":[(290,125,62,78),(780,125,66,78)],
 "10":[(296,178,78,82),(785,168,72,80)],
 "11":[(303,178,70,82),(794,170,62,78)],
 "12":[(300,180,78,85),(785,205,70,82),(513,345,15,50)],   # third: bystander at the panel edge
 "13":[(285,160,70,95),(765,175,68,82)],
 "14":[(288,312,72,88),(768,322,58,74)],
 "15":[(288,235,78,100),(760,270,92,105)],
 "16":[(345,175,80,95),(810,170,82,100)],
 "17":[(300,262,62,85),(790,255,70,82)],
 "18":[(279,174,66,80),(799,150,78,95)],
 "19":[(280,275,76,92),(790,190,58,66)],
 "20":[(306,262,72,88),(792,250,78,100)],
 "21":[(330,215,62,78),(825,245,60,78)],
 "22":[(290,148,68,82),(818,156,70,85)],
 "23":[(300,180,66,90),(745,165,72,88)],
 "24":[(365,215,65,95),(760,210,72,95)],
}
RADIUS=26; FEATHER=7
def blur_regions(im,boxes):
    out=im.copy()
    for cx,cy,rx,ry in boxes:
        pad=RADIUS*3
        box=(cx-rx-pad,cy-ry-pad,cx+rx+pad,cy+ry+pad)
        crop=im.crop(box)
        b=crop.filter(ImageFilter.GaussianBlur(RADIUS)).filter(ImageFilter.GaussianBlur(RADIUS))
        m=Image.new("L",crop.size,0); ImageDraw.Draw(m).ellipse((pad,pad,pad+2*rx,pad+2*ry),fill=255)
        m=m.filter(ImageFilter.GaussianBlur(FEATHER))
        out.paste(b,box[:2],m)
    return out
if __name__=="__main__":
    src=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
    for n,boxes in FACES.items():
        f=glob.glob(os.path.join(src,f"comparison-{n}.*"))[0]
        im=Image.open(f).convert("RGB")
        assert im.size==(1080,1080),(n,im.size)
        blur_regions(im,boxes).save(os.path.join(OUT,f"result-{n}.webp"),"WEBP",quality=86,method=6)
        print("blurred",n,len(boxes),"faces")
