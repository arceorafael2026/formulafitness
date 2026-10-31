#!/usr/bin/env python3
"""Build favicon files from the existing logo mark (public/images/logo.png, 70x81, white on transparent).
Only the diamond mark is used (the FORMULA FITNESS wordmark is illegible at small sizes). White mark on a black tile.
Outputs (public/): favicon.ico (16/32/48), favicon-16x16.png, favicon-32x32.png, apple-touch-icon.png (180, opaque), icon-192.png, icon-512.png.
Run from the project root: python3 tools/build-favicons.py"""
import os
from PIL import Image, ImageDraw, ImageFilter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PUB=os.path.join(ROOT,"public")
logo=Image.open(os.path.join(PUB,"images","logo.png")).convert("RGBA")
a=logo.getchannel("A")
# keep only the mark (above the wordmark): first run of rows with ink, stop at the first empty row after it
rows=[any(a.getpixel((x,y))>40 for x in range(a.width)) for y in range(a.height)]
y0=rows.index(True); y1=y0
while y1<len(rows) and rows[y1]: y1+=1
mark=a.crop((0,y0,a.width,y1)); mark=mark.crop(mark.point(lambda v:255 if v>40 else 0).getbbox())
S=16  # smooth the 70px source: upscale, soften, re-threshold for crisp edges
big=mark.resize((mark.width*S,mark.height*S),Image.LANCZOS).filter(ImageFilter.GaussianBlur(S*0.55)).point(lambda v:255 if v>118 else 0)
def tile(size,radius,fill=0.74):
    sc=4; N=size*sc
    img=Image.new("RGBA",(N,N),(0,0,0,0)); d=ImageDraw.Draw(img)
    if radius: d.rounded_rectangle((0,0,N-1,N-1),radius=int(N*radius),fill=(0,0,0,255))
    else: d.rectangle((0,0,N,N),fill=(0,0,0,255))
    h=int(N*fill); w=round(big.width*h/big.height); m=big.resize((w,h),Image.LANCZOS)
    white=Image.new("RGBA",(w,h),(255,255,255,255)); img.paste(white,((N-w)//2,(N-h)//2),m)
    return img.resize((size,size),Image.LANCZOS)
out={}
for n,r,f in ((16,0.18,0.80),(32,0.18,0.78),(48,0.18,0.76),(192,0.18,0.70),(512,0.18,0.70)):
    out[n]=tile(n,r,f)
out[16].save(os.path.join(PUB,"favicon-16x16.png")); out[32].save(os.path.join(PUB,"favicon-32x32.png"))
out[192].save(os.path.join(PUB,"icon-192.png")); out[512].save(os.path.join(PUB,"icon-512.png"))
tile(180,0,0.64).convert("RGB").save(os.path.join(PUB,"apple-touch-icon.png"))  # iOS applies its own rounding; must be opaque
out[48].save(os.path.join(PUB,"favicon.ico"),sizes=[(16,16),(32,32),(48,48)],append_images=[out[16],out[32]])
print("done")
