"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import numpy
import random

import brfss
import first
import thinkstats2
import thinkplot

# TODO: add BRFSS data to git repo.

def ComputeSkewnesses():
    live, firsts, others = first.MakeFrames()
    data = live.totalwgt_lb.dropna()

    pdf = thinkstats2.EstimatedPdf(data)
    thinkplot.Pdf(pdf)
    thinkplot.Save(root='density_totalwgt_kde',
                   xlabel='birth weight (lbs)',
                   ylabel='PDF',
                   legend=False)

    print('Birth weight')
    print('skewness', thinkstats2.Skewness(data))
    print('pearson skeweness', 
          thinkstats2.PearsonMedianSkewness(data))

    df = brfss.ReadBrfss(nrows=1000)
    data = df.wtkg2.dropna()

    pdf = thinkstats2.EstimatedPdf(data)
    thinkplot.Pdf(pdf)
    thinkplot.Save(root='density_wtkg2_kde',
                   xlabel='adult weight (kg)',
                   ylabel='PDF',
                   legend=False)

    print('Adult weight')
    print('skewness', thinkstats2.Skewness(data))
    print('pearson skeweness', 
          thinkstats2.PearsonMedianSkewness(data))


def main():
    ComputeSkewnesses()
    return

    random.seed(17)

    # mean and var of women's heights in cm, from the BRFSS
    mean, var = 163, 52.8
    std = math.sqrt(var)

    # make a PDF and compute a density, FWIW
    pdf = thinkstats2.GaussianPdf(mean, std)
    print(pdf.Density(mean + std))

    # make a PMF and plot it
    thinkplot.PrePlot(2)
    thinkplot.Pdf(pdf, label='Gaussian')

    # make a sample, make an estimated PDF, and plot it
    sample = [random.gauss(mean, std) for i in range(100)]
    sample_pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(sample_pdf, label='sample KDE')

    thinkplot.Save(root='pdf_example',
                   xlabel='Height (cm)',
                   ylabel='Density')


if __name__ == '__main__':
    main()
