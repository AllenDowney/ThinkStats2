"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import first

import thinkstats2
import thinkplot

import copy
import random
import numpy as np
import matplotlib.pyplot as pyplot


class CoinTest(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        heads, tails = data
        test_stat = abs(heads - tails)
        return test_stat

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        heads, tails = self.data
        n = heads + tails
        sample = [random.choice('HT') for _ in range(n)]
        hist = thinkstats2.Hist(sample)
        data = hist['H'], hist['T']
        return data


class DiffMeansPermute(thinkstats2.HypothesisTest):

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


class DiffMeansOneSided(DiffMeansPermute):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = group1.mean() - group2.mean()
        return test_stat


class DiffStdPermute(DiffMeansPermute):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = group1.std() - group2.std()
        return test_stat


class DiffMeansResample(DiffMeansPermute):

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2


class CorrelationPermute(thinkstats2.HypothesisTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        xs, ys = data
        test_stat = abs(thinkstats2.Corr(xs, ys))
        return test_stat

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        xs, ys = self.data
        xs = np.random.permutation(xs)
        return xs, ys


class DiceTest(thinkstats2.HypothesisTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        observed = data
        n = sum(self.data)
        expected = np.ones(6) * n / 6
        test_stat = sum(abs(observed - expected))
        return test_stat

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        n = sum(self.data)
        rolls = [random.randint(1,6) for _ in range(n)]
        hist = thinkstats2.Hist(rolls)
        xs, freqs = hist.Render()
        return freqs


class DiceChiTest(DiceTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        observed = data
        n = sum(self.data)
        expected = np.ones(6) * n / 6
        test_stat = sum((observed - expected)**2 / expected)
        return test_stat


def RunTests(data, iters=10000):
    # test the difference in means
    ht = DiffMeansPermute(data)
    p_value = ht.PValue(iters=iters)
    print('means permute two-sided')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis1',
                   title='Permutation test',
                   xlabel='difference in means (weeks)',
                   ylabel='CDF',
                   legend=False) 
    
    # test the difference in std
    ht = DiffStdPermute(data)
    p_value = ht.PValue(iters=iters)
    print('std permute one-sided')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis2',
                   title='Permutation test',
                   xlabel='difference in std (weeks)',
                   ylabel='CDF',
                   legend=False) 
    
    # test the difference in means by resampling
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=iters)
    print('means resample two-sided')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    ht.PlotCdf()
    thinkplot.Save(root='hypothesis3',
                   title='Resampling test',
                   xlabel='difference in means (weeks)',
                   ylabel='CDF',
                   legend=False) 
    
    # test the difference in means
    ht = DiffMeansOneSided(data)
    p_value = ht.PValue(iters=iters)
    print('means permute one-sided')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())


def main():
    thinkstats2.RandomSeed(19)

    data = [8, 9, 19, 6, 8, 10]
    dt = DiceTest(data)
    print('dice test', dt.PValue())
    dt = DiceChiTest(data)
    print('dice test', dt.PValue())
    dt.PlotCdf()
    thinkplot.Show()
    return

    live, firsts, others = first.MakeFrames()
    mean_var = thinkstats2.MeanVar(live.prglngth)

    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live.agepreg.values, live.totalwgt_lb.values
    ht = CorrelationPermute(data)
    p_value = ht.PValue()
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
    return

    # compare birth weights
    print('agepreg')
    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    RunTests(data)

    # compare pregnancy lengths
    print('prglngth')
    data = firsts.prglngth.values, others.prglngth.values
    RunTests(data)

    # run the coin test
    ct = CoinTest((140, 110))
    pvalue = ct.PValue()
    print('coin test p-value', pvalue)


if __name__ == "__main__":
    main()
