"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import numpy
import random

import thinkstats2
import thinkplot


def main():
    random.seed(17)

    # mean and var of women's heights in cm, from the BRFSS
    mean, var = 163, 52.8
    sigma = math.sqrt(var)

    # make a PDF and compute a density, FWIW
    pdf = thinkstats2.GaussianPdf(mean, sigma)
    print pdf.Density(mean + sigma)

    # make a PMF and plot it
    xs = numpy.linspace(mean - 3*sigma, mean + 3*sigma, 100)
    pmf = pdf.MakePmf(xs)
    thinkplot.Pmf(pmf, label='Gaussian')

    # make a sample, make an estimated PDF, and plot it
    sample = [random.gauss(mean, sigma) for i in range(1000)]
    sample_pdf = thinkstats2.EstimatedPdf(sample)
    sample_pmf = sample_pdf.MakePmf(xs)
    thinkplot.Pmf(sample_pmf, label='KDE')

    thinkplot.Save(root='pdf_example',
                   xlabel='Height (cm)',
                   ylabel='Density')


if __name__ == '__main__':
    main()
