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

    thinkplot.PrePlot(rows=2, cols=3)
    thinkplot.SubPlot(1)
    thinkplot.Cdf(cdf)
    thinkplot.Config(title='linear')

    thinkplot.SubPlot(2)
    scale = thinkplot.Cdf(cdf, xscale='log')
    thinkplot.Config(title='logx', **scale)

    thinkplot.SubPlot(3)
    scale = thinkplot.Cdf(cdf, transform='exponential')
    thinkplot.Config(title='expo', **scale)

    thinkplot.SubPlot(4)
    xs, ys = thinkstats2.NormalProbability(data)
    thinkplot.Plot(xs, ys)
    thinkplot.Config(title='normal')

    thinkplot.SubPlot(5)
    scale = thinkplot.Cdf(cdf, transform='pareto')
    thinkplot.Config(title='pareto', **scale)

    thinkplot.SubPlot(6)
    scale = thinkplot.Cdf(cdf, transform='weibull')
    thinkplot.Config(title='weibull', **scale)

    thinkplot.Show(legend=False)


if __name__ == '__main__':
    main(*sys.argv)
