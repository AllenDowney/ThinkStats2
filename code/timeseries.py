"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import pandas
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as smtsa

import matplotlib.pyplot as pyplot

import thinkplot
import thinkstats2

FORMATS = ['png']

def ReadData():
    """Reads data about cannabis transactions.

    http://zmjones.com/static/data/mj-clean.csv

    returns: DataFrame
    """
    transactions = pandas.read_csv('mj-clean.csv', parse_dates=[5])
    return transactions


def tmean(series):
    """Computes a trimmed mean.

    series: Series 

    returns: float
    """
    t = series.values
    n = len(t)
    if n <= 3:
        return t.mean()
    trim = max(1, n/10)
    return np.mean(sorted(t)[trim:n-trim])


def GroupByDay(transactions, func=np.mean):
    """Groups transactions by day and compute the daily mean ppg.

    transactions: DataFrame of transactions

    returns: DataFrame of daily prices
    """
    groups = transactions[['date', 'ppg']].groupby('date')
    daily = groups.aggregate(func)

    daily['date'] = daily.index
    start = daily.date[0]
    one_year = np.timedelta64(1, 'Y')
    daily['years'] = (daily.date - start) / one_year

    return daily


def GroupByQualityAndDay(transactions):
    """Divides transactions by quality and computes mean daily price.

    transaction: DataFrame of transactions
    
    returns: map from quality to time series of ppg
    """
    groups = transactions.groupby('quality')
    dailies = {}
    for name, group in groups:
        dailies[name] = GroupByDay(group)        

    return dailies


def PlotDailies(dailies):
    """Makes a plot with daily prices for different qualities.

    dailies: map from name to DataFrame
    """
    thinkplot.PrePlot(rows=3)
    for i, (name, daily) in enumerate(dailies.items()):
        thinkplot.SubPlot(i+1)
        title = 'price per gram ($)' if i == 0 else ''
        thinkplot.Config(ylim=[0, 20], title=title)
        thinkplot.Scatter(daily.ppg, s=10, label=name)
        if i == 2: 
            pyplot.xticks(rotation=30)
        else:
            thinkplot.Config(xticks=[])

    thinkplot.Save(root='timeseries1',
                   formats=FORMATS)


def RunLinearModel(daily):
    """Runs a linear model of prices versus years.

    daily: DataFrame of daily prices

    returns: model, results
    """
    model = smf.ols('ppg ~ years', data=daily)
    results = model.fit()
    return model, results


def PlotFittedValues(model, results, label=''):
    """Plots original data and fitted values.

    model: StatsModel model object
    results: StatsModel results object
    """
    years = model.exog[:, 1]
    values = model.endog
    thinkplot.Scatter(years, values, s=15, label=label)
    thinkplot.Plot(years, results.fittedvalues, label='model')


def PlotResiduals(model, results):
    """Plots the residuals of a model.

    model: StatsModel model object
    results: StatsModel results object    
    """
    years = model.exog[:, 1]
    thinkplot.Plot(years, results.resid, linewidth=0.5, alpha=0.5)


def PlotResidualPercentiles(model, results, index=1, num_bins=20):
    """Plots percentiles of the residuals.

    model: StatsModel model object
    results: StatsModel results object
    index: which exogenous variable to use
    num_bins: how many bins to divide the x-axis into
    """
    exog = model.exog[:, index]
    resid = results.resid.values
    df = pandas.DataFrame(dict(exog=exog, resid=resid))

    bins = np.linspace(np.min(exog), np.max(exog), num_bins)
    indices = np.digitize(exog, bins)
    groups = df.groupby(indices)

    means = [group.exog.mean() for _, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.resid) for _, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        percentiles = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(means, percentiles, label=label)


def SimulateResults(daily, iters=101, func=RunLinearModel):
    """Run simulations based on resampling residuals.

    daily: DataFrame of daily prices
    iters: number of simulations
    func: function that fits a model to the data

    returns: list of result objects
    """
    _, results = func(daily)
    fake = daily.copy()
    
    result_seq = []
    for _ in range(iters):
        fake.ppg = results.fittedvalues + thinkstats2.Resample(results.resid)
        _, fake_results = func(fake)
        result_seq.append(fake_results)

    return result_seq


