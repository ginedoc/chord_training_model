import numpy as np
import os
import pretty_midi
import mido
import pyace
from pydub import AudioSegment
import locale
from locale import atof
from midi2audio import FluidSynth

def midi2mp3(path):
    fname=os.path.basename(path)
    fname=os.path.splitext(fname)[0]
    fs = FluidSynth()
    fs.midi_to_audio(path, '../mp3/'+fname+'.wav')
    AudioSegment.from_wav('../mp3/'+fname+'.wav').export('../mp3/'+fname+'.mp3', format="mp3")
    os.remove('../mp3/'+fname+'.wav')
    return fname

def midi2pianoroll(mid):
    midd=mido.MidiFile(mid)
    midp=pretty_midi.PrettyMIDI(mid)
    # basic information
    tempo=get_tempo(midd)
    bpm=mido.tempo2bpm(tempo)
    sixteen_t=(1/(bpm/60))/4
    midi_length=int(midd.length/sixteen_t)

    # 
    notes=np.zeros((midi_length, 13))
    for instrument in midp.instruments:
        print(instrument)
        if instrument.is_drum==False:
            pr = instrument.get_piano_roll(1/sixteen_t)
            for i, ppr in enumerate(pr):
                for j, nt in enumerate(ppr):
                    if nt>0:
                        notes[j][i%12+1] += 1
                    else:       # note off
                        notes[j][0] += 1
    return notes, sixteen_t

def ace_info(src):
    des='./result.txt'
    pyace.simpleace(src, des)
    f=open(des, 'r')
    info=(f.read()).split()
    info=np.array(info).reshape((int(len(info)/3),3))
    os.remove(des)
    return info

def ratio_train_data(notes, chords, seg_t):
    note_ratio=[]
    chord_data=[]
    for chord in chords:
        tptr = atof(chord[0])
        while tptr+8*seg_t < atof(chord[1]):
            t=int(tptr/seg_t)
            note_ratio.append(roll2ration(notes[t:t+8]))
            chord_data.append(chord[2])
            tptr += seg_t
    return (note_ratio, chord_data)
def roll2ration(notes):
    scale = np.zeros(13)
    for seg in notes:
        for i, note in enumerate(seg):
            scale[i] += note
    total=scale.sum()
    scale=scale/total
    return scale

def get_tempo(mid):
    for m in mid:
        if m.is_meta and m.type=='set_tempo':
            tempo = m.tempo
            break
    if tempo is None:
        tempo=500000
    return tempo
