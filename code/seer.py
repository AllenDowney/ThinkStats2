"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys
import gzip
import math

import thinkstats2
import thinkplot

from table import Table, Record


class SeerTable(Table):
    """Represents the record table."""

    def ReadRecords(self, data_dir=None, n=None):
        if data_dir == None:
            data_dir = '.'
        filename = self.GetFilename()
        self.ReadFile(data_dir, filename, Record, n)
        self.Recode()

    def GetFilename(self):
        return 'BREAST.TXT.gz'

    def GetFields(self):
        """Returns a tuple specifying the fields to extract.

        The elements of the tuple are field, start, end, case.

                field is the name of the variable
                start and end are the indices as specified in the NSFG docs
                cast is a callable that converts the result to int, float, etc.

        Codes:
        sex: 1=male, 2=female
        age: years or 999
        seqno: 0 = only one primary in lifetime
        diagmo: 1-12
        diagyr: 1973+
        site:
        follow: 2 or 4 = active followup
        behavior: 3 = malignant
        race:
        hisp:
        stage: 
        survival: YYMM or 9999
        cause:
        status: 1=alive, 4=dead
        deathclass: 0=considered "alive"  1=death due to primary tumor

        The Survival Time Recode is calculated using the date of
        diagnosis and one of the following: date of death, date last known to
        be alive, or follow-up cutoff date used for this file (see title page
        for date for this file). Thus a person diagnosed in May 1976 and who
        died in May 1980 has a Survival Time Recode of 04 years and 00 months.

        """
        return [
            ('caseid', 1, 8, int),
            ('sex', 24, 24, int),
            ('age', 25, 27, int),
            ('seqno', 35, 36, int),
            ('diagmo', 37, 38, int),
            ('diagyr', 39, 42, int),
            ('site', 43, 46, int),
            ('follow', 181, 181, int),
            ('behavior', 215, 215, int),
            ('race', 224, 224, int),
            ('hisp', 225, 225, int),
            ('stage', 229, 230, int),
            ('survival', 241, 244, str),
            ('cause', 245, 249, int),
            ('status', 255, 255, int),
            ('deathclass', 264, 264, int),
            ]

    def Recode(self):
        """Computes recoded variables."""
        for r in self.records:
            # convert survival time in YYMM to decimal years
            years, months = int(r.survival[:2]), int(r.survival[2:])
            assert months < 12
            r.interval = years + months / 12.0

            r.diagdate = r.diagyr + r.diagmo / 12.0

    def MakeHists(self):
        """Makes a histogram for each attribute."""
        for field in self.GetFields():
            attr = field[0]
            if attr not in ['caseid', 'cause', 'survival']:
                self.MakeHist(attr)

    def MakeHist(self, attr):
        """Makes a histogram for the given attribute and prints it."""
        vals = [getattr(record, attr) for record in self.records]
        hist = thinkstats2.MakeHistFromList(vals)

        print attr
        for val, freq in hist.Items():
            print val, freq
        print

    def Filter(self):
        """Makes a new table with a subset of the records.

        Selects malignant tumors, patients with only one primary tumor
        in their lifetimes, and cases with active follow-up.
        """
        table = SeerTable()
        table.records = [r for r in self.records if (
                r.behavior == 3 and r.seqno == 0 and r.follow in [2, 4]
                )]
        return table

    def FilterAge(self, low, high):
        """Makes a new table with only records in the given age range."""
        table = SeerTable()
        table.records = [r for r in self.records if (
                low <= r.age < high
                )]
        return table

    def FilterDate(self, low, high):
        """Makes a new table with only records in the given age range."""
        table = SeerTable()
        table.records = [r for r in self.records if (
                low <= r.diagdate < high
                )]
        return table

    def FilterInterval(self, low):
        """Makes a new table with only records with interval > low."""
        table = SeerTable()
        table.records = [r for r in self.records if (
                r.interval >= low
                )]
        return table

    def MeanDiagDate(self):
        xs = [r.diagdate for r in self.records]
        return thinkstats2.Mean(xs)

    def ComputeHazard(self, t):
        """Computes the fraction of the cohort that dies at time t.

        If we use deathclass==1, we get the "Net cancer-specific survival".

        If we use status==4, we get "Observed all cause survival"

        The right stat for purposes of prognosis is Crude probability of death
        """
        deaths = [r for r in self.records if (
                r.interval == t and r.status==4
                )]
        d, n = len(deaths), len(self.records)
        return d, n, Fraction(d, n)

    def ComputeSurvivalCurve(self, high=20, factor=3, save_tables=False):
        """Estimates the survival curve and event density.

        Uses the Kaplan-Meier product-limit estimator:
        http://www.statsdirect.com/help/survival_analysis/kaplan.htm
        http://tkchen.wordpress.com/2008/09/21/
        kaplan-meier-and-nelson-aalen-estimators/

        Returns:
          tables: list of Table objects, conditioned on each value of t
          ts: times in years
          lams: Pmf representing the hazard function
          ss: list of values for the survival curve
        """
        lams = thinkstats2.Pmf(name='hazard')
        tables = []
        ts, ss = [], []
        prod = 1.0

        table = self
        intervals = set(r.interval for r in self.records)

        for t in sorted(intervals):
            if t > high:
                break

            # find the cohort at risk
            if save_tables:
                tables.append(table)
            table = table.FilterInterval(t)

            # find the number of deaths and death rate
            d, n, f = table.ComputeHazard(t)

            # find the cumulative probability of survival
            s = prod
            prod *= (1 - f)

            ts.append(t)
            ss.append(s)

            index = math.floor(t*factor) / factor
            lams.Incr(index, f)

        return tables, ts, lams, ss


