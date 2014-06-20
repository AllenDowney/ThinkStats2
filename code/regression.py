"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import pandas
import random
import numpy as np
import statsmodels.formula.api as smf

import first
import thinkplot
import thinkstats2

def AlmostEquals(x, y, tol=1e-6):
    return abs(x-y) < tol

def RunSimpleRegression(live):
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

    assert(AlmostEquals(results.params['Intercept'], inter))
    assert(AlmostEquals(results.params['agepreg'], slope))
    assert(AlmostEquals(results.rsquared, r2))


def RunModels(live, firsts, others):
    live['isfirst'] = live.birthord == 1

    table = pandas.pivot_table(live, 'totalwgt_lb', rows='isfirst')
    print(table)
    table = pandas.pivot_table(live, 'agepreg', rows='isfirst')
    print(table)

    columns = ['isfirst[T.True]', 'agepreg', 'isyoung[T.True]', 'isold[T.True]',]

    def Summarize(results):
        t = []
        for col in columns:
            coef = results.params.get(col, np.nan)
            pval = results.pvalues.get(col, np.nan)
            if pval < 0.001:
                s = '%0.3g (*)' % (coef)
            else:
                s = '%0.3g (%0.2g)' % (coef, pval)
            t.append(s)
        t.append('%.2g' % results.rsquared)
        return t

    rows = []
    formula = 'totalwgt_lb ~ isfirst'
    results = smf.ols(formula, data=live).fit()
    rows.append(Summarize(results))

    formula = 'totalwgt_lb ~ agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(Summarize(results))
    
    formula = 'totalwgt_lb ~ isfirst + agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(Summarize(results))
    
    live['isyoung'] = live.agepreg < 20
    formula = 'totalwgt_lb ~ isfirst + isyoung'
    results = smf.ols(formula, data=live).fit()
    rows.append(Summarize(results))
    
    formula = 'totalwgt_lb ~ isfirst + agepreg + isyoung'
    results = smf.ols(formula, data=live).fit()
    rows.append(Summarize(results))

    header = ['isfirst', 'agepreg', 'isyoung']
    PrintTabular(rows, header)


def PrintTabular(rows, header):
    s = r'\hline' + ' & '.join(header) + r' \\ \hline'
    print(s)

    for row in rows:
        s = ' & '.join(row) + r' \\'
        print(s)

    print(r'\hline')

def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    RunModels(live, firsts, others)
    return

    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    RunSimpleRegression(live)



if __name__ == '__main__':
    import sys
    main(*sys.argv)
