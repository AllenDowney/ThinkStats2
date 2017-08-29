"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np

import density
import hinc
import thinkplot
import thinkstats2

"""This file contains a solution to an exercise in Think Stats:

The distribution of income is famously skewed to the right.  In this
exercise, we'll measure how strong that skew is.
...

Compute the median, mean, skewness and Pearson's skewness of the
resulting sample.  What fraction of households reports a taxable
income below the mean?  How do the results depend on the assumed
upper bound?

My results with log_upper=6

mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
cdf[mean] 0.660005879567

With log_upper=7

mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277
cdf[mean] 0.856563066521

With a higher upper bound, the moment-based skewness increases, as
expected.  Surprisingly, the Pearson skewness goes down!  The reason
seems to be that increasing the upper bound has a modest effect on the
mean, and a stronger effect on standard deviation.  Since std is in
the denominator with exponent 3, it has a stronger effect on the
result.

So this is apparently an example where Pearson skewness is not working
well as a summary statistic.  A better choice is a statistic that has
meaning in context, like the fraction of people with income below the
mean.  Or something like the Gini coefficient designed to quantify a
property of the distribution (like the relative difference we expect
between two random people).

"""

def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample


def main():
    df = hinc.ReadData()
    log_sample = InterpolateSample(df, log_upper=6.0)

    log_cdf = thinkstats2.Cdf(log_sample)
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')

    sample = np.power(10, log_sample)
    mean, median = density.Summarize(sample)

    cdf = thinkstats2.Cdf(sample)
    print('cdf[mean]', cdf[mean])

    pdf = thinkstats2.EstimatedPdf(sample)
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='PDF')


if __name__ == "__main__":
    main()
