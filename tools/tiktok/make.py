import math, sys, os
from PIL import Image, ImageDraw, ImageFilter
SRC, OUT = sys.argv[1], sys.argv[2]
W,H=1080,1920; FPS=30; DUR=8; N=FPS*DUR
BG=(243,235,218); INK=(30,26,22)
card=Image.open(SRC).convert('RGB').resize((680,850),Image.LANCZOS)
cx0,cy0=(W-680)//2,(H-850)//2
# frame line around card
def sprite(phase):
    S=4; w,h=220*S,260*S
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    pink=(236,150,170); dark=(150,70,95)
    ox=w//2
    # legs (alternate)
    for sgn in (-1,1):
        sw=math.sin(phase+ (0 if sgn<0 else math.pi))
        lx=ox+sgn*36*S; top=170*S
        fx=lx+sw*26*S; fy=240*S-max(0,sw)*14*S
        d.line([(lx,top),(fx,fy)],fill=INK,width=9*S)
        d.ellipse([fx-14*S,fy-6*S,fx+22*S,fy+10*S],fill=INK)
    # arms
    for sgn in (-1,1):
        sw=math.sin(phase+(math.pi if sgn<0 else 0))
        ax=ox+sgn*82*S; ay=120*S
        d.line([(ax,ay),(ax+sgn*26*S,ay+34*S+sw*18*S)],fill=INK,width=8*S)
    # brain body: two lobes
    d.ellipse([ox-92*S,40*S,ox+4*S,190*S],fill=pink,outline=INK,width=6*S)
    d.ellipse([ox-4*S,40*S,ox+92*S,190*S],fill=pink,outline=INK,width=6*S)
    # folds
    for yy,ln in ((78,40),(112,52),(146,40)):
        d.arc([ox-70*S,yy*S,ox-70*S+ln*S,(yy+22)*S],200,340,fill=dark,width=5*S)
        d.arc([ox+30*S,yy*S,ox+30*S+ln*S,(yy+22)*S],200,340,fill=dark,width=5*S)
    d.line([(ox,46*S),(ox,186*S)],fill=dark,width=5*S)
    # eyes + smile
    for ex in (-30,30):
        d.ellipse([ox+ex*S-13*S,100*S,ox+ex*S+13*S,126*S],fill='white',outline=INK,width=4*S)
        d.ellipse([ox+ex*S-5*S,108*S,ox+ex*S+7*S,120*S],fill=INK)
    d.arc([ox-22*S,126*S,ox+22*S,160*S],20,160,fill=INK,width=5*S)
    return im.resize((int(w//S*0.62),int(h//S*0.62)),Image.LANCZOS)
# perimeter path around card (offset outward)
off=92
x0,y0,x1,y1=cx0-off,cy0-off,cx0+680+off,cy0+850+off
segs=[((x0,y0),(x1,y0),0),((x1,y0),(x1,y1),90),((x1,y1),(x0,y1),180),((x0,y1),(x0,y0),270)]
# rotation: sprite upright means feet down toward card? place feet toward card (inward)
lens=[math.dist(a,b) for a,b,_ in segs]; total=sum(lens)
def pos(t):
    s=(t%1)*total
    for (a,b,ang),L in zip(segs,lens):
        if s<=L:
            f=s/L; return (a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f),ang
        s-=L
os.makedirs(OUT,exist_ok=True)
base=Image.new('RGB',(W,H),BG)
bd=ImageDraw.Draw(base)
bd.rectangle([cx0-12,cy0-12,cx0+680+12,cy0+850+12],outline=INK,width=3)
base.paste(card,(cx0,cy0))
for i in range(N):
    t=i/N; fr=base.copy()
    (px,py),ang=pos(t)
    ph=i*0.55
    sp=sprite(ph)
    bob=abs(math.sin(ph))*8
    # sprite feet point toward card: top edge -> feet down (ang 0), right edge -> feet left (rotate -90 => +90 ccw?)
    rot=sp.rotate(-ang,expand=True,resample=Image.BICUBIC)
    # shift bob inward-opposite
    fr.paste(rot,(int(px-rot.width/2),int(py-rot.height/2-bob)),rot)
    fr.save(f'{OUT}/f{i:04d}.png')
