# Short (about 18s) full-screen Reel/TikTok cut: quote, 1 body line, question, CTA.
# usage: python3 short.py <dayDir> <postId> <out.mp4>   (run in a dir containing sprite2.py, music.py)
import math, sys, os, subprocess, glob, json
from PIL import Image
DAY, PID, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W,H=1080,1920; FPS=30; XF=0.3
BG=(243,235,218)
post=[p for p in json.load(open(f'{DAY}/posts.json')) if p['id']==PID][0]
types=[s['type'] for s in post['slides']]
qi=types.index('question') if 'question' in types else 7
pick=[0,1,qi,len(types)-1]
durs=[5.0,4.5,5.0,4.0]
cards=[Image.open(f'{DAY}/{PID}_{i+1:02d}.png').convert('RGB') for i in pick]
from sprite2 import sprite
starts=[sum(durs[:i]) for i in range(4)]; dur=sum(durs); N=int(dur*FPS)
fd='sframes'; os.makedirs(fd,exist_ok=True)
for f in glob.glob(fd+'/*.png'): os.remove(f)
y0=(H-cards[0].height)//2-40
for i in range(N):
    t=i/FPS; idx=max(k for k in range(4) if starts[k]<=t); loc=t-starts[idx]
    c=cards[idx]
    if idx<3 and loc>durs[idx]-XF: c=Image.blend(cards[idx],cards[idx+1],(loc-(durs[idx]-XF))/XF)
    fr=Image.new('RGB',(W,H),BG); fr.paste(c,(0,y0))
    ph=i*0.5; sp=sprite(ph,final_w=150); bob=abs(math.sin(ph))*8
    x=(t/9.0%1)*(W+300)-150          # crosses the bottom strip every 9s
    fr.paste(sp,(int(x-sp.width/2),int(H-y0+ -60-sp.height-bob+ (y0-60))),sp)
    fr.save(f'{fd}/f{i:05d}.png')
subprocess.run(['python3','music.py','smusic.wav',str(dur)],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{fd}/f%05d.png','-i','smusic.wav','-c:v','libx264','-preset','veryfast','-pix_fmt','yuv420p','-crf','21','-c:a','aac','-b:a','160k','-shortest',OUT],check=True)
print('done',dur)
