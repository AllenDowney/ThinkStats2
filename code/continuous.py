"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import erf
import Cdf
import cumulative
import math
import myplot
import random
import rankit
import thinkstats
import matplotlib.pyplot as pyplot

def ExpoCdf(x, lam):
    """Evaluates CDF of the exponential distribution with parameter lam."""
    return 1 - math.exp(-lam * x)

def ParetoCdf(x, alpha, xmin):
    """Evaluates CDF of the Pareto distribution with parameters alpha, xmin."""
    if x < xmin:
        return 0
    return 1 - pow(x / xmin, -alpha)

def ParetoMedian(xmin, alpha):
    """Computes the median of a Pareto distribution."""
    return xmin * pow(2, 1/alpha)

def MakeExpoCdf():
    """Generates a plot of the exponential CDF."""
    n = 40
    max = 2.5
    xs = [max*i/n for i in range(n)]
    
    lam = 2.0
    ps = [ExpoCdf(x, lam) for x in xs]
    
    percentile = -math.log(0.05) / lam
    print 'Fraction <= ', percentile, ExpoCdf(lam, percentile)

    pyplot.clf()
    pyplot.plot(xs, ps, linewidth=2)
    myplot.Save('expo_cdf',
                title='Exponential CDF',
                xlabel='x',
                ylabel='CDF',
                legend=False)
    
def MakeParetoCdf():
    """Generates a plot of the Pareto CDF."""
    n = 50
    max = 10.0
    xs = [max*i/n for i in range(n)]
    
    xmin = 0.5
    alpha = 1.0
    ps = [ParetoCdf(x, alpha, xmin) for x in xs]
    print 'Fraction <= 10', ParetoCdf(xmin, alpha, 10)
    
    pyplot.clf()
    pyplot.plot(xs, ps, linewidth=2)
    myplot.Save('pareto_cdf',
                title = 'Pareto CDF',
                xlabel = 'x',
                ylabel = 'CDF',
                legend=False)
    

def MakeParetoCdf2():
    """Generates a plot of the CDF of height in Pareto World."""
    n = 50
    max = 1000.0
    xs = [max*i/n for i in range(n)]
    
    xmin = 100
    alpha = 1.7
    ps = [ParetoCdf(x, alpha, xmin) for x in xs]
    print 'Median', ParetoMedian(xmin, alpha)
    
    pyplot.clf()
    pyplot.plot(xs, ps, linewidth=2)
    myplot.Save('pareto_height',
                title='Pareto CDF',
                xlabel='height (cm)',
                ylabel='CDF',
                legend=False)
    


def RenderNormalCdf(mu, sigma, max, n=50):
    """Generates sequences of xs and ps for a normal CDF."""
    xs = [max * i / n for i in range(n)]    
    ps = [erf.NormalCdf(x, mu, sigma) for x in xs]
    return xs, ps


def MakeNormalCdf():
    """Generates a plot of the normal CDF."""
    xs, ps = RenderNormalCdf(2.0, 0.5, 4.0)
    
    pyplot.clf()
    pyplot.plot(xs, ps, linewidth=2)
    myplot.Save('normal_cdf',
              title='Normal CDF',
              xlabel='x',
              ylabel='CDF',
              legend=False)
    
    
def MakeNormalModel(weights):
    """Plot the CDF of birthweights with a normal model."""
    
    # estimate parameters: trimming outliers yields a better fit
    mu, var = thinkstats.TrimmedMeanVar(weights, p=0.01)
    print 'Mean, Var', mu, var
    
    # plot the model
    sigma = math.sqrt(var)
    print 'Sigma', sigma
    xs, ps = RenderNormalCdf(mu, sigma, 200)

    pyplot.clf()
    pyplot.plot(xs, ps, label='model', linewidth=4, color='0.8')

    # plot the data
    cdf = Cdf.MakeCdfFromList(weights)
    xs, ps = cdf.Render()
    pyplot.plot(xs, ps, label='data', linewidth=2, color='blue')
 
    myplot.Save('nsfg_birthwgt_model',
                title='Birth weights',
                xlabel='birth weight (oz)',
                ylabel='CDF')


def MakeNormalPlot(weights):
    """Generates a normal probability plot of birth weights."""
    rankit.MakeNormalPlot(weights, 
                          root='nsfg_birthwgt_normal',
                          ylabel='Birth weights (oz)',)

def main():
    random.seed(17)

    # make the continuous CDFs
    MakeExpoCdf()
    MakeParetoCdf()
    MakeParetoCdf2()
    MakeNormalCdf()

    # test the distribution of birth weights for normality
    pool, _, _ = cumulative.MakeTables()
    
    t = pool.weights
    MakeNormalModel(t)
    MakeNormalPlot(t)

    
if __name__ == "__main__":
    main()
