# -*- coding: utf-8 -*-
"""
Learns a model for classifying images of handwritten digits.
The specific dataset is hosted at UCI Machine Learning Repository 
Created on Thu Mar  6 13:36:38 2014

@author: pruvolo
"""

import matplotlib.pyplot as plt
import numpy
from numpy import argmax
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

data = load_digits()
print data.DESCR
n_trials = 10
train_percentage = 90
# Set the parameters by cross-validation
# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
neighbor_params = [{'n_neighbors' : range(1,5)}]
forest_params = [{'n_estimators' : range(1,20), 'max_features' : range(1,10)}]

test_accuracies = numpy.zeros(n_trials)

for n in range(n_trials):
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percentage/100.0, random_state=n)
#    model = GridSearchCV(RandomForestClassifier(), forest_params, cv=5)
#    model = GridSearchCV(KNeighborsClassifier(), neighbor_params, cv=5)
    model = GridSearchCV(SVC(C=1), tuned_parameters, cv=5)
    model.fit(X_train, y_train)
    print model.best_estimator_
    test_accuracies[n] = model.score(X_test, y_test)

print 'Average accuracy is %f' % (test_accuracies.mean())