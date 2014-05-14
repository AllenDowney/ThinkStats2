"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import numpy as np

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


def ScatterPlot(root, heights, weights, alpha=1.0):
    """Make a scatter plot and save it.

    root: string filename root
    heights: sequence of float
    weights: sequence of float
    alpha: float
    """
    thinkplot.Scatter(heights, weights, alpha=alpha)
    thinkplot.Save(root=root,
                   xlabel='Height (cm)',
                   ylabel='Weight (kg)',
                   axis=[140, 210, 20, 200],
                   legend=False)


def HexBin(root, heights, weights, bins=None):
    """Make a hexbin plot and save it.

    root: string filename root
    heights: sequence of float
    weights: sequence of float
    bins: 'log' or None for linear
    """
    thinkplot.HexBin(heights, weights, bins=bins)
    thinkplot.Save(root=root,
                xlabel='Height (cm)',
                ylabel='Weight (kg)',
                axis=[140, 210, 20, 200],
                legend=False)


def SampleRows(df, nrows, replace=False):
    """Choose a sample of rows from a DataFrame.

    df: DataFrame
    nrows: number of rows
    replace: whether to sample with replacement

    returns: DataFrame
    """
    indices = range(len(df))
    sample_indices = np.random.choice(indices, nrows, replace=False)
    sample = df.iloc[sample_indices]
    return sample


def MakeFigures():
    """Make scatterplots.
    """
    thinkstats2.RandomSeed(17)
    
    df = brfss.ReadBrfss(nrows=None)
    sample = SampleRows(df, 5000, replace=False)

    heights, weights = GetHeightWeight(sample)
    assert(heights.values[100] == 175)
    assert(weights.values[100] == 86.36)

    ScatterPlot('brfss_scatter1', heights, weights)

    heights, weights = GetHeightWeight(sample, hjitter=1.5, wjitter=1.1)
    assert(int(heights.values[100]) == 173)
    assert(int(weights.values[100]) == 85)

    ScatterPlot('brfss_scatter2', heights, weights)
    ScatterPlot('brfss_scatter3', heights, weights, alpha=0.1)

    # make a hexbin of all records
    heights, weights = GetHeightWeight(df, hjitter=1.3, wjitter=1.1)
    assert(int(heights.values[100]) == 171)
    assert(int(weights.values[100]) == 55)
    HexBin('brfss_scatter4', heights, weights)


def main(script):
    MakeFigures()


if __name__ == '__main__':
    main(*sys.argv)
