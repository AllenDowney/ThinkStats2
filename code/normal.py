"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import numpy as np
import random
import scipy.stats

import first
import hypothesis
import thinkstats2
import thinkplot


class Normal(object):
    """Represents a Normal distribution"""

    def __init__(self, mu, sigma2, label=''):
        """Initializes.

        mu: mean
        sigma2: variance
        """
        self.mu = mu
        self.sigma2 = sigma2
        self.label = label

    def __repr__(self):
        """Returns a string representation."""
        if self.label:
            return 'Normal(%g, %g, %s)' % (self.mu, self.sigma2, self.label)
        else:
            return 'Normal(%g, %g)' % (self.mu, self.sigma2)

    __str__ = __repr__

    @property
    def sigma(self):
        """Returns the standard deviation."""
        return math.sqrt(self.sigma2)

    def __add__(self, other):
        """Adds a number or other Normal.

        other: number or Normal

        returns: new Normal
        """
        if isinstance(other, Normal):
            return Normal(self.mu + other.mu, self.sigma2 + other.sigma2)
        else:
            return Normal(self.mu + other, self.sigma2)

    __radd__ = __add__

    def __sub__(self, other):
        """Subtracts a number or other Normal.

        other: number or Normal

        returns: new Normal
        """
        if isinstance(other, Normal):
            return Normal(self.mu - other.mu, self.sigma2 + other.sigma2)
        else:
            return Normal(self.mu - other, self.sigma2)

    __rsub__ = __sub__

    def __mul__(self, factor):
        """Multiplies by a scalar.

        factor: number

        returns: new Normal
        """
        return Normal(factor * self.mu, factor**2 * self.sigma2)

    __rmul__ = __mul__

    def __div__(self, divisor):
        """Divides by a scalar.

        divisor: number

        returns: new Normal
        """
        return 1.0 / divisor * self

    __truediv__ = __div__

    def Sum(self, n):
        """Returns the distribution of the sum of n values.

        n: int

        returns: new Normal
        """
        return Normal(n * self.mu, n * self.sigma2)

    def Render(self):
        """Returns pair of xs, ys suitable for plotting.
        """
        mean, std = self.mu, self.sigma
        low, high = mean - 3 * std, mean + 3 * std
        xs, ys = thinkstats2.RenderNormalCdf(mean, std, low, high)
        return xs, ys

    def Prob(self, x):
        """Cumulative probability of x.

        x: numeric
        """
        return thinkstats2.EvalNormalCdf(x, self.mu, self.sigma)

    def Percentile(self, p):
        """Inverse CDF of p.

        p: percentile rank 0-100
        """
        return thinkstats2.EvalNormalCdfInverse(p/100, self.mu, self.sigma)


def NormalPlotSamples(samples, plot=1, ylabel=''):
    """Makes normal probability plots for samples.

    samples: list of samples
    label: string
    """
    for n, sample in samples:
        thinkplot.SubPlot(plot)
        thinkstats2.NormalProbabilityPlot(sample)

        thinkplot.Config(title='n=%d' % n,
                         legend=False,
                         xticks=[],
                         yticks=[],
                         ylabel=ylabel)
        plot += 1


def MakeExpoSamples(beta=2.0, iters=1000):
    """Generates samples from an exponential distribution.

    beta: parameter
    iters: number of samples to generate for each size

    returns: list of samples
    """
    samples = []
    for n in [1, 10, 100]:
        sample = [np.sum(np.random.exponential(beta, n))
                  for _ in range(iters)]
        samples.append((n, sample))
    return samples


def MakeLognormalSamples(mu=1.0, sigma=1.0, iters=1000):
    """Generates samples from a lognormal distribution.

    mu: parmeter
    sigma: parameter
    iters: number of samples to generate for each size

    returns: list of samples
    """
    samples = []
    for n in [1, 10, 100]:
        sample = [np.sum(np.random.lognormal(mu, sigma, n))
                  for _ in range(iters)]
        samples.append((n, sample))
    return samples


def MakeParetoSamples(alpha=1.0, iters=1000):
    """Generates samples from a Pareto distribution.

    alpha: parameter
    iters: number of samples to generate for each size

    returns: list of samples
    """
    samples = []

    for n in [1, 10, 100]:
        sample = [np.sum(np.random.pareto(alpha, n))
                  for _ in range(iters)]
        samples.append((n, sample))
    return samples


def GenerateCorrelated(rho, n):
    """Generates a sequence of correlated values from a standard normal dist.
    
    rho: coefficient of correlation
    n: length of sequence

    returns: iterator
    """
    x = random.gauss(0, 1)
    yield x

    sigma = math.sqrt(1 - rho**2)
    for _ in range(n-1):
        x = random.gauss(x * rho, sigma)
        yield x


def GenerateExpoCorrelated(rho, n):
    """Generates a sequence of correlated values from an exponential dist.

    rho: coefficient of correlation
    n: length of sequence

    returns: NumPy array
    """
    normal = list(GenerateCorrelated(rho, n))
    uniform = scipy.stats.norm.cdf(normal)
    expo = scipy.stats.expon.ppf(uniform)
    return expo


