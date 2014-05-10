"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import first

import thinkstats2
import thinkplot

# TODO: find out what resample was used for or remove it

def Resample(cdf, n=10000):
    """
    """
    sample = cdf.Sample(n)
    new_cdf = thinkstats2.MakeCdfFromList(sample, 'resampled')
    thinkplot.Clf()
    thinkplot.Cdfs([cdf, new_cdf])
    thinkplot.Save(root='resample_cdf',
               title='CDF',
               xlabel='weight in oz',
               ylabel='CDF(x)') 


def MakeExample():
    """Make a simple example CDF."""
    t = [2, 1, 3, 2, 5]
    cdf = thinkstats2.MakeCdfFromList(t)
    thinkplot.Clf()
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='example_cdf',
                   title='CDF',
                   xlabel='x',
                   ylabel='CDF(x)',
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

    first_pmf = thinkstats2.MakePmfFromList(first_wgt_dropna, name='first')
    other_pmf = thinkstats2.MakePmfFromList(other_wgt_dropna, name='other')

    first_cdf = thinkstats2.MakeCdfFromPmf(first_pmf)
    other_cdf = thinkstats2.MakeCdfFromPmf(other_pmf)

    width = 0.4 / 16

    # plot PMFs of birth weights for first babies and others
    thinkplot.PrePlot(2)
    thinkplot.Hist(first_pmf, width=-width)
    thinkplot.Hist(other_pmf, width=width)
    thinkplot.Save(root='nsfg_birthwgt_pmf',
                   title='Birth weight PMF',
                   xlabel='weight (pounds)',
                   ylabel='probability')

    # plot CDFs of birth weights for first babies and others
    thinkplot.PrePlot(2)
    thinkplot.Cdf(first_cdf)
    thinkplot.Cdf(other_cdf)
    thinkplot.Save(root='nsfg_birthwgt_cdf',
                   title='Birth weight CDF',
                   xlabel='weight (pounds)',
                   ylabel='probability',
              #     axis=[0, 200/16.0, 0, 1]
                   )


def main(name, data_dir=''):
    live, firsts, others = first.MakeFrames()
    MakeFigures(live, firsts, others)
    MakeExample()
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
