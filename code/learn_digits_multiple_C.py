# -*- coding: utf-8 -*-
"""
Learns a model for classifying images of handwritten digits.
The specific dataset is hosted at UCI Machine Learning Repository 
Created on Thu Mar  6 13:36:38 2014

@author: pruvolo
"""

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
print data.DESCR
n_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

fig = plt.figure()
legend_entries = []
num_train = []

for ridge in range(-4,5,2):
    legend_entries.append('C=1e%d' % ridge)
    for (i,train_percent) in enumerate(train_percentages):
        print train_percent
        test_accuracy = numpy.zeros(n_trials)
        for n in range(n_trials):
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percent/100.0, random_state=n)
            if len(num_train) <=  i:
                num_train.append(len(y_train))
            model = LogisticRegression(C=10**ridge)
            model.fit(X_train, y_train)
            test_accuracy[n] = model.score(X_test, y_test)
        test_accuracies[i] = test_accuracy.mean()
    plt.hold(True)
    plt.plot(num_train, test_accuracies)

plt.legend(legend_entries,loc=4)

plt.xlabel('Number of Training Instances')
plt.ylabel('Accuracy on Test Set')
plt.show()