from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.utils import np_utils
from func import load_data, chord2index
import numpy as np

(x_train, y_train) = load_data('../data/train_note.csv', '../data/train_chord.csv')

# data pre-processing
y_train=np_utils.to_categorical(y_train, num_classes=24)

x_test=x_train
y_test=y_train


#
max_features = 1024

model = Sequential()
model.add(Embedding(max_features, output_dim=13))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(24, activation='sigmoid'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)
