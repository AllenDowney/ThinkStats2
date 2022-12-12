"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
import numpy as np
import math

import brfss
import thinkplot
import thinkstats2


def GetHeightWeight(df, hjitter=0.0, wjitter=0.0):
    """Get sequences of height and weight.

    df: DataFrame with htm3 and wtkg2
    hjitter: float magnitude of random noise added to heights
    wjitter: float magnitude of random noise added to weights

    returns: tuple of sequences (heights, weights)
    """
    heights = df.htm3
    if hjitter:
        heights = thinkstats2.Jitter(heights, hjitter)

    weights = df.wtkg2
    if wjitter:
        weights = thinkstats2.Jitter(weights, wjitter)

    return heights, weights


def ScatterPlot(heights, weights, alpha=1.0):
    """Make a scatter plot and save it.

    heights: sequence of float
    weights: sequence of float
    alpha: float
    """
    thinkplot.Scatter(heights, weights, alpha=alpha)
    thinkplot.Config(xlabel='height (cm)',
                     ylabel='weight (kg)',
                     axis=[140, 210, 20, 200],
                     legend=False)


def HexBin(heights, weights, bins=None):
    """Make a hexbin plot and save it.

    heights: sequence of float
    weights: sequence of float
    bins: 'log' or None for linear
    """
    thinkplot.HexBin(heights, weights, bins=bins)
    thinkplot.Config(xlabel='height (cm)',
                     ylabel='weight (kg)',
                     axis=[140, 210, 20, 200],
                     legend=False)


def MakeFigures(df):
    """Make scatterplots.
    """
    sample = thinkstats2.SampleRows(df, 5000)

    # simple scatter plot
    thinkplot.PrePlot(cols=2)
    heights, weights = GetHeightWeight(sample)
    ScatterPlot(heights, weights)

    # scatter plot with jitter
    thinkplot.SubPlot(2)
    heights, weights = GetHeightWeight(sample, hjitter=1.3, wjitter=0.5)
    ScatterPlot(heights, weights)

    thinkplot.Save(root='scatter1')

    # with jitter and transparency
    thinkplot.PrePlot(cols=2)
    ScatterPlot(heights, weights, alpha=0.1)

    # hexbin plot
    thinkplot.SubPlot(2)
    heights, weights = GetHeightWeight(df, hjitter=1.3, wjitter=0.5)
    HexBin(heights, weights)
    thinkplot.Save(root='scatter2')


def BinnedPercentiles(df):
    """Bin the data by height and plot percentiles of weight for eachbin.

    df: DataFrame
    """
    cdf = thinkstats2.Cdf(df.htm3)
    print('Fraction between 140 and 200 cm', cdf[200] - cdf[140])

    bins = np.arange(135, 210, 5)
    indices = np.digitize(df.htm3, bins)
    groups = df.groupby(indices)

    heights = [group.htm3.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.wtkg2) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(heights, weights, label=label)

    thinkplot.Save(root='scatter3',
                   xlabel='height (cm)',
                   ylabel='weight (kg)')


def Correlations(df):
    print('pandas cov', df.htm3.cov(df.wtkg2))
    #print('NumPy cov', np.cov(df.htm3, df.wtkg2, ddof=0))
    print('thinkstats2 Cov', thinkstats2.Cov(df.htm3, df.wtkg2))
    print()

    print('pandas corr', df.htm3.corr(df.wtkg2))
    #print('NumPy corrcoef', np.corrcoef(df.htm3, df.wtkg2, ddof=0))
    print('thinkstats2 Corr', thinkstats2.Corr(df.htm3, df.wtkg2))
    print()

    print('pandas corr spearman', df.htm3.corr(df.wtkg2, method='spearman'))
    print('thinkstats2 SpearmanCorr', 
          thinkstats2.SpearmanCorr(df.htm3, df.wtkg2))
    print('thinkstats2 SpearmanCorr log wtkg3', 
          thinkstats2.SpearmanCorr(df.htm3, np.log(df.wtkg2)))
    print()

    print('thinkstats2 Corr log wtkg3',
          thinkstats2.Corr(df.htm3, np.log(df.wtkg2)))
    print()


def main(script):
    thinkstats2.RandomSeed(17)
    
    df = brfss.ReadBrfss(nrows=None)
    df = df.dropna(subset=['htm3', 'wtkg2'])
    Correlations(df)
    return

    MakeFigures(df)
    BinnedPercentiles(df)
    

if __name__ == '__main__':
    main(*sys.argv)
