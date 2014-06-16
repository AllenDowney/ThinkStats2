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

        data: list of frequencies
        """
        observed = data
        n = sum(observed)
        expected = np.ones(6) * n / 6
        test_stat = sum(abs(observed - expected))
        return test_stat

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        n = sum(self.data)
        values = [1,2,3,4,5,6]
        rolls = np.random.choice(values, n, replace=True)
        hist = thinkstats2.Hist(rolls)
        freqs = hist.Freqs(values)
        return freqs


class DiceChiTest(DiceTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: list of frequencies
        """
        observed = data
        n = sum(observed)
        expected = np.ones(6) * n / 6
        test_stat = sum((observed - expected)**2 / expected)
        return test_stat


class PregLengthTest(thinkstats2.HypothesisTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: pair of lists of pregnancy lengths
        """
        firsts, others = data
        stat = self.ChiSquared(firsts) + self.ChiSquared(others)
        return stat

    def ChiSquared(self, lengths):
        """Computes the chi-squared statistic.
        
        lengths: sequence of lengths

        returns: float
        """
        hist = thinkstats2.Hist(lengths)
        observed = np.array(hist.Freqs(self.values))
        expected = self.expected_probs * hist.Total()
        stat = sum((observed - expected)**2 / expected)
        return stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        firsts, others = self.data
        self.n = len(firsts)
        self.pool = np.hstack((firsts, others))

        pmf = thinkstats2.Pmf(self.pool)
        self.values = range(35, 46)
        self.expected_probs = np.array(pmf.Probs(self.values))

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data


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


def RunDiceTest():
    data = [8, 9, 19, 5, 8, 11]
    dt = DiceTest(data)
    print('dice test', dt.PValue(iters=10000))
    dt = DiceChiTest(data)
    print('dice test', dt.PValue(iters=10000))
    dt.PlotCdf()
    thinkplot.Show()


def FalseNegRate(data, num_runs=100):
    """Compute the chance of a false negative based on resampling.

    data: pair of sequences
    num_runs: how many experiments to simulate

    returns: float false negative rate
    """
    group1, group2 = data
    count = 0

    for i in range(num_runs):
        sample1 = np.random.choice(group1, len(group1), replace=True)
        sample2 = np.random.choice(group2, len(group2), replace=True)
        ht = DiffMeansPermute((sample1, sample2))
        p_value = ht.PValue(iters=101)
        print('actual, p', ht.actual, p_value)
        if p_value > 0.05:
            count += 1

    return count / num_runs


def main():
    thinkstats2.RandomSeed(17)

    live, firsts, others = first.MakeFrames()
    data = firsts.prglngth.values, others.prglngth.values
    neg_rate = FalseNegRate(data)
    print('neg_rate', neg_rate)
    return

    # compare pregnancy lengths (chi-squared)
    ht = PregLengthTest(data)
    p_value = ht.PValue()
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
    return

    # test correlation
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live.agepreg.values, live.totalwgt_lb.values
    ht = CorrelationPermute(data)
    p_value = ht.PValue()
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    # compare birth weights
    print('agepreg')
    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    RunTests(data)

    # compare pregnancy lengths
    print('prglngth')
    RunTests(data)

    # run the coin test
    ct = CoinTest((140, 110))
    pvalue = ct.PValue()
    print('coin test p-value', pvalue)

    # run the dice test
    RunDiceTest()


if __name__ == "__main__":
    main()
