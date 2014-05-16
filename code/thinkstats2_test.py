"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import unittest
import random

import thinkstats2

class Test(unittest.TestCase):

    def testOdds(self):
        p = 0.75
        o = thinkstats2.Odds(p)
        self.assertEquals(o, 3)

        p = thinkstats2.Probability(o)
        self.assertEquals(p, 0.75)
        
        p = thinkstats2.Probability2(3, 1)
        self.assertEquals(p, 0.75)
        
    def testMean(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        self.assertEquals(mean, 100)

    def testVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean = thinkstats2.Mean(t)
        var1 = thinkstats2.Var(t)
        var2 = thinkstats2.Var(t, mean)
        
        self.assertAlmostEquals(mean, 100.0)
        self.assertAlmostEquals(var1, 48217.0)
        self.assertAlmostEquals(var2, 48217.0)

    def testMeanVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mean, var = thinkstats2.MeanVar(t)
        
        self.assertAlmostEquals(mean, 100.0)
        self.assertAlmostEquals(var, 48217.0)

    def testBinomialCoef(self):
        res = thinkstats2.BinomialCoef(10, 3)
        self.assertEquals(round(res), 120)

        res = thinkstats2.BinomialCoef(100, 4)
        self.assertEquals(round(res), 3921225)

    def testInterpolator(self):
        xs = [1, 2, 3]
        ys = [4, 5, 6]
        interp = thinkstats2.Interpolator(xs, ys)

        y = interp.Lookup(1)
        self.assertAlmostEquals(y, 4)

        y = interp.Lookup(2)
        self.assertAlmostEquals(y, 5)

        y = interp.Lookup(3)
        self.assertAlmostEquals(y, 6)

        y = interp.Lookup(1.5)
        self.assertAlmostEquals(y, 4.5)

        y = interp.Lookup(2.75)
        self.assertAlmostEquals(y, 5.75)

        x = interp.Reverse(4)
        self.assertAlmostEquals(x, 1)

        x = interp.Reverse(6)
        self.assertAlmostEquals(x, 3)

        x = interp.Reverse(4.5)
        self.assertAlmostEquals(x, 1.5)

        x = interp.Reverse(5.75)
        self.assertAlmostEquals(x, 2.75)

    def testTrim(self):
        t = range(100)
        random.shuffle(t)
        trimmed = thinkstats2.Trim(t, p=0.05)
        n = len(trimmed)
        self.assertEquals(n, 90)

    def testHist(self):
        hist = thinkstats2.MakeHistFromList('allen')
        self.assertEquals(hist.Freq('l'), 2)


if __name__ == "__main__":
    unittest.main()
