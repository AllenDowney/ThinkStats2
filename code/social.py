"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import gzip
import math
import os
import sys

import Cdf
import Pmf
import myplot
import thinkstats


def BiasPmf(pmf, name, invert=False):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    If invert=True, computes in inverse operation; for example,
    unbiasing a sample collected from students.

    Args:
      pmf: Pmf object.
      invert: boolean

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy()
    new_pmf.name = name

    for x, p in pmf.Items():
        if invert:
            new_pmf.Mult(x, 1.0/x)
        else:
            new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


def ReadFile(filename='soc-Slashdot0902.txt.gz', n=None):
    """Reads a compressed data file.

    Args:
        filename: string name of the file to read
    """
    if filename.endswith('gz'):
        fp = gzip.open(filename)
    else:
        fp = open(filename)

    srcs = {}
    for i, line in enumerate(fp):
        if i == n:
            break

        if line.startswith('#'):
            continue

        src, dest = line.split()

        srcs.setdefault(src, []).append(dest)

    fp.close()

    return srcs


def Summarize(srcs):
    """Computes the number of edges for each source."""
    lens = [len(t) for t in srcs.itervalues()]
    mu, sigma2 = thinkstats.MeanVar(lens)
    print mu, math.sqrt(sigma2)
    return lens


def MakePmfs(lens):
    """Computes the PMF of the given list and the biased PMF."""
    pmf = Pmf.MakePmfFromList(lens, 'slashdot')
    print 'unbiased mean', pmf.Mean()

    biased_pmf = BiasPmf(pmf, 'biased')
    print 'biased mean', biased_pmf.Mean()

    return pmf, biased_pmf


def MakeFigures(pmf, biased_pmf):
    """Makes figures showing the CDF of the biased and unbiased PMFs"""
    cdf = Cdf.MakeCdfFromPmf(pmf, 'unbiased')
    print 'unbiased median', cdf.Percentile(50)
    print 'percent < 100', cdf.Prob(100)
    print 'percent < 1000', cdf.Prob(1000)


    biased_cdf = Cdf.MakeCdfFromPmf(biased_pmf, 'biased')
    print 'biased median', biased_cdf.Percentile(50)

    myplot.Clf()
    myplot.Cdfs([cdf, biased_cdf])
    myplot.Save(root='slashdot.logx',
                xlabel='Number of friends/foes',
                ylabel='CDF',
                xscale='log')


def MakeCdfs(lens):
    cdf = Cdf.MakeCdfFromList(lens, 'slashdot')

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='slashdot.logx',
                xlabel='Number of friends/foes',
                ylabel='CDF',
                xscale='log')

    myplot.Clf()
    myplot.Cdf(cdf, complement=True)
    myplot.Save(root='slashdot.loglog',
                xlabel='Number of friends/foes',
                ylabel='CDF',
                xscale='log',
                yscale='log')

def PmfProbLess(pmf1, pmf2):
    """Probability that a value from pmf1 is less than a value from pmf2.

    Args:
        pmf1: Pmf object
        pmf2: Pmf object

    Returns:
        float
    """
    total = 0.0
    for v1, p1 in pmf1.Items():
        for v2, p2 in pmf2.Items():
            if v1 < v2:
                total += p1 * p2
    return total


def main(name):
    srcs = ReadFile(n=100000)
    lens = Summarize(srcs)
    pmf, biased_pmf = MakePmfs(lens)
    MakeFigures(pmf, biased_pmf)
    prob = PmfProbLess(pmf, biased_pmf)
    print prob


if __name__ == '__main__':
    main(*sys.argv)
