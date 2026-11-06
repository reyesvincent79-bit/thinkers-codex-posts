import numpy as np, wave, sys
sr=44100; dur=float(sys.argv[2]); out=sys.argv[1]
n=int(sr*dur); t=np.arange(n)/sr
mix=np.zeros(n)
bpm=68; beat=60/bpm
def note(f,start,length,amp):
    i0=int(start*sr); L=int(length*sr)
    if i0>=n: return
    L=min(L,n-i0); tt=np.arange(L)/sr
    env=np.exp(-tt*2.2)*(1-np.exp(-tt*80))
    s=(np.sin(2*np.pi*f*tt)+0.35*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*4)+0.12*np.sin(2*np.pi*3*f*tt)*np.exp(-tt*6))
    mix[i0:i0+L]+=amp*env*s
def hz(m): return 440*2**((m-69)/12)
# Cmaj9 - Am9 - Dm9 - G13 ; 4 beats each (soft, jazzy)
chords=[[48,55,59,62,64],[45,55,60,64,67],[50,57,60,64,65],[43,53,57,59,64]]
bar=beat*4; k=0; tpos=0
while tpos<dur:
    ch=chords[k%4]
    # pad (bass + sustained)
    note(hz(ch[0]-12),tpos,bar*1.1,0.16)
    for m in ch[1:]:
        note(hz(m),tpos,bar*1.0,0.07)
    # gentle arpeggio on eighth notes
    for j in range(8):
        m=ch[1:][ (j*2)%4 ]+12 if j%2==0 else ch[1:][(j)%4]+12
        note(hz(m),tpos+j*beat/2,beat*1.6,0.10)
    tpos+=bar; k+=1
# soft echo/reverb
d1=int(0.28*sr); d2=int(0.53*sr)
wet=mix.copy(); wet[d1:]+=0.35*mix[:-d1]; wet[d2:]+=0.2*mix[:-d2]
wet=np.convolve(wet,np.ones(9)/9,'same')
wet/=np.max(np.abs(wet))*1.25
fade=int(1.5*sr); wet[:fade]*=np.linspace(0,1,fade); wet[-fade:]*=np.linspace(1,0,fade)
st=np.stack([wet,wet],1)
with wave.open(out,'wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((st*32767).astype('<i2').tobytes())