def SimulateIntervals(daily, iters=101, func=RunLinearModel):
    """Run simulations based on different subsets of the data.

    daily: DataFrame of daily prices
    iters: number of simulations
    func: function that fits a model to the data

    returns: list of result objects
    """
    result_seq = []
    starts = np.linspace(0, len(daily), iters).astype(int)

    for start in starts[:-2]:
        subset = daily[start:]
        _, results = func(subset)
        fake = subset.copy()

        for _ in range(iters):
            fake.ppg = (results.fittedvalues + 
                        thinkstats2.Resample(results.resid))
            _, fake_results = func(fake)
            result_seq.append(fake_results)

    return result_seq


def GeneratePredictions(result_seq, years, add_resid=False):
    """Generates an array of predicted values from a list of model results.

    When add_resid is False, predictions represent sampling error only.

    When add_resid is True, they also include residual error (which is
    more relevant to prediction).
    
    result_seq: list of model results
    years: sequence of times (in years) to make predictions for
    add_resid: boolean, whether to add in resampled residuals

    returns: sequence of predictions
    """
    n = len(years)
    d = dict(Intercept=np.ones(n), years=years, years2=years**2)
    predict_df = pandas.DataFrame(d)
    
    predict_seq = []
    for fake_results in result_seq:
        predict = fake_results.predict(predict_df)
        if add_resid:
            predict += thinkstats2.Resample(fake_results.resid, n)
        predict_seq.append(predict)

    return predict_seq


def GenerateSimplePrediction(results, years):
    """Generates a simple prediction.

    results: results object
    years: sequence of times (in years) to make predictions for

    returns: sequence of predicted values
    """
    n = len(years)
    inter = np.ones(n)
    d = dict(Intercept=inter, years=years, years2=years**2)
    predict_df = pandas.DataFrame(d)
    predict = results.predict(predict_df)
    return predict


def PlotPredictions(daily, years, iters=101, percent=90, func=RunLinearModel):
    """Plots predictions.

    daily: DataFrame of daily prices
    years: sequence of times (in years) to make predictions for
    iters: number of simulations
    percent: what percentile range to show
    func: function that fits a model to the data
    """
    result_seq = SimulateResults(daily, iters=iters, func=func)
    p = (100 - percent) / 2
    percents = p, 100-p

    predict_seq = GeneratePredictions(result_seq, years, add_resid=True)
    low, high = thinkstats2.PercentileRows(predict_seq, percents)
    thinkplot.FillBetween(years, low, high, alpha=0.3, color='gray')

    predict_seq = GeneratePredictions(result_seq, years, add_resid=False)
    low, high = thinkstats2.PercentileRows(predict_seq, percents)
    thinkplot.FillBetween(years, low, high, alpha=0.5, color='gray')


def PlotIntervals(daily, years, iters=101, percent=90, func=RunLinearModel):
    """Plots predictions based on different intervals.

    daily: DataFrame of daily prices
    years: sequence of times (in years) to make predictions for
    iters: number of simulations
    percent: what percentile range to show
    func: function that fits a model to the data
    """
    result_seq = SimulateIntervals(daily, iters=iters, func=func)
    p = (100 - percent) / 2
    percents = p, 100-p

    predict_seq = GeneratePredictions(result_seq, years, add_resid=True)
    low, high = thinkstats2.PercentileRows(predict_seq, percents)
    thinkplot.FillBetween(years, low, high, alpha=0.2, color='gray')


def Correlate(dailies):
    """Compute the correlation matrix between prices for difference qualities.

    dailies: map from quality to time series of ppg

    returns: correlation matrix
    """
    df = pandas.DataFrame()
    for name, daily in dailies.items():
        df[name] = daily.ppg

    return df.corr()
        

def CorrelateResid(dailies):
    """Compute the correlation matrix between residuals.

    dailies: map from quality to time series of ppg

    returns: correlation matrix
    """
    df = pandas.DataFrame()
    for name, daily in dailies.items():
        _, results = RunLinearModel(daily)
        df[name] = results.resid

    return df.corr()


def TestCorrelateResid(dailies, iters=101):
    """Tests observed correlations.

    dailies: map from quality to time series of ppg
    iters: number of simulations
    """

    t = []
    names = ['high', 'medium', 'low']
    for name in names:
        daily = dailies[name]
        t.append(SimulateResults(daily, iters=iters))

    corr = CorrelateResid(dailies)

    arrays = []
    for result_seq in zip(*t):
        df = pandas.DataFrame()
        for name, results in zip(names, result_seq):
            df[name] = results.resid

        opp_sign = corr * df.corr() < 0
        arrays.append((opp_sign.astype(int)))

    print(np.sum(arrays))


