"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function


import random
import numpy as np
import scipy.stats

def write_sample(sample, filename):
    """Write a sequence of floats to a file.
    """
    fp = open(filename, 'w')
    for x in sample:
        fp.write('%f\n' % x)
    fp.close()

def uniform_sample(n):
    return [random.uniform(0, 100) for i in range(n)]
        
def triangular_sample(n):
    return [random.triangular(0, 100) for i in range(n)]
        
def expo_sample(n):
    return [random.expovariate(1.0/50) for i in range(n)]
        
def gauss_sample(n):
    return [random.gauss(50, 25) for i in range(n)]
        
def lognorm_sample(n):
    return [random.lognormvariate(3, 1.3) for i in range(n)]
        
def pareto_sample(n):
    return [10 * random.paretovariate(1.2) for i in range(n)]
        
def weibull_sample(n):
    return [random.weibullvariate(60, 5) for i in range(n)]
        
def gumbel_sample(n):
    rv = scipy.stats.gumbel_r(45, 10)
    return rv.rvs(n)
        
def main():

    funcs = [uniform_sample, triangular_sample, expo_sample,
             gauss_sample, lognorm_sample, pareto_sample,
             weibull_sample, gumbel_sample]

    for i in range(len(funcs)):
        sample = funcs[i](1000)
        print(np.mean(sample))
        filename = 'mystery%d.dat' % i
        write_sample(sample, filename)


if __name__ == '__main__':
    main()