def ComputeProbSurvival(ts, ss, t):
    """Given a survival curve, find the probability of survival >= t."""
    ps = [1-s for s in ss]
    cdf = thinkstats2.Cdf(ts, ps)
    s = 1 - cdf.Prob(t)
    return s


def ComputeConditionalSurvival(ts, tables):
    """Compute the probability of surviving an addition 5 or 10 years
    conditioned on surviving at least t.
    """
    ps = []
    newts = []

    for t, table in zip(ts, tables):
        if t>10:
            break

        _, ts, lams, ss = table.ComputeSurvivalCurve()        
        p5 = ComputeProbSurvival(ts, ss, t+5)
        p10 = ComputeProbSurvival(ts, ss, t+10)
        print t, p5, p10

        newts.append(t)
        ps.append((p5, p10))

    return newts, ps


def PlotConditionalSurvival(ts, ps):
    """Plot the probability of surviving an addition 5 or 10 years
    conditioned on surviving at least t.
    """
    thinkplot.Clf()
    p5s, p10s = zip(*ps)
    thinkplot.Plot(ts, p5s, linewidth=2, color='blue', label='5 years')
    thinkplot.Plot(ts, p10s, linewidth=2, color='green', label='10 years')
    thinkplot.Save(root='seer5',
                title='',
                xlabel='Survival time (years)',
                ylabel='Probability')


def PlotSurvivalCurve(ts, lams, ss):
    """
    
    ts: times in years
    lams: Pmf representing the hazard function
    ss: list of values for the survival curve
    """
    # scale lams
    denom = max(lams.Probs())
    lams.MultAll(1/denom)
    thinkplot.Pmf(lams, linewidth=2, linestyle='dashed', color='0.7')

    thinkplot.Plot(ts, ss, linewidth=2, color='blue', label='survival')
    thinkplot.Save(root='seer1',
                   title='',
                   xlabel='Survival time (years)',
                   ylabel='Probability')


def PlotDiagDates(ts, tables):
    """Plot the mean date of diagnosis for successive cohorts."""
    thinkplot.Clf()
    mus = [table.MeanDiagDate() for table in tables]
    thinkplot.Plot(ts, mus, linewidth=2, color='green')
    thinkplot.Save(root='seer2',
                title='',
                xlabel='Survival time (years)',
                ylabel='Mean diagnosis date')


def Fraction(n, m):
    return float(n) / m


def PartitionByAge(table):
    thinkplot.Clf()
    for age in [20, 30, 40, 50, 60, 70]:
        part = table.FilterAge(age, age+10)
        print age, len(part.records)
        _, ts, lams, ss = part.ComputeSurvivalCurve()
        thinkplot.Plot(ts, ss, linewidth=2, label=str(age))

    thinkplot.Save(root='seer3',
                xlabel='Survival time (years)',
                ylabel='Probability')


def PartitionByDate(table):
    thinkplot.Clf()
    for date in [1995, 1990, 1985, 1980, 1975, 1970]:
        part = table.FilterDate(date, date+5)
        print date, len(part.records)
        _, ts, lams, ss = part.ComputeSurvivalCurve()
        thinkplot.Plot(ts, ss, linewidth=2, label=str(date))

    thinkplot.Save(root='seer4',
                xlabel='Survival time (years)',
                ylabel='Probability')


def main(name, data_dir=None):
    table = SeerTable()
    table.ReadRecords(data_dir=data_dir, n=1000000)
    print 'Number of records', len(table.records)

    table.MakeHists()

    table = table.Filter()
    print 'Malignant, single primary with follow-up', len(table.records)

    #PartitionByAge(table)

    table = table.FilterAge(30, 39)
    print 'Age in 30s', len(table.records)

    tables, ts, lams, ss = table.ComputeSurvivalCurve(save_tables=True)

    PlotSurvivalCurve(ts, lams, ss)
    return

    PlotDiagDates(ts, tables)

    PartitionByDate(table)

    ts, ps = ComputeConditionalSurvival(ts, tables)
    PlotConditionalSurvival(ts, ps)


if __name__ == '__main__':
    main(*sys.argv)