def RunModels(dailies):
    """Runs linear regression for each group in dailies.

    dailies: map from group name to DataFrame
    """
    rows = []
    for daily in dailies.values():
        _, results = RunLinearModel(daily)
        intercept, slope = results.params
        p1, p2 = results.pvalues
        r2 = results.rsquared
        s = r'%0.3f (%0.2g) & %0.3f (%0.2g) & %0.3f \\'
        row = s % (intercept, p1, slope, p2, r2)
        rows.append(row)

    # print results in a LaTeX table
    print(r'\begin{tabular}{|c|c|c|}')
    print(r'\hline')
    print(r'intercept & slope & $R^2$ \\ \hline')
    for row in rows:
        print(row)
    print(r'\hline')
    print(r'\end{tabular}')


def FillMissing(daily, span=30):
    """Fills missing values with an exponentially weighted moving average.

    Resulting DataFrame has new columns 'ewma' and 'resid'.

    daily: DataFrame of daily prices
    span: window size (sort of) passed to ewma

    returns: new DataFrame of daily prices
    """
    dates = pandas.date_range(daily.index.min(), daily.index.max())
    reindexed = daily.reindex(dates)

    ewma = pandas.ewma(reindexed.ppg, span=span)

    resid = (reindexed.ppg - ewma).dropna()
    fake_data = ewma + thinkstats2.Resample(resid, len(reindexed))
    reindexed.ppg.fillna(fake_data, inplace=True)

    reindexed['ewma'] = ewma
    reindexed['resid'] = reindexed.ppg - ewma
    return reindexed


def AddWeeklySeasonality(daily):
    """Adds a weekly pattern.

    daily: DataFrame of daily prices

    returns: new DataFrame of daily prices
    """
    frisat = (daily.index.dayofweek==4) | (daily.index.dayofweek==5)
    fake = daily.copy()
    fake.ppg[frisat] += np.random.uniform(0, 2, frisat.sum())
    return fake


def PrintSerialCorrelations(dailies):
    """Prints a table of correlations with different lags.

    dailies: map from category name to DataFrame of daily prices
    """
    filled_dailies = {}
    for name, daily in dailies.items():
        filled_dailies[name] = FillMissing(daily, span=30)

    # print serial correlations for raw price data
    for name, filled in filled_dailies.items():            
        corr = thinkstats2.SerialCorr(filled.ppg, lag=1)
        print(name, corr)

    rows = []
    for lag in [1, 7, 30, 365]:
        row = [str(lag)]
        for name, filled in filled_dailies.items():            
            corr = thinkstats2.SerialCorr(filled.resid, lag)
            row.append('%.2g' % corr)
        rows.append(row)

    print(r'\begin{tabular}{|c|c|c|c|}')
    print(r'\hline')
    print(r'lag & high & medium & low \\ \hline')
    for row in rows:
        print(' & '.join(row) + r' \\')
    print(r'\hline')
    print(r'\end{tabular}')

    filled = filled_dailies['high']
    acf = smtsa.acf(filled.resid, nlags=365, unbiased=True)
    print('%0.3f, %0.3f, %0.3f, %0.3f, %0.3f' % 
          (acf[0], acf[1], acf[7], acf[30], acf[365]))


def SimulateAutocorrelation(daily, iters=1001, nlags=40):
    """Resample residuals, compute autocorrelation, and plot percentiles.

    daily: DataFrame
    iters: number of simulations to run
    nlags: maximum lags to compute autocorrelation
    """
    # run simulations
    t = []
    for _ in range(iters):
        filled = FillMissing(daily, span=30)
        resid = thinkstats2.Resample(filled.resid)
        acf = smtsa.acf(resid, nlags=nlags, unbiased=True)[1:]
        t.append(np.abs(acf))

    high = thinkstats2.PercentileRows(t, [97.5])[0]
    low = -high
    lags = range(1, nlags+1)
    thinkplot.FillBetween(lags, low, high, alpha=0.2, color='gray')


def PlotAutoCorrelation(dailies, nlags=40, add_weekly=False):
    """Plots autocorrelation functions.

    dailies: map from category name to DataFrame of daily prices
    nlags: number of lags to compute
    add_weekly: boolean, whether to add a simulated weekly pattern
    """
    thinkplot.PrePlot(3)
    daily = dailies['high']
    SimulateAutocorrelation(daily)

    for name, daily in dailies.items():

        if add_weekly:
            daily = AddWeeklySeasonality(daily)

        filled = FillMissing(daily, span=30)

        acf = smtsa.acf(filled.resid, nlags=nlags, unbiased=True)
        lags = np.arange(len(acf))
        thinkplot.Plot(lags[1:], acf[1:], label=name)


