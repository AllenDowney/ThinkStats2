"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function


import thinkstats2
import thinkplot


def BiasPmf(pmf, label):
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


def UnbiasPmf(pmf, label):
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
                   ylabel='PMF')
    
 
def main():
    ClassSizes()


if __name__ == '__main__':
    main()
