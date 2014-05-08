"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import numpy

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


def BinData(data, low, high, n):
    """Rounds data off into bins.

    data: sequence of numbers
    low: low value
    high: high value
    n: number of bins

    returns: sequence of numbers
    """
    bins = numpy.linspace(low, high, n)
    data = (numpy.array(data) - low) / (high - low) * n
    data = numpy.round(data) * (high - low) / n + low
    return data


def main():
    filename = 'mystery0.dat'
    data = read_file(filename)

    pmf = thinkstats2.MakePmfFromList(data)
    cdf = thinkstats2.MakeCdfFromList(data)

    pdf = thinkstats2.EstimatedPdf(data)
    low, high = min(data), max(data)
    xs = numpy.linspace(low, high, 101)
    kde_pmf = pdf.MakePmf(xs)

    bin_data = BinData(data, low, high, 51)
    bin_pmf = thinkstats2.MakePmfFromList(bin_data)
    
    thinkplot.SubPlot(2, 2, 1)
    thinkplot.Hist(pmf, width=0.1)
    thinkplot.Config(title='Naive Pmf')

    thinkplot.SubPlot(2, 2, 2)
    thinkplot.Hist(bin_pmf)
    thinkplot.Config(title='Binned Hist')

    thinkplot.SubPlot(2, 2, 3)
    thinkplot.Pmf(kde_pmf)
    thinkplot.Config(title='KDE PDF')

    thinkplot.SubPlot(2, 2, 4)
    thinkplot.Cdf(cdf)
    thinkplot.Config(title='CDF')

    thinkplot.Show()


if __name__ == '__main__':
    main()
