from func import midi2mp3, midi2pianoroll, ratio_train_data, ace_info
import glob

if __name__ == "__main__":
    
    fn = open('../data/train_note.csv', 'w')
    fc = open('../data/train_chord.csv', 'w')
    for mid in glob.glob('../midi/*'):
        print('processing: '+mid)
        fname=midi2mp3(mid)
        notes, sixteen_time = midi2pianoroll(mid)

        chord = ace_info('../mp3/'+fname+'.mp3')

        ratio, c_arr = ratio_train_data(notes, chord, sixteen_time)

        for seg in ratio:
            for n in seg:
                fn.write(str(n)+',')
            fn.write('\n')

        for c in c_arr:
            fc.write(str(c)+',\n')
    fn.close()
    fc.close()
