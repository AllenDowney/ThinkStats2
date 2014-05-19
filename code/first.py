"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math

import nsfg
import thinkstats2
import thinkplot


def MakeFrames():
    """Reads pregnancy data and partitions first babies and others.

    returns: DataFrames (all live births, first babies, others)
    """
    preg = nsfg.ReadFemPreg()

    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    assert len(live) == 9148
    assert len(firsts) == 4413
    assert len(others) == 4735

    return live, firsts, others


def Summarize():
    """Prints summary statistics for first babies and others.
    """
    live, firsts, others = MakeFrames()

    print(len(live), 'live births')
    print(len(firsts), 'first live births')
    print(len(others), 'other live births')

    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()

    print('Mean gestation in weeks:')
    print('First babies', mean1)
    print('Others', mean2)
    
    print('Difference in weeks', mean1 - mean2)
    print('Difference in days', (mean1 - mean2) * 7.0)


def Summarize(live, firsts, others):
    """Print various summary statistics."""

    mean0 = live.prglngth.mean()
    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()

    var0 = live.prglngth.var()
    var1 = firsts.prglngth.var()
    var2 = others.prglngth.var()

    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance')
    print('First babies', var1)
    print('Others', var2)

    diff_mean = mean1 - mean2
    print('Difference in mean', diff_mean)

    print('Live mean', mean0)
    print('Live variance', var0)
    print('Live sigma', math.sqrt(var0))


def PrintExtremes(live):
    """Plots the histogram of pregnancy lengths and prints the extremes.

    live: DataFrame of live births
    """
    length_hist = thinkstats2.MakeHistFromList(live.prglngth)
    thinkplot.PrePlot(1)
    thinkplot.Hist(length_hist, label='live births')

    thinkplot.Save(root='nsfg_hist_live', 
                   title='Histogram',
                   xlabel='weeks',
                   ylabel='frequency')

    items = list(length_hist.Items())
    items.sort()

    print('Shortest lengths:')
    for weeks, count in items[:10]:
        print(weeks, count)

    print('Longest lengths:')
    for weeks, count in items[-10:]:
        print(weeks, count)
    

def MakeFigures(live, firsts, others):
    """Plot Hists and Pmfs for pregnancy length.

    firsts: DataFrame
    others: DataFrame
    """
    first_hist = thinkstats2.MakeHistFromList(firsts.prglngth)
    first_pmf = thinkstats2.MakePmfFromHist(first_hist)

    other_hist = thinkstats2.MakeHistFromList(others.prglngth)
    other_pmf = thinkstats2.MakePmfFromHist(other_hist)

    width = 0.4
    first_options = dict(label='first', width=-width)
    other_options = dict(label='other', width=width)

    # plot the histograms
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_hist, **first_options)
    thinkplot.Hist(other_hist, **other_options)

    axis = [27, 46, 0, 2700]
    thinkplot.Save(root='nsfg_hist', 
                   title='Histogram',
                   xlabel='weeks',
                   ylabel='frequency',
                   axis=axis)

    # plot the PMFs
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_pmf, **first_options)
    thinkplot.Hist(other_pmf, **other_options)

    axis = [27, 46, 0, 0.6]
    thinkplot.Save(root='nsfg_pmf',
                   title='PMF',
                   xlabel='weeks',
                   ylabel='probability',
                   axis=axis)

    # plot the differences in the PMFs
    weeks = range(35, 46)
    diffs = []
    for week in weeks:
        p1 = first_pmf.Prob(week)
        p2 = other_pmf.Prob(week)
        diff = 100 * (p1 - p2)
        diffs.append(diff)

    thinkplot.PrePlot(1)
    thinkplot.Bar(weeks, diffs, align='center')
    thinkplot.Save(root='nsfg_diffs',
                   title='Difference in PMFs',
                   xlabel='weeks',
                   ylabel='percentage points',
                   legend=False)


def main(script):
    live, firsts, others = MakeFrames()

    PrintExtremes(live)

    MakeFigures(live, firsts, others)

    Summarize(live, firsts, others)



if __name__ == '__main__':
    import sys
    main(*sys.argv)


