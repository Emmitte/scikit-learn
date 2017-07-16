__author__ = 'wangyida_'

import dataProcess
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

X,Y = dataProcess.getTrainData()

model = DecisionTreeClassifier()
model.fit(X,Y)

X,Y = dataProcess.getTestData()

predict = model.predict(X)

print metrics.classification_report(Y,predict)
print dataProcess.calculateAccuracy(Y,predict)