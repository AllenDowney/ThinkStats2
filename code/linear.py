"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import numpy as np

import first
import thinkplot
import thinkstats2


def Summarize(estimates, actual=None):
    """Prints standard error and 90% confidence interval.

    estimates: sequence of estimates
    actual: float actual value
    """
    mean = thinkstats2.Mean(estimates)
    stderr = thinkstats2.Std(estimates, mu=actual)
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.ConfidenceInterval(90)
    print('mean, SE, CI', mean, stderr, ci)


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


def PlotConfidenceIntervals(xs, inters, slopes, 
                            res=None, percent=90, **options):
    """Plots the 90% confidence intervals for weights based on ages.

    xs: sequence
    inters: estimated intercepts
    slopes: estimated slopes
    res: residuals
    percent: what percentile range to show
    """
    fys_seq = []
    for inter, slope in zip(inters, slopes):
        fxs, fys = thinkstats2.FitLine(xs, inter, slope)
        if res is not None:
            fys += np.random.permutation(res)
        fys_seq.append(fys)

    p = (100 - percent) / 2
    percents = p, 100 - p
    low, high = thinkstats2.PercentileRows(fys_seq, percents)
    thinkplot.FillBetween(fxs, low, high, **options)


def PlotSamplingDistributions(live):
    """Plots confidence intervals for the fitted curve and sampling dists.

    live: DataFrame
    """
    ages = live.agepreg
    weights = live.totalwgt_lb
    inter, slope = thinkstats2.LeastSquares(ages, weights)
    res = thinkstats2.Residuals(ages, weights, inter, slope)
    r2 = thinkstats2.CoefDetermination(weights, res)

    print('rho', thinkstats2.Corr(ages, weights))
    print('R2', r2)
    print('R', math.sqrt(r2))
    print('Std(ys)', thinkstats2.Std(weights))
    print('Std(res)', thinkstats2.Std(res))

    # plot the confidence intervals
    inters, slopes = SamplingDistributions(live, iters=1001)
    PlotConfidenceIntervals(ages, inters, slopes, percent=90, 
                            alpha=0.3, label='90% CI')
    thinkplot.Text(42, 7.53, '90%')
    PlotConfidenceIntervals(ages, inters, slopes, percent=50,
                            alpha=0.5, label='50% CI')
    thinkplot.Text(42, 7.59, '50%')

    thinkplot.Save(root='linear3',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   legend=False)

    # plot the confidence intervals
    thinkplot.PrePlot(2)
    thinkplot.Scatter(ages, weights, color='gray', alpha=0.1)
    PlotConfidenceIntervals(ages, inters, slopes, res=res, alpha=0.2)
    PlotConfidenceIntervals(ages, inters, slopes)
    thinkplot.Save(root='linear5',
                   xlabel='age (years)',
                   ylabel='birth weight (lbs)',
                   title='90% CI',
                   axis=[10, 45, 0, 15],
                   legend=False)

    # plot the sampling distribution of slope under null hypothesis
    # and alternate hypothesis
    sampling_cdf = thinkstats2.Cdf(slopes)
    print('p-value, sampling distribution', sampling_cdf[0])

    ht = SlopeTest((ages, weights))
    pvalue = ht.PValue()
    print('p-value, slope test', pvalue)

    print('inter', inter, thinkstats2.Mean(inters))
    Summarize(inters, inter)
    print('slope', slope, thinkstats2.Mean(slopes))
    Summarize(slopes, slope)

    thinkplot.PrePlot(2)
    thinkplot.Plot([0, 0], [0, 1], color='0.8')
    ht.PlotCdf(label='null hypothesis')
    thinkplot.Cdf(sampling_cdf, label='sampling distribution')
    thinkplot.Save(root='linear4',
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
    thinkplot.Save(root='linear1',
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

    ages = [group.agepreg.mean() for _, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.residual) for _, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='linear2',
                   xlabel='age (years)',
                   ylabel='residual (lbs)',
                   xlim=[10, 45])


class SlopeTest(thinkstats2.HypothesisTest):
    """Tests the slope of a linear least squares fit. """

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        ages, weights = data
        _, slope = thinkstats2.LeastSquares(ages, weights)
        return slope

    def MakeModel(self):
        """Builds a model of the null hypothesis.
        """
        _, weights = self.data
        self.ybar = weights.mean()
        self.res = weights - self.ybar

    def RunModel(self):
        """Runs the model of the null hypothesis.

        returns: simulated data
        """
        ages, _ = self.data
        weights = self.ybar + np.random.permutation(self.res)
        return ages, weights


def ResampleRowsWeighted(df, attr='finalwgt'):
    """Resamples a DataFrame using probabilities proportional to finalwgt.

    df: DataFrame
    attr: string column name to use as weights

    returns: DataFrame
    """
    weights = df[attr]
    cdf = thinkstats2.Pmf(weights).MakeCdf()
    indices = cdf.Sample(len(weights))
    sample = df.loc[indices]
    return sample


def EstimateBirthWeight(live, iters=1001):
    """Estimate mean birth weight by resampling, with and without weights.

    live: DataFrame
    iters: number of experiments to run
    """

    mean = live.totalwgt_lb.mean()
    print('mean', mean)

    estimates = [thinkstats2.ResampleRows(live).totalwgt_lb.mean()
                 for _ in range(iters)]
    Summarize(estimates)

    estimates = [ResampleRowsWeighted(live).totalwgt_lb.mean()
                 for _ in range(iters)]
    Summarize(estimates)
    

def main():
    thinkstats2.RandomSeed(17)
    
    live, _, _ = first.MakeFrames()
    EstimateBirthWeight(live)

    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    PlotSamplingDistributions(live)
    
    PlotFit(live)
    PlotResiduals(live)


if __name__ == '__main__':
    main()
