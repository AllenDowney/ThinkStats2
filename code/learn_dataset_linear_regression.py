# -*- coding: utf-8 -*-
"""
Learns a model of Boston housing prices using randomly selected
subsets of the original 13 features.
This example is intended to demonstrate the gap between training and testing
performance and its relationship to model complexity.
Created on Thu Mar  6 13:36:38 2014

@author: pruvolo
"""
from sklearn.linear_model import LinearRegression
import numpy
import matplotlib.pyplot as plt
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split

n_trials = 1000

boston = load_boston()

# Example of learning using the Boston housing prices dataset
print boston.DESCR

X = boston.data
y = boston.target

d = boston.data.shape[1]

avg_train_r2 = numpy.zeros(d)
avg_test_r2 = numpy.zeros(d)

for n_features in range(1,d+1):
	r2_train = numpy.zeros(n_trials)
	r2_test = numpy.zeros(n_trials)

	for i in range(n_trials):
		# permute the columns of X
		X_t = X.transpose()
		numpy.random.shuffle(X_t)
		X = X_t.transpose()

		X_train, X_test, y_train, y_test = train_test_split(X[:,0:n_features], y, train_size=0.5)

		model = LinearRegression()
		model.fit(X_train, y_train)
		r2_train[i] = model.score(X_train, y_train)
		r2_test[i] = model.score(X_test,y_test)

	avg_train_r2[n_features-1] = r2_train.mean()
	avg_test_r2[n_features-1] = r2_test.mean()

fig = plt.figure()
train_line, = plt.plot(range(1,d+1),avg_train_r2)
plt.hold(True)
test_line, = plt.plot(range(1,d+1),avg_test_r2)
plt.legend([train_line, test_line],['Average Training R^2','Average Testing R^2'],loc="upper left")
plt.xlabel('Number of Features')
plt.show()
