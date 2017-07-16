__author__ = 'wangyida_'

import numpy as np

train_dir = "train/"
test_dir = "test/"
train_x_path = train_dir + "train_x"
train_y_path = train_dir + "train_y"
test_x_path = test_dir + "test_x"
test_y_path = test_dir + "test_y"

train_X = np.loadtxt(train_x_path,delimiter='\t',dtype=float)
train_Y = np.loadtxt(train_y_path,delimiter='\t',dtype=float)
print train_X
print train_Y