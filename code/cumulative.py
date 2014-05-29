"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np

import nsfg
import first

import thinkstats2
import thinkplot


def MakeExample():
    """Make a simple example CDF."""
    t = [2, 1, 3, 2, 5]
    cdf = thinkstats2.Cdf(t)
    thinkplot.Clf()
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='cumulative_example_cdf',
                   xlabel='x',
                   ylabel='CDF',
                   axis=[0, 6, 0, 1],
                   legend=False)    


def MakeFigures(live, firsts, others):
    """Creates several figures for the book.

    live: DataFrame
    firsts: DataFrame
    others: DataFrame
    """

    first_wgt = firsts.totalwgt_lb
    first_wgt_dropna = first_wgt.dropna()
    print('Firsts', len(first_wgt), len(first_wgt_dropna))
    #assert len(first_wgt_dropna) == 4381
 
    other_wgt = others.totalwgt_lb
    other_wgt_dropna = other_wgt.dropna()
    print('Others', len(other_wgt), len(other_wgt_dropna))
    #assert len(other_wgt_dropna) == 4706

    first_pmf = thinkstats2.Pmf(first_wgt_dropna, label='first')
    other_pmf = thinkstats2.Pmf(other_wgt_dropna, label='other')

    width = 0.4 / 16

    # plot PMFs of birth weights for first babies and others
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_pmf, align='right', width=width)
    thinkplot.Hist(other_pmf, align='left', width=width)
    thinkplot.Save(root='cumulative_birthwgt_pmf',
                   title='Birth weight',
                   xlabel='weight (pounds)',
                   ylabel='PMF')

    # plot CDFs of birth weights for first babies and others
    first_cdf = thinkstats2.Cdf(firsts.totalwgt_lb, label='first')
    other_cdf = thinkstats2.Cdf(others.totalwgt_lb, label='other')

    thinkplot.PrePlot(2)
    thinkplot.Cdfs([first_cdf, other_cdf])
    thinkplot.Save(root='cumulative_birthwgt_cdf',
                   title='Birth weight',
                   xlabel='weight (pounds)',
                   ylabel='CDF',
                   axis=[0, 12.5, 0, 1]
                   )


def MakeCdf(live):
    """Plot the CDF of pregnancy lengths for live births.
   
    live: DataFrame for live births
    """
    cdf = thinkstats2.Cdf(live.prglngth, label='prglngth')
    thinkplot.Cdf(cdf)
    thinkplot.Save('cumulative_prglngth_cdf',
                   title='Pregnancy length',
                   xlabel='weeks',
                   ylabel='CDF')


def RandomFigure(live):
    weights = live.totalwgt_lb
    cdf = thinkstats2.Cdf(weights, label='totalwgt_lb')

    sample = np.random.choice(weights, 100, replace=True)
    ranks = [cdf.PercentileRank(x) for x in sample]

    rank_cdf = thinkstats2.Cdf(ranks, label='percentile ranks')
    thinkplot.Cdf(rank_cdf)
    thinkplot.Save(root='cumulative_random',
                   xlabel='percentile rank',
                   ylabel='CDF')


def TestSample(live):
    weights = live.totalwgt_lb
    cdf = thinkstats2.Cdf(weights, label='totalwgt_lb')

    sample = cdf.Sample(1000)
    sample_cdf = thinkstats2.Cdf(sample, label='sample')

    thinkplot.PrePlot(2)
    thinkplot.Cdfs([cdf, sample_cdf])
    thinkplot.Save(root='cumulative_sample',
                   xlabel='weight (pounds)',
                   ylabel='CDF')


def main(name, data_dir=''):
    thinkstats2.RandomSeed(17)

    MakeExample()
    live, firsts, others = first.MakeFrames()
    RandomFigure(live)
    TestSample(live)
    MakeCdf(live)
    MakeFigures(live, firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
