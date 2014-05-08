"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import math
import random


def WriteFile(data, filename):
    """Writes a list of numbers to a file.

    data: sequence of numbers
    filename: string
    """
    fp = open(filename, 'w')
    for x in data:
        fp.write('%f\n' % x)
    fp.close()


def ReadFile(filename):
    """Reads a list of numbers from a file.

    filename: string

    returns: list of float
    """
    fp = open(filename)
    data = []
    for line in fp:
        x = float(line.strip())
        data.append(x)
    return data


def CorrelatedGenerator(n, rho):
    """Generates standard normal variates with correlation.

    rho: target coefficient of correlation

    Returns: list of pairs
    """
    sigma = math.sqrt(1 - rho**2);    
    
    res = []
    for i in range(n):
        x = random.gauss(0, 1)
        y = random.gauss(x * rho, sigma)
        res.append((x, y))

    return res


def main():
    random.seed(17)

    rho = -0.8
    res = CorrelatedGenerator(1000, rho)
    xs, ys = zip(*res)

    a = 1.0
    b = 0.0
    xs = [a * x + b for x in xs]

    print 'mean, var of x', thinkstats2.MeanVar(xs)
    print 'mean, var of y', thinkstats2.MeanVar(ys)
    print 'covariance', thinkstats2.Cov(xs, ys)
    print 'Pearson corr', thinkstats2.Corr(xs, ys)
    print 'Spearman corr', thinkstats2.SpearmanCorr(xs, ys)

    thinkplot.Scatter(xs, ys)
    thinkplot.Show()


if __name__ == '__main__':
    main()
