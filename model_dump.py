import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score, confusion_matrix
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from keras.utils import to_categorical
from keras import optimizers

from keras.callbacks import TensorBoard


data = np.load("data/processed/devanagari-processed.npz")
X_train, y_train, X_val, y_val, X_test, y_test = data['X_train'], data['y_train'], data['X_val'], data['y_val'], data['X_test'], data['y_test']
X_train = X_train / 255
X_val = X_val / 255
# Turn integer labels to one-hots. 
y_train_binary = to_categorical(y_train, num_classes=46)
y_val_binary = to_categorical(y_val, num_classes=46)
# Reshape X_train and X_val to have a channel
X_train = X_train.reshape(64400,32,32,1)
X_val = X_val.reshape(13800,32,32,1)
model = Sequential()
model.add(Conv2D(filters=100, kernel_size=3,activation='relu', input_shape=(32,32,1)))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(filters=50, kernel_size=3,activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
# Flatten => RELU layers
model.add(Flatten())
model.add(Dense(100, activation ="relu"))
# a softmax classifier
model.add(Dense(46, activation ="softmax"))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train_binary, validation_data=(X_val, y_val_binary), epochs=5, batch_size=128)
model.save('out/Conv.h5')