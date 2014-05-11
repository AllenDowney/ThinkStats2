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
        self.MakeModel()
        self.sample_stats = None
        self.sample_cdf = None

    def PValue(self, iters=1000):
        """Computes the sample distribution of the test statistic and p-value.

        iters: number of iterations

        returns: Cdf object, float p-value
        """
        self.sample_stats = [self.TestStatistic(self.RunModel()) 
                             for i in range(iters)]
        self.sample_cdf = thinkstats2.MakeCdfFromList(self.sample_stats)

        p_value = 1 - self.sample_cdf.Prob(self.actual)
        return p_value

    def PlotCdf(self):
        """Draws a Cdf with vertical lines at the observed test stat.
        """
        def VertLine(x):
            """Draws a vertical line at x."""
            xs = [x, x]
            ys = [0, 1]
            thinkplot.Plot(xs, ys, color='0.7')

        VertLine(self.actual)

        thinkplot.PrePlot(1)
        thinkplot.Cdf(self.sample_cdf)

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        raise thinkstats2.UnimplementedMethodException()

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        raise thinkstats2.UnimplementedMethodException()

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        raise thinkstats2.UnimplementedMethodException()


class DiffMeansPermute(HypothesisTest):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data


class DiffStdPermute(DiffMeansPermute):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.std() - group2.std())
        return test_stat


class DiffMeansResample(DiffMeansPermute):

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2


def main():
    thinkstats2.RandomSeed(17)

    # get the data
    live, firsts, others = first.MakeFrames()
    mean_var = thinkstats2.MeanVar(live.prglngth)
    print('(Mean, Var) of prglength for live births', mean_var)
    data = firsts.prglngth.values, others.prglngth.values

    # test the difference in means
    ht = DiffMeansPermute(data)
    p_value = ht.PValue(iters=1000)
    print('p-value =', p_value)

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis1',
                   title='Permutation test',
                   xlabel='difference in means (weeks)',
                   ylabel='CDF',
                   legend=False) 
    
    # test the difference in std
    ht = DiffStdPermute(data)
    p_value = ht.PValue(iters=1000)
    print('p-value =', p_value)

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis2',
                   title='Permutation test',
                   xlabel='difference in std (weeks)',
                   ylabel='CDF',
                   legend=False) 
    
    # test the difference in means by resampling
    ht = DiffStdPermute(data)
    p_value = ht.PValue(iters=1000)
    print('p-value =', p_value)

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis3',
                   title='Resampling test',
                   xlabel='difference in means (weeks)',
                   ylabel='CDF',
                   legend=False) 
    

if __name__ == "__main__":
    main()
