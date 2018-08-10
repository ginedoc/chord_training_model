import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
from keras.optimizers import SGD
from func import load_data, chord2index

# Generate dummy data
import numpy as np

(x_train, y_train) = load_data('../data/train_note.csv', '../data/train_chord.csv')

# data pre-processing
y_train=np_utils.to_categorical(y_train, num_classes=25)

x_test=x_train
y_test=y_train



model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(4, activation='relu', input_dim=13))
model.add(Dropout(0.5))
model.add(Dense(4, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(25, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=4)
score = model.evaluate(x_test, y_test, batch_size=4)
