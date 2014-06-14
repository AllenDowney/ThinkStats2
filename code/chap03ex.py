"""Lindsey Vanderlyn thinkstats2 creating mean and varience functions
for PMFs"""

import numpy as np

import nsfg
import thinkstats2
import thinkplot

def findmean(pmf):
	"""calculates float mean of pmf"""
    mean = 0.0
    for x, p in pmf.d.items():
        mean += p * x
    return mean

def findvariance(pmf):
	"""calculates float variance from mean of a pmf"""
	var = 0.0
	for x, p in pmf.d.items():
		var += p*(x-findmean(pmf))**2
		return var