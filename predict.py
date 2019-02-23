import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score, confusion_matrix
from PIL import Image
from keras.models import load_model
import cv2


with open("ext/dev-char.txt",encoding="utf8") as f:
    chars = f.readline().split(',')
    image = cv2.imread(r'C:\wamp64\www\drawingapp\images\request.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    X_val = np.asarray(image, dtype=np.uint8)
    X_val = X_val.reshape(1,32,32)
    model = load_model('out/Conv.h5.h5')
    y_pred = model.predict_classes(X_val)
    print(chars[y_pred[0]].encode("utf-8"))