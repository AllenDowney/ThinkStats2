"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys

import survey
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

def SurvivalFunction(cdf):
    """Computes a survival function.

    cdf: distribution of durations

    returns: tuple of (t, S(t))
    """
    ts, ps = cdf.Values(), cdf.Probs()

    ss = [1-p for p in ps]
    return ts, ss


def HazardFunction(ts, ss):
    """Computes the hazard function.

    ts: times
    ss: survival function S(t)

    returns: Pmf that maps times to hazard rates
    """
    lams = thinkstats2.Pmf()

    for i in range(len(ts) - 1):
        hazard = (ss[i] - ss[i+1]) / ss[i]
        lams.Set(ts[i], hazard)

    return lams


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

    return SurvivalFunction(thinkstats2.MakeCdfFromPmf(cond))


def DurationPmf(ts, ss):
    """Computes the Pmf of durations from a survival curve.

    ts: times
    ss: survival function S(t)

    returns: Pmf of durations
    """
    cdf = DurationCdf(ts, ss)
    pmf = thinkstats2.MakePmfFromCdf(cdf)
    return pmf


def DurationCdf(ts, ss):
    """Computes the Pmf of durations from a survival curve.

    ts: times
    ss: survival function S(t)

    returns: Cdf of durations
    """
    ps = [1-s for s in ss]
    cdf = thinkstats2.Cdf(ts, ps)
    return cdf


def GetDurations(data_dir, keep_codes):
    """Reads pregnancy durations from NSFG data.

    data_dir: location of the data file
    """
    preg = survey.Pregnancies()
    preg.ReadRecords(data_dir)
    print 'Number of pregnancies', len(preg.records)

    pmf = thinkstats2.Pmf()
    for record in preg.records:
        pmf.Incr(record.outcome)
        
    pmf.Print()

    durations = [record.prglength for record in preg.records
                 if record.outcome in keep_codes]

    print 'Number of relevant pregnancies', len(durations)
    return durations


def PlotSurvival(durations):
    """Plots survival and hazard curves.

    durations: list of durations
    """
    cdf = thinkstats2.MakeCdfFromList(durations)
    thinkplot.Cdf(cdf, alpha=0.1)
    thinkplot.PrePlot(2)

    ts, ss = SurvivalFunction(cdf)

    thinkplot.Plot(ts, ss, label="S(t)")

    haz_func = HazardFunction(ts, ss) 
    thinkplot.Pmf(haz_func, label='lam(t)')

    thinkplot.Show(xlabel='t (weeks)')


def PlotConditionalSurvival(durations):
    """Plots conditional survival curves for a range of t0.

    durations: list of durations
    """
    pmf = thinkstats2.MakePmfFromList(durations)
    
    times = [8, 16, 24, 32]
    thinkplot.PrePlot(len(times))

    for t0 in times:
        ts, ss = ConditionalSurvival(pmf, t0)
        label = 't0=%d' % t0
        thinkplot.Plot(ts, ss, label=label)

        duration_cdf = DurationCdf(ts, ss)
        print t0, duration_cdf.Mean()

    thinkplot.Show()


def PlotHazard(past, current):
    """Plots the hazard function and survival function.

    past: list of durations for complete pregnancies
    current: list of durations for current pregnancies
    """
    # plot S(t) based on only past pregnancies
    cdf = thinkstats2.MakeCdfFromList(past)
    ts, ss = SurvivalFunction(cdf)
    thinkplot.Plot(ts, ss, label='old S(t)', alpha=0.1)

    thinkplot.PrePlot(2)

    ts, lams = EstimateHazardFuncion(past, current)
    thinkplot.Plot(ts, lams, label='lams(t)', alpha=0.5)

    ts, ss = MakeSurvivalFromHazard(ts, lams)
    thinkplot.Plot(ts, ss, label='S(t)')
    thinkplot.Show(xlabel='t (weeks)')


def EstimateHazardFuncion(past, current):
    """Estimates the hazard function by Kaplan-Meier.

    http://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator

    past: list of durations for complete pregnancies
    current: list of durations for current pregnancies    
    """
    # pmf of pregnancies known to have ended at each timestep
    pmf = thinkstats2.MakePmfFromList(past)

    # survival curve for the known pregnancy lengths
    n = len(past)
    cdf_dur = thinkstats2.MakeCdfFromList(past)
    ts, ss = SurvivalFunction(cdf_dur)

    # CDF of duration for current pregnancies
    m = len(current)
    cdf_cur = thinkstats2.MakeCdfFromList(current)

    hazard_func = []

    for t, s in zip(ts, ss):
        ended = n * pmf.Prob(t)
        ongoing = n * s + m * (1 - cdf_cur.Prob(t))
        at_risk = ended + ongoing
        hazard = ended / at_risk
        hazard_func.append((t, hazard))

    return zip(*hazard_func)


def MakeSurvivalFromHazard(ts, lams):
    """Given a hazard function, make the survival function.
    
    ts: sequence of times
    lams: sequence of hazards

    returns: tuple of ts, ss
    """
    s = 1.0
    res = []

    for t, lam in zip(ts, lams):
        print t, s, lam
        res.append((t, s))
        s *= 1-lam

    return zip(*res)


def main(name, data_dir='.'):
    past = GetDurations(data_dir, [1, 3, 4])
    current = GetDurations(data_dir, [6])
    PlotHazard(past, current)
    return

    durations = GetDurations(data_dir, [1, 3, 4])
    PlotSurvival(durations)
    PlotConditionalSurvival(durations)


if __name__ == '__main__':
    main(*sys.argv)
