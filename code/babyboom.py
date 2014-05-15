"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import random
import pandas as pd

import thinkplot
import thinkstats2


FORMATS = ['eps', 'pdf']

def ReadBabyboom(filename='babyboom.dat'):
    """Reads the babyboom data.

    filename: string

    returns: DataFrame
    """
    var_info = [
        ('time', 1, 8, int),
        ('sex', 9, 16, int),
        ('weight_g', 17, 24, int),
        ('minutes', 25, 32, int),
        ]
    columns = ['name', 'start', 'end', 'type']
    variables = pd.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = thinkstats2.FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(filename, skiprows=59)

    # compute the interarrival times
    df['diffs'] = df.minutes.diff()
    return df


def MakeFigure(df):
    """Plot CDF of interarrival time on log and linear scales.

    df: DataFrame
    """
    diffs = df.diffs.dropna()
    n = len(diffs)
    mu = thinkstats2.Mean(diffs)
        
    print('mean interarrival time', mu)
    
    cdf = thinkstats2.MakeCdfFromList(diffs, 'actual')

    sample = [random.expovariate(1/mu) for _ in range(n)]
    model = thinkstats2.MakeCdfFromList(sample, 'model')
    
    thinkplot.PrePlot(1)
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='babyboom_interarrivals',
                   title='Time between births',
                   xlabel='minutes',
                   ylabel='CDF',
                   legend=False,
                   formats=FORMATS)

    thinkplot.PrePlot(2)
    thinkplot.Cdfs([cdf, model], complement=True)
    thinkplot.Save(root='babyboom_interarrivals_model',
                   title='Time between births',
                   xlabel='minutes',
                   ylabel='Complementary CDF',
                   yscale='log',
                   formats=FORMATS)

    thinkplot.PrePlot(1)
    thinkplot.Cdf(cdf, complement=True)
    thinkplot.Save(root='babyboom_interarrivals_logy',
                   title='Time between births',
                   xlabel='minutes',
                   ylabel='Complementary CDF',
                   yscale='log',
                   legend=False,
                   formats=FORMATS)


def main():
    df = ReadBabyboom()
    MakeFigure(df)

    
if __name__ == "__main__":
    main()
