from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import RMSprop
import numpy as np
from func import load_data, chord2index

(x_train, y_train) = load_data('../data/train_note.csv', '../data/train_chord.csv')

# data pre-processing
y_train=np_utils.to_categorical(y_train, num_classes=24)

x_test=x_train[0:100]
y_test=y_train[0:100]


#print(x_train[1])
print(x_train[1].shape)
print(y_train[1])

#
model = Sequential([
    Dense(48, input_dim=13),
    Activation('relu'),
#    Dense(60, input_dim=80),
#    Activation('sigmoid'),
#    Dense(48, input_dim=60),
#    Activation('tanh'),
    Dense(24),
    Activation('softmax'),
])

#
rmsprop=RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
#
model.compile(optimizer=rmsprop,
            loss='categorical_crossentropy',
            metrics=['accuracy'])
#
print('\nTraining....')
model.fit(x_train, y_train, epochs=100, batch_size=10)

#
print('\nTesting.....')
loss, accuracy = model.evaluate(x_test, y_test)

print('test loss:', loss)
print('test accuracy:', accuracy)
model.save('model_single.h5')

