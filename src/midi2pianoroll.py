import pretty_midi
import mido
import numpy as np
import glob

def get_bpm(tempo):
    bpm=mido.tempo2bpm(tempo)
    return bpm

def get_tempo(mid):
    for m in mid:
        if m.is_meta and m.type=='set_tempo':
            return m.tempo
def midi2pianoroll(flist):
	fw = open('../note.txt')
	for midif in (flist.read()).split():
		mid_mido=mido.MidiFile(midif)
		mid_pret=pretty_midi.PrettyMIDI(midif)
		resolution=mid_mido.ticks_per_beat
		tempo=get_tempo(mid_mido)
		if tempo==None:
		    tempo=500000
		bpm=get_bpm(tempo)
		sixteenth_t=(1/(bpm/60))/4
		length=int(mid_mido.length/sixteenth_t)
		arr = np.zeros((length, 13))
		
		for instrument in mid_pret.instruments:
		    print(instrument)
		    if instrument.is_drum==False:
		        pr=instrument.get_piano_roll(1/sixteenth_t)
		        for i,ppr in enumerate(pr):
		            for j,nt in enumerate(ppr):
		                if nt>0:
		                    arr[j][i%12+1]=1
		for row in arr:
			for element in row:
				fw.write(str(element)+',')
			fw.write('\n')
	fw.close()

