"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import copy
import math
import numpy as np
import sys

import brfss
import hypothesis
import thinkstats2
import thinkplot


"""
Results:

Number of records: 414509
Pearson correlation (weights): 0.508736478974
Pearson correlation (log weights): 0.531728260599
Spearman correlation (weights): 0.541529498192

The Pearson correlation is low because of the effect of outliers.
Either of the others is a reasonable choice, but in this case because
we know the distribution of weights is lognormal, the log transform
might be the best choice.

If we didn't know what transform to use, I would be more inclined to
use Spearman's correlation, but I am less comfortable with it because
mapping to ranks is an information-losing transform, and Log is not.

"""

def almostEquals(x, y, tol=1e-7):
    """Returns True if the difference between x and y is less than tol.
    """
    return abs(x - y) < tol


def ComputeCorrelations(heights, weights):
    """Compute correlations and least squares fit.

    heights: sequence
    weights: sequence
    """
    pearson = thinkstats2.Corr(heights, weights)
    assert almostEquals(pearson, 0.508736478973)
    print('Pearson correlation (weights):', pearson)

    log_weights = np.log(weights)
    log_pearson = thinkstats2.Corr(heights, log_weights)
    assert almostEquals(log_pearson, 0.531728260598)
    print('Pearson correlation (log weights):', log_pearson)

    spearman = thinkstats2.SpearmanCorr(heights, weights)
    print('Spearman correlation (weights):', spearman)
    assert almostEquals(spearman, 0.541535836332)

    inter, slope = thinkstats2.LeastSquares(heights, log_weights)
    print('Least squares inter, slope (log weights):', inter, slope)

    res = thinkstats2.Residuals(heights, log_weights, inter, slope)
    R2 = thinkstats2.CoefDetermination(log_weights, res)
    R = math.sqrt(R2)
    print('Coefficient of determination:', R2)
    print('sqrt(R^2):', R)

    assert almostEquals(R, log_pearson)


class CorrelationPermute(hypothesis.HypothesisTest):
    """Tests correlations by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        xs, ys = self.data
        test_stat = abs(thinkstats2.Corr(xs, ys))
        return test_stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        xs, ys = self.data
        self.model = copy.copy(xs), copy.copy(ys)

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        xs, ys = self.model
        np.random.shuffle(xs)
        return self.model


def TestCorrelation(heights, weights):
    """Test whether the correlation is statistically significant.

    heights: sequence
    weights: sequence
    """

    test = CorrelationPermute((heights, weights))
    p_value = test.PValue()
    print('p-value', p_value)
    print('actual test statitic', test.actual)
    print('max test statitic', test.MaxTestStat())

    test.PlotCdf()
    thinkplot.Show(xlabel='resampled correlation', ylabel='CDF')


def main(name, nrows=None):
    thinkstats2.RandomSeed(17)

    if nrows is not None:
        nrows = int(nrows)

    df = brfss.ReadBrfss(nrows=nrows)

    columns = df[['htm3', 'wtkg2']].dropna()
    heights, weights = columns.htm3.values, columns.wtkg2.values

    TestCorrelation(heights, weights)
    if nrows == None:
        ComputeCorrelations(heights, weights)


if __name__ == '__main__':
    main(*sys.argv)
