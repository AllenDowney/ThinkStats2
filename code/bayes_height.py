"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import numpy
import cPickle
import random

import brfss
import correlation
import Cdf
import myplot
import Pmf
import thinkstats
import rankit

import matplotlib.pyplot as pyplot


def MakeUniformPrior(t, num_points, label, spread=3.0):
    """Makes a prior distribution for mu and sigma based on a sample.

    t: sample
    num_points: number of values in each dimension
    label: string label for the new Pmf
    spread: number of standard errors to include

    Returns: Pmf that maps from (mu, sigma) to prob.
    """
    # estimate mean and stddev of t
    n = len(t)
    xbar, S2 = thinkstats.MeanVar(t)
    sighat = math.sqrt(S2)

    print xbar, sighat, sighat / xbar

    # compute standard error for mu and the range of ms
    stderr_xbar = sighat / math.sqrt(n)
    mspread = spread * stderr_xbar
    ms = numpy.linspace(xbar-mspread, xbar+mspread, num_points)

    # compute standard error for sigma and the range of ss
    stderr_sighat = sighat / math.sqrt(2 * (n-1))
    sspread = spread * stderr_sighat
    ss = numpy.linspace(sighat-sspread, sighat+sspread, num_points)

    # populate the PMF
    pmf = Pmf.Pmf(name=label)
    for m in ms:
        for s in ss:
            pmf.Set((m, s), 1)
    return ms, ss, pmf


def LogUpdate(suite, evidence):
    """Updates a suite of hypotheses based on new evidence.

    Modifies the suite directly; if you want to keep the original, make
    a copy.

    Args:
        suite: Pmf object
        evidence: whatever kind of object Likelihood expects
    """
    for hypo in suite.Values():
        likelihood = LogLikelihood(evidence, hypo)
        suite.Incr(hypo, likelihood)
    print suite.Total()


def LogLikelihood(evidence, hypo):
    """Computes the log likelihood of the evidence under the hypothesis.

    Args:
        evidence: a list of values
        hypo: tuple of hypothetical mu and sigma

    Returns:
        log likelihood of the sample given mu and sigma
    """
    t = evidence
    mu, sigma = hypo

    total = Summation(t, mu)
    return -len(t) * math.log(sigma) - total / 2 / sigma**2


def Summation(t, mu, cache={}):
    """Computes the sum of (x-mu)**2 for x in t.

    Caches previous results.

    t: tuple of values
    mu: hypothetical mean
    cache: cache of previous results
    """
    try:
        return cache[t, mu]
    except KeyError:
        ds = [(x-mu)**2 for x in t]
        total = sum(ds)
        cache[t, mu] = total
        return total


def EstimateParameters(t, label, num_points=31):
    """Computes the posterior distibution of mu and sigma.

    t: sequence of values
    label: string label for the suite of hypotheses
    num_points: number of values in each dimension

    Returns
      xs: sequence of hypothetical values for mu
      ys: sequence of hypothetical values for sigma
      suite: Pmf that maps from (mu, sigma) to prob
    """
    xs, ys, suite = MakeUniformPrior(t, num_points, label)

    suite.Log()
    LogUpdate(suite, tuple(t))
    suite.Exp()
    suite.Normalize()

    return xs, ys, suite


def ComputeMarginals(suite):
    """Computes the marginal distributions for mu and sigma.

    suite: Pmf that maps (x, y) to z

    Returns: Pmf objects for mu and sigma
    """
    pmf_m = Pmf.Pmf()
    pmf_s = Pmf.Pmf()
    for (m, s), p in suite.Items():
        pmf_m.Incr(m, p)
        pmf_s.Incr(s, p)
    return pmf_m, pmf_s


def ComputeCoefVariation(suite):
    """Computes the distribution of CV.

    suite: Pmf that maps (x, y) to z

    Returns: Pmf object for CV.
    """
    pmf = Pmf.Pmf()
    for (m, s), p in suite.Items():
        pmf.Incr(s/m, p)
    return pmf


def ProbBigger(pmf1, pmf2):
    """Returns the probability that a value from one pmf exceeds another."""
    total = 0.0
    for v1, p1 in pmf1.Items():
        for v2, p2 in pmf2.Items():
            if v1 > v2:
                total += p1 * p2
    return total


def PlotPosterior(xs, ys, suite, pcolor=False, contour=True):
    """Makes a contour plot.
    
    xs: sequence of values
    ys: sequence of values
    suite: Pmf that maps (x, y) to z
    """
    X, Y = numpy.meshgrid(xs, ys)
    func = lambda x, y: suite.Prob((x, y))
    prob = numpy.vectorize(func)
    Z = prob(X, Y)

    pyplot.clf()
    if pcolor:
        pyplot.pcolor(X, Y, Z)
    if contour:
        pyplot.contour(X, Y, Z)

    myplot.Save(root='bayes_height_posterior_%s' % suite.name,
                title='Posterior joint distribution',
                xlabel='Mean height (cm)',
                ylabel='Stddev (cm)')


