"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import numpy as np

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


def Summarize(live, firsts, others):
    """Print various summary statistics."""

    mean0 = live.prglngth.mean()
    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()

    var0 = live.prglngth.var()
    var1 = firsts.prglngth.var()
    var2 = others.prglngth.var()

    print('Live mean', mean0)
    print('Live variance', var0)
    print('Live std', math.sqrt(var0))

    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance')
    print('First babies', var1)
    print('Others', var2)

    print('Difference in weeks', mean1 - mean2)
    print('Difference in hours', (mean1 - mean2) * 7 * 24)

    print('Difference relative to 39 weeks', (mean1 - mean2) / 39 * 100)

    d = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
    print('Cohen d', d)


def PrintExtremes(live):
    """Plots the histogram of pregnancy lengths and prints the extremes.

    live: DataFrame of live births
    """
    length_hist = thinkstats2.Hist(live.prglngth)
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
    

def MakeHists(live):
    """Plot Hists for live births

    live: DataFrame
    others: DataFrame
    """
    hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
    thinkplot.Hist(hist)
    thinkplot.Save(root='first_wgt_lb_hist', 
                   xlabel='pounds',
                   ylabel='frequency',
                   axis=[-1, 14, 0, 3200])

    hist = thinkstats2.Hist(live.birthwgt_oz, label='birthwgt_oz')
    thinkplot.Hist(hist)
    thinkplot.Save(root='first_wgt_oz_hist', 
                   xlabel='ounces',
                   ylabel='frequency',
                   axis=[-1, 16, 0, 1200])

    hist = thinkstats2.Hist(np.floor(live.agepreg), label='agepreg')
    thinkplot.Hist(hist)
    thinkplot.Save(root='first_agepreg_hist', 
                   xlabel='years',
                   ylabel='frequency')

    hist = thinkstats2.Hist(live.prglngth, label='prglngth')
    thinkplot.Hist(hist)
    thinkplot.Save(root='first_prglngth_hist', 
                   xlabel='weeks',
                   ylabel='frequency',
                   axis=[-1, 53, 0, 5000])


def MakeFigures(firsts, others):
    """Plot Hists and Pmfs of pregnancy length.

    firsts: DataFrame
    others: DataFrame
    """
    first_hist = thinkstats2.Hist(firsts.prglngth)
    other_hist = thinkstats2.Hist(others.prglngth)

    width = 0.4
    first_options = dict(label='first', align='left', width=-width)
    other_options = dict(label='other', align='left', width=width)

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
    first_pmf = thinkstats2.MakePmfFromHist(first_hist)
    other_pmf = thinkstats2.MakePmfFromHist(other_hist)

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

    thinkplot.Bar(weeks, diffs, align='center')
    thinkplot.Save(root='nsfg_diffs',
                   title='Difference in PMFs',
                   xlabel='weeks',
                   ylabel='percentage points',
                   legend=False)


def main(script):
    live, firsts, others = MakeFrames()

    MakeHists(live)
    return

    PrintExtremes(live)
    MakeFigures(firsts, others)
    Summarize(live, firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)


