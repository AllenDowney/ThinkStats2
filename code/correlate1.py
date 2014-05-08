"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

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


def SimulateNull(xs, ys):
    random.shuffle(xs)
    random.shuffle(ys)
    return thinkstats2.Corr(xs, ys)


def PValue(xs, ys, n=10):
    actual = thinkstats2.Corr(xs, ys)

    xs_copy = list(xs)
    ys_copy = list(ys)

    corrs = []
    for i in range(n):
        corr = SimulateNull(xs_copy, ys_copy)
        corrs.append(corr)

    # what does the distribution of corrs look like?

    hits = [corr for corr in corrs if abs(corr) >= abs(actual)]
    p = len(hits) / float(n)
    return p


def main(name, data_dir='.'):
    xs, ys = ReadData(data_dir)

    thinkplot.Scatter(xs, ys, alpha=0.05)
    thinkplot.Save(root='correlate1',
                   xlabel='Age (years)',
                   ylabel='Birth weight (oz)',
                   axis=[9,45,0,250])

    print 'Pearson', thinkstats2.Corr(xs, ys)
    print 'Spearman', thinkstats2.SpearmanCorr(xs, ys)

    for i in range(10):
        print SimulateNull(list(xs), list(ys))

    print PValue(xs, ys, 1000)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
