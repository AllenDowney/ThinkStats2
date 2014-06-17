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


def SamplingDistributions(fxs, fys, res, iters=101):
    """Estimates sampling distributions by permuting residuals.

    fxs: sequence of xs
    fys: sequence of fitted ys
    res: sequence of residuals
    iters: number of times to run simulations

    returns: pair of sequences (inters, slopes)
    """
    t = []
    for _ in range(iters):
        random.shuffle(res)
        estimates = thinkstats2.LeastSquares(fxs, fys + res)
        t.append(estimates)

    inters, slopes = zip(*t)
    return inters, slopes


def PlotConfidenceIntervals(ages, inters, slopes):

    rows = len(slopes)
    cols = len(ages)
    array = np.zeros([rows, cols])

    for i, (inter, slope) in enumerate(zip(inters, slopes)):
        print(i)
        fxs, fys = thinkstats2.FitLine(ages, inter, slope)
        array[i,] = fys

    array = np.sort(array, axis=0)

    for index in [25, 50, 75]:
        thinkplot.Plot(fxs, array[index,])
    thinkplot.Show()

    # TODO: fillbetween
        
    
    



def Summarize(values, actual):
    """Prints standard error and 90% confidence interval.

    values: sequence of estimates
    actual: float actual value
    """
    std = thinkstats2.Std(values, mu=actual)
    cdf = thinkstats2.Cdf(values)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('SE, CI', std, ci)


def PlotFit(live):
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    ages = live.agepreg
    weights = live.totalwgt_lb

    inter, slope = thinkstats2.LeastSquares(ages, weights)
    fit_xs, fit_ys = thinkstats2.FitLine(ages, inter, slope)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    live['residual'] = res

    inters, slopes = SamplingDistributions(fit_xs, fit_ys, res)
    print('inter', inter)
    Summarize(inters, inter)
    print('slope', slope)
    Summarize(slopes, slope)

    PlotConfidenceIntervals(ages, inters, slopes)
    return

    thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)
    thinkplot.Plot(fit_xs, fit_ys, color='white', linewidth=3)
    thinkplot.Plot(fit_xs, fit_ys, color='blue', linewidth=2)
    thinkplot.Save(root='regression1',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   axis=[10, 45, 0, 15],
                   legend=False)

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




def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    
    PlotFit(live)
    return

    xs, ys = ReadData(data_dir)
    inter = thinkstats2.Mean(ys)
    slope = 0
    fxs, fys = thinkstats2.FitLine(xs, inter, slope)
    res = thinkstats2.Residuals(xs, ys, inter, slope)

    inter_cdf, slope_cdf = SamplingDistributions(fxs, fys, res, n=1000)

    thinkplot.Cdf(slope_cdf)
    thinkplot.Save(root='regress1',
                   xlabel='Estimated slope (oz/year)',
                   ylabel='CDF',
                   title='Sampling distribution')

    return

    inter, slope = thinkstats2.LeastSquares(xs, ys)
    
    fxs, fys = thinkstats2.FitLine(xs, inter, slope)
    i = len(fxs) / 2
    print('median weight, age', fxs[i], fys[i])

    res = thinkstats2.Residuals(xs, ys, inter, slope)
    R2 = thinkstats2.CoefDetermination(ys, res)
    print('R2', R2)
    print('R', math.sqrt(R2))

    #thinkplot.Plot(fxs, fys, color='gray', alpha=0.5)
    #thinkplot.Scatter(xs, ys, alpha=0.05)
    #thinkplot.Show()

    inter_cdf, slope_cdf = SamplingDistributions(fxs, fys, res, n=1000)
    thinkplot.Cdf(slope_cdf)
    thinkplot.Save(root='regress1',
                   xlabel='Estimated slope (oz/year)',
                   ylabel='CDF',
                   title='Sampling distribution')


if __name__ == '__main__':
    import sys
    main(*sys.argv)
