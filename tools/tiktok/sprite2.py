import math
from PIL import Image, ImageDraw
INK=(30,26,22)
def sprite(phase, final_w=170):
    S=4; w,h=260*S,275*S
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    pink=(244,166,184); dark=(196,96,124); cheek=(236,104,128)
    cx,cy=130*S,100*S; rx,ry=96*S,66*S
    # legs & arms first (behind body)
    for sgn,hx in ((-1,-42),(1,6)):
        sw=math.sin(phase+(0 if sgn<0 else math.pi))
        lx=cx+hx*S; top=cy+55*S
        fx=lx+sw*28*S; fy=cy+128*S-max(0,sw)*14*S
        d.line([(lx,top),(fx,fy)],fill=INK,width=9*S)
        d.ellipse([fx-14*S,fy-7*S,fx+24*S,fy+9*S],fill=INK)
    for sgn in (-1,1):
        sw=math.sin(phase+(math.pi if sgn<0 else 0))
        ax=cx+sgn*92*S; ay=cy+8*S
        ex=ax+sgn*30*S; ey=ay+32*S+sw*20*S
        d.line([(ax,ay),(ex,ey)],fill=INK,width=8*S)
        d.ellipse([ex-8*S,ey-8*S,ex+8*S,ey+8*S],fill=INK)
    # stem + cerebellum
    d.rounded_rectangle([cx+26*S,cy+50*S,cx+44*S,cy+92*S],radius=6*S,fill=dark,outline=INK,width=5*S)
    d.ellipse([cx+34*S,cy+44*S,cx+104*S,cy+88*S],fill=(226,132,156),outline=INK,width=5*S)
    for k in range(3):
        y=cy+(54+k*10)*S
        d.arc([cx+42*S,y,cx+96*S,y+14*S],10,170,fill=dark,width=3*S)
    # bumpy cloud body: outline pass then fill pass
    pts=[]
    for k in range(18):
        a=2*math.pi*k/18
        pts.append((cx+rx*0.92*math.cos(a), cy+ry*0.92*math.sin(a), (26 if k%2==0 else 22)*S))
    for x,y,r in pts: d.ellipse([x-r-5*S,y-r-5*S,x+r+5*S,y+r+5*S],fill=INK)
    d.ellipse([cx-rx*0.92-5*S,cy-ry*0.92-5*S,cx+rx*0.92+5*S,cy+ry*0.92+5*S],fill=INK)
    for x,y,r in pts: d.ellipse([x-r,y-r,x+r,y+r],fill=pink)
    d.ellipse([cx-rx*0.92,cy-ry*0.92,cx+rx*0.92,cy+ry*0.92],fill=pink)
    # brain folds (wavy lines) around the face area
    def wave(x_a,x_b,y,amp,wl,ph0=0):
        P=[]; x=x_a
        while x<=x_b:
            P.append((x,y+amp*math.sin((x-x_a)/wl*2*math.pi+ph0))); x+=2*S
        d.line(P,fill=dark,width=4*S,joint='curve')
    wave(cx-70*S,cx-20*S,cy-48*S,6*S,34*S)
    wave(cx+10*S,cx+66*S,cy-50*S,6*S,34*S,1.5)
    wave(cx-82*S,cx-58*S,cy-20*S,5*S,24*S)
    wave(cx+60*S,cx+82*S,cy-24*S,5*S,24*S,1)
    d.arc([cx-12*S,cy-72*S,cx+12*S,cy-30*S],270,90,fill=dark,width=4*S)
    # face
    for ex in (-30,30):
        X=cx+ex*S; Y=cy-4*S
        d.ellipse([X-15*S,Y-17*S,X+15*S,Y+17*S],fill='white',outline=INK,width=4*S)
        d.ellipse([X-7*S,Y-9*S,X+9*S,Y+9*S],fill=INK)
        d.ellipse([X-1*S,Y-7*S,X+5*S,Y-1*S],fill='white')
    d.ellipse([cx-62*S,cy+12*S,cx-40*S,cy+30*S],fill=cheek)
    d.ellipse([cx+40*S,cy+12*S,cx+62*S,cy+30*S],fill=cheek)
    # big open smile
    d.pieslice([cx-26*S,cy+8*S,cx+26*S,cy+50*S],0,180,fill=(150,40,60),outline=INK,width=4*S)
    d.pieslice([cx-14*S,cy+30*S,cx+14*S,cy+50*S],180,360,fill=(240,120,130))
    return im.resize((final_w,int(final_w*h/w)),Image.LANCZOS)
if __name__=='__main__':
    s=sprite(0.6,final_w=520); bg=Image.new('RGB',s.size,(243,235,218)); bg.paste(s,(0,0),s); bg.save('sprite_test.png')
