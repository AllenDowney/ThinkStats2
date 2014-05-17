"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""
Results:

On a log-log scale the tail of the CCDF looks like a straight line,
which suggests a Pareto distribution, but that turns out to be misleading.

On a log-x scale the distribution has the characteristic sigmoid of
a lognormal distribution.

The normal probability plot of log(sizes) confirms that the data fit the
lognormal model very well.

Many phenomena that have been described with Pareto models can be described
as well, or better, with lognormal models.

"""


import Cdf
import math
import myplot
import populations
import rankit
import thinkstats


def MakeFigures():
    pops = populations.ReadData()
    print len(pops)
    
    cdf = Cdf.MakeCdfFromList(pops, 'populations')

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='populations',
               title='City/Town Populations',
               xlabel='population',
               ylabel='CDF',
               legend=False)

    myplot.Clf()
    myplot.Cdf(cdf) 
    myplot.Save(root='populations_logx',
                title='City/Town Populations',
                xlabel='population',
                ylabel='CDF',
                xscale='log',
                legend=False)

    myplot.Clf()
    myplot.Cdf(cdf, complement=True) 
    myplot.Save(root='populations_loglog',
                title='City/Town Populations',
                xlabel='population',
                ylabel='Complementary CDF',
                yscale='log',
                xscale='log',
                legend=False)
    
    t = [math.log(x) for x in pops]
    t.sort()
    rankit.MakeNormalPlot(t, 'populations_rankit')


def main():
    MakeFigures()


if __name__ == "__main__":
    main()
