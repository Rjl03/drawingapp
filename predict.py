import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score, confusion_matrix
from PIL import Image
from keras.models import load_model



filename = Image.open(r'C:\wamp64\www\drawingapp\images\request.png')
X_val = np.asarray(filename, dtype=np.uint8)
X_val = X_val.T
X_val = X_val.reshape(3,1024)
model = load_model('out/ProjectModel-15.h5')
# model.load_weights('out/ProjectModel-15.h5')
y_pred = model.predict_classes(X_val)
print(y_pred)