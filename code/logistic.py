"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import random
import numpy as np

import first
import thinkplot
import thinkstats2
import statsmodels.formula.api as smf


def RunOls(live):
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    formula = 'totalwgt_lb ~ agepreg'
    model = smf.ols(formula, data=live)
    # OLS object
    results = model.fit()
    # RegressionResults object
    print(results.f_pvalue)
    print(results.mse_model)
    print(results.mse_resid)
    print(results.mse_total)
    print(results.params['Intercept'], inter)
    print(results.params['agepreg'], slope)
    print(results.pvalues)
    print(thinkstats2.Std(results.resid), thinkstats2.Std(res))
    print(results.rsquared, r2)
    print(results.rsquared_adj)
    print(results.fittedvalues)
    print(results.summary())


def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    RunOls(live)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
