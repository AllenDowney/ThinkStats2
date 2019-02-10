"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys

import thinkstats2
import thinkplot


def ReadFile(filename):
    """Reads a list of numbers from a file.

    filename: string

    returns: list of float
    """
    fp = open(filename)
    data = []
    for line in fp:
        x = float(line.strip())
        data.append(x)
    return data


def main(script, filename='mystery0.dat'):
    data = ReadFile(filename)
    cdf = thinkstats2.Cdf(data)

    thinkplot.PrePlot(num=6, rows=2, cols=3)
    thinkplot.SubPlot(1)
    thinkplot.Cdf(cdf, color='C0', label=filename)
    thinkplot.Config(title='CDF on linear scale', ylabel='CDF')

    thinkplot.SubPlot(2)
    scale = thinkplot.Cdf(cdf, xscale='log', color='C0')
    thinkplot.Config(title='CDF on log-x scale', ylabel='CDF', **scale)

    thinkplot.SubPlot(3)
    scale = thinkplot.Cdf(cdf, transform='exponential', color='C0')
    thinkplot.Config(title='CCDF on log-y scale', ylabel='log CCDF', **scale)

    thinkplot.SubPlot(4)
    xs, ys = thinkstats2.NormalProbability(data)
    thinkplot.Plot(xs, ys, color='C0')
    thinkplot.Config(title='Normal probability plot',
                     xlabel='random normal', ylabel='data')

    thinkplot.SubPlot(5)
    scale = thinkplot.Cdf(cdf, transform='pareto', color='C0')
    thinkplot.Config(title='CCDF on log-log scale',  ylabel='log CCDF', **scale)

    thinkplot.SubPlot(6)
    scale = thinkplot.Cdf(cdf, transform='weibull', color='C0')
    thinkplot.Config(title='CCDF on loglog-y log-x scale',
                     ylabel='log log CCDF', **scale)

    thinkplot.Show(legend=False)


if __name__ == '__main__':
    main(*sys.argv)
