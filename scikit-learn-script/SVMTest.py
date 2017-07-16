__author__ = 'wangyida_'

import dataProcess
from sklearn import metrics
from sklearn.svm import SVC

X,Y =dataProcess.getTrainData()

model = SVC()
model.fit(X,Y)

X,Y = dataProcess.getTestData()

predict = model.predict(X)

print metrics.classification_report(Y,predict)
print dataProcess.calculateAccuracy(Y,predict)