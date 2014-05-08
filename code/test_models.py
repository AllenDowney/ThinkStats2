"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot


def read_file(filename):
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


def main():
    filename = 'mystery0.dat'
    data = read_file(filename)
    cdf = thinkstats2.MakeCdfFromList(data)

    thinkplot.SubPlot(2, 3, 1)
    thinkplot.Cdf(cdf)
    thinkplot.Config(title='linear')

    thinkplot.SubPlot(2, 3, 2)
    scale = thinkplot.Cdf(cdf, xscale='log')
    thinkplot.Config(title='logx', **scale)

    thinkplot.SubPlot(2, 3, 3)
    scale = thinkplot.Cdf(cdf, transform='exponential')
    thinkplot.Config(title='expo', **scale)

    thinkplot.SubPlot(2, 3, 4)
    xs, ys = thinkstats2.NormalProbability(data)
    thinkplot.Plot(xs, ys)
    thinkplot.Config(title='normal')

    thinkplot.SubPlot(2, 3, 5)
    scale = thinkplot.Cdf(cdf, transform='pareto')
    thinkplot.Config(title='pareto', **scale)

    thinkplot.SubPlot(2, 3, 6)
    scale = thinkplot.Cdf(cdf, transform='weibull')
    thinkplot.Config(title='weibull', **scale)

    thinkplot.Show()


if __name__ == '__main__':
    main()