def PlotCoefVariation(suites):
    """Plot the posterior distributions for CV.

    suites: map from label to Pmf of CVs.
    """
    pyplot.clf()

    pmfs = {}
    for label, suite in suites.iteritems():
        pmf = ComputeCoefVariation(suite)
        cdf = Cdf.MakeCdfFromPmf(pmf, label)
        myplot.Cdf(cdf)
    
        pmfs[label] = pmf

    myplot.Save(root='bayes_height_cv',
                title='Coefficient of variation',
                xlabel='cv',
                ylabel='CDF')

    print 'female bigger', ProbBigger(pmfs['female'], pmfs['male'])
    print 'male bigger', ProbBigger(pmfs['male'], pmfs['female'])


def PlotCdfs(samples):
    """Make CDFs showing the distribution of outliers."""
    cdfs = []
    for label, sample in samples.iteritems():
        outliers = [x for x in sample if x < 150]

        cdf = Cdf.MakeCdfFromList(outliers, label)
        cdfs.append(cdf)

    myplot.Clf()
    myplot.Cdfs(cdfs)
    myplot.Save(root='bayes_height_cdfs',
                title='CDF of height',
                xlabel='Reported height (cm)',
                ylabel='CDF')


def NormalProbPlot(samples):
    """Makes a normal probability plot for each sample in samples."""
    pyplot.clf()

    markers = dict(male='b', female='g')

    for label, sample in samples.iteritems():
        NormalPlot(sample, label, markers[label], jitter=0.0)
    
    myplot.Save(show=True,
                #root='bayes_height_normal',
                title='Normal probability plot',
                xlabel='Standard normal',
                ylabel='Reported height (cm)')


def NormalPlot(ys, label, color='b', jitter=0.0, **line_options):
    """Makes a normal probability plot.
    
    Args:
        ys: sequence of values
        label: string label for the plotted line
        color: color string passed along to pyplot.plot
        jitter: float magnitude of jitter added to the ys 
        line_options: dictionary of options for pyplot.plot        
    """
    n = len(ys)
    xs = [random.gauss(0.0, 1.0) for i in range(n)]
    xs.sort()
    ys = [y + random.uniform(-jitter, +jitter) for y in ys]
    ys.sort()

    inter, slope = correlation.LeastSquares(xs, ys)
    fit = correlation.FitLine(xs, inter, slope)
    pyplot.plot(*fit, color=color, linewidth=0.5, alpha=0.5)

    pyplot.plot(sorted(xs), sorted(ys),
                color=color,
                marker='.',
                label=label,
                markersize=3,
                alpha=0.1,
                **line_options)
 

def PlotMarginals(suite):
    """Plot the marginal distributions for a 2-D joint distribution."""
    pmf_m, pmf_s = ComputeMarginals(suite)

    pyplot.clf()
    pyplot.figure(1, figsize=(7, 4))

    pyplot.subplot(1, 2, 1)
    cdf_m = Cdf.MakeCdfFromPmf(pmf_m, 'mu')
    myplot.Cdf(cdf_m)
    pyplot.xlabel('Mean height (cm)')
    pyplot.ylabel('CDF')

    pyplot.subplot(1, 2, 2)
    cdf_s = Cdf.MakeCdfFromPmf(pmf_s, 'sigma')
    myplot.Cdf(cdf_s)
    pyplot.xlabel('Std Dev height (cm)')
    pyplot.ylabel('CDF')

    myplot.Save(root='bayes_height_marginals_%s' % suite.name)


def PlotAges(resp):
    """Plot the distribution of ages."""
    ages = [r.age for r in resp.records]
    cdf = Cdf.MakeCdfFromList(ages)
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Show()


def DumpHeights(data_dir='.', n=10000):
    """Read the BRFSS dataset, extract the heights and pickle them."""
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir, n)

    #PlotAges(resp)

    d = {1:[], 2:[]}
    [d[r.sex].append(r.htm3) for r in resp.records if r.htm3 != 'NA']

    fp = open('bayes_height_data.pkl', 'wb')
    cPickle.dump(d, fp)
    fp.close()


def LoadHeights():
    """Read the pickled height data."""
    fp = open('bayes_height_data.pkl', 'r')
    d = cPickle.load(fp)
    fp.close()
    return d


def Winsorize(xs, p=0.01):
    """Compresses outliers."""
    cdf = Cdf.MakeCdfFromList(xs)
    low, high = cdf.Value(p), cdf.Value(1-p)
    print low, high

    outliers = [x for x in xs if x < low or x > high]
    outliers.sort()
    print outliers

    wxs = [min(max(low, x), high) for x in xs]
    return wxs


def main():
    if False:
        random.seed(16)
        t = [random.gauss(3, 5) for i in range(100000)]
        EstimateParameters(t)
        return

    #DumpHeights(n=1000000)
    d = LoadHeights()

    labels = {1:'male', 2:'female'}

    samples = {}
    suites = {}
    for key, t in d.iteritems():
        label = labels[key]
        print label, len(t)

        t = Winsorize(t, 0.0001)
        samples[label] = t

        xs, ys, suite = EstimateParameters(t, label)
        suites[label] = suite

        PlotPosterior(xs, ys, suite)
        PlotMarginals(suite)

    #PlotCdfs(samples)
    #NormalProbPlot(samples)
    PlotCoefVariation(suites)


if __name__ == '__main__':
    main()
