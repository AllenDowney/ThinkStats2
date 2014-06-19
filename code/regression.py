"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import random
import numpy as np

import first
import thinkplot
import thinkstats2
import statsmodels.formula.api as smf

def Summarize(values, actual):
    """Prints standard error and 90% confidence interval.

    values: sequence of estimates
    actual: float actual value
    """
    std = thinkstats2.Std(values, mu=actual)
    cdf = thinkstats2.Cdf(values)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('SE, CI', std, ci)


def SamplingDistributions(live, iters=101):
    """Estimates sampling distributions by resampling rows.

    live: DataFrame
    iters: number of times to run simulations

    returns: pair of sequences (inters, slopes)
    """
    t = []
    for _ in range(iters):
        sample = thinkstats2.ResampleRows(live)
        ages = sample.agepreg
        weights = sample.totalwgt_lb
        estimates = thinkstats2.LeastSquares(ages, weights)
        t.append(estimates)

    inters, slopes = zip(*t)
    return inters, slopes


def PlotConfidenceIntervals(xs, inters, slopes, res=None, **options):
    """Plots the 90% confidence intervals for weights based on ages.

    xs: sequence
    inters: estimated intercepts
    slopes: estimated slopes
    res: residuals
    """
    size = len(slopes), len(xs)
    array = np.zeros(size)

    for i, (inter, slope) in enumerate(zip(inters, slopes)):
        fxs, fys = thinkstats2.FitLine(xs, inter, slope)
        if res is not None:
            fys += np.random.permutation(res)
        array[i,] = fys

    xs = np.sort(xs)
    array = np.sort(array, axis=0)

    def Percentile(p):
        index = int(len(slopes) * p / 100)
        print(index)
        return array[index,]

    low = thinkstats2.Smooth(Percentile(5))
    high = thinkstats2.Smooth(Percentile(95))
    thinkplot.FillBetween(xs, low, high, **options)


def PlotSamplingDistributions(live):
    """Plots confidence intervals for the fitted curve and sampling dists.

    live: DataFrame
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    print('Std(res)', thinkstats2.Std(res))
    print('Std(ys)', thinkstats2.Std(weights))
    print('R2', r2)
    print('R', math.sqrt(r2))
    print('rho', thinkstats2.Corr(ages, weights))

    # plot the confidence intervals
    inters, slopes = SamplingDistributions(live, iters=1001)
    PlotConfidenceIntervals(ages, inters, slopes)
    thinkplot.Save(root='regression3',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   title='90% CI',
                   legend=False)

    # plot the confidence intervals
    thinkplot.PrePlot(2)
    thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)
    PlotConfidenceIntervals(ages, inters, slopes, res=res, alpha=0.2)
    PlotConfidenceIntervals(ages, inters, slopes)
    thinkplot.Save(root='regression5',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   title='90% CI',
                   axis=[10, 45, 0, 15],
                   legend=False)

    # plot the sampling distribution of slope under null hypothesis
    # and alternate hypothesis
    slope_cdf = thinkstats2.Cdf(slopes)
    print('p-value of slope', slope_cdf[0])

    print('inter', inter, thinkstats2.Mean(inters))
    Summarize(inters, inter)
    print('slope', slope, thinkstats2.Mean(slopes))
    Summarize(slopes, slope)

    ht = SlopeTest((ages, weights))
    pvalue = ht.PValue()
    cdf = thinkstats2.Cdf(slopes)

    thinkplot.PrePlot(2)
    thinkplot.Plot([0, 0], [0, 1], color='0.8')
    ht.PlotCdf(label='null hypothesis')
    thinkplot.Cdf(cdf, label='sampling distribution')
    thinkplot.Save(root='regression4',
                   xlabel='slope (lbs / year)',
                   ylabel='CDF',
                   xlim=[-0.03, 0.03],
                   loc='upper left')


def PlotFit(live):
    """Plots a scatter plot and fitted curve.

    live: DataFrame
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    fit_xs, fit_ys = thinkstats2.FitLine(ages, inter, slope)

    thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)
    thinkplot.Plot(fit_xs, fit_ys, color='white', linewidth=3)
    thinkplot.Plot(fit_xs, fit_ys, color='blue', linewidth=2)
    thinkplot.Save(root='regression1',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   axis=[10, 45, 0, 15],
                   legend=False)


def PlotResiduals(live):
    """Plots percentiles of the residuals.

    live: DataFrame
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    live['residual'] = thinkstats2.Residuals(ages, weights, inter, slope)

    bins = np.arange(10, 48, 3)
    indices = np.digitize(live.agepreg, bins)
    groups = live.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.residual) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='regression2',
                   xlabel='age (years)',
                   ylabel='residual (lbs)',
                   xlim=[10, 45])


def RunOls(live):
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    formula = 'totalwgt_lb ~ agepreg'
    model = smf.ols(formula, data=live)
    # OLS object
    results = model.fit()
    # RegressionResults object
    print(results.f_pvalue)
    print(results.mse_model)
    print(results.mse_resid)
    print(results.mse_total)
    print(results.params['Intercept'], inter)
    print(results.params['agepreg'], slope)
    print(results.pvalues)
    print(thinkstats2.Std(results.resid), thinkstats2.Std(res))
    print(results.rsquared, r2)
    print(results.rsquared_adj)
    print(results.fittedvalues)
    print(results.summary())


class SlopeTest(thinkstats2.HypothesisTest):
    """Tests the slope of a linear regression. """

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        ages, weights = data
        inter, slope = thinkstats2.LeastSquares(ages, weights)
        return slope

    def MakeModel(self):
        """Builds a model of the null hypothesis.
        """
        ages, weights = self.data
        self.ybar = weights.mean()
        self.res = weights - self.ybar

    def RunModel(self):
        """Runs the model of the null hypothesis.

        returns: simulated data
        """
        ages, _ = self.data
        weights = self.ybar + np.random.permutation(self.res)
        return ages, weights


def ResampleRowsWeighted(live):
    """Resamples a DataFrame using probabilities proportional to finalwgt.

    live: DataFrame

    returns: DataFrame
    """
    weights = live.finalwgt
    cdf = thinkstats2.Pmf(weights.iteritems()).MakeCdf()
    indices = cdf.Sample(len(weights))
    sample = live.loc[indices]
    return sample


def EstimateBirthWeight(live, iters=1001):

    def Summarize(estimates):
        mean = thinkstats2.Mean(estimates)
        stderr = thinkstats2.Std(estimates)
        cdf = thinkstats2.Cdf(estimates)
        ci = cdf.Percentile(5), cdf.Percentile(95)
        print('mean', mean)
        print('stderr', stderr)
        print('ci', ci)

    mean = live.totalwgt_lb.mean()
    print('mean', mean)

    estimates = [thinkstats2.ResampleRows(live).totalwgt_lb.mean()
                 for _ in range(iters)]
    Summarize(estimates)

    estimates = [ResampleRowsWeighted(live).totalwgt_lb.mean()
                 for _ in range(iters)]
    Summarize(estimates)
    

def main(name, data_dir='.'):
    thinkstats2.RandomSeed(17)
    
    live, firsts, others = first.MakeFrames()
    EstimateBirthWeight(live)
    return

    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

    return

    PlotSamplingDistributions(live)
    return

    RunOls(live)
    return

    #PlotFit(live)
    #PlotResiduals(live)



if __name__ == '__main__':
    import sys
    main(*sys.argv)
