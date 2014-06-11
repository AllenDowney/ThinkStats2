"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import random
import scipy.stats

import numpy as np
import pandas

import nsfg
import thinkplot
import thinkstats2


def ParetoMedian(xmin, alpha):
    """Computes the median of a Pareto distribution."""
    return xmin * pow(2, 1/alpha)


def MakeExpoCdf():
    """Generates a plot of the exponential CDF."""

    thinkplot.PrePlot(3)
    for lam in [2.0, 1, 0.5]:
        xs, ps = thinkstats2.RenderExpoCdf(lam, 0, 3.0, 50)        
        thinkplot.Plot(xs, ps, label='lam=%g' % lam)
    
    thinkplot.Save(root='analytic_expo_cdf',
                   title='Exponential CDF',
                   xlabel='x',
                   ylabel='CDF')

    
def ReadBabyBoom(filename='babyboom.dat'):
    """Reads the babyboom data.

    filename: string

    returns: DataFrame
    """
    var_info = [
        ('time', 1, 8, int),
        ('sex', 9, 16, int),
        ('weight_g', 17, 24, int),
        ('minutes', 25, 32, int),
        ]
    columns = ['name', 'start', 'end', 'type']
    variables = pandas.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = thinkstats2.FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(filename, skiprows=59)
    return df


def MakeBabyBoom():
    """Plot CDF of interarrival time on log and linear scales.
    """
    # compute the interarrival times
    df = ReadBabyBoom()
    diffs = df.minutes.diff()
    cdf = thinkstats2.Cdf(diffs, label='actual')

    thinkplot.PrePlot(cols=2)
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='minutes',
                     ylabel='CDF',
                     legend=False)

    thinkplot.SubPlot(2)
    thinkplot.Cdf(cdf, complement=True)
    thinkplot.Config(xlabel='minutes',
                     ylabel='CCDF',
                     yscale='log',
                     legend=False)

    thinkplot.Save(root='analytic_interarrivals')

    n = len(diffs)
    lam = 44 / 24 * 60.0
    sample = [random.expovariate(lam) for _ in range(n)]
    model = thinkstats2.Cdf(sample, label='model')
    
    thinkplot.PrePlot(2)
    thinkplot.Cdfs([cdf, model], complement=True)
    thinkplot.Save(root='analytic_interarrivals_model',
                   title='Time between births',
                   xlabel='minutes',
                   ylabel='CCDF',
                   yscale='log')


def MakeParetoCdf():
    """Generates a plot of the Pareto CDF."""
    xmin = 0.5

    thinkplot.PrePlot(3)
    for alpha in [2.0, 1.0, 0.5]:
        xs, ps = thinkstats2.RenderParetoCdf(xmin, alpha, 0, 10.0, n=100) 
        thinkplot.Plot(xs, ps, label='alpha=%g' % alpha)
    
    thinkplot.Save(root='analytic_pareto_cdf',
                   title='Pareto CDF',
                   xlabel='x',
                   ylabel='CDF')
    

def MakeParetoCdf2():
    """Generates a plot of the CDF of height in Pareto World."""
    xmin = 100
    alpha = 1.7    
    xs, ps = thinkstats2.RenderParetoCdf(xmin, alpha, 0, 1000.0, n=100) 
    thinkplot.Plot(xs, ps)

    median = ParetoMedian(xmin, alpha)

    thinkplot.Save(root='analytic_pareto_height',
                   title='Pareto CDF',
                   xlabel='height (cm)',
                   ylabel='CDF',
                   legend=False)
    

def MakeGaussianCdf():
    """Generates a plot of the gaussian CDF."""
    
    thinkplot.PrePlot(3)

    mus = [1.0, 2.0, 3.0]
    sigmas = [0.5, 0.4, 0.3]
    for mu, sigma in zip(mus, sigmas):
        xs, ps = thinkstats2.RenderGaussianCdf(mu=mu, sigma=sigma, 
                                               low=-1.0, high=4.0)
        label = 'mu=%g, sigma=%g' % (mu, sigma)
        thinkplot.Plot(xs, ps, label=label)

    thinkplot.Save(root='analytic_gaussian_cdf',
                   title='Gaussian CDF',
                   xlabel='x',
                   ylabel='CDF',
                   loc=2)
    
    
def MakeGaussianModel(weights):
    """Plot the CDF of birthweights with a gaussian model."""
    
    # estimate parameters: trimming outliers yields a better fit
    mu, var = thinkstats2.TrimmedMeanVar(weights, p=0.01)
    print('Mean, Var', mu, var)
    
    # plot the model
    sigma = math.sqrt(var)
    print('Sigma', sigma)
    xs, ps = thinkstats2.RenderGaussianCdf(mu, sigma, low=0, high=12.5)

    thinkplot.Plot(xs, ps, label='model', color='0.8')

    # plot the data
    cdf = thinkstats2.Cdf(weights, label='data')

    thinkplot.PrePlot(1)
    thinkplot.Cdf(cdf) 
    thinkplot.Save(root='analytic_birthwgt_model',
                   title='Birth weights',
                   xlabel='birth weight (lbs)',
                   ylabel='CDF')


def MakeExampleNormalPlot():
    """Generates a sample normal probability plot.
    """
    n = 1000
    thinkplot.PrePlot(3) 

    mus = [0, 1, 5]
    sigmas = [1, 1, 2]
    for mu, sigma in zip(mus, sigmas):
        sample = np.random.normal(mu, sigma, n)
        xs, ys = thinkstats2.NormalProbability(sample)
        label = 'mu=%d, sigma=%d' % (mu, sigma)
        thinkplot.Plot(xs, ys, label=label)

    thinkplot.Save(root='analytic_normal_prob_example',
                   title='Normal probability plot',
                   xlabel='standard normal sample',
                   ylabel='sample values')


def MakeNormalPlot(weights, term_weights):
    """Generates a normal probability plot of birth weights."""

    mean, var = thinkstats2.TrimmedMeanVar(weights, p=0.01)
    std = math.sqrt(var)

    xs = [-4, 4]
    xs, ys = thinkstats2.FitLine(xs, mean, std)
    thinkplot.Plot(xs, ys, linewidth=4, color='0.8')

    thinkplot.PrePlot(2) 
    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys, label='all live')

    xs, ys = thinkstats2.NormalProbability(term_weights)
    thinkplot.Plot(xs, ys, label='full term')
    thinkplot.Save(root='analytic_birthwgt_normal',
                   title='Normal probability plot',
                   xlabel='Standard deviations from mean',
                   ylabel='Birth weight (lbs)')


def main():
    thinkstats2.RandomSeed(18)
    MakeExampleNormalPlot()

    # make the analytic CDFs
    MakeExpoCdf()
    MakeBabyBoom()

    MakeParetoCdf()
    MakeParetoCdf2()
    MakeGaussianCdf()

    # test the distribution of birth weights for normality
    preg = nsfg.ReadFemPreg()
    full_term = preg[preg.prglngth >= 37]

    weights = preg.totalwgt_lb.dropna()
    term_weights = full_term.totalwgt_lb.dropna()

    MakeGaussianModel(weights)
    MakeNormalPlot(weights, term_weights)

    
if __name__ == "__main__":
    main()
