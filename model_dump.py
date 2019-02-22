import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score, confusion_matrix
from PIL import Image


data = np.load("data/raw/devanagari.npz")
train_x, train_y, test_x, test_y = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
train_y_series = pd.Series(train_y)
test_y_series = pd.Series(test_y)
X = train_x[train_y_series.index]
X = X.reshape(78200, 1024)
y = np.concatenate([np.ones(39100), np.zeros(39100)])
X_test = test_x[test_y_series.index]
X_test = X_test.reshape(13800, 1024)
y_test = np.concatenate([np.ones(6900), np.zeros(6900)])
X = X / 255
X_test = X_test / 255
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_shape=(1024,)))
model.compile(optimizer='sgd', loss='binary_crossentropy')
model.fit(X, y, epochs=15)
model.save("../out/ProjectModel-15.h5")
