"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import random
import scipy.stats

import thinkstats2
import thinkplot

from collections import Counter


def ParetoCdf(x, alpha, xmin):
    """Evaluates CDF of the Pareto distribution with parameters alpha, xmin."""
    if x < xmin:
        return 0
    return 1 - pow(x / xmin, -alpha)


def ParetoMedian(xmin, alpha):
    """Computes the median of a Pareto distribution."""
    return xmin * pow(2, 1/alpha)


def MakeParetoCdf():
    """Generates a plot of the CDF of height in Pareto World."""
    n = 50
    max = 1000.0
    xs = [max*i/n for i in range(n)]
    
    xmin = 100
    alpha = 1.7
    ps = [ParetoCdf(x, alpha, xmin) for x in xs]
    print('Median', ParetoMedian(xmin, alpha))
    
    pyplot.clf()
    pyplot.plot(xs, ps, linewidth=2)
    myplot.Save('pareto_world1',
                title = 'Pareto CDF',
                xlabel = 'height (cm)',
                ylabel = 'CDF',
                legend=False)


def MakeFigure(xmin=100, alpha=1.7, mu=150, sigma=25):
    """Makes a figure showing the CDF of height in ParetoWorld.

    Compared to a normal distribution.

    xmin: parameter of the Pareto distribution
    alpha: parameter of the Pareto distribution
    mu: parameter of the Normal distribution
    sigma: parameter of the Normal distribution
    """

    t1 = [xmin * random.paretovariate(alpha) for i in range(10000)]
    cdf1 = Cdf.MakeCdfFromList(t1, name='pareto')

    t2 = [random.normalvariate(mu, sigma) for i in range(10000)]
    cdf2 = Cdf.MakeCdfFromList(t2, name='normal')

    myplot.Clf()
    myplot.Cdfs([cdf1, cdf2])
    myplot.Save(root='pareto_world2',
                title='Pareto World',
                xlabel='height (cm)',
                ylabel='CDF')


def TallestPareto(iters=2, n=10000, xmin=100, alpha=1.7):
    """Find the tallest person in Pareto World.

    iters: how many samples to generate
    n: how many in each sample
    xmin: parameter of the Pareto distribution
    alpha: parameter of the Pareto distribution
    """
    tallest = 0
    for i in range(iters):
        t = [xmin * random.paretovariate(alpha) for i in range(n)]
        tallest = max(max(t), tallest)
    return tallest


def ParetoSample(alpha, xmin, n):
    t = scipy.stats.pareto.rvs(b=alpha, size=n) * xmin
    return t.round()


def main():
    
    counter = Counter()
    for i in range(10000):
        sample = ParetoSample(1.7, 0.001, 10000)
        counter.update(Counter(sample))

    print(len(counter))
    return

    pmf = thinkstats2.Pmf(counter)
    print('mean', pmf.Mean())
    for x, prob in pmf.Largest(10):
        print(x)

    cdf = thinkstats2.Cdf(pmf)
    thinkplot.Cdf(cdf, complement=True)
    thinkplot.Show(xscale='log',
                   yscale='log')
    return

    MakeFigure()
    MakeParetoCdf()
    print(TallestPareto(iters=2))


if __name__ == "__main__":
    main()
