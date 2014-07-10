"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import numpy as np

import nsfg
import thinkstats2
import thinkplot

"""

Outcome codes from http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611932

1	LIVE BIRTH	 	9148
2	INDUCED ABORTION	1862
3	STILLBIRTH	 	120
4	MISCARRIAGE	 	1921
5	ECTOPIC PREGNANCY	190
6	CURRENT PREGNANCY	352
"""

class SurvivalFunction(object):
    """Represents a survival function."""

    def __init__(self, cdf, label=''):
        self.cdf = cdf
        self.label = label or cdf.label

    @property
    def ts(self):
        return self.cdf.xs

    @property
    def ss(self):
        return 1 - self.cdf.ps

    def __getitem__(self, t):
        return self.Prob(t)

    def Prob(self, t):
        """Returns S(t), the probability that corresponds to value t.

        t: time

        returns: float probability
        """
        return 1 - self.cdf.Prob(t)

    def Mean(self):
        return self.cdf.Mean()

    def Items(self):
        return zip(self.ts, self.ss)

    def Render(self):
        """Generates a sequence of points suitable for plotting.

        returns: tuple of (sorted times, survival function)
        """
        return self.ts, self.ss

    def MakeHazard(self):
        """Computes the hazard function.

        sf: survival function

        returns: Pmf that maps times to hazard rates
        """
        ts, ss = self.ts, self.ss
        lams = {}
        for i in range(len(ts) - 1):
            hazard = (ss[i] - ss[i+1]) / ss[i]
            lams[ts[i]] = hazard

        return HazardFunction(lams)

    def GetCdf(self):
        """Cdf of durations from a survival curve.

        returns: Cdf of durations
        """
        return self.cdf


class HazardFunction(object):

    def __init__(self, d, label=''):
        self.d = d
        self.label = label

    def Items(self):
        """Gets an unsorted sequence of (value, freq/prob) pairs."""
        return self.d.items()

    def Render(self):
        """Generates a sequence of points suitable for plotting.

        returns: tuple of (sorted times, hazard function)
        """
        return zip(*sorted(self.Items()))

    def MakeSurvival(self):
        """Makes the survival function.

        returns: SurvivalFunction
        """
        s = 1.0
        res = []

        for t, lam in sorted(self.Items()):
            res.append((t, s))
            s *= 1-lam

        # TODO: should I be adding the last point?
        ts, ss = zip(*res)
        ps = 1 - np.asarray(ss)
        cdf = thinkstats2.Cdf(ts, ps)
        sf = SurvivalFunction(cdf)
        return sf


def ConditionalSurvival(pmf, t0):
    """Computes conditional survival function.

    Probability that duration exceeds t0+t, given that
    duration >= t0.

    pmf: Pmf of durations
    t0: minimum time

    returns: tuple of (ts, conditional survivals)
    """
    cond = thinkstats2.Pmf()
    for t, p in pmf.Items():
        if t >= t0:
            cond.Set(t-t0, p)

    return SurvivalFunction(thinkstats2.Cdf(cond))


def PlotSurvival(durations):
    """Plots survival and hazard curves.

    durations: list of durations
    """
    cdf = thinkstats2.Cdf(durations)
    thinkplot.Cdf(cdf, alpha=0.1)
    thinkplot.PrePlot(2)

    sf = SurvivalFunction(cdf)
    thinkplot.Plot(sf, label="S(t)")

    hf = sf.MakeHazard()
    thinkplot.Plot(hf, label='lam(t)')

    thinkplot.Show(xlabel='t (weeks)')


def PlotConditionalSurvival(durations):
    """Plots conditional survival curves for a range of t0.

    durations: list of durations
    """
    pmf = thinkstats2.Pmf(durations)
    
    times = [8, 16, 24, 32]
    thinkplot.PrePlot(len(times))

    for t0 in times:
        sf = ConditionalSurvival(pmf, t0)
        label = 't0=%d' % t0
        thinkplot.Plot(sf, label=label)

        print t0, sf.Mean()

    thinkplot.Show()


def PlotHazard(past, current):
    """Plots the hazard function and survival function.

    past: list of durations for complete pregnancies
    current: list of durations for current pregnancies
    """
    # plot S(t) based on only past pregnancies
    cdf = thinkstats2.Cdf(past)
    sf = SurvivalFunction(cdf)
    thinkplot.Plot(sf, label='old S(t)', alpha=0.1)

    thinkplot.PrePlot(2)

    # plot the hazard function
    hf = EstimateHazardFunction(past, current)
    thinkplot.Plot(hf, label='lams(t)', alpha=0.5)

    # plot the survival function
    sf = hf.MakeSurvival()
    thinkplot.Plot(sf, label='S(t)')
    thinkplot.Show(xlabel='t (weeks)')


def EstimateHazardFunction(past, current):
    """Estimates the hazard function by Kaplan-Meier.

    http://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator

    past: list of durations for complete pregnancies
    current: list of durations for current pregnancies    
    """
    # pmf and sf of known pregnancy lengths
    n = len(past)
    pmf_past = thinkstats2.Pmf(past)
    sf_past = SurvivalFunction(thinkstats2.Cdf(pmf_past))

    # sf for current pregnancies
    m = len(current)
    sf_curr = SurvivalFunction(thinkstats2.Cdf(current))

    lams = {}
    for t, s in sf_past.Items():
        ended = n * pmf_past[t]
        ongoing = n * s + m * sf_curr[t]
        at_risk = ended + ongoing
        hazard = ended / at_risk
        lams[t] = hazard

    return HazardFunction(lams)


def GetDurations(keep_codes):
    """Reads pregnancy durations from NSFG data.

    """
    preg = nsfg.ReadFemPreg()
    print 'Number of pregnancies', len(preg)

    hist = thinkstats2.Hist(preg.outcome)
    hist.Print()

    # TODO: include other outcomes?
    durations = preg.query('outcome in keep_codes').prglngth
    print 'Number of relevant pregnancies', len(durations)
    return durations


def main():
    past = GetDurations([1, 3, 4])
    current = GetDurations([6])
    PlotHazard(past, current)
    return

    durations = GetDurations([1, 3, 4])
    PlotSurvival(durations)
    PlotConditionalSurvival(durations)


if __name__ == '__main__':
    main()
