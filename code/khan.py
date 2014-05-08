"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import Pmf
import Cdf
import random
import myplot
import thinkstats

import matplotlib.pyplot as pyplot
import numpy
import scipy
import scipy.stats


def ChiSquared(expected, observed):
    """Compute the Chi-squared statistic for two tables.
    
    Args:
      expected: Hist of expected values
      observed: Hist of observed values
      
    Returns:
      float chi-squared statistic
    """
    total = 0.0
    for x, exp in expected.Items():
        obs = observed.Freq(x)
        total += (obs - exp)**2 / exp
    return total


def Simulate(pa, q, n):
    """Run a simulation.

    pa: probability of showing version A
    q:  probability of success for both A and B
    n:  number of trials
    
    Returns: tuple of
       diff_list: simulated differences
       chi2_list: simulated chi-square values
       pvalue_list: simulated p-values
    """
    hist = Pmf.Hist()
    diff_list = []
    chi2_list = []
    pvalue_list = []

    for i in range(1, n+1):
        version = Flip(pa, 'A', 'B')
        outcome = Flip(q, 'Y', 'N')
        hist.Incr((version, outcome))
        
        expected = Expected(pa, q, i)
        try:
            rate_a, rate_b = ComputeRates(hist)
            diff = rate_b - rate_a
            chi2 = ChiSquared(expected, hist)
            pvalue = Pvalue(chi2, df=3)

            diff_list.append((i, diff))
            chi2_list.append((i, chi2))
            pvalue_list.append((i, pvalue))
        except ZeroDivisionError:
            pass

    return diff_list, chi2_list, pvalue_list
        

def Flip(p, y='Y', n='N'):
    """Returns y with probability p; otherwise n."""
    return y if random.random() <= p else n


def ComputeRates(hist):
    """Returns a sequence of success rates, one for each version."""
    rates = []
    for version in ['A', 'B']:
        hits = hist.Freq((version, 'Y'))
        misses = hist.Freq((version, 'N'))
        rate = float(hits) / (hits + misses)
        rates.append(rate)

    return rates


def Expected(pa, q, n):
    """Makes a Pmf with the expected number of trials in each of four bins.

    pa: probability of offering version A
    q:  probability of success for both A and B
    n:  number of trials

    Returns:
      hist that maps (version, outcome) to expected number, where version
      is string A or B and outcome is string Y or N.
    """
    versions = Pmf.MakePmfFromDict(dict(A=pa, B=1-pa))
    outcomes = Pmf.MakePmfFromDict(dict(Y=q, N=1-q))

    hist = Pmf.Hist()
    for version, pp in versions.Items():
        for outcome, qq in outcomes.Items():
            hist.Incr((version, outcome), pp * qq * n)
    return hist


def Pvalue(chi2, df):
    """Returns the p-value of getting chi2 from a chi-squared distribution.

    chi2: observed chi-squared statistic
    df: degrees of freedom
    """
    return 1 - scipy.stats.chi2.cdf(chi2, df)


def Crosses(ps, thresh):
    """Tests whether a sequence of p-values ever drops below thresh."""
    if thresh is None:
        return False

    for p in ps:
        if p <= thresh:
            return True
    return False


def CheckCdf():
    """Compare chi2 values from simulation with chi2 distributions.
    """
    for df in [1, 2, 3]:
        xs, ys = Chi2Cdf(df=df, high=15)
        pyplot.plot(xs, ys, label=df)

    t = [SimulateChi2() for i in range(1000)]
    cdf = Cdf.MakeCdfFromList(t)

    myplot.Cdf(cdf)
    myplot.Save(root='khan3',
                xlabel='chi2 value',
                ylabel="CDF",
                formats=['png'])


def CheckCdf2():
    """Compare chi2 values from the simulation with a chi-squared dist."""
    df = 3
    t = [SimulateChi2() for i in range(1000)]
    t2 = [scipy.stats.chi2.cdf(x, df) for x in t]
    cdf = Cdf.MakeCdfFromList(t2)

    myplot.Cdf(cdf)
    myplot.Show()


def Chi2Cdf(df=2, high=5, n=100):
    """Evaluates the chi-squared CDF.

    df: degrees of freedom
    high: high end of the range of x
    n: number of values between 0 and high
    """
    xs = numpy.linspace(0, high, n)
    ys = scipy.stats.chi2.cdf(xs, df)
    return xs, ys


def SimulateChi2(pa=0.5, q=0.5, n=100):
    """Run a simulation and return the chi2 statistic."""
    expected = Expected(pa, q, n)

    simulated = Pmf.Hist()

    for i in range(1, n+1):
        version = Flip(pa, 'A', 'B')
        outcome = Flip(q, 'Y', 'N')
        simulated.Incr((version, outcome))

    chi2 = ChiSquared(expected, simulated)
    return chi2


def MakeSpaghetti(iters=1000, lines=100, n=300, thresh=0.05, index=2):
    """Makes a spaghetti plot of random-walk lines.
    
    iters: number of simulations to run
    lines: number of lines to plot
    n: number of trials to simulate
    thresh: threshold p-value
    """
    pyplot.clf()
    if thresh is not None:
        pyplot.plot([1,n], [thresh, thresh], color='red', alpha=1, linewidth=2)
    
    count = 0.0
    for i in range(iters):
        lists = Simulate(0.5, 0.5, n)
        pairs = lists[index]
        xs, ys = zip(*pairs)
        if Crosses(ys, thresh):
            count += 1

        if i < lines:
            pyplot.plot(xs, ys, alpha=0.2)
    
    print iters, count / iters

    labels = ['Difference in success rate', 'chi-squared stat', 'p-value']

    myplot.Save(root='khan%d' % index,
                xlabel='Number of trials',
                ylabel=labels[index],
                title='A-B test random walk',
                formats=['png']
                )

def main():
    CheckCdf()
    return

    random.seed(17)
    MakeSpaghetti(10, 10, 200, index=0, thresh=None)
    MakeSpaghetti(10, 10, 1000, index=1, thresh=None)
    MakeSpaghetti(20, 20, 1000, index=2, thresh=0.05)

if __name__ == "__main__":
    main()
