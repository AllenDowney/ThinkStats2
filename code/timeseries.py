"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import pandas
import thinkplot
import thinkstats2
import datetime
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as smtsa

import matplotlib.pyplot as pyplot

def ReadData(filename='mj-clean.csv'):
    df = pandas.read_csv(filename, parse_dates=[5])
    return df


def GroupByDay(df):
    grouped = df[['date', 'ppg']].groupby('date')
    series = grouped.aggregate(np.mean)

    dates = pandas.date_range(series.index.min(), series.index.max())
    series = series.reindex(dates)

    series['date'] = series.index
    start = series.date[0]
    one_day = np.timedelta64(1, 'D')
    series['days'] = ((series.date - start) / one_day).astype(int)

    return series


def PlotSeries(series_map):

    thinkplot.PrePlot(rows=3)

    i = 1
    for name, series in series_map.items():
        thinkplot.SubPlot(i)
        thinkplot.Plot(series.index, series.ppg,
                       linewidth=0.5, alpha=0.5, label=name)
        thinkplot.Config(ylim=[0, 20])

        if i == 3: 
            pyplot.xticks(rotation=30)
        else:
            thinkplot.Config(xticks=[])
        i += 1

    thinkplot.Save(root='timeseries1',
                   title='price per gram ($)')


def RunLinearModel(series):
    series['years'] = series.days / 365.0
    model = smf.ols('ppg ~ years', data=series)
    results = model.fit()
    # print(results.summary())
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


def GroupByDayOfWeek(df):
    grouped = df[['dayofweek', 'ppg']].groupby('dayofweek')
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
    autocorrelation_plot(series.ppg.diff().dropna())


def CompareStates():
    high = df[df.quality=='high']
    ca_high = high[high.state=='CA']
    thinkplot.Scatter(ca_high.days, ca_high.ppg, alpha=0.05)
    ma_high = high[high.state=='MA']
    thinkplot.Scatter(ma_high.days, ma_high.ppg, alpha=0.05, color='red')



def main(name, data_dir='.'):
    df = ReadData()

    series = GroupByDay(df)

    grouped = df.groupby('quality')
    #qs = grouped.aggregate(GroupByDay)
    #print(qs)

    series_map = {}
    for name, group in grouped:
        series_map[name] = GroupByDay(group)        
    PlotSeries(series_map)

    for name, series in series_map.items():
        model, results = RunLinearModel(series)
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
