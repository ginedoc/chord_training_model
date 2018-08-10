from keras.models import load_model
from func import load_data
import numpy as np

#x,y = load_data('../data/train_note.csv', '../data/train_chord.csv')
#x = x[0:1]
x=np.array([[0,0.3,0,0,0,0.3,0,0,0.4,0,0,0,0]])
print(x)
model = load_model('model_single.h5')
print(model.predict(x))
