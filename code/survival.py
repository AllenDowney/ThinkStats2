"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import numpy as np
import pandas

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
        """Mean survival time."""
        return self.cdf.Mean()

    def Items(self):
        """Sorted list of (t, s) pairs."""
        return zip(self.ts, self.ss)

    def Render(self):
        """Generates a sequence of points suitable for plotting.

        returns: tuple of (sorted times, survival function)
        """
        return self.ts, self.ss

    def MakeHazard(self, label=''):
        """Computes the hazard function.

        sf: survival function

        returns: Pmf that maps times to hazard rates
        """
        ss = self.ss
        lams = {}
        for i, t in enumerate(self.ts[:-1]):
            hazard = (ss[i] - ss[i+1]) / ss[i]
            lams[t] = hazard

        return HazardFunction(lams, label=label)


class HazardFunction(object):
    """Represents a hazard function."""

    def __init__(self, d, label=''):
        """Initialize the hazard function.

        d: dictionary (or anything that can initialize a series)
        label: string
        """
        self.series = pandas.Series(d)
        self.label = label

    def __getitem__(self, t):
        return self.series[t]

    def Render(self):
        """Generates a sequence of points suitable for plotting.

        returns: tuple of (sorted times, hazard function)
        """
        return self.series.index, self.series.values

    def MakeSurvival(self):
        """Makes the survival function.

        returns: SurvivalFunction
        """
        ts = self.series.index
        ss = (1 - self.series).cumprod()
        cdf = thinkstats2.Cdf(ts, 1-ss)
        sf = SurvivalFunction(cdf)
        return sf

    def MakeSurvival2(self):
        """Makes the survival function.

        returns: SurvivalFunction
        """
        ts = self.series.index
        s = 1.0
        ps = []
        for lam in self.series:
            s *= 1-lam
            ps.append(1-s)

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


def PlotSurvival(complete):
    """Plots survival and hazard curves.

    complete: list of complete lifetimes
    """
    thinkplot.PrePlot(3, rows=2)

    cdf = thinkstats2.Cdf(complete, label='cdf')
    sf = SurvivalFunction(cdf, label='survival')
    print(cdf[13])
    print(sf[13])

    thinkplot.Plot(sf)
    thinkplot.Cdf(cdf, alpha=0.2)
    thinkplot.Config()

    thinkplot.SubPlot(2)
    hf = sf.MakeHazard(label='hazard')
    print(hf[39])
    thinkplot.Plot(hf)
    thinkplot.Config(ylim=[0, 0.75])


def PlotHazard(complete, ongoing):
    """Plots the hazard function and survival function.

    complete: list of complete lifetimes
    ongoing: list of ongoing lifetimes
    """
    # plot S(t) based on only complete pregnancies
    cdf = thinkstats2.Cdf(complete)
    sf = SurvivalFunction(cdf)
    thinkplot.Plot(sf, label='old S(t)', alpha=0.1)

    thinkplot.PrePlot(2)

    # plot the hazard function
    hf = EstimateHazardFunction(complete, ongoing)
    thinkplot.Plot(hf, label='lams(t)', alpha=0.5)

    # plot the survival function
    sf = hf.MakeSurvival()
    sf2 = hf.MakeSurvival2()
    print(sf.cdf == sf2.cdf)
    thinkplot.Plot(sf, label='S(t)')
    thinkplot.Show(xlabel='t (weeks)')


def EstimateHazardFunction(complete, ongoing):
    """Estimates the hazard function by Kaplan-Meier.

    http://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator

    complete: list of complete lifetimes
    ongoing: list of ongoing lifetimes
    """
    # pmf and sf of complete lifetimes
    n = len(complete)
    pmf_complete = thinkstats2.Pmf(complete)
    sf_complete = SurvivalFunction(thinkstats2.Cdf(complete))

    # sf for ongoing lifetimes
    m = len(ongoing)
    sf_curr = SurvivalFunction(thinkstats2.Cdf(ongoing))

    lams = {}
    for t, s in sf_complete.Items():
        ended = n * pmf_complete[t]
        at_risk = ended + n * s + m * sf_curr[t]
        print t, ended, at_risk
        lams[t] = ended / at_risk

    return HazardFunction(lams)


def PlotMarriageData():
    resp = chap01ex_soln.ReadFemResp()
    resp.cmmarrhx.replace([9997, 9998, 9999], np.nan, inplace=True)

    resp['agemarry'] = (resp.cmmarrhx - resp.cmbirth) / 12.0
    cdf = thinkstats2.Cdf(resp.agemarry)
    resp['age'] = (resp.cmintvw - resp.cmbirth) / 12.0
    cdf = thinkstats2.Cdf(resp.age)

    complete = resp[resp.evrmarry==1].agemarry
    ongoing = resp[resp.evrmarry==0].age

    hf = survival.EstimateHazardFunction(complete, ongoing)
    sf = hf.MakeSurvival()

    thinkplot.Plot(hf)
    thinkplot.Plot(sf)
    


def main():

    preg = nsfg.ReadFemPreg()
    print 'Number of pregnancies', len(preg)

    complete = preg.query('outcome in [1, 3, 4]').prglngth
    print 'Number of complete pregnancies', len(complete)
    ongoing = preg[preg.outcome==6].prglngth
    print 'Number of ongoing pregnancies', len(ongoing)

    PlotSurvival(complete)
    thinkplot.Save(root='survival1',
                   xlabel='t (weeks)')


    

    #PlotHazard(complete, ongoing)
    #PlotConditionalSurvival(complete)


if __name__ == '__main__':
    main()
