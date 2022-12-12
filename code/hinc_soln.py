"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import pandas

import hinc
import thinkplot
import thinkstats2

"""This file contains a solution to an exercise in Think Stats:

The distributions of wealth and income are sometimes modeled using
lognormal and Pareto distributions.  To see which is better, let's
look at some data.

The Current Population Survey (CPS) is joint effort of the Bureau
of Labor Statistics and the Census Bureau to study income and related
variables.  Data collected in 2013 is available from
http://www.census.gov/hhes/www/cpstables/032013/hhinc/toc.htm.
I downloaded hinc06.xls, which is an Excel spreadsheet with
information about household income, and converted it to hinc06.csv,
a CSV file you will find in the repository for this book.  You
will also find hinc.py, which reads the CSV file.

Extract the distribution of incomes from this dataset.  Are any of the
analytic distributions in this chapter a good model of the data?  A
solution to this exercise is in hinc_soln.py.

My solution generates three figures:

1) The CDF of income on a linear scale.

2) The CCDF on a log-log scale along with a Pareto model intended
to match the tail behavior.

3) The CDF on a log-x scale along with a lognormal model chose to
match the median and inter-quartile range.

My conclusions based on these figures are:

1) The Pareto model is probably a reasonable choice for the top
   10-20% of incomes.

2) The lognormal model captures the shape of the distribution better,
   but the data deviate substantially from the model.  With different
   choices for sigma, you could match the upper or lower tail, but not
   both at the same time.
 
In summary I would say that neither model captures the whole distribution,
so you might have to 

1) look for another analytic model, 
2) choose one that captures the part of the distribution that is most 
   relevent, or 
3) avoid using an analytic model altogether.

"""


class SmoothCdf(thinkstats2.Cdf):
    """Represents a CDF based on calculated quantiles.
    """
    def Render(self):
        """Because this CDF was not computed from a sample, it
        should not be rendered as a step function.
        """
        return self.xs, self.ps

    def Prob(self, x):
        """Compute CDF(x), interpolating between known values.
        """
        return np.interp(x, self.xs, self.ps)

    def Value(self, p):
        """Compute inverse CDF(x), interpolating between probabilities.
        """
        return np.interp(p, self.ps, self.xs)


def MakeFigures(df):
    """Plots the CDF of income in several forms.
    """
    xs, ps = df.income.values, df.ps.values
    cdf = SmoothCdf(xs, ps, label='data')
    cdf_log = SmoothCdf(np.log10(xs), ps, label='data')
    
    # linear plot
    thinkplot.Cdf(cdf) 
    thinkplot.Save(root='hinc_linear',
                   xlabel='household income',
                   ylabel='CDF')

    # pareto plot
    # for the model I chose parameters by hand to fit the tail
    xs, ys = thinkstats2.RenderParetoCdf(xmin=55000, alpha=2.5, 
                                         low=0, high=250000)
    thinkplot.Plot(xs, 1-ys, label='model', color='0.8')

    thinkplot.Cdf(cdf, complement=True) 
    thinkplot.Save(root='hinc_pareto',
                   xlabel='log10 household income',
                   ylabel='CCDF',
                   xscale='log',
                   yscale='log')

    # lognormal plot
    # for the model I estimate mu and sigma using 
    # percentile-based statistics
    median = cdf_log.Percentile(50)
    iqr = cdf_log.Percentile(75) - cdf_log.Percentile(25)
    std = iqr / 1.349

    # choose std to match the upper tail
    std = 0.35
    print(median, std)

    xs, ps = thinkstats2.RenderNormalCdf(median, std, low=3.5, high=5.5)
    thinkplot.Plot(xs, ps, label='model', color='0.8')

    thinkplot.Cdf(cdf_log) 
    thinkplot.Save(root='hinc_normal',
                   xlabel='log10 household income',
                   ylabel='CDF')
    

def main():
    df = hinc.ReadData()
    MakeFigures(df)


if __name__ == "__main__":
    main()