def MakeAcfPlot(dailies):
    """Makes a figure showing autocorrelation functions.

    dailies: map from category name to DataFrame of daily prices    
    """
    axis = [0, 41, -0.2, 0.2]

    thinkplot.PrePlot(cols=2)
    PlotAutoCorrelation(dailies, add_weekly=False)
    thinkplot.Config(axis=axis, 
                     loc='lower right',
                     ylabel='correlation',
                     xlabel='lag (day)')

    thinkplot.SubPlot(2)
    PlotAutoCorrelation(dailies, add_weekly=True)
    thinkplot.Save(root='timeseries9',
                   axis=axis,
                   loc='lower right',
                   xlabel='lag (days)',
                   formats=FORMATS)


def PlotRollingMean(daily, name):
    """Plots rolling mean and EWMA.

    daily: DataFrame of daily prices
    """
    dates = pandas.date_range(daily.index.min(), daily.index.max())
    reindexed = daily.reindex(dates)

    thinkplot.PrePlot(cols=2)
    thinkplot.Scatter(reindexed.ppg, s=15, alpha=0.1, label=name)
    roll_mean = pandas.rolling_mean(reindexed.ppg, 30)
    thinkplot.Plot(roll_mean, label='rolling mean')
    pyplot.xticks(rotation=30)
    thinkplot.Config(ylabel='price per gram ($)')

    thinkplot.SubPlot(2)
    thinkplot.Scatter(reindexed.ppg, s=15, alpha=0.1, label=name)
    ewma = pandas.ewma(reindexed.ppg, span=30)
    thinkplot.Plot(ewma, label='EWMA')
    pyplot.xticks(rotation=30)
    thinkplot.Save(root='timeseries10',
                   formats=FORMATS)


def PlotFilled(daily, name):
    """Plots the EWMA and filled data.

    daily: DataFrame of daily prices
    """
    filled = FillMissing(daily, span=30)
    thinkplot.Scatter(filled.ppg, s=15, alpha=0.3, label=name)
    thinkplot.Plot(filled.ewma, label='EWMA', alpha=0.4)
    pyplot.xticks(rotation=30)
    thinkplot.Save(root='timeseries8',
                   ylabel='price per gram ($)',
                   formats=FORMATS)
    

def PlotLinearModel(daily, name):
    """Plots a linear fit to a sequence of prices, and the residuals.
    
    daily: DataFrame of daily prices
    name: string
    """
    model, results = RunLinearModel(daily)
    PlotFittedValues(model, results, label=name)
    thinkplot.Save(root='timeseries2',
                   title='fitted values',
                   xlabel='years',
                   xlim=[-0.1, 3.8],
                   ylabel='price per gram ($)',
                   formats=FORMATS)

    PlotResidualPercentiles(model, results)
    thinkplot.Save(root='timeseries3',
                   title='residuals',
                   xlabel='years',
                   ylabel='price per gram ($)',
                   formats=FORMATS)
    
    #years = np.linspace(0, 5, 101)
    #predict = GenerateSimplePrediction(results, years)


def main(name):
    thinkstats2.RandomSeed(18)
    transactions = ReadData()

    dailies = GroupByQualityAndDay(transactions)
    PlotDailies(dailies)
    RunModels(dailies)
    PrintSerialCorrelations(dailies)
    MakeAcfPlot(dailies)

    name = 'high'
    daily = dailies[name]

    PlotLinearModel(daily, name)
    PlotRollingMean(daily, name)
    PlotFilled(daily, name)

    years = np.linspace(0, 5, 101)
    thinkplot.Scatter(daily.years, daily.ppg, alpha=0.1, label=name)
    PlotPredictions(daily, years)
    xlim = years[0]-0.1, years[-1]+0.1
    thinkplot.Save(root='timeseries4',
                   title='predictions',
                   xlabel='years',
                   xlim=xlim,
                   ylabel='price per gram ($)',
                   formats=FORMATS)

    name = 'medium'
    daily = dailies[name]

    thinkplot.Scatter(daily.years, daily.ppg, alpha=0.1, label=name)
    PlotIntervals(daily, years)
    PlotPredictions(daily, years)
    xlim = years[0]-0.1, years[-1]+0.1
    thinkplot.Save(root='timeseries5',
                   title='predictions',
                   xlabel='years',
                   xlim=xlim,
                   ylabel='price per gram ($)',
                   formats=FORMATS)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
