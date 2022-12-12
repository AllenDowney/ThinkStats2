"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy as np

import nsfg
import first

import thinkstats2
import thinkplot


def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank

scores = [55, 66, 77, 88, 99]
your_score = 88

print('score, percentile rank')
for score in scores:
    print(score, PercentileRank(scores, score))
print()

def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores.sort()
    index = percentile_rank * (len(scores)-1) // 100
    return scores[index]

print('prank, score, score')
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print(percentile_rank, 
          Percentile(scores, percentile_rank),
          Percentile2(scores, percentile_rank))


def EvalCdf(sample, x):
    """Computes CDF(x) in a sample.

    sample: sequence
    x: value

    returns: cumulative probability
    """
    count = 0.0
    for value in sample:
        if value <= x:
            count += 1.0

    prob = count / len(sample)
    return prob

sample = [1, 2, 2, 3, 5]

print('x', 'CDF(x)')
for x in range(0, 7):
    print(x, EvalCdf(sample, x))



def PositionToPercentile(position, field_size):
    """Converts from position in the field to percentile.

    position: int
    field_size: int
    """
    beat = field_size - position + 1
    percentile = 100.0 * beat / field_size
    return percentile


def PercentileToPosition(percentile, field_size):
    """Converts from percentile to hypothetical position in the field.

    percentile: 0-100
    field_size: int
    """
    beat = percentile * field_size / 100.0
    position = field_size - beat + 1
    return position


# my time 42:44
print('Percentile rank in field', PositionToPercentile(97, 1633))
print('Percentile rank in age group', PositionToPercentile(26, 256))

percentile = PositionToPercentile(26, 256)
print('Equivalent position in M50-59', PercentileToPosition(percentile, 171))
# 17th place = 46:05
print('Equivalent position in F20-29', PercentileToPosition(percentile, 448))
# 48:28


def MakeExample():
    """Makes a simple example CDF."""
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
    """Plots the distribution of weights against a random sample.

    live: DataFrame for live births
    """
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
