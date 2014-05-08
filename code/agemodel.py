"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math

import survey
import first
import descriptive
import cumulative
import thinkstats2
import thinkplot

"""
* Results:

First babies, ages, trimmed mean: 23.0784947977
Other babies, ages, trimmed mean: 26.6647683689
Difference in means: 3.5862735712

First babies, weights, trimmed mean: 115.558686539
Other babies, weights, trimmed mean: 117.734924078
Difference in means: 2.17623753873


* First babies are 2.2 oz lighter; their mothers are 3.5 years younger.


Pearson correlation 0.0683745752519
Spearman correlation 0.0987971917949
(inter, slope): 109.522876323 0.287729420217
R^2 0.00467508254087

* The units of inter are ounces; the units of slope are ounces per year.
* Each additional year adds 0.3 ounces to the mean birth weight.

* But the correlation is quite weak.

Weight difference explained by age: 1.03187641538
Fraction explained: 0.474156151163

* The age difference could account for 50% of the weight difference.

* If we bin births by mother's age, we see that the relationship is nonlinear,
* so the estimated slope is probably too low, which means that the fraction
* of the weight difference explained by age is probably more than 50%.

Bin Mean weight (oz)
10.0 117.295081967
15.0 113.487096774
20.0 116.505546218
25.0 118.190963342
30.0 118.323802716
35.0 118.743842365
40.0 114.054054054

* If we trim very low and very high weights, the correlations are a
* little higher, but the difference is small enough that it is a non-issue.

Pearson correlation 0.084795033619
Spearman correlation 0.103080620319
(inter, slope): 110.400666041 0.297751296651
R^2 0.00719019772646


"""


def Process(table, name):
    """Runs various analyses on this table.

    Creates instance variables:
        ages: sequence of int ages in years
        age_pmf: Pmf object
        age_cdf: Cdf object
        weights: sequence of total weight in ounces
        weight_cdf: Cdf object
    """
    cumulative.Process(table, name)

    table.ages = [p.agepreg for p in table.records
                  if p.agepreg != 'NA']
    table.age_pmf = thinkstats2.MakePmfFromList(table.ages, table.name)
    table.age_cdf = thinkstats2.MakeCdfFromList(table.ages, table.name)

    table.weights = [p.totalwgt_oz for p in table.records
                     if p.totalwgt_oz != 'NA']
    table.weight_cdf = thinkstats2.MakeCdfFromList(table.weights, table.name)


def MakeTables(data_dir='.'):
    """Reads survey data and returns a tuple of Tables"""
    table, firsts, others = first.MakeTables(data_dir)
    pool = descriptive.PoolRecords(firsts, others)

    Process(pool, 'live births')
    Process(firsts, 'first babies')
    Process(others, 'others')
        
    return pool, firsts, others


def GetAgeWeight(table, low=0.0, high=20.0):
    """Get sequences of mother's age and birth weight.

    Args:
        table: Table object
        low: float min weight in pounds
        high: float max weight in pounds

    Returns:
        tuple of sequences (ages, weights)
    """
    ages = []
    weights = []
    for r in table.records:
        if r.agepreg == 'NA' or r.totalwgt_oz == 'NA':
            continue

        if r.totalwgt_oz < low*16 or r.totalwgt_oz > high*16:
            continue

        ages.append(r.agepreg)
        weights.append(r.totalwgt_oz)

    return ages, weights


def Partition(ages, weights, bin_size=2):
    """Break ages into bins.

    Returns a map from age to list of weights.
    """
    weight_dict = {}
    for age, weight in zip(ages, weights):
        bin = bin_size * math.floor(age / bin_size) + bin_size/2.0
        weight_dict.setdefault(bin, []).append(weight)

    for bin, bin_weights in weight_dict.iteritems():
        try:
            mean = thinkstats2.Mean(bin_weights)
        except ZeroDivisionError:
            continue

    return weight_dict


