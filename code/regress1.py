"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import random
import survey
import thinkplot
import thinkstats2


def ReadData(data_dir='.'):
    preg = survey.Pregnancies()
    preg.ReadRecords(data_dir)
    print 'Number of pregnancies', len(preg.records)

    res = []
    for p in preg.records:
        if p.outcome == 1 and p.totalwgt_oz != 'NA':
            res.append((p.agepreg, p.totalwgt_oz))
    
    return zip(*res)


def Permute(fxs, fys, res):
    random.shuffle(res)
    inter, slope = thinkstats2.LeastSquares(fxs, fys + res)
    return inter, slope


def SamplingDistributions(fxs, fys, res, n=10):
    res_copy = list(res)

    t = []
    for i in range(n):
        estimates = Permute(fxs, fys, res)
        t.append(estimates)

    inters, slopes = zip(*t)
    inter_cdf = thinkstats2.MakeCdfFromList(inters)
    slope_cdf = thinkstats2.MakeCdfFromList(slopes)

    return inter_cdf, slope_cdf


def main(name, data_dir='.'):
    random.seed(17)
    
    xs, ys = ReadData(data_dir)
    inter = thinkstats2.Mean(ys)
    slope = 0
    fxs, fys = thinkstats2.FitLine(xs, inter, slope)
    res = thinkstats2.Residuals(xs, ys, inter, slope)

    inter_cdf, slope_cdf = SamplingDistributions(fxs, fys, res, n=1000)

    thinkplot.Cdf(slope_cdf)
    thinkplot.Save(root='regress1',
                   xlabel='Estimated slope (oz/year)',
                   ylabel='CDF',
                   title='Sampling distribution')

    return

    inter, slope = thinkstats2.LeastSquares(xs, ys)
    print 'inter', inter
    print 'slope', slope
    
    fxs, fys = thinkstats2.FitLine(xs, inter, slope)
    i = len(fxs) / 2
    print 'median weight, age', fxs[i], fys[i]

    res = thinkstats2.Residuals(xs, ys, inter, slope)
    R2 = thinkstats2.CoefDetermination(ys, res)
    print 'R2', R2
    print 'R', math.sqrt(R2)

    #thinkplot.Plot(fxs, fys, color='gray', alpha=0.5)
    #thinkplot.Scatter(xs, ys, alpha=0.05)
    #thinkplot.Show()

    inter_cdf, slope_cdf = SamplingDistributions(fxs, fys, res, n=1000)
    thinkplot.Cdf(slope_cdf)
    thinkplot.Save(root='regress1',
                   xlabel='Estimated slope (oz/year)',
                   ylabel='CDF',
                   title='Sampling distribution')


if __name__ == '__main__':
    import sys
    main(*sys.argv)
