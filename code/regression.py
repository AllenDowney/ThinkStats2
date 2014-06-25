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
import re

import chap01ex_soln
import first
import thinkplot
import thinkstats2


def QuickLeastSquares(xs, ys):
    """Estimates linear least squares fit and returns MSE.

    xs: sequence of values
    ys: sequence of values

    returns: inter, slope, mse
    """
    n = float(len(xs))

    meanx = xs.mean()
    dxs = xs - meanx
    varx = np.dot(dxs, dxs) / n

    meany = ys.mean()
    dys = ys - meany

    cov = np.dot(dxs, dys) / n
    slope = cov / varx
    inter = meany - slope * meanx

    res = ys - (inter + slope * xs)
    mse = np.dot(res, res) / n
    return inter, slope, mse


def ReadVariables():
    vars1 = thinkstats2.ReadStataDct('2002FemPreg.dct').variables
    vars2 = thinkstats2.ReadStataDct('2002FemResp.dct').variables

    all_vars = vars1.append(vars2)
    all_vars.index = all_vars.name
    return all_vars


def GoMining(live):
    """
    """
    resp = chap01ex_soln.ReadFemResp()
    resp.index = resp.caseid

    live = live[live.prglngth>30]
    join = live.join(resp, on='caseid', rsuffix='_r')
    join.screentime = pandas.to_datetime(join.screentime)
    print(len(join), len(join.columns))

    t = []
    for name in join.columns:
        try:
            if join[name].var() < 1e-7:
                continue

            formula = 'totalwgt_lb ~ agepreg + ' + name
            model = smf.ols(formula, data=join)
            if model.nobs < len(join)/2:
                continue

            results = model.fit()
        except (ValueError, TypeError):
            continue

        t.append((results.rsquared, name))

    all_vars = ReadVariables()

    t.sort(reverse=True)
    for mse, name in t[:30]:
        key = re.sub('_r$', '', name)
        try:
            desc = all_vars.loc[key].desc
            if isinstance(desc, pandas.Series):
                desc = desc[0]
            print(name, mse, desc)
        except KeyError:
            print(name, mse)

    formula = ('totalwgt_lb ~ agepreg + C(race) + babysex==1 + '
               'nbrnaliv>1 + paydu==1 + totincr')
    results = smf.ols(formula, data=join).fit()
    Summarize(results)
    print(results.summary())


def Summarize(results):
    """Prints the most important parts of linear regression results:

    results: RegressionResults object
    """
    for name, param in results.params.iteritems():
        pvalue = results.pvalues[name]
        print('%12s\t%0.3g\t(%.3g)' % (name, param, pvalue))

    print('R^2 %.4g' % results.rsquared)

    ys = results.model.endog
    print('Std(ys) %.4g' % ys.std())
    print('Std(res) %.4g' % results.resid.std())


def RunSimpleRegression(live):
    live_dropna = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    ages = live_dropna.agepreg
    weights = live_dropna.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    formula = 'totalwgt_lb ~ agepreg'
    model = smf.ols(formula, data=live)
    # OLS object
    results = model.fit()
    # RegressionResults object

    #print('p-value', results.f_pvalue)
    #print('mse model', results.mse_model)
    #print('mse resid', results.mse_resid)
    #print('mse total', results.mse_total)
    #print('r2', results.rsquared, r2)
    #print('r2 adj', results.rsquared_adj)
    #print('inter', results.params['Intercept'], inter)
    #print('p-value', results.pvalues['Intercept'])
    #print('slope', results.params['agepreg'], slope)
    #print('p-value', results.pvalues['agepreg'])
    #print('Std(res)', thinkstats2.Std(results.resid), thinkstats2.Std(res))
    #print('fittedvalues', len(results.fittedvalues))

    Summarize(results)

    def AlmostEquals(x, y, tol=1e-6):
        return abs(x-y) < tol

    assert(AlmostEquals(results.params['Intercept'], inter))
    assert(AlmostEquals(results.params['agepreg'], slope))
    assert(AlmostEquals(results.rsquared, r2))


def RunModels(live, firsts, others):
    live['isfirst'] = live.birthord == 1

    table = pandas.pivot_table(live, rows='isfirst',
                               values=['totalwgt_lb', 'agepreg'])
    print(table)

    columns = ['isfirst[T.True]', 'agepreg', 'agepreg2']

    def MakeRow(results):
        t = []
        for col in columns:
            coef = results.params.get(col, np.nan)
            pval = results.pvalues.get(col, np.nan)
            if np.isnan(coef):
                s = '--'
            elif pval < 0.001:
                s = '%0.3g (*)' % (coef)
            else:
                s = '%0.3g (%0.2g)' % (coef, pval)
            t.append(s)
        t.append('%.2g' % results.rsquared)
        return t

    rows = []
    formula = 'totalwgt_lb ~ isfirst'
    results = smf.ols(formula, data=live).fit()
    rows.append(MakeRow(results))
    print(formula)
    Summarize(results)

    formula = 'totalwgt_lb ~ agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(MakeRow(results))
    print(formula)
    Summarize(results)
    
    formula = 'totalwgt_lb ~ isfirst + agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(MakeRow(results))
    print(formula)
    Summarize(results)
    
    live['agepreg2'] = live.agepreg**2
    formula = 'totalwgt_lb ~ isfirst + agepreg + agepreg2'
    results = smf.ols(formula, data=live).fit()
    rows.append(MakeRow(results))
    print(formula)
    Summarize(results)
    
    #live['isyoung'] = live.agepreg < 20
    #formula = 'totalwgt_lb ~ isfirst + isyoung'
    #results = smf.ols(formula, data=live).fit()
    #rows.append(MakeRow(results))
    
    #formula = 'totalwgt_lb ~ isfirst + agepreg + isyoung'
    #results = smf.ols(formula, data=live).fit()
    #rows.append(MakeRow(results))

    header = ['isfirst', 'agepreg', 'agepreg2']
    PrintTabular(rows, header)


def PrintTabular(rows, header):
    s = r'\hline ' + ' & '.join(header) + r' \\ \hline'
    print(s)

    for row in rows:
        s = ' & '.join(row) + r' \\'
        print(s)

    print(r'\hline')


def JoinRespFile(live):
    resp = chap01ex_soln.ReadFemResp()
    resp.index = resp.caseid
    print(resp)
    
    # live.join(resp, on='caseid', how='inner')
    join = pandas.merge(live, resp, left_on='caseid', right_index=True,
                        how='inner', sort=False)
    print(join.columns)


def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()

    GoMining(live)
    return

    RunModels(live, firsts, others)
    return

    RunSimpleRegression(live)
    return

    JoinRespFile(live)
    return



if __name__ == '__main__':
    import sys
    main(*sys.argv)
