__author__ = 'wangyida_'

from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import dataProcess

X,Y = dataProcess.getTrainData()

model = GaussianNB()
model.fit(X,Y)

X,Y = dataProcess.getTestData()

predict = model.predict(X)

print metrics.classification_report(Y,predict)
print dataProcess.calculateAccuracy(Y,predict)