"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import first

import thinkstats2
import thinkplot

import random
import numpy as np
import matplotlib.pyplot as pyplot


class HypothesisTest(object):
    """Represents a hypothesis test."""

    def __init__(self, data):
        """Initializes.

        data: data in whatever form is relevant
        """
        self.data = data
        self.actual = self.TestStatistic(data)

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        mean1 = thinkstats2.Mean(group1)
        mean2 = thinkstats2.Mean(group2)
        test_stat = abs(mean1 - mean2)
        return test_stat

    def SimulateNull(self):
        """Simulates the null hypothesis.

        returns: test statistic based on simulated data
        """
        group1, group2 = self.data
        n, m = len(group1), len(group2)
        pool = np.hstack((group1, group2))
        np.random.shuffle(pool)
        data = pool[:n], pool[n:]
        test_stat = self.TestStatistic(data)
        return test_stat

    def PValue(self, iters=1000):
        """Computes the sample distribution of the test statistic and p-value.

        iters: number of iterations

        returns: Cdf object, float p-value
        """
        self.sample_stats = [self.SimulateNull() for i in range(iters)]
        self.sample_cdf = thinkstats2.MakeCdfFromList(self.sample_stats)

        p_value = 1 - self.sample_cdf.Prob(self.actual)
        return p_value

    def PlotCdf(self, root):
        """Draws a Cdf with vertical lines at the observed test stat.

        root: string used to generate filenames
        """
        def VertLine(x):
            """Draws a vertical line at x."""
            xs = [x, x]
            ys = [0, 1]
            thinkplot.Plot(xs, ys, color='0.7')

        VertLine(self.actual)

        thinkplot.PrePlot(1)
        thinkplot.Cdf(self.sample_cdf)

        thinkplot.Save(root,
                       title='Permutation test',
                       xlabel='difference in means (weeks)',
                       ylabel='CDF',
                       legend=False) 


def main():
    thinkstats2.RandomSeed(17)

    # get the data
    live, firsts, others = first.MakeFrames()
    mean_var = thinkstats2.MeanVar(live.prglngth)
    print('(Mean, Var) of prglength for live births', mean_var)
    data = firsts.prglngth.values, others.prglngth.values

    # run the test
    ht = HypothesisTest(data)
    ht.SimulateNull()
    p_value = ht.PValue(iters=1000)
    print('p-value =', p_value)
    ht.PlotCdf(root='hypothesis1')
    

if __name__ == "__main__":
    main()
