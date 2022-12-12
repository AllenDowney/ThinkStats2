"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import first
import hypothesis
import scatter
import thinkstats2

import numpy as np


"""This file contains a solution to exercises in Think Stats:

As sample size increases, the power of a hypothesis test increases,
which means it is more likely to be positive if the effect is real.
Conversely, as sample size decreases, the test is less likely to
be positive even if the effect is real.

To investigate this behavior, run the tests in this chapter with
different subsets of the NSFG data.  You can use thinkstats2.SampleRows
to select a random subset of the rows in a DataFrame.

What happens to the p-values of these tests as sample size decreases?
What is the smallest sample size that yields a positive test?

My results:

test1: difference in mean pregnancy length
test2: difference in mean birth weight
test3: correlation of mother's age and birth weight
test4: chi-square test of pregnancy length

n       test1   test2   test2   test4
9148	0.16	0.00	0.00	0.00
4574	0.10	0.01	0.00	0.00
2287	0.25	0.06	0.00	0.00
1143	0.24	0.03	0.39	0.03
571	0.81	0.00	0.04	0.04
285	0.57	0.41	0.48	0.83
142	0.45	0.08	0.60	0.04

Conclusion: As expected, tests that are positive with large sample
sizes become negative as we take away data.  But the pattern is
erratic, with some positive tests even at small sample sizes.


In Section~\ref{testing}, we simulated the null hypothesis by
permutation; that is, we treated the observed values as if they
represented the entire population, and randomly assigned the
members of the population to the two groups.

An alternative is to use the sample to estimate the distribution for
the population, then draw a random sample from that distribution.
This process is called resampling.  There are several ways to
implement the resampling, but one of the simplest is to draw a sample,
with replacement, from the observed values, as in Section~\ref{power}.

Write a class named {\tt DiffMeansResample} that inherits from
{\tt DiffMeansPermute} and overrides {\tt RunModel} to implement
resampling, rather than permutation.

Use this model to test the differences in pregnancy length and
birth weight.  How much does the model affect the results?

Results:

means permute preglength
p-value = 0.1674
actual = 0.0780372667775
ts max = 0.226752436104

means permute birthweight
p-value = 0.0
actual = 0.124761184535
ts max = 0.112243501197


Conclusions: Using resampling instead of permutation has very
little effect on the results.

The two models are based on slightly difference assumptions, and in
this example there is no compelling reason to choose one or the other.
But in general p-values depend on the choice of the null hypothesis;
different models can yield very different results.


"""

class DiffMeansResample(hypothesis.DiffMeansPermute):
    """Tests a difference in means using resampling."""
    
    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2
  

def RunResampleTest(firsts, others):
    """Tests differences in means by resampling.

    firsts: DataFrame
    others: DataFrame
    """
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = hypothesis.DiffMeansPermute(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())


def RunTests(live, iters=1000):
    """Runs the tests from Chapter 9 with a subset of the data.

    live: DataFrame
    iters: how many iterations to run
    """
    n = len(live)
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    # compare pregnancy lengths
    data = firsts.prglngth.values, others.prglngth.values
    ht = hypothesis.DiffMeansPermute(data)
    p1 = ht.PValue(iters=iters)

    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = hypothesis.DiffMeansPermute(data)
    p2 = ht.PValue(iters=iters)

    # test correlation
    live2 = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live2.agepreg.values, live2.totalwgt_lb.values
    ht = hypothesis.CorrelationPermute(data)
    p3 = ht.PValue(iters=iters)

    # compare pregnancy lengths (chi-squared)
    data = firsts.prglngth.values, others.prglngth.values
    ht = hypothesis.PregLengthTest(data)
    p4 = ht.PValue(iters=iters)

    print('%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f' % (n, p1, p2, p3, p4))


def main():
    thinkstats2.RandomSeed(18)

    live, firsts, others = first.MakeFrames()
    RunResampleTest(firsts, others)

    n = len(live)
    for _ in range(7):
        sample = thinkstats2.SampleRows(live, n)
        RunTests(sample)
        n //= 2


if __name__ == '__main__':
    main()
