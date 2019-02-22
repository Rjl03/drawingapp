import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(sys.argv[1:])
data = np.load("data/raw/devanagari.npz")
train_x, train_y, test_x, test_y = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
train_y_series = pd.Series(train_y)
test_y_series = pd.Series(test_y)
train_ka = train_x[train_y_series[train_y_series == 1].index]
test_ka = test_x[test_y_series[test_y_series == 1].index]
train_kha = train_x[train_y_series[train_y_series == 2].index]
test_kha = test_x[test_y_series[test_y_series == 2].index]
plt.imshow(train_ka[0])

