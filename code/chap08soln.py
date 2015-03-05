"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError


"""This file contains a solution to exercises in Think Stats:

Exercise 8.1

In this chapter we used $\xbar$ and median to estimate $\mu$, and
found that $\xbar$  yields lower MSE.
Also, we used $S^2$ and $S_{n-1}^2$ to estimate $\sigma$, and found that
$S^2$ is biased and $S_{n-1}^2$ unbiased.

Run similar experiments to see if $\xbar$ and median are biased estimates
of $\mu$.
Also check whether $S^2$ or $S_{n-1}^2$ yields a lower MSE.

My conclusions:

1) xbar and median yield lower mean error as m increases, so neither
one is obviously biased, as far as we can tell from the experiment.

2) The biased estimator of variance yields lower RMSE than the unbiased
estimator, by about 10%.  And the difference holds up as m increases.


Exercise 8.2

Suppose you draw a sample with size $n=10$ from a population 
with an exponential disrtribution with $\lambda=2$.  Simulate
this experiment 1000 times and plot the sampling distribution of
the estimate $\lamhat$.  Compute the standard error of the estimate
and the 90\% confidence interval.

Repeat the experiment with a few different values of $n$ and make
a plot of standard error versus $n$.

1) With sample size 10:

standard error 0.896717911545
confidence interval (1.2901330772324622, 3.8692334892427911)

2) As sample size increases, standard error and the width of
the CI decrease:

10      0.90    (1.3, 3.9)
100     0.21    (1.7, 2.4)
1000    0.06    (1.9, 2.1)

All three confidence intervals contain the actual value, 2.


Exercise 8.3

In games like hockey and soccer, the time between goals is
roughly exponential.  So you could estimate a team's goal-scoring rate
by observing the number of goals they score in a game.  This
estimation process is a little different from sampling the time
between goals, so let's see how it works.

Write a function that takes a goal-scoring rate, {\tt lam}, in goals
per game, and simulates a game by generating the time between goals
until the total time exceeds 1 game, then returns the number of goals
scored.

Write another function that simulates many games, stores the
estimates of {\tt lam}, then computes their mean error and RMSE.

Is this way of making an estimate biased?  Plot the sampling
distribution of the estimates and the 90\% confidence interval.  What
is the standard error?  What happens to sampling error for increasing
values of {\tt lam}?

My conclusions:

1) RMSE for this way of estimating lambda is 1.4

2) The mean error is small and decreases with m, so this estimator
appears to be unbiased.

One note: If the time between goals is exponential, the distribution
of goals scored in a game is Poisson.

See https://en.wikipedia.org/wiki/Poisson_distribution

"""

def Estimate1(n=7, m=100000):
    """Mean error for xbar and median as estimators of population mean.

    n: sample size
    m: number of iterations
    """
    mu = 0
    sigma = 1

    means = []
    medians = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        xbar = np.mean(xs)
        median = np.median(xs)
        means.append(xbar)
        medians.append(median)

    print('Experiment 1')
    print('mean error xbar', MeanError(means, mu))
    print('mean error median', MeanError(medians, mu))


def Estimate2(n=7, m=100000):
    """RMSE for biased and unbiased estimators of population variance.

    n: sample size
    m: number of iterations
    """
    mu = 0
    sigma = 1

    estimates1 = []
    estimates2 = []
    for _ in range(m):
        xs = [random.gauss(mu, sigma) for i in range(n)]
        biased = np.var(xs)
        unbiased = np.var(xs, ddof=1)
        estimates1.append(biased)
        estimates2.append(unbiased)

    print('Experiment 2')
    print('RMSE biased', RMSE(estimates1, sigma**2))
    print('RMSE unbiased', RMSE(estimates2, sigma**2))


def SimulateSample(lam=2, n=10, m=1000):
    """Sampling distribution of L as an estimator of exponential parameter.

    lam: parameter of an exponential distribution
    n: sample size
    m: number of iterations
    """
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)

    stderr = RMSE(estimates, lam)
    print('standard error', stderr)

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimation2',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')

    return stderr


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


def Estimate4(lam=2, m=1000000):

    estimates = []
    for i in range(m):
        L = SimulateGame(lam)
        estimates.append(L)

    print('Experiment 4')
    print('rmse L', RMSE(estimates, lam))
    print('mean error L', MeanError(estimates, lam))
    
    pmf = thinkstats2.Pmf(estimates)

    thinkplot.Hist(pmf)
    thinkplot.Show()
        

def main():
    thinkstats2.RandomSeed(17)

    Estimate1()
    Estimate2()

    print('Experiment 3')
    for n in [10, 100, 1000]:
        stderr = SimulateSample(n=n)
        print(n, stderr)

    Estimate4()


if __name__ == '__main__':
    main()
