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
    bw = random.choice(birth_weights)
    factors = np.random.normal(1.09, 0.03, n)
    aw = bw * np.prod(factors)
    return aw

def PlotAdultWeights(live):

    birth_weights = live.totalwgt_lb.dropna().values
    aws = [GenerateAdultWeight(birth_weights, 40) for _ in range(1000)]
    log_aws = np.log10(aws)
    thinkstats2.NormalProbabilityPlot(log_aws)
    thinkplot.Show(xlabel='standard normal values',
                   ylabel='adult weight (log10 lbs)')




def main():
    thinkstats2.RandomSeed(17)

    live, firsts, others = first.MakeFrames()
    PlotAdultWeights(live)
    return
    PlotPregLengths(live, firsts, others)


if __name__ == '__main__':
    main()

