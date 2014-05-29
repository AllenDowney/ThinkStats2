"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import csv
import logging
import sys
import numpy as np
import pandas

import thinkplot
import thinkstats2


def Clean(s):
    """Converts dollar amounts to integers."""
    try:
        return int(s.lstrip('$').replace(',', ''))
    except ValueError:
        if s == 'Under':
            return 0
        elif s == 'over':
            return np.inf
        return None


class SpecialCdf(thinkstats2.Cdf):
    """Special version of a CDF that's rendered differently.
    """
    def Render(self):
        """Because this CDF was not computed from a sample, it
        should not be rendered as a step function.
        """
        return self.xs, self.ps


def ReadData(filename='hinc06.csv'):
    """Reads filename and returns populations in thousands

    filename: string

    returns: pandas Series of populations in thousands
    """
    data = pandas.read_csv(filename, header=None, skiprows=9)
    cols = data[[0, 1]]
        
    res = []
    for i, row in cols.iterrows():
        label, count = row.values
        count = int(count.replace(',', ''))

        t = label.split()
        low, high = Clean(t[0]), Clean(t[-1])

        res.append((high, count))

    df = pandas.DataFrame(res)
    # correct the first range
    df[0][0] -= 1
    # compute the cumulative sum of the counts
    df[2] = df[1].cumsum()
    # normalize the cumulative counts
    total = df[2][41]
    df[3] = df[2] / total
    # add column names
    df.columns = ['income',  'count', 'total count', 'ps']
    return df


def MakeFigures():
    """Plots the CDF of populations in several forms.

    On a log-log scale the tail of the CCDF looks like a straight line,
    which suggests a Pareto distribution, but that turns out to be misleading.

    On a log-x scale the distribution has the characteristic sigmoid of
    a lognormal distribution.

    The normal probability plot of log(sizes) confirms that the data fit the
    lognormal model very well.

    Many phenomena that have been described with Pareto models can be described
    as well, or better, with lognormal models.
    """
    df = ReadData()
    print(df)

    cdf = SpecialCdf(df.income.values, df.ps.values,
                     label='household income')

    cdf_log = SpecialCdf(np.log10(df.income.values), df.ps.values,
                         label='household income')
    
    # pareto plot
    xs, ys = thinkstats2.RenderParetoCdf(xmin=55000, alpha=2.5, 
                                         low=0, high=250000)
    thinkplot.Plot(xs, 1-ys, label='model', color='0.8')

    thinkplot.Cdf(cdf, complement=True) 
    thinkplot.Config(xlabel='log10 population',
                     ylabel='CCDF',
                     xscale='log',
                     yscale='log')
    thinkplot.Save(root='hinc_pareto')

    # lognormal plot
    median = cdf_log.Percentile(50)
    iqr = cdf_log.Percentile(75) - cdf_log.Percentile(25)
    std = iqr / 1.349
    print(median, std)

    xs, ps = thinkstats2.RenderGaussianCdf(median, std, low=3.5, high=5.5)
    thinkplot.Plot(xs, ps, label='model', color='0.8')

    thinkplot.Cdf(cdf_log) 
    thinkplot.Config(xlabel='log10 population',
                     ylabel='CDF')

    thinkplot.Save(root='hinc_normal')
    

def main():
    thinkstats2.RandomSeed(17)
    MakeFigures()


if __name__ == "__main__":
    main()
