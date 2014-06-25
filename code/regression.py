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
import statsmodels.api as sm
import statsmodels.formula.api as smf
import re

import chap01ex_soln
import first
import linear
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
    """Reads Stata dictionary files for NSFG data.

    returns: DataFrame that maps variables names to descriptions
    """
    vars1 = thinkstats2.ReadStataDct('2002FemPreg.dct').variables
    vars2 = thinkstats2.ReadStataDct('2002FemResp.dct').variables

    all_vars = vars1.append(vars2)
    all_vars.index = all_vars.name
    return all_vars


def JoinFemResp(df):
    """Reads the female respondent file and joins on caseid.

    df: DataFrame
    """
    resp = chap01ex_soln.ReadFemResp()
    resp.index = resp.caseid

    join = df.join(resp, on='caseid', rsuffix='_r')

    # convert from colon-separated time strings to datetimes
    join.screentime = pandas.to_datetime(join.screentime)

    return join


def GoMining(df, formula='totalwgt_lb ~ agepreg + '):
    """Searches for variables that predict birth weight.

    df: DataFrame of pregnancy records
    formula: string Patsy formula
    """
    t = []
    for name in df.columns:
        try:
            if df[name].var() < 1e-7:
                continue

            formula += name
            model = smf.ols(formula, data=df)
            if model.nobs < len(df)/2:
                continue

            results = model.fit()
        except (ValueError, TypeError):
            continue

        t.append((results.rsquared, name))

    return t


def MiningReport(t, n=30):
    """Prints variables with the highest R^2.

    t: list of (R^2, variable name) pairs
    n: number of pairs to print
    """
    all_vars = ReadVariables()

    t.sort(reverse=True)
    for mse, name in t[:n]:
        key = re.sub('_r$', '', name)
        try:
            desc = all_vars.loc[key].desc
            if isinstance(desc, pandas.Series):
                desc = desc[0]
            print(name, mse, desc)
        except KeyError:
            print(name, mse)


def PredictBirthWeight(live):
    """Predict birth weight of a baby at 30 weeks.

    live: DataFrame of live births
    """
    live = live[live.prglngth>30]
    join = JoinFemResp(live)

    t = GoMining(join)
    MiningReport(t)

    formula = ('totalwgt_lb ~ agepreg + C(race) + babysex==1 + '
               'nbrnaliv>1 + paydu==1 + totincr')
    results = smf.ols(formula, data=join).fit()
    SummarizeResults(results)
    #print(results.summary())


def SummarizeResults(results):
    """Prints the most important parts of linear regression results:

    results: RegressionResults object
    """
    for name, param in results.params.iteritems():
        pvalue = results.pvalues[name]
        print('%s   %0.3g   (%.3g)' % (name, param, pvalue))

    try:
        print('R^2 %.4g' % results.rsquared)
        ys = results.model.endog
        print('Std(ys) %.4g' % ys.std())
        print('Std(res) %.4g' % results.resid.std())
    except AttributeError:
        print('R^2 %.4g' % results.prsquared)


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

    SummarizeResults(results)

    def AlmostEquals(x, y, tol=1e-6):
        return abs(x-y) < tol

    assert(AlmostEquals(results.params['Intercept'], inter))
    assert(AlmostEquals(results.params['agepreg'], slope))
    assert(AlmostEquals(results.rsquared, r2))


def PivotTables(live):
    table = pandas.pivot_table(live, rows='isfirst',
                               values=['totalwgt_lb', 'agepreg'])
    print(table)


def FormatRow(results, columns):
    """Converts regression results to a string.

    results: RegressionResults object

    returns: string
    """
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

    try:
        t.append('%.2g' % results.rsquared)
    except AttributeError:
        t.append('%.2g' % results.prsquared)
        
    return t


def RunModels(live):
    """Runs regressions that predict birth weight.

    live: DataFrame of pregnancy records
    """
    live['isfirst'] = live.birthord == 1

    columns = ['isfirst[T.True]', 'agepreg', 'agepreg2']
    header = ['isfirst', 'agepreg', 'agepreg2']

    rows = []
    formula = 'totalwgt_lb ~ isfirst'
    results = smf.ols(formula, data=live).fit()
    rows.append(FormatRow(results, columns))
    print(formula)
    SummarizeResults(results)

    formula = 'totalwgt_lb ~ agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(FormatRow(results, columns))
    print(formula)
    SummarizeResults(results)
    
    formula = 'totalwgt_lb ~ isfirst + agepreg'
    results = smf.ols(formula, data=live).fit()
    rows.append(FormatRow(results, columns))
    print(formula)
    SummarizeResults(results)
    
    live['agepreg2'] = live.agepreg**2
    formula = 'totalwgt_lb ~ isfirst + agepreg + agepreg2'
    results = smf.ols(formula, data=live).fit()
    rows.append(FormatRow(results, columns))
    print(formula)
    SummarizeResults(results)
    
    PrintTabular(rows, header)


def PrintTabular(rows, header):
    """Prints results in LaTeX tabular format.

    rows: list of rows
    header: list of strings
    """
    s = r'\hline ' + ' & '.join(header) + r' \\ \hline'
    print(s)

    for row in rows:
        s = ' & '.join(row) + r' \\'
        print(s)

    print(r'\hline')


def LogisticRegressionExample():
    """Runs a simple example of logistic regression and prints results.
    """
    y = np.array([0, 1, 0, 1, 1])
    x1 = np.array([0, 0, 1, 1, 0])
    x2 = np.array([0, 1, 1, 1, 1])

    beta = [-1.5, 1.3, 1.8]

    log_o = beta[0] + beta[1] * x1 + beta[2] * x2 
    print(log_o)

    o = np.exp(log_o)
    print(o)

    p = o / (o+1)
    print(p)

    like = y * p + (1-y) * (1-p)
    print(like)
    print(np.prod(like))

    df = pandas.DataFrame(dict(y=y, x1=x1, x2=x2))
    results = smf.logit('y ~ x1', data=df).fit()
    print(results.summary())


def RunLogisticModels(live):
    """Runs regressions that predict sex.

    live: DataFrame of pregnancy records
    """
    #live = linear.ResampleRowsWeighted(live)

    df = live[live.prglngth>30]
    # df = JoinFemResp(df)

    df['boy'] = (df.babysex==1).astype(int)
    df['isyoung'] = (df.agepreg<20).astype(int)
    df['isold'] = (df.agepreg<35).astype(int)

    model = smf.logit('boy ~ agepreg', data=df)
    results = model.fit()
    print(type(results))
    SummarizeResults(results)

    model = smf.logit('boy ~ isold + isyoung', data=df)
    results = model.fit()
    SummarizeResults(results)


def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    #LogisticRegressionExample()

    live, firsts, others = first.MakeFrames()

    RunLogisticModels(live)
    return

    RunSimpleRegression(live)
    RunModels(live)
    return

    PredictBirthWeight(live)
    return

    JoinRespFile(live)
    return



if __name__ == '__main__':
    import sys
    main(*sys.argv)
