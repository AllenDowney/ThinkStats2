"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import numpy
import urllib

import thinkplot
import thinkstats2

results = 'http://www.coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml'

"""
Sample line.

Place Div/Tot  Div   Guntime Nettime  Pace  Name                   Ag S Race# City/state              
===== ======== ===== ======= =======  ===== ====================== == = ===== ======================= 
   97  26/256  M4049   42:48   42:44   6:53 Allen Downey           42 M   337 Needham MA 
"""

def ConvertPaceToSpeed(pace):
    """Converts pace in MM:SS per mile to MPH."""
    m, s = [int(x) for x in pace.split(':')]
    secs = m*60 + s
    mph  = 1.0 / secs * 60 * 60 
    return mph


def CleanLine(line):
    """Converts a line from coolrunning results to a tuple of values."""
    t = line.split()
    if len(t) < 6:
        return None
    
    place, divtot, div, gun, net, pace = t[0:6]

    if not '/' in divtot:
        return None

    for time in [gun, net, pace]:
        if ':' not in time:
            return None

    return place, divtot, div, gun, net, pace


def ReadResults(url=results):
    """Read results from coolrunning and return a list of tuples."""
    results = []
    conn = urllib.urlopen(url)
    for line in conn.fp:
        t = CleanLine(line)
        if t:
            results.append(t)
    return results


def GetSpeeds(results, column=5):
    """Extract the pace column and return a list of speeds in MPH."""
    speeds = []
    for t in results:
        pace = t[column]
        speed = ConvertPaceToSpeed(pace)
        speeds.append(speed)
    return speeds


def BinData(data, low, high, n):
    """Rounds data off into bins.

    data: sequence of numbers
    low: low value
    high: high value
    n: number of bins

    returns: sequence of numbers
    """
    bins = numpy.linspace(low, high, n)
    data = (numpy.array(data) - low) / (high - low) * n
    data = numpy.round(data) * (high - low) / n + low
    return data


def main():

    results = ReadResults()
    speeds = GetSpeeds(results)

    # speeds = BinData(speeds, 3, 12, 100)

    pmf = thinkstats2.MakePmfFromList(speeds, 'speeds')

    thinkplot.Hist(pmf)
    thinkplot.Show(title='PMF of running speed',
               xlabel='speed (mph)',
               ylabel='probability')


if __name__ == '__main__':
    main()
