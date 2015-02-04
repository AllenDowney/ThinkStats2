"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkstats2
import thinkplot

import relay


def ObservedPmf(pmf, speed, label=None):
    """Returns a new Pmf representing speeds observed at a given speed.

    The chance of observing a runner is proportional to the difference
    in speed.

    Args:
        pmf: distribution of actual speeds
        speed: speed of the observing runner
        label: string label for the new dist

    Returns:
        Pmf object
    """
    new = pmf.Copy(label=label)
    for val in new.Values():
        diff = abs(val - speed)
        new.Mult(val, diff)
    new.Normalize()
    return new


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    speeds = relay.BinData(speeds, 3, 12, 100)

    # plot the distribution of actual speeds
    pmf = thinkstats2.Pmf(speeds, 'actual speeds')

    # plot the biased distribution seen by the observer
    biased = ObservedPmf(pmf, 7.5, label='observed speeds')

    thinkplot.Pmf(biased)
    thinkplot.Save(root='observed_speeds',
                   title='PMF of running speed',
                   xlabel='speed (mph)',
                   ylabel='PMF')

    cdf = thinkstats2.Cdf(pmf)
    cdf_biased = thinkstats2.Cdf(biased)

    thinkplot.PrePlot(2)
    thinkplot.Cdfs([cdf, cdf_biased])
    thinkplot.Save(root='observed_speeds_cdf',
                   title='CDF of running speed',
                   xlabel='speed (mph)',
                   ylabel='CDF')


if __name__ == '__main__':
    main()
