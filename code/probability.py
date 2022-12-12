"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot


def MakeHists(live):
    """Plot Hists for live births

    live: DataFrame
    others: DataFrame
    """
    hist = thinkstats2.Hist(np.floor(live.agepreg), label='agepreg')
    thinkplot.PrePlot(2, cols=2)

    thinkplot.SubPlot(1)
    thinkplot.Hist(hist)
    thinkplot.Config(xlabel='years',
                     ylabel='frequency',
                     axis=[0, 45, 0, 700])

    thinkplot.SubPlot(2)
    thinkplot.Pmf(hist)

    thinkplot.Save(root='probability_agepreg_hist', 
                   xlabel='years',
                   axis=[0, 45, 0, 700])


def MakeFigures(firsts, others):
    """Plot Pmfs of pregnancy length.

    firsts: DataFrame
    others: DataFrame
    """
    # plot the PMFs
    first_pmf = thinkstats2.Pmf(firsts.prglngth, label='first')
    other_pmf = thinkstats2.Pmf(others.prglngth, label='other')
    width = 0.45

    thinkplot.PrePlot(2, cols=2)
    thinkplot.Hist(first_pmf, align='right', width=width)
    thinkplot.Hist(other_pmf, align='left', width=width)
    thinkplot.Config(xlabel='weeks',
                     ylabel='probability',
                     axis=[27, 46, 0, 0.6])

    thinkplot.PrePlot(2)
    thinkplot.SubPlot(2)
    thinkplot.Pmfs([first_pmf, other_pmf])
    thinkplot.Save(root='probability_nsfg_pmf',
                   xlabel='weeks',
                   axis=[27, 46, 0, 0.6])

    # plot the differences in the PMFs
    weeks = range(35, 46)
    diffs = []
    for week in weeks:
        p1 = first_pmf.Prob(week)
        p2 = other_pmf.Prob(week)
        diff = 100 * (p1 - p2)
        diffs.append(diff)

    thinkplot.Bar(weeks, diffs)
    thinkplot.Save(root='probability_nsfg_diffs',
                   title='Difference in PMFs',
                   xlabel='weeks',
                   ylabel='percentage points',
                   legend=False)


def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


def UnbiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to 1/value.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, 1.0/x)
        
    new_pmf.Normalize()
    return new_pmf


def ClassSizes():
    """Generate PMFs of observed and actual class size.
    """
    # start with the actual distribution of class sizes from the book
    d = { 7: 8, 12: 8, 17: 14, 22: 4, 
          27: 6, 32: 12, 37: 8, 42: 3, 47: 2 }

    # form the pmf
    pmf = thinkstats2.Pmf(d, label='actual')
    print('mean', pmf.Mean())
    print('var', pmf.Var())
    
    # compute the biased pmf
    biased_pmf = BiasPmf(pmf, label='observed')
    print('mean', biased_pmf.Mean())
    print('var', biased_pmf.Var())

    # unbias the biased pmf
    unbiased_pmf = UnbiasPmf(biased_pmf, label='unbiased')
    print('mean', unbiased_pmf.Mean())
    print('var', unbiased_pmf.Var())

    # plot the Pmfs
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Save(root='class_size1',
                   xlabel='class size',
                   ylabel='PMF',
                   axis=[0, 52, 0, 0.27])
    
 
def main(script):
    live, firsts, others = first.MakeFrames()
    MakeFigures(firsts, others)
    MakeHists(live)

    ClassSizes()


if __name__ == '__main__':
    import sys
    main(*sys.argv)