def MakeFigures(pool, firsts, others):
    """Creates several figures for the book."""

    # CDF of all ages
    thinkplot.Clf()
    thinkplot.Cdf(pool.age_cdf)
    thinkplot.Save(root='agemodel_age_cdf',
                title="Distribution of mother's age",
                xlabel='age (years)',
                ylabel='CDF',
                legend=False)

    # CDF of all weights
    thinkplot.Clf()
    thinkplot.Cdf(pool.weight_cdf)
    thinkplot.Save(root='agemodel_weight_cdf',
                title="Distribution of birth weight",
                xlabel='birth weight (oz)',
                ylabel='CDF',
                legend=False)

    # plot CDFs of birth ages for first babies and others
    thinkplot.Clf()
    thinkplot.Cdfs([firsts.age_cdf, others.age_cdf])
    thinkplot.Save(root='agemodel_age_cdfs',
                title="Distribution of mother's age",
                xlabel='age (years)',
                ylabel='CDF')

    thinkplot.Clf()
    thinkplot.Cdfs([firsts.weight_cdf, others.weight_cdf])
    thinkplot.Save(root='agemodel_weight_cdfs',
                title="Distribution of birth weight",
                xlabel='birth weight (oz)',
                ylabel='CDF')

    # make a scatterplot of ages and weights
    ages, weights = GetAgeWeight(pool)
    thinkplot.clf()
    thinkplot.Scatter(ages, weights, alpha=0.2)
    thinkplot.Save(root='agemodel_scatter',
                xlabel='Age (years)',
                ylabel='Birth weight (oz)',
                legend=False)


def DifferenceInMeans(firsts, others, attr):
    """Compute the difference in means between tables for a given attr.

    Prints summary statistics.
    """
    firsts_mean = thinkstats2.Mean(getattr(firsts, attr))
    print 'First babies, %s, trimmed mean:' % attr, firsts_mean

    others_mean = thinkstats2.Mean(getattr(others, attr))
    print 'Other babies, %s, trimmed mean:' % attr, others_mean

    diff = others_mean - firsts_mean
    print 'Difference in means:', diff
    print

    return diff


def ComputeLeastSquares(ages, weights):
    """Computes least squares fit for ages and weights.

    Prints summary statistics.
    """
    # compute the correlation between age and weight
    print 'Pearson correlation', thinkstats2.Corr(ages, weights)
    print 'Spearman correlation', thinkstats2.SpearmanCorr(ages, weights)

    # compute least squares fit
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    print '(inter, slope):', inter, slope

    res = thinkstats2.Residuals(ages, weights, inter, slope)
    R2 = thinkstats2.CoefDetermination(weights, res)

    print 'R^2', R2
    print
    return inter, slope, R2


def MakeLinePlot(age_bins):
    xs = []
    ys = []
    for bin, weights in sorted(age_bins.iteritems()):
        xs.append(bin)
        ys.append(thinkstats2.Mean(weights))

    thinkplot.Plot(xs, ys, 'bs-')
    thinkplot.Save(root='agemodel_line',
                xlabel="Mother's age (years)",
                ylabel='Mean birthweight (oz)',
                legend=False)


def main(name, data_dir=''):
    pool, firsts, others = MakeTables(data_dir)

    for table in [pool, firsts, others]:
        print table.name, len(table.records),
        print len(table.ages), len(table.weights)

    # compute differences in mean age and weight
    age_diff = DifferenceInMeans(firsts, others, 'ages')
    weight_diff = DifferenceInMeans(firsts, others, 'weights')

    # get ages and weights
    ages, weights = GetAgeWeight(pool)
    print 'Mean, var weight', thinkstats2.MeanVar(weights)

    # compute a least squares fit
    inter, slope, R2 = ComputeLeastSquares(ages, weights)

    # see how much of the weight difference is explained by age
    weight_diff_explained = age_diff * slope
    print 'Weight difference explained by age:', weight_diff_explained
    print 'Fraction explained:', weight_diff_explained / weight_diff
    print

    # make a table of mean weight for 5-year age bins
    weight_dict = Partition(ages, weights)
    MakeLinePlot(weight_dict)

    # the correlations are slightly higher if we trim outliers
    ages, weights = GetAgeWeight(pool, low=4, high=12)
    inter, slope, R2 = ComputeLeastSquares(ages, weights)

    MakeFigures(pool, firsts, others)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
