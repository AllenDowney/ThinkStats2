"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import math

import thinkstats2

def RawMoment(xs, k):
    return sum(x**k for x in xs) / float(len(xs))


def CentralMoment(xs, k):
    xbar = RawMoment(xs, 1)
    return sum((x - xbar)**k for x in xs) / len(xs)


def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    sigma = math.sqrt(var)
    return CentralMoment(xs, k) / sigma**k


def Skewness(xs):
    return StandardizedMoment(xs, 3)


def Median(xs):
    cdf = thinkstats2.MakeCdfFromList(xs)
    return cdf.Value(0.5)


def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp


def main():
    xs = range(10)

    print 'mean', RawMoment(xs, 1)
    print 'median', Median(xs)
    print 'var', CentralMoment(xs, 2)
    print 'skewness', Skewness(xs)
    print 'Pearson skewness', PearsonMedianSkewness(xs)


if __name__ == '__main__':
    main()
