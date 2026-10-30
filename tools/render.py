import json, re, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
W,H=1080,1350; M=120
FD="/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-"
def F(style,size): return ImageFont.truetype(FD+style+".otf",size)
BG=(243,235,218); INK=(18,16,14); MUTE=(120,108,90)
def paper():
    im=Image.new("RGB",(W,H),BG); px=im.load(); random.seed(7)
    n=Image.effect_noise((W,H),14).convert("L")
    n=Image.eval(n,lambda v:int(v*0.0+ (v-128)*0.12))
    base=Image.new("RGB",(W,H),BG)
    from PIL import ImageChops
    nn=Image.merge("RGB",[n.point(lambda v:v+128)]*3)
    im=Image.blend(base,ImageChops.multiply(base,nn.point(lambda v:min(255,v+127))),0.35)
    # soft vignette
    v=Image.new("L",(W,H),0); d=ImageDraw.Draw(v); d.ellipse((-250,-250,W+250,H+250),fill=255)
    v=v.filter(ImageFilter.GaussianBlur(160))
    dark=Image.new("RGB",(W,H),(214,200,172))
    return Image.composite(im,dark,v)
def tokens(par):
    out=[]; ital=False; bold=False
    for part in re.split(r"(\*\*|\*)",par):
        if part=="**": bold=not bold
        elif part=="*": ital=not ital
        elif part:
            st="bolditalic" if bold and ital else "bold" if bold else "italic" if ital else "regular"
            if part[0].isspace() and out: out[-1]=(out[-1][0].rstrip()+" ",out[-1][1])
            for w in re.findall(r"\S+\s*",part): out.append((w,st))
    return out
def layout(par,size,maxw,d,base="regular"):
    lines=[[]]; x=0
    for w,st in tokens(par):
        if base=="bold" and st=="regular": st="bold"
        f=F(st,size); ww=d.textlength(w.rstrip(),font=f); sp=d.textlength(w,font=f)
        if x+ww>maxw and lines[-1]: lines.append([]); x=0
        lines[-1].append((w,st)); x+=sp
    return lines
def draw_block(d,pars,size,y0,maxw,lh=1.38,gap=0.7,center=False,base="regular",measure=False):
    y=y0
    for p in pars:
        for ln in layout(p,size,maxw,d,base):
            tw=sum(d.textlength(w,font=F(st,size)) for w,st in ln)
            x=M+(maxw-tw)/2 if center else M
            if not measure:
                for w,st in ln:
                    d.text((x,y),w.rstrip() if w is ln[-1][0] else w,font=F(st,size),fill=INK); x+=d.textlength(w,font=F(st,size))
            y+=size*lh
        y+=size*gap
    return y-size*gap
def fit(d,pars,top,bot,maxw,smax,smin,**kw):
    for s in range(smax,smin-1,-2):
        h=draw_block(d,pars,s,top,maxw,measure=True,**kw)-top
        if h<=bot-top: return s,h
    return smin,h
def frame(d,i,n,header):
    d.text((M,92),(header or "").upper() if False else "",font=F("regular",20),fill=MUTE)
    d.line((M,H-130,W-M,H-130),fill=(190,176,150),width=2)
    d.text((M,H-100),"THE THINKER'S CODEX",font=F("bold",22),fill=INK)
    t=f"{i} / {n}"; d.text((W-M-d.textlength(t,font=F("regular",22)),H-100),t,font=F("regular",22),fill=MUTE)
    if i<n:
        a="swipe  →"; d.text((W/2-d.textlength(a,font=F("italic",22))/2,H-100),a,font=F("italic",22),fill=MUTE)
def spaced(d,txt,x,y,font,fill,sp=6,center=False,width=0):
    tw=sum(d.textlength(c,font=font)+sp for c in txt)-sp
    if center: x=x+(width-tw)/2
    for c in txt: d.text((x,y),c,font=font,fill=fill); x+=d.textlength(c,font=font)+sp
def render(post,outdir,base):
    slides=post["slides"]; n=len(slides); paths=[]
    for i,s in enumerate(slides,1):
        im=paper(); d=ImageDraw.Draw(im); maxw=W-2*M; t=s["type"]
        top,bot=190,H-190
        if t=="cover":
            spaced(d,post["header"].upper(),M,150,F("bold",26),INK,sp=7,center=True,width=maxw)
            d.line((W/2-40,205,W/2+40,205),fill=INK,width=3)
            sz,h=fit(d,s["text"],260,bot,maxw,76,44,center=True,base="bold",lh=1.3)
            y=260+(bot-260-h)/2-(40 if s.get("attr") else 0); yy=draw_block(d,s["text"],sz,y,maxw,center=True,base="bold",lh=1.3)
            if s.get("attr"):
                d.line((W/2-40,yy+55,W/2+40,yy+55),fill=INK,width=3)
                spaced(d,"— "+s["attr"],M,yy+90,F("bold",30),INK,sp=6,center=True,width=maxw)
        elif t=="cta":
            sz,h=fit(d,s["text"],top,bot-170,maxw,60,40,center=True)
            y=top+(bot-170-top-h)/2; yy=draw_block(d,s["text"],sz,y,maxw,center=True)
            bx=(M+60,bot-110,W-M-60,bot-20); d.rectangle(bx,outline=INK,width=3)
            spaced(d,s.get("button","LINK IN BIO"),bx[0],bx[1]+30,F("bold",28),INK,sp=6,center=True,width=bx[2]-bx[0])
        else:
            q = t=="question"
            sz,h=fit(d,s["text"],top,bot,maxw,58 if not q else 64,36,center=q)
            y=top+(bot-top-h)/2 if (q or h<(bot-top)*0.6) else top
            draw_block(d,s["text"],sz,y,maxw,center=q)
        frame(d,i,n,post["header"])
        p=f"{outdir}/{base}_{i:02d}.png"; im.save(p); paths.append(p)
    return paths
if __name__=="__main__":
    f=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
    for post in json.load(open(f)):
        print(render(post,out,post["id"])[0])
