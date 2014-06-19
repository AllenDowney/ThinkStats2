"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import random
import numpy as np

import first
import thinkplot
import thinkstats2
import statsmodels.formula.api as smf

def Summarize(values, actual):
    """Prints standard error and 90% confidence interval.

    values: sequence of estimates
    actual: float actual value
    """
    std = thinkstats2.Std(values, mu=actual)
    cdf = thinkstats2.Cdf(values)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('SE, CI', std, ci)


def SamplingDistributions(live, iters=101):
    """Estimates sampling distributions by resampling rows.

    live: DataFrame
    iters: number of times to run simulations

    returns: pair of sequences (inters, slopes)
    """
    t = []
    for _ in range(iters):
        sample = thinkstats2.SampleRows(live, len(live), replace=True)
        ages = sample.agepreg
        weights = sample.totalwgt_lb
        estimates = thinkstats2.LeastSquares(ages, weights)
        t.append(estimates)

    inters, slopes = zip(*t)
    return inters, slopes


def PlotConfidenceIntervals(xs, inters, slopes, res=None, **options):
    """Plots the 90% confidence intervals for weights based on ages.

    To keep it simple, this function assumes that len(inters)
    and len(slopes) are 101.

    xs: sequence
    inters: estimated intercepts
    slopes: estimated slopes
    res: residuals
    """
    assert(len(slopes) == 101)
    size = len(slopes), len(xs)
    array = np.zeros(size)

    for i, (inter, slope) in enumerate(zip(inters, slopes)):
        fxs, fys = thinkstats2.FitLine(xs, inter, slope)
        if res:
            fys += np.random.permutation(res)
        array[i,] = fys

    xs = np.sort(xs)
    array = np.sort(array, axis=0)
    
    low = array[5,]
    high = array[95,]
    thinkplot.FillBetween(xs, low, high, **options)


def PlotSamplingDistributions(live):
    """
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    inters, slopes = SamplingDistributions(live)
    print('inter', inter)
    Summarize(inters, inter)
    print('slope', slope)
    Summarize(slopes, slope)

    print('norm of residuals', thinkstats2.Std(res))
    print('RMSE', thinkstats2.Std(weights))
    print('R2', r2)
    print('R', math.sqrt(r2))
    print('rho', thinkstats2.Corr(ages, weights))

    # thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)

    PlotConfidenceIntervals(ages, inters, slopes)
    thinkplot.Save(root='regression3',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   title='90% CI',
                   legend=False)


def PlotFit(live):
    """
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    fit_xs, fit_ys = thinkstats2.FitLine(ages, inter, slope)

    thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)
    thinkplot.Plot(fit_xs, fit_ys, color='white', linewidth=3)
    thinkplot.Plot(fit_xs, fit_ys, color='blue', linewidth=2)
    thinkplot.Save(root='regression1',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   axis=[10, 45, 0, 15],
                   legend=False)


def PlotResiduals(live):
    """
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    live['residual'] = thinkstats2.Residuals(ages, weights, inter, slope)

    bins = np.arange(10, 48, 3)
    indices = np.digitize(live.agepreg, bins)
    groups = live.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.residual) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='regression2',
                   xlabel="age (years)",
                   ylabel='residual (lbs)',
                   xlim=[10, 45])


def RunOlm(live):
    formula = 'totalwgt_lb ~ agepreg'
    results = smf.ols(formula, data=live).fit()
    print(results.summary())

def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    RunOlm(live)
    return

    #PlotFit(live)
    #PlotResiduals(live)
    PlotSamplingDistributions(live)



if __name__ == '__main__':
    import sys
    main(*sys.argv)
