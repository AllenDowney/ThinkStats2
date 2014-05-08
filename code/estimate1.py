"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import math
import random
import numpy

from scipy import stats


def MeanError(estimates, actual):
    """Computes the mean error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float mean error
    """
    errors = [estimate-actual for estimate in estimates]
    return numpy.mean(errors)


def RMSE(estimates, actual):
    """Computes the root mean squared error of a sequence of estimates.

    estimate: sequence of numbers
    actual: actual value

    returns: float RMSE
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = numpy.mean(e2)
    return math.sqrt(mse)


def Estimate1(n=7, m=1000):
    mu = 0
    sigma = 1

    means = []
    medians = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        xbar = numpy.mean(xs)
        median = thinkstats2.Median(xs)
        means.append(xbar)
        medians.append(median)

    print 'Experiment 1'
    print 'rmse xbar', RMSE(means, mu)
    print 'rmse median', RMSE(medians, mu)


def Estimate2(n=7, m=1000):
    mu = 0
    sigma = 1

    estimates1 = []
    estimates2 = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        biased = numpy.var(xs)
        unbiased = numpy.var(xs, ddof=1)
        estimates1.append(biased)
        estimates2.append(unbiased)

    print 'Experiment 2'
    print 'mean error biased', MeanError(estimates1, sigma**2)
    print 'mean error unbiased', MeanError(estimates2, sigma**2)


def Estimate3(n=7, m=1000):
    lam = 2

    means = []
    medians = []
    for _ in range(m):
        xs = [random.expovariate(lam) for i in range(n)]
        L = 1 / numpy.mean(xs)
        Lm = math.log(2) / thinkstats2.Median(xs)
        means.append(L)
        medians.append(Lm)

    print 'Experiment 3'
    print 'rmse L', RMSE(means, lam)
    print 'rmse Lm', RMSE(medians, lam)
    print 'mean error L', MeanError(means, lam)
    print 'mean error Lm', MeanError(medians, lam)


def SimulateSample(mu=90, sigma=7.5, n=9, m=1000):
    
    means = []
    for j in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        xbar = numpy.mean(xs)
        means.append(xbar)

    print 'rmse', RMSE(means, mu)

    cdf = thinkstats2.MakeCdfFromList(means)
    print 'confidence interval', cdf.Percentile(5), cdf.Percentile(95) 

    # estimate the PDF by KDE
    pdf = thinkstats2.EstimatedPdf(means)
    stderr = sigma / math.sqrt(n)
    vals = numpy.linspace(mu-3*stderr, mu+3*stderr, 101)
    pmf = pdf.MakePmf(vals)
    #thinkplot.Pmf(pmf)

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimate1',
                   xlabel='sample mean',
                   ylabel='CDF',
                   title='Sampling distribution'
                   )


def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.

    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1

    # estimated goal-scoring rate is the actual number of goals scored
    L = goals
    return L


def Estimate4(lam=2.5, m=100):
    pmf = thinkstats2.Pmf()

    for i in range(m):
        L = SimulateGame(lam)
        pmf.Incr(L)

    pmf.Normalize()

    thinkplot.Hist(pmf)
    thinkplot.Show()
        

def main():
    random.seed(17)

    Estimate1()
    Estimate2()
    Estimate3(m=100000)
    SimulateSample()



if __name__ == '__main__':
    main()
