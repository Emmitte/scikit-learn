__author__ = 'wangyida_'

import numpy as np

def loadX(path):
    dataset = []
    fr = open(path)
    lines = fr.readlines()
    fr.close()
    for line in lines:
        line = line.strip('\n').split('\t')
        arr = []
        for data in line:
            arr.append(float(data))
        dataset.append(arr)
    return dataset

def loadY(path):
    dataset = []
    fr = open(path)
    lines = fr.readlines()
    fr.close()
    for line in lines:
        dataset.append(float(line.strip('\n')))
    return dataset

def getTrainData():
    train_dir = "train/"
    train_x_path = train_dir + "train_x"
    train_y_path = train_dir + "train_y"

    X = []
    Y = []

    #X = loadX(train_x_path)
    #Y = loadY(train_y_path)

    X = np.loadtxt(train_x_path,delimiter='\t',dtype=float)
    Y = np.loadtxt(train_y_path,delimiter='\t',dtype=float)

    return X,Y

def getTestData():
    test_dir = "test/"
    test_x_path = test_dir + "test_x"
    test_y_path = test_dir + "test_y"

    X = []
    Y = []

    #X = loadX(test_x_path)
    #Y = loadY(test_y_path)

    X = np.loadtxt(test_x_path,delimiter='\t',dtype=float)
    Y = np.loadtxt(test_y_path,delimiter='\t',dtype=float)

    return X,Y

def calculateAccuracy(y,predict):
    count = 0
    sum = len(y)
    i = 0
    for p in predict:
        if p == y[i]:
            count += 1
        i += 1
    accuracy = (count*1.0/sum)*100
    return accuracy