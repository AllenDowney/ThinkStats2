"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy as np
import random

import first
import normal
import thinkstats2
import thinkplot


def PlotPregLengths(live, firsts, others):
    """Plots sampling distributions under the null and alternate hypotheses.

    live, firsts, others: DataFrames

    Results:  
    null hypothesis N(0, 0.00319708)
    0.0837707042554 0.0837707042554     (90% CI)

    estimated params N(0.0780373, 0.00321144)
    -0.0151758158699 0.171250349425     (90% CI)

    Sampling distribution under the null hypothesis is centered
    around 0.

    Sampling distribution under the null hypothesis is centered
    around the observed difference, 0.078.

    The variance of the two distributions is very similar; in practice,
    you could reasonably compute whichever one is easier.

    """
    print('prglngth example')
    delta = firsts.prglngth.mean() - others.prglngth.mean()
    print(delta)

    dist1 = normal.SamplingDistMean(live.prglngth, len(firsts))
    dist2 = normal.SamplingDistMean(live.prglngth, len(others))
    dist = dist1 - dist2
    print('null hypothesis', dist)
    print(dist.Prob(-delta), 1 - dist.Prob(delta))

    thinkplot.PrePlot(2)
    thinkplot.Plot(dist, label='null hypothesis')

    dist1 = normal.SamplingDistMean(firsts.prglngth, len(firsts))
    dist2 = normal.SamplingDistMean(others.prglngth, len(others))
    dist = dist1 - dist2
    print('estimated params', dist)
    print(dist.Percentile(5), dist.Percentile(95))

    thinkplot.Plot(dist, label='estimated params')
    thinkplot.Show(xlabel='difference in means (weeks)',
                   ylabel='CDF')


def GenerateAdultWeight(birth_weights, n):
    """Generate a random adult weight by simulating annual gain.

    birth_weights: sequence of birth weights in lbs
    n: number of years to simulate

    returns: adult weight in lbs
    """
    bw = random.choice(birth_weights)
    factors = np.random.normal(1.09, 0.03, n)
    aw = bw * np.prod(factors)
    return aw


def PlotAdultWeights(live):
    """Makes a normal probability plot of log10 adult weight.

    live: DataFrame of live births

    results: 

    With n=40 the distribution is approximately lognormal except for
    the lowest weights.

    Actual distribution might deviate from lognormal because it is
    a mixture of people at different ages, or because annual weight
    gains are correlated.
    """
    birth_weights = live.totalwgt_lb.dropna().values
    aws = [GenerateAdultWeight(birth_weights, 40) for _ in range(1000)]
    log_aws = np.log10(aws)
    thinkstats2.NormalProbabilityPlot(log_aws)
    thinkplot.Show(xlabel='standard normal values',
                   ylabel='adult weight (log10 lbs)')


def TestIntervention():
    """Tests whether reported changes are statistically significant.

    Results:
    -1.66 4.73095323208e-05
    -0.26 0.125267987207
     1.4 0.00182694836898

    Conclusions:

    1) Gender gap before intervention was 1.66 points (p-value 5e-5)

    2) Genger gap after was 0.26 points (p-value 0.13, no significant)

    3) Change in gender gap was 1.4 points (p-value 0.002, significant).
    """
    male_before = normal.Normal(3.57, 0.28**2)
    male_after = normal.Normal(3.44, 0.16**2)

    female_before = normal.Normal(1.91, 0.32**2)
    female_after = normal.Normal(3.18, 0.16**2)

    diff_before = female_before - male_before
    print('mean, p-value', diff_before.mu, 1-diff_before.Prob(0))
    print('CI', diff_before.Percentile(5), diff_before.Percentile(95))
    print('stderr', diff_before.sigma)

    diff_after = female_after - male_after
    print('mean, p-value', diff_after.mu, 1-diff_after.Prob(0))
    print('CI', diff_after.Percentile(5), diff_after.Percentile(95))
    print('stderr', diff_after.sigma)

    diff = diff_after - diff_before
    print('mean, p-value', diff.mu, diff.Prob(0))
    print('CI', diff.Percentile(5), diff.Percentile(95))
    print('stderr', diff.sigma)


def main():
    thinkstats2.RandomSeed(17)

    TestIntervention()
    return

    live, firsts, others = first.MakeFrames()
    PlotAdultWeights(live)

    PlotPregLengths(live, firsts, others)


if __name__ == '__main__':
    main()
