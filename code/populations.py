"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
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


def ReadData(filename='PEP_2012_PEPANNRES_with_ann.csv'):
    """Reads filename and returns populations in thousands

    filename: string

    returns: pandas Series of populations in thousands
    """
    df = pandas.read_csv(filename, header=None, skiprows=2,
                         encoding='iso-8859-1')
    populations = df[7]
    populations.replace(0, np.nan, inplace=True)
    return populations.dropna()


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
    pops = ReadData()
    print('Number of cities/towns', len(pops))
    
    log_pops = np.log10(pops)
    cdf = thinkstats2.Cdf(pops, label='data')
    cdf_log = thinkstats2.Cdf(log_pops, label='data')

    # pareto plot
    xs, ys = thinkstats2.RenderParetoCdf(xmin=5000, alpha=1.4, low=0, high=1e7)
    thinkplot.Plot(np.log10(xs), 1-ys, label='model', color='0.8')

    thinkplot.Cdf(cdf_log, complement=True) 
    thinkplot.Config(xlabel='log10 population',
                     ylabel='CCDF',
                     yscale='log')
    thinkplot.Save(root='populations_pareto')

    # lognormal plot
    thinkplot.PrePlot(cols=2)

    mu, sigma = log_pops.mean(), log_pops.std()
    xs, ps = thinkstats2.RenderNormalCdf(mu, sigma, low=0, high=8)
    thinkplot.Plot(xs, ps, label='model', color='0.8')

    thinkplot.Cdf(cdf_log) 
    thinkplot.Config(xlabel='log10 population',
                     ylabel='CDF')

    thinkplot.SubPlot(2)
    thinkstats2.NormalProbabilityPlot(log_pops, label='data')
    thinkplot.Config(xlabel='z',
                     ylabel='log10 population',
                     xlim=[-5, 5])

    thinkplot.Save(root='populations_normal')
    

def main():
    thinkstats2.RandomSeed(17)
    MakeFigures()


if __name__ == "__main__":
    main()
