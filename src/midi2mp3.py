from midi2audio import FluidSynth
import glob
import os
from pydub import AudioSegment

mp3list=open('../mp3list.txt', 'w')
midlist=open('../midlist.txt', 'w')
for mid in glob.glob('../midi/*.mid'):
    fs=FluidSynth()
    fname=os.path.basename(mid)
    fs.midi_to_audio(mid, '../mp3/'+fname+'.wav')
    AudioSegment.from_wav('../mp3/'+fname+'.wav').export('../mp3/'+fname+'.mp3', format="mp3")
    os.remove('../mp3/'+fname+'.wav')
    mp3list.write('../mp3/'+fname+'.mp3')
    mp3list.write('\n')
    midlist.write(mid)
    midlist.write('\n')

