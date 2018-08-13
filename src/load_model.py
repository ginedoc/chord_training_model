from keras.models import load_model
from func import load_data, midi2pianoroll, roll2ration
import numpy as np

#x,y = load_data('../data/train_note.csv', '../data/train_chord.csv')
#x = x[0:1]
#x=np.array([[0,0.3,0,0,0,0.3,0,0,0.4,0,0,0,0]])
notes, seg_t = midi2pianoroll('melody.mid')
note_ratio = []
for i in range(0, len(notes), 8):
    note_ratio.append(roll2ration(notes[i:i+8]))
note_ratio=np.array(note_ratio)
print(note_ratio)

model = load_model('model_single.h5')
predict = model.predict(note_ratio)

for p in predict:
    print(p)
