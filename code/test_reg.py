"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import math
import random
import numpy

from scipy import stats

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


def SatIqData(n, rho):
    res = CorrelatedGenerator(n, rho)
    xs, ys = zip(*res)
    xs = numpy.array(xs) * 100 + 500
    ys = numpy.array(ys) * 15 + 100

    return xs, ys


def main():
    random.seed(17)

    rho = 0.8
    xs, ys = SatIqData(1000, rho)
    print 'mean, var of x', thinkstats2.MeanVar(xs)
    print 'mean, var of y', thinkstats2.MeanVar(ys)
    print 'Pearson corr', thinkstats2.Corr(xs, ys)

    inter, slope = thinkstats2.LeastSquares(xs, ys)
    print 'inter', inter
    print 'slope', slope
    
    fxs, fys = thinkstats2.FitLine(xs, inter, slope)
    res = thinkstats2.Residuals(xs, ys, inter, slope)
    R2 = thinkstats2.CoefDetermination(ys, res)
    print 'R2', R2

    thinkplot.Plot(fxs, fys, color='gray', alpha=0.2)
    thinkplot.Scatter(xs, ys)
    thinkplot.Show()


if __name__ == '__main__':
    main()
