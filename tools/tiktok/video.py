import math, sys, os, subprocess, glob
from PIL import Image, ImageDraw
sys.argv_backup=sys.argv
DAY, PID, OUTMP4 = sys.argv[1], sys.argv[2], sys.argv[3]
W,H=1080,1920; FPS=30; PER=3.0; XF=0.35
slides=sorted(glob.glob(f'{DAY}/{PID}_[0-9][0-9].png'))
CW,CH=680,850; cx0,cy0=(W-CW)//2,(H-CH)//2
cards=[Image.open(p).convert('RGB').resize((CW,CH),Image.LANCZOS) for p in slides]
BG=(243,235,218); INK=(30,26,22)
exec(open('make.py').read().split('# perimeter path')[0].split("card=Image.open")[0].split("SRC, OUT")[0])  # imports only
src=open('make.py').read()
# reuse sprite()
ns={}
exec("import math\nfrom PIL import Image, ImageDraw\nINK=(30,26,22)\n"+src[src.index('def sprite'):src.index('# perimeter path')],ns)
from sprite2 import sprite
off=92; x0,y0,x1,y1=cx0-off,cy0-off,cx0+CW+off,cy0+CH+off
segs=[((x0,y0),(x1,y0),0),((x1,y0),(x1,y1),90),((x1,y1),(x0,y1),180),((x0,y1),(x0,y0),270)]
lens=[math.dist(a,b) for a,b,_ in segs]; total=sum(lens)
def pos(t):
    s=(t%1)*total
    for (a,b,ang),L in zip(segs,lens):
        if s<=L: f=s/L; return (a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f),ang
        s-=L
dur=PER*len(cards); N=int(dur*FPS)
fd='vframes'; os.makedirs(fd,exist_ok=True)
for f in glob.glob(fd+'/*.png'): os.remove(f)
frame_border=Image.new('RGB',(W,H),BG); ImageDraw.Draw(frame_border).rectangle([cx0-12,cy0-12,cx0+CW+12,cy0+CH+12],outline=INK,width=3)
for i in range(N):
    tsec=i/FPS; idx=min(int(tsec//PER),len(cards)-1); local=tsec-idx*PER
    card=cards[idx]
    if idx<len(cards)-1 and local>PER-XF:
        a=(local-(PER-XF))/XF; card=Image.blend(cards[idx],cards[idx+1],a)
    fr=frame_border.copy(); fr.paste(card,(cx0,cy0))
    (px,py),ang=pos(tsec/ (PER*4))   # one lap every 12s... slow walk
    ph=i*0.5; sp=sprite(ph); bob=abs(math.sin(ph))*8
    rot=sp.rotate(-ang,expand=True,resample=Image.BICUBIC)
    fr.paste(rot,(int(px-rot.width/2),int(py-rot.height/2-bob)),rot)
    fr.save(f'{fd}/f{i:05d}.png')
subprocess.run(['python3','music.py','music.wav',str(dur)],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{fd}/f%05d.png','-i','music.wav','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','21','-c:a','aac','-b:a','160k','-shortest',OUTMP4],check=True)
print('done',N,'frames',dur,'s')
