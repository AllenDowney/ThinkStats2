"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import numpy
import random

import thinkstats2
import thinkplot


def main():
    random.seed(17)

    # mean and var of women's heights in cm, from the BRFSS
    mean, var = 163, 52.8
    std = math.sqrt(var)

    # make a PDF and compute a density, FWIW
    pdf = thinkstats2.GaussianPdf(mean, std)
    print(pdf.Density(mean + std))

    # make a PMF and plot it
    low, high, n = mean - 3*std, mean + 3*std, 100
    pmf = pdf.MakePmf(low, high, n)

    thinkplot.PrePlot(2)
    thinkplot.Pdf(pmf, label='Gaussian')

    # make a sample, make an estimated PDF, and plot it
    sample = [random.gauss(mean, std) for i in range(100)]
    sample_pdf = thinkstats2.EstimatedPdf(sample)
    sample_pmf = sample_pdf.MakePmf(low, high, n)
    thinkplot.Pdf(sample_pmf, label='sample KDE')

    thinkplot.Save(root='pdf_example',
                   xlabel='Height (cm)',
                   ylabel='Density')


if __name__ == '__main__':
    main()
