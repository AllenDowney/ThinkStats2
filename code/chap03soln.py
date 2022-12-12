"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot


def PmfMean(pmf):
    """Computes the mean of a PMF.

    Returns:
        float mean
    """
    mean = 0.0
    for x, p in pmf.d.items():
        mean += p * x
    return mean


def PmfVar(pmf, mu=None):
    """Computes the variance of a PMF.

    Args:
        mu: the point around which the variance is computed;
            if omitted, computes the mean

    Returns:
        float variance
    """
    if mu is None:
        mu = pmf.Mean()

    var = 0.0
    for x, p in pmf.d.items():
        var += p * (x - mu) ** 2
    return var


def Diffs(t):
    """List of differences between the first elements and others.

    t: list of numbers
    
    returns: list of numbers
    """
    first = t[0]
    rest = t[1:]
    diffs = [first - x for x in rest]
    return diffs


def PairWiseDifferences(live):
    """Summarize pairwise differences for children of the same mother.

    live: DataFrame of pregnancy records for live births
    """
    live = live[live.prglngth >= 37]
    preg_map = nsfg.MakePregMap(live)

    diffs = []
    for caseid, indices in preg_map.items():
        lengths = live.loc[indices].prglngth.values
        if len(lengths) >= 2:
            diffs.extend(Diffs(lengths))

    mean = thinkstats2.Mean(diffs)
    print('Mean difference between pairs', mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='Difference in weeks',
                   ylabel='PMF')


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    PairWiseDifferences(live)

    # test PmfMean and PmfVar
    prglngth = live.prglngth
    pmf = thinkstats2.Pmf(prglngth)
    mean = PmfMean(pmf)
    var = PmfVar(pmf)

    assert(mean == pmf.Mean())
    assert(var == pmf.Var())
    print('mean/var preg length', mean, var)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
