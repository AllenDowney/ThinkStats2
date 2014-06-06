"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import itertools
import numpy as np
import pandas

import hinc
import thinkplot
import thinkstats2


def GenerateSample(df):
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)

    df.log_lower[0] = 0
    df.log_upper[41] = 6

    arrays = []
    for i, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    sample = np.concatenate(arrays)
    pdf = thinkstats2.EstimatedPdf(sample)

    thinkplot.Pdf(pdf, low=3, high=6.5)
    thinkplot.Show()


def main():
    df = hinc.ReadData()
    GenerateSample(df)


if __name__ == "__main__":
    main()
