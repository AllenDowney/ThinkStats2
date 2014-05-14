"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
from __future__ import print_function

import brfss
import math
import sys

import thinkplot
import thinkstats2


def MakeNormalModel(weights, root,
               xmax=175, 
               xlabel='adult weight (kg)',
               axis=None):

    cdf = thinkstats2.MakeCdfFromList(weights)

    t = weights.values.tolist()
    t.sort()
    mean, var = thinkstats2.TrimmedMeanVar(t)
    print('n, Mean, Var', len(weights), mean, var)

    std = math.sqrt(var)
    print('Std', std)

    xs, ps = thinkstats2.RenderNormalCdf(mean, std, xmax)
    thinkplot.plot(xs, ps, label='model', linewidth=4, color='0.7')

    xs, ps = cdf.Render()
    thinkplot.plot(xs, ps, label='data', linewidth=2, color='blue')

    thinkplot.Save(root,
                   title = 'Adult weight',
                   xlabel = xlabel,
                   ylabel = 'CDF',
                   axis=axis or [0, xmax, 0, 1])


def MakeFigures(df):
    """Generates CDFs and normal prob plots for weights and log weights."""
    weights = df.wtkg2

    MakeNormalModel(weights, root='brfss_weight_model')

    thinkstats2.MakeNormalPlot(weights,
                               root='brfss_weight_normal',
                               title='Adult weight',
                               ylabel='Weight (kg)')

    log_weights = np.log10(weights)
    xmax = math.log(175.0)
    axis = [3.5, 5.2, 0, 1]

    MakeNormalModel(df, log_weights, 
                    root='brfss_weight_log',
                    xmax=xmax,
                    xlabel='adult weight (log10 kg)',
                    axis=axis)

    thinkstats2.MakeNormalPlot(log_weights, 
                               root='brfss_weight_lognormal',
                               title='Adult weight',
                               ylabel='Weight (log10 kg)')


def main(script):
    thinkstats2.RandomSeed(17)
    
    df = brfss.ReadBrfss(nrows=1000)

    MakeFigures(df)

    
if __name__ == '__main__':
    main(*sys.argv)