def MakeCorrelatedSamples(rho=0.9, iters=1000):
    """Generates samples from a correlated exponential distribution.

    rho: correlation
    iters: number of samples to generate for each size

    returns: list of samples
    """    
    samples = []
    for n in [1, 10, 100]:
        sample = [np.sum(GenerateExpoCorrelated(rho, n))
                  for _ in range(iters)]
        samples.append((n, sample))
    return samples


def SamplingDistMean(data, n):
    """Computes the sampling distribution of the mean.

    data: sequence of values representing the population
    n: sample size

    returns: Normal object
    """
    mean, var = data.mean(), data.var()
    dist = Normal(mean, var)
    return dist.Sum(n) / n


def PlotPregLengths(live, firsts, others):
    """Plots sampling distribution of difference in means.

    live, firsts, others: DataFrames
    """
    print('prglngth example')
    delta = firsts.prglngth.mean() - others.prglngth.mean()
    print(delta)

    dist1 = SamplingDistMean(live.prglngth, len(firsts))
    dist2 = SamplingDistMean(live.prglngth, len(others))
    dist = dist1 - dist2
    print('null hypothesis', dist)
    print(dist.Prob(-delta), 1 - dist.Prob(delta))

    thinkplot.Plot(dist, label='null hypothesis')
    thinkplot.Save(root='normal3',
                   xlabel='difference in means (weeks)',
                   ylabel='CDF')


class CorrelationPermute(hypothesis.CorrelationPermute):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        xs, ys = data
        return np.corrcoef(xs, ys)[0][1]


def ResampleCorrelations(live):
    """Tests the correlation between birth weight and mother's age.

    live: DataFrame for live births

    returns: sample size, observed correlation, CDF of resampled correlations
    """
    live2 = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live2.agepreg.values, live2.totalwgt_lb.values
    ht = CorrelationPermute(data)
    p_value = ht.PValue()
    return len(live2), ht.actual, ht.test_cdf


def StudentCdf(n):
    """Computes the CDF correlations from uncorrelated variables.

    n: sample size

    returns: Cdf
    """
    ts = np.linspace(-3, 3, 101)
    ps = scipy.stats.t.cdf(ts, df=n-2)
    rs = ts / np.sqrt(n - 2 + ts**2)
    return thinkstats2.Cdf(rs, ps)


def TestCorrelation(live):
    """Tests correlation analytically.

    live: DataFrame for live births

    """
    n, r, cdf = ResampleCorrelations(live)

    model = StudentCdf(n)
    thinkplot.Plot(model.xs, model.ps, color='gray',
                   alpha=0.3, label='Student t')
    thinkplot.Cdf(cdf, label='sample')

    thinkplot.Save(root='normal4',
                   xlabel='correlation',
                   ylabel='CDF')

    t = r * math.sqrt((n-2) / (1-r**2))
    p_value = 1 - scipy.stats.t.cdf(t, df=n-2)
    print(r, p_value)


def ChiSquaredCdf(n):
    """Discrete approximation of the chi-squared CDF with df=n-1.

    n: sample size
    
    returns: Cdf
    """
    xs = np.linspace(0, 25, 101)
    ps = scipy.stats.chi2.cdf(xs, df=n-1)
    return thinkstats2.Cdf(xs, ps)


def TestChiSquared():
    """Performs a chi-squared test analytically.
    """
    data = [8, 9, 19, 5, 8, 11]
    dt = hypothesis.DiceChiTest(data)
    p_value = dt.PValue(iters=1000)
    n, chi2, cdf = len(data), dt.actual, dt.test_cdf

    model = ChiSquaredCdf(n)
    thinkplot.Plot(model.xs, model.ps, color='gray',
                   alpha=0.3, label='chi squared')
    thinkplot.Cdf(cdf, label='sample')

    thinkplot.Save(root='normal5',
                   xlabel='chi-squared statistic',
                   ylabel='CDF',
                   loc='lower right')

    # compute the p-value
    p_value = 1 - scipy.stats.chi2.cdf(chi2, df=n-1)
    print(chi2, p_value)


def MakeCltPlots():
    """Makes plot showing distributions of sums converging to normal.
    """
    thinkplot.PrePlot(num=3, rows=2, cols=3)
    samples = MakeExpoSamples()
    NormalPlotSamples(samples, plot=1, ylabel='sum of expo values')

    thinkplot.PrePlot(num=3)
    samples = MakeLognormalSamples()
    NormalPlotSamples(samples, plot=4, ylabel='sum of lognormal values')
    thinkplot.Save(root='normal1', legend=False)


    thinkplot.PrePlot(num=3, rows=2, cols=3)
    samples = MakeParetoSamples()
    NormalPlotSamples(samples, plot=1, ylabel='sum of Pareto values')

    thinkplot.PrePlot(num=3)
    samples = MakeCorrelatedSamples()
    NormalPlotSamples(samples, plot=4, ylabel='sum of correlated expo values')
    thinkplot.Save(root='normal2', legend=False)


def main():
    thinkstats2.RandomSeed(17)

    MakeCltPlots()

    print('Gorilla example')
    dist = Normal(90, 7.5**2)
    print(dist)
    dist_xbar = dist.Sum(9) / 9
    print(dist_xbar.sigma)
    print(dist_xbar.Percentile(5), dist_xbar.Percentile(95))

    live, firsts, others = first.MakeFrames()
    TestCorrelation(live)
    PlotPregLengths(live, firsts, others)

    TestChiSquared()


if __name__ == '__main__':
    main()

