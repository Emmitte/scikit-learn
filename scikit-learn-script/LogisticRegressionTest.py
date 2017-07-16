__author__ = 'wangyida_'

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import dataProcess

train_dir = "train/"
test_dir = "test/"
train_x_path = train_dir + "train_x"
train_y_path = train_dir + "train_y"
test_x_path = test_dir + "test_x"
test_y_path = test_dir + "test_y"

X = []
Y = []
X = dataProcess.loadX(train_x_path)
Y = dataProcess.loadY(train_y_path)

model = LogisticRegression(C=1000)
model.fit(X,Y)

X = []
Y = []
X = dataProcess.loadX(test_x_path)
Y = dataProcess.loadY(test_y_path)

predict = model.predict(X)

print metrics.classification_report(Y,predict)
print dataProcess.calculateAccuracy(Y,predict)