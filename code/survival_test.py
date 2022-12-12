"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import unittest
import survival

import thinkstats2
import thinkplot

class Test(unittest.TestCase):

    def testSurvival(self):
        complete = [1, 2, 3, 4, 5]
        ongoing = [3, 4, 5]
        hf = survival.EstimateHazardFunction(complete, ongoing)
        self.assertAlmostEqual(hf[3], 1/6.0)
        self.assertAlmostEqual(hf[5], 0.5)

        sf = hf.MakeSurvival()
        self.assertAlmostEqual(sf[3], 0.625)
        self.assertAlmostEqual(sf[5], 0.234375)


if __name__ == "__main__":
    unittest.main()
