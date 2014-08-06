"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import random

import brfss
import first
import thinkstats2
import thinkplot


def Summarize(data):
    """Prints summary statistics.

    data: pandas Series
    """
    mean = data.mean()
    std = data.std()
    median = thinkstats2.Median(data)
    print('mean', mean)
    print('std', std)
    print('median', median)
    print('skewness', thinkstats2.Skewness(data))
    print('pearson skewness', 
          thinkstats2.PearsonMedianSkewness(data))

    return mean, median


def ComputeSkewnesses():
    """Plots KDE of birthweight and adult weight.
    """
    def VertLine(x, y):
        thinkplot.Plot([x, x], [0, y], color='0.6', linewidth=1)

    live, firsts, others = first.MakeFrames()
    data = live.totalwgt_lb.dropna()
    print('Birth weight')
    mean, median = Summarize(data)

    y = 0.35
    VertLine(mean, y)
    thinkplot.Text(mean-0.15, 0.1*y, 'mean', horizontalalignment='right')
    VertLine(median, y)
    thinkplot.Text(median+0.1, 0.1*y, 'median', horizontalalignment='left')

    pdf = thinkstats2.EstimatedPdf(data)
    thinkplot.Pdf(pdf, label='birth weight')
    thinkplot.Save(root='density_totalwgt_kde',
                   xlabel='lbs',
                   ylabel='PDF')

    df = brfss.ReadBrfss(nrows=None)
    data = df.wtkg2.dropna()
    print('Adult weight')
    mean, median = Summarize(data)

    y = 0.02499
    VertLine(mean, y)
    thinkplot.Text(mean+1, 0.1*y, 'mean', horizontalalignment='left')
    VertLine(median, y)
    thinkplot.Text(median-1.5, 0.1*y, 'median', horizontalalignment='right')

    pdf = thinkstats2.EstimatedPdf(data)
    thinkplot.Pdf(pdf, label='adult weight')
    thinkplot.Save(root='density_wtkg2_kde',
                   xlabel='kg',
                   ylabel='PDF',
                   xlim=[0, 200])


def MakePdfExample(n=500):
    """Plots a normal density function and a KDE estimate.

    n: sample size
    """
    # mean and var of women's heights in cm, from the BRFSS
    mean, var = 163, 52.8
    std = math.sqrt(var)

    # make a PDF and compute a density, FWIW
    pdf = thinkstats2.NormalPdf(mean, std)
    print(pdf.Density(mean + std))

    # make a PMF and plot it
    thinkplot.PrePlot(2)
    thinkplot.Pdf(pdf, label='normal')

    # make a sample, make an estimated PDF, and plot it
    sample = [random.gauss(mean, std) for _ in range(n)]
    sample_pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(sample_pdf, label='sample KDE')

    thinkplot.Save(root='pdf_example',
                   xlabel='Height (cm)',
                   ylabel='Density')


def main():
    thinkstats2.RandomSeed(17)

    MakePdfExample()
    ComputeSkewnesses()


if __name__ == '__main__':
    main()
