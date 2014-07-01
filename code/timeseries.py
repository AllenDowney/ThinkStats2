"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import pandas
import datetime
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as smtsa

import matplotlib.pyplot as pyplot

import thinkplot
import thinkstats2
import regression

import warnings

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


def GroupByDay(transactions):
    """Groups transactions by day and compute the daily mean ppg.

    transactions: DataFrame of transactions

    returns: DataFrame of daily prices
    """
    #warnings.filterwarnings("error")

    grouped = transactions[['date', 'ppg']].groupby('date')
    daily = grouped.aggregate(tmean)
    #daily = grouped.aggregate(np.mean)

    dates = pandas.date_range(daily.index.min(), daily.index.max())
    daily = daily.reindex(dates)

    daily['date'] = daily.index
    start = daily.date[0]
    one_day = np.timedelta64(1, 'D')
    daily['days'] = ((daily.date - start) / one_day).astype(int)

    return daily


def PlotDailies(dailies):
    """Makes a plot with daily prices for different qualities.

    dailies: map from name to DataFrame
    """
    thinkplot.PrePlot(rows=3)

    i = 1
    for name, daily in dailies.items():
        thinkplot.SubPlot(i)
        thinkplot.Plot(daily.index, daily.ppg,
                       linewidth=0.5, alpha=0.5, label=name)
        thinkplot.Config(ylim=[0, 20])

        if i == 3: 
            pyplot.xticks(rotation=30)
        else:
            thinkplot.Config(xticks=[])
        i += 1

    thinkplot.Save(root='timeseries1',
                   title='price per gram ($)')


def RunLinearModel(daily):
    """Runs a linear model of prices versus years.

    daily: DataFrame of daily prices

    returns: model, results
    """
    daily['years'] = daily.days / 365.0
    model = smf.ols('ppg ~ years', data=daily)
    results = model.fit()
    return model, results


def PlotFittedValues(model, results, label=''):
    """Plots original data and fitted values.

    model: StatsModel model object
    results: StatsModel results object
    """
    years = model.exog[:,1]
    values = model.endog
    thinkplot.Plot(years, values, linewidth=0.5, alpha=0.5, label=label)
    thinkplot.Plot(years, results.fittedvalues, color='white')
    thinkplot.Plot(years, results.fittedvalues, linewidth=2)


def PlotResiduals(model, results):
    years = model.exog[:,1]
    thinkplot.Plot(years, results.resid, linewidth=0.5, alpha=0.5)


def PlotResidualPercentiles(model, results, index=1, num_bins=20):
    """Plots percentiles of the residuals.

    model: StatsModel model object
    results: StatsModel results object
    index: which exogenous variable to use
    num_bins: how many bins to divide the x-axis into
    """
    exog = model.exog[:,index]
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


def GroupByDayOfWeek(transactions):
    grouped = transactions[['dayofweek', 'ppg']].groupby('dayofweek')
    cdfs = grouped.aggregate(thinkstats2.Cdf)
    thinkplot.Cdfs(cdfs.ppg)




def Get2001(ppg):
    year11 = ppg[121:121+365]
    year11
    year11.date[121], year11.date[121+364]


def PlotRollingMean():
    thinkplot.Plot(year11.index, year11.ppg)
    roll_mean = pandas.rolling_mean(year11.ppg, 30, center=True)
    thinkplot.Plot(year11.index, roll_mean, color='yellow')
    year11.date[250], year11.date[350], year11.date[430]


def PlotWindows():
    """Makes a plot showing the shapes of windows for rolling means.

    """
    import scipy.signal as sig
    gaussian = sig.get_window(('gaussian', 7.5), 30)
    gaussian_mean = gaussian.mean()
    gaussian /= gaussian.mean()
    thinkplot.Plot(gaussian)

    boxcar = sig.get_window('boxcar', 30)
    boxcar_mean = boxcar.mean()
    boxcar /= boxcar.mean()
    thinkplot.Plot(boxcar)

    triangle = sig.get_window('triangle', 30)
    triangle_mean = triangle.mean()
    triangle /= triangle.mean()
    thinkplot.Plot(triangle)


def PlotTriangle():
    thinkplot.Plot(year11.index, year11.ppg)
    roll_mean = pandas.rolling_window(year11.ppg, 30, 'triang', center=True)
    roll_mean /= triangle_mean
    thinkplot.Plot(year11.index, roll_mean, color='yellow')
    year11.date[250], year11.date[350], year11.date[430]


def PlotGaussian():
    thinkplot.Plot(year11.index, year11.ppg)
    roll_mean = pandas.rolling_window(year11.ppg, 30, 'gaussian', std=7.5, center=True)
    roll_mean /= gaussian_mean
    thinkplot.Plot(year11.index, roll_mean, color='yellow')
    year11.date[250], year11.date[350], year11.date[430]


def Autocorrelation():
    from pandas.tools.plotting import autocorrelation_plot
    autocorrelation_plot(daily.ppg.diff().dropna())


def CompareStates():
    high = transactions[transactions.quality=='high']
    ca_high = high[high.state=='CA']
    thinkplot.Scatter(ca_high.days, ca_high.ppg, alpha=0.05)
    ma_high = high[high.state=='MA']
    thinkplot.Scatter(ma_high.days, ma_high.ppg, alpha=0.05, color='red')



def main(name, data_dir='.'):
    transactions = ReadData()

    grouped = transactions.groupby('quality')

    dailies = {}
    for name, group in grouped:
        dailies[name] = GroupByDay(group)        

    PlotDailies(dailies)

    for name, daily in dailies.items():
        model, results = RunLinearModel(daily)

        print(name)
        regression.SummarizeResults(results)
        
        if name == 'high':
            PlotFittedValues(model, results, label=name)
            thinkplot.Save(root='timeseries2',
                           title='fitted values',
                           xlabel='years',
                           ylabel='price per gram ($)')

            PlotResidualPercentiles(model, results)
            thinkplot.Save(root='timeseries3',
                           title='residuals',
                           xlabel='years',
                           ylabel='price per gram ($)')


if __name__ == '__main__':
    import sys
    main(*sys.argv)
