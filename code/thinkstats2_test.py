"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import unittest
import random

from collections import Counter
import numpy as np

import thinkstats2
import thinkplot

class Test(unittest.TestCase):

    def testOdds(self):
        p = 0.75
        o = thinkstats2.Odds(p)
        self.assertEqual(o, 3)

        p = thinkstats2.Probability(o)
        self.assertEqual(p, 0.75)
        
        p = thinkstats2.Probability2(3, 1)
        self.assertEqual(p, 0.75)
        
    def testMean(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        self.assertEqual(mean, 100)

    def testVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        var1 = thinkstats2.Var(t)
        var2 = thinkstats2.Var(t, mean)
        
        self.assertAlmostEqual(mean, 100.0)
        self.assertAlmostEqual(var1, 48217.0)
        self.assertAlmostEqual(var2, 48217.0)

    def testMeanVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean, var = thinkstats2.MeanVar(t)
        
        self.assertAlmostEqual(mean, 100.0)
        self.assertAlmostEqual(var, 48217.0)

    def testBinomialCoef(self):
        res = thinkstats2.BinomialCoef(10, 3)
        self.assertEqual(round(res), 120)

        res = thinkstats2.BinomialCoef(100, 4)
        self.assertEqual(round(res), 3921225)

    def testInterpolator(self):
        xs = [1, 2, 3]
        ys = [4, 5, 6]
        interp = thinkstats2.Interpolator(xs, ys)

        y = interp.Lookup(1)
        self.assertAlmostEqual(y, 4)

        y = interp.Lookup(2)
        self.assertAlmostEqual(y, 5)

        y = interp.Lookup(3)
        self.assertAlmostEqual(y, 6)

        y = interp.Lookup(1.5)
        self.assertAlmostEqual(y, 4.5)

        y = interp.Lookup(2.75)
        self.assertAlmostEqual(y, 5.75)

        x = interp.Reverse(4)
        self.assertAlmostEqual(x, 1)

        x = interp.Reverse(6)
        self.assertAlmostEqual(x, 3)

        x = interp.Reverse(4.5)
        self.assertAlmostEqual(x, 1.5)

        x = interp.Reverse(5.75)
        self.assertAlmostEqual(x, 2.75)

    def testTrim(self):
        t = list(range(100))
        random.shuffle(t)
        trimmed = thinkstats2.Trim(t, p=0.05)
        n = len(trimmed)
        self.assertEqual(n, 90)

    def testHist(self):
        hist = thinkstats2.Hist('allen')
        self.assertEqual(len(str(hist)), 38)

        self.assertEqual(len(hist), 4)
        self.assertEqual(hist.Freq('l'), 2)

        hist = thinkstats2.Hist(Counter('allen'))
        self.assertEqual(len(hist), 4)
        self.assertEqual(hist.Freq('l'), 2)

        hist2 = thinkstats2.Hist('nella')
        self.assertEqual(hist, hist2)

    def testPmf(self):
        pmf = thinkstats2.Pmf('allen')
        # this one might not be a robust test
        self.assertEqual(len(str(pmf)), 45)

        self.assertEqual(len(pmf), 4)
        self.assertEqual(pmf.Prob('l'), 0.4)
        self.assertEqual(pmf['l'], 0.4)
        self.assertEqual(pmf.Percentile(50), 'l')

        pmf = thinkstats2.Pmf(Counter('allen'))
        self.assertEqual(len(pmf), 4)
        self.assertEqual(pmf.Prob('l'), 0.4)

        pmf = thinkstats2.Pmf(pmf)
        self.assertEqual(len(pmf), 4)
        self.assertEqual(pmf.Prob('l'), 0.4)

        pmf2 = pmf.Copy()
        self.assertEqual(pmf, pmf2)

        xs, ys = pmf.Render()
        self.assertEqual(tuple(xs), tuple(sorted(pmf.Values())))

    def testSortedItems(self):
        pmf = thinkstats2.Pmf('allen')
        items = pmf.SortedItems()
        self.assertEqual(len(items), 4)

        pmf =  thinkstats2.Pmf(['a', float('nan'), 1, pmf])
        # should generate a warning
        items = pmf.SortedItems()
        self.assertEqual(len(items), 4)

    def testPmfAddSub(self):
        pmf = thinkstats2.Pmf([1, 2, 3, 4, 5, 6])

        pmf1 = pmf + 1
        self.assertAlmostEqual(pmf1.Mean(), 4.5)

        pmf2 = pmf + pmf
        self.assertAlmostEqual(pmf2.Mean(), 7.0)

        pmf3 = pmf - 1
        self.assertAlmostEqual(pmf3.Mean(), 2.5)

        pmf4 = pmf - pmf
        self.assertAlmostEqual(pmf4.Mean(), 0)

    def testPmfMulDiv(self):
        pmf = thinkstats2.Pmf([1, 2, 3, 4, 5, 6])

        pmf1 = pmf * 2
        self.assertAlmostEqual(pmf1.Mean(), 7)

        pmf2 = pmf * pmf
        self.assertAlmostEqual(pmf2.Mean(), 12.25)

        pmf3 = pmf / 2
        self.assertAlmostEqual(pmf3.Mean(), 1.75)

        pmf4 = pmf / pmf
        self.assertAlmostEqual(pmf4.Mean(), 1.4291667)

    def testPmfProbLess(self):
        d6 = thinkstats2.Pmf(range(1,7))
        self.assertEqual(d6.ProbLess(4), 0.5)
        self.assertEqual(d6.ProbGreater(3), 0.5)
        two = d6 + d6
        three = two + d6
        # Pmf no longer supports magic comparators
        self.assertAlmostEqual(two.ProbGreater(three), 0.15200617284)
        self.assertAlmostEqual(two.ProbLess(three), 0.778549382716049)

    def testPmfMax(self):
        d6 = thinkstats2.Pmf(range(1,7))
        two = d6 + d6
        three = two + d6
        cdf = three.Max(6)
        thinkplot.Cdf(cdf)
        self.assertAlmostEqual(cdf[14], 0.558230962626)

    def testCdf(self):
        t = [1, 2, 2, 3, 5]
        pmf = thinkstats2.Pmf(t)
        hist = thinkstats2.Hist(t)

        cdf = thinkstats2.Cdf(pmf)
        self.assertEqual(len(str(cdf)), 37)

        self.assertEqual(cdf[0], 0)
        self.assertAlmostEqual(cdf[1], 0.2)
        self.assertAlmostEqual(cdf[2], 0.6)
        self.assertAlmostEqual(cdf[3], 0.8)
        self.assertAlmostEqual(cdf[4], 0.8)
        self.assertAlmostEqual(cdf[5], 1)
        self.assertAlmostEqual(cdf[6], 1)

        xs = range(-1, 7)
        ps = cdf.Probs(xs)
        for p1, p2 in zip(ps, [0, 0, 0.2, 0.6, 0.8, 0.8, 1, 1]):
            self.assertAlmostEqual(p1, p2)

        self.assertEqual(cdf.Value(0), 1)
        self.assertEqual(cdf.Value(0.1), 1)
        self.assertEqual(cdf.Value(0.2), 1)
        self.assertEqual(cdf.Value(0.3), 2)
        self.assertEqual(cdf.Value(0.4), 2)
        self.assertEqual(cdf.Value(0.5), 2)
        self.assertEqual(cdf.Value(0.6), 2)
        self.assertEqual(cdf.Value(0.7), 3)
        self.assertEqual(cdf.Value(0.8), 3)
        self.assertEqual(cdf.Value(0.9), 5)
        self.assertEqual(cdf.Value(1), 5)

        ps = np.linspace(0, 1, 11)
        xs = cdf.ValueArray(ps)
        self.assertTrue((xs == [1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5]).all())

        np.random.seed(17)
        xs = cdf.Sample(7)
        self.assertListEqual(xs.tolist(), [2, 2, 1, 1, 3, 3, 3])

        # when you make a Cdf from a Pdf, you might get some floating
        # point representation error
        self.assertEqual(len(cdf), 4)
        self.assertAlmostEqual(cdf.Prob(2), 0.6)
        self.assertAlmostEqual(cdf[2], 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.MakeCdfFromPmf(pmf)
        self.assertEqual(len(cdf), 4)
        self.assertAlmostEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.MakeCdfFromItems(pmf.Items())
        self.assertEqual(len(cdf), 4)
        self.assertAlmostEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(pmf.d)
        self.assertEqual(len(cdf), 4)
        self.assertAlmostEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.MakeCdfFromDict(pmf.d)
        self.assertEqual(len(cdf), 4)
        self.assertAlmostEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(hist)
        self.assertEqual(len(cdf), 4)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.MakeCdfFromHist(hist)
        self.assertEqual(len(cdf), 4)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(t)
        self.assertEqual(len(cdf), 4)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.MakeCdfFromList(t)
        self.assertEqual(len(cdf), 4)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf = thinkstats2.Cdf(Counter(t))
        self.assertEqual(len(cdf), 4)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Value(0.6), 2)

        cdf2 = cdf.Copy()
        self.assertEqual(cdf2.Prob(2), 0.6)
        self.assertEqual(cdf2.Value(0.6), 2)
        
    def testShift(self):
        t = [1, 2, 2, 3, 5]
        cdf = thinkstats2.Cdf(t)
        cdf2 = cdf.Shift(1)
        self.assertEqual(cdf[1], cdf2[2])

    def testScale(self):
        t = [1, 2, 2, 3, 5]
        cdf = thinkstats2.Cdf(t)
        cdf2 = cdf.Scale(2)
        self.assertEqual(cdf[2], cdf2[4])

    def testCdfRender(self):
        t = [1, 2, 2, 3, 5]
        cdf = thinkstats2.Cdf(t)
        xs, ps = cdf.Render()
        self.assertEqual(xs[0], 1)
        self.assertEqual(ps[2], 0.2)
        self.assertEqual(sum(xs), 22)
        self.assertEqual(sum(ps), 4.2)
        
    def testPmfFromCdf(self):
        t = [1, 2, 2, 3, 5]
        pmf = thinkstats2.Pmf(t)
        cdf = thinkstats2.Cdf(pmf)
        pmf2 = thinkstats2.Pmf(cdf)
        for x in pmf.Values():
            self.assertAlmostEqual(pmf[x], pmf2[x])

        pmf3 = cdf.MakePmf()
        for x in pmf.Values():
            self.assertAlmostEqual(pmf[x], pmf3[x])

    def testNormalPdf(self):
        pdf = thinkstats2.NormalPdf(mu=1, sigma=2)
        self.assertEqual(len(str(pdf)), 29)
        self.assertAlmostEqual(pdf.Density(3), 0.12098536226)

        pmf = pdf.MakePmf()
        self.assertAlmostEqual(pmf[1.0], 0.0239951295619)
        xs, ps = pdf.Render()
        self.assertEqual(xs[0], -5.0)
        self.assertAlmostEqual(ps[0], 0.0022159242059690038)

        pmf = thinkstats2.Pmf(pdf)
        self.assertAlmostEqual(pmf[1.0], 0.0239951295619)
        xs, ps = pmf.Render()
        self.assertEqual(xs[0], -5.0)
        self.assertAlmostEqual(ps[0], 0.00026656181123)
        
        cdf = thinkstats2.Cdf(pdf)
        self.assertAlmostEqual(cdf[1.0], 0.51199756478094904)
        xs, ps = cdf.Render()
        self.assertEqual(xs[0], -5.0)
        self.assertAlmostEqual(ps[0], 0.0)
        
    def testExponentialPdf(self):
        pdf = thinkstats2.ExponentialPdf(lam=0.5)
        self.assertEqual(len(str(pdf)), 24)
        self.assertAlmostEqual(pdf.Density(3), 0.11156508007421491)
        pmf = pdf.MakePmf()
        self.assertAlmostEqual(pmf[1.0], 0.02977166586593202)
        xs, ps = pdf.Render()
        self.assertEqual(xs[0], 0.0)
        self.assertAlmostEqual(ps[0], 0.5)
        
    def testEstimatedPdf(self):
        pdf = thinkstats2.EstimatedPdf([1, 2, 2, 3, 5])
        self.assertEqual(len(str(pdf)), 30)
        self.assertAlmostEqual(pdf.Density(3)[0], 0.19629968)
        pmf = pdf.MakePmf()
        self.assertAlmostEqual(pmf[1.0], 0.010172282816895044)        
        pmf = pdf.MakePmf(low=0, high=6)
        self.assertAlmostEqual(pmf[0.0], 0.0050742294053582942)
        
    def testEvalNormalCdf(self):
        p = thinkstats2.EvalNormalCdf(0)
        self.assertAlmostEqual(p, 0.5)

        p = thinkstats2.EvalNormalCdf(2, 2, 3)
        self.assertAlmostEqual(p, 0.5)

        p = thinkstats2.EvalNormalCdf(1000, 0, 1)
        self.assertAlmostEqual(p, 1.0)

        p = thinkstats2.EvalNormalCdf(-1000, 0, 1)
        self.assertAlmostEqual(p, 0.0)

        x = thinkstats2.EvalNormalCdfInverse(0.95, 0, 1)
        self.assertAlmostEqual(x, 1.64485362695)
        x = thinkstats2.EvalNormalCdfInverse(0.05, 0, 1)
        self.assertAlmostEqual(x, -1.64485362695)

    def testEvalPoissonPmf(self):
        p = thinkstats2.EvalPoissonPmf(2, 1)
        self.assertAlmostEqual(p, 0.1839397205)

    def testCov(self):
        t = [0, 4, 7, 3, 8, 1, 6, 2, 9, 5]
        a = np.array(t)
        t2 = [5, 4, 3, 0, 8, 9, 7, 6, 2, 1]

        self.assertAlmostEqual(thinkstats2.Cov(t, a), 8.25)
        self.assertAlmostEqual(thinkstats2.Cov(t, -a), -8.25)

        self.assertAlmostEqual(thinkstats2.Corr(t, a), 1)
        self.assertAlmostEqual(thinkstats2.Corr(t, -a), -1)
        self.assertAlmostEqual(thinkstats2.Corr(t, t2), -0.1878787878)
        
        self.assertAlmostEqual(thinkstats2.SpearmanCorr(t, -a), -1)
        self.assertAlmostEqual(thinkstats2.SpearmanCorr(t, t2), -0.1878787878)
        
    def testReadStataDct(self):
        dct = thinkstats2.ReadStataDct('2002FemPreg.dct')
        self.assertEqual(len(dct.variables), 243)
        self.assertEqual(len(dct.colspecs), 243)
        self.assertEqual(len(dct.names), 243)
        self.assertEqual(dct.colspecs[-1][1], -1)

    def testCdfProbs(self):
        t = [-1, 1, 2, 2, 3, 5]
        cdf = thinkstats2.Cdf(t)
        ps = cdf.Probs(t)
        print(ps)

    def testPmfOfHist(self):
        bowl1 = thinkstats2.Hist(dict(vanilla=30, chocolate=10))
        bowl2 = thinkstats2.Hist(dict(vanilla=20, chocolate=20))
        pmf = thinkstats2.Pmf([bowl1, bowl2])
        pmf.Print()

if __name__ == "__main__":
    unittest.main()
