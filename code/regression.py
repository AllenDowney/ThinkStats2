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

import chap01soln
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
    resp = chap01soln.ReadFemResp()
    resp.index = resp.caseid

    join = df.join(resp, on='caseid', rsuffix='_r')

    # convert from colon-separated time strings to datetimes
    join.screentime = pandas.to_datetime(join.screentime)

    return join


def GoMining(df):
    """Searches for variables that predict birth weight.

    df: DataFrame of pregnancy records

    returns: list of (rsquared, variable name) pairs
    """
    variables = []
    for name in df.columns:
        try:
            if df[name].var() < 1e-7:
                continue

            formula=('totalwgt_lb ~ agepreg + ' + name).encode('ascii')  # encode needed to avoid 'PatsyError: model is missing required outcome variables', per https://readditing.com/r/pystats/comments/2cn0go
            model = smf.ols(formula, data=df)
            if model.nobs < len(df)/2:
                continue

            results = model.fit()
        except (ValueError, TypeError):
            continue

        variables.append((results.rsquared, name))

    return variables


def MiningReport(variables, n=30):
    """Prints variables with the highest R^2.

    t: list of (R^2, variable name) pairs
    n: number of pairs to print
    """
    all_vars = ReadVariables()

    variables.sort(reverse=True)
    for mse, name in variables[:n]:
        key = re.sub('_r$', '', name)
        try:
            desc = all_vars.loc[key].desc
            if isinstance(desc, pandas.Series):
                desc = desc[0]
            print(name, mse, desc)
        except KeyError:
            print(name, mse)


def PredictBirthWeight(live):
    """Predicts birth weight of a baby at 30 weeks.

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
    """Runs a simple regression and compare results to thinkstats2 functions.

    live: DataFrame of live births
    """
    # run the regression with thinkstats2 functions
    live_dropna = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    ages = live_dropna.agepreg
    weights = live_dropna.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    # run the regression with statsmodels
    formula = 'totalwgt_lb ~ agepreg'
    model = smf.ols(formula, data=live)
    results = model.fit()
    SummarizeResults(results)

    def AlmostEquals(x, y, tol=1e-6):
        return abs(x-y) < tol

    assert(AlmostEquals(results.params['Intercept'], inter))
    assert(AlmostEquals(results.params['agepreg'], slope))
    assert(AlmostEquals(results.rsquared, r2))


def PivotTables(live):
    """Prints a pivot table comparing first babies to others.

    live: DataFrame of live births
    """
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
    y = np.array([0, 1, 0, 1])
    x1 = np.array([0, 0, 0, 1])
    x2 = np.array([0, 1, 1, 1])

    beta = [-1.5, 2.8, 1.1]

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
    results = smf.logit('y ~ x1 + x2', data=df).fit()
    print(results.summary())

    

def RunLogisticModels(live):
    """Runs regressions that predict sex.

    live: DataFrame of pregnancy records
    """
    #live = linear.ResampleRowsWeighted(live)

    df = live[live.prglngth>30]

    df['boy'] = (df.babysex==1).astype(int)
    df['isyoung'] = (df.agepreg<20).astype(int)
    df['isold'] = (df.agepreg<35).astype(int)
    df['season'] = (((df.datend+1) % 12) / 3).astype(int)

    # run the simple model
    model = smf.logit('boy ~ agepreg', data=df)    
    results = model.fit()
    print('nobs', results.nobs)
    print(type(results))
    SummarizeResults(results)

    # run the complex model
    model = smf.logit('boy ~ agepreg + hpagelb + birthord + C(race)', data=df)
    results = model.fit()
    print('nobs', results.nobs)
    print(type(results))
    SummarizeResults(results)

    # make the scatter plot
    exog = pandas.DataFrame(model.exog, columns=model.exog_names)
    endog = pandas.DataFrame(model.endog, columns=[model.endog_names])
    
    xs = exog['agepreg']
    lo = results.fittedvalues
    o = np.exp(lo)
    p = o / (o+1)

    #thinkplot.Scatter(xs, p, alpha=0.1)
    #thinkplot.Show()

    # compute accuracy
    actual = endog['boy']
    baseline = actual.mean()

    predict = (results.predict() >= 0.5)
    true_pos = predict * actual
    true_neg = (1 - predict) * (1 - actual)

    acc = (sum(true_pos) + sum(true_neg)) / len(actual)
    print(acc, baseline)

    columns = ['agepreg', 'hpagelb', 'birthord', 'race']
    new = pandas.DataFrame([[35, 39, 3, 1]], columns=columns)
    y = results.predict(new)
    print(y)


def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    #LogisticRegressionExample()

    live, firsts, others = first.MakeFrames()
    live['isfirst'] = (live.birthord == 1)

    RunLogisticModels(live)
    return

    RunSimpleRegression(live)
    RunModels(live)

    PredictBirthWeight(live)



if __name__ == '__main__':
    import sys
    main(*sys.argv)
