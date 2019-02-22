import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense

print(sys.argv[1:])
data = np.load("data/raw/devanagari.npz")
train_x, train_y, test_x, test_y = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
train_y_series = pd.Series(train_y)
test_y_series = pd.Series(test_y)
train_x = train_x[train_y_series.index]
test_x = test_x[test_y_series.index]
X = train_x.reshape(78200,1024)
X_test = test_x.reshape(13800,1024)
y = np.concatenate([np.ones(39100),np.zeros(39100)])
y_test = np.concatenate([np.ones(6900), np.zeros(6900)])
X = X/255
X_test = X_test/255
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_shape=(1024,)))
model.compile(optimizer='sgd', loss='binary_crossentropy')
model.fit(X, y, epochs=15)
y_pred = model.predict_classes(X_test)
print(accuracy_score(y_test, y_pred))



