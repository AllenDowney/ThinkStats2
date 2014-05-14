"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import math
import sys

import brfss
import continuous

import thinkplot
import thinkstats2


def MakeGaussianModel(weights, root, xlabel, axis=None):
    """Plots a CDF with a Gaussian model.
    """
    cdf = thinkstats2.MakeCdfFromList(weights, name='data')

    mean, var = thinkstats2.TrimmedMeanVar(weights)
    std = math.sqrt(var)
    print('n, Mean, Var', len(weights), mean, var)
    print('Std', std)

    xmin = mean - 4 * std
    xmax = mean + 4 * std

    xs, ps = continuous.RenderGaussianCdf(mean, std, xmin, xmax)
    thinkplot.Plot(xs, ps, label='model', linewidth=4, color='0.8')

    thinkplot.PrePlot(1)
    thinkplot.Cdf(cdf)

    thinkplot.Save(root,
                   title='Adult weight (kg)',
                   xlabel=xlabel,
                   ylabel='CDF',
                   loc='lower right',
                   axis=axis or [xmin, xmax, 0, 1])


def MakeNormalPlot(weights, root, ylabel):
    """Generates a normal probability plot of birth weights.

    weights:
    root:
    ylabel:
    """
    mean, var = thinkstats2.TrimmedMeanVar(weights, p=0.01)
    std = math.sqrt(var)

    xs = [-4, 4]
    xs, ys = thinkstats2.FitLine(xs, mean, std)
    thinkplot.Plot(xs, ys, linewidth=4, color='0.8')

    thinkplot.PrePlot(1) 
    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys)

    thinkplot.Save(root=root,
                   title='Normal probability plot',
                   xlabel='Standard deviations from mean',
                   ylabel=ylabel,
                   legend=False)


def MakeFigures(df):
    """Generates CDFs and normal prob plots for weights and log weights."""
    weights = df.wtkg2.dropna()

    MakeGaussianModel(weights, 
                      root='brfss_weight_model',
                      xlabel='adult weight (kg)')

    MakeNormalPlot(weights,
                   root='brfss_weight_normal',
                   ylabel='adult weight (kg)')

    log_weights = np.log10(weights)
    axis = [3.5, 5.2, 0, 1]

    MakeGaussianModel(log_weights, 
                      root='brfss_weight_log',
                      xlabel='adult weight (log10 kg)')

    MakeNormalPlot(log_weights, 
                   root='brfss_weight_lognormal',
                   ylabel='adult weight (log10 kg)')


def main(script):
    thinkstats2.RandomSeed(17)
    
    df = brfss.ReadBrfss(nrows=None)
    MakeFigures(df)

    
if __name__ == '__main__':
    main(*sys.argv)
