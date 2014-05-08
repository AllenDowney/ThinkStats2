"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This file contains a solution to the Blink Monty Problem, by
Allen Downey:

Suppose you are on Let's Make a Deal and you are playing the Monty
Hall Game, with one difference: before you went on the show you
analyzed tapes of previous shows and discovered that Monty has a tell:
when the contestant picks the correct door, Monty is more likely to
blink.

Specifically, of the 15 shows you watched, the contestant chose the
correct door 5 times, and Monty blinked three of those times.  Of the
other 10 times, Monty blinked three times.

Assume that you choose Door A.  Monty opens door B and blinks.  What
should you do, and what is your chance of winning?


You can read a discussion of this problem at XXX

"""

import myplot
import Pmf


def MakeUniformSuite(low, high, steps, name=''):
    """Makes a PMF that represents a suite of hypotheses with equal p.
    
    Args:
        low: low end of range
        high: high end of range
        steps: number of values
        name: string name for the Pmf

    Returns:
        Pmf object
    """
    hypos = [low + (high-low) * i / (steps-1.0) for i in range(steps)]
    pmf = Pmf.MakePmfFromList(hypos, name=name)
    return pmf


def Update(suite, evidence):
    """Updates a suite of hypotheses based on new evidence.

    Modifies the suite directly; if you want to keep the original, make
    a copy.

    Args:
        suite: Pmf object
        evidence: whatever kind of object Likelihood expects
    """
    for hypo in suite.Values():
        likelihood = Likelihood(evidence, hypo)
        suite.Mult(hypo, likelihood)
    suite.Normalize()


def Likelihood(evidence, hypo):
    """Computes the likelihood of the evidence assuming the hypothesis is true.

    Args:
        evidence: a tuple of (number of successes, number of failures)
        hypo: float probability of success

    Returns:
        unnormalized likelihood of getting the given number of successes
        and failures if the probability of success is p
    """
    heads, tails = evidence
    p = hypo
    return pow(p, heads) * pow(1-p, tails)


def TotalProbability(pmf1, pmf2, func):
    """Enumerates pairs from the Pmfs, calls the func, and returns
    the total probability.

    pmf1: Pmf object
    pmf2: Pmf object
    func: a callable that takes a value from each Pmf and returns probability.
    """
    total = 0.0
    for x, px in pmf1.Items():
        for y, py in pmf2.Items():
            if px and py:
                total += px * py * func(x, y)
    return total


def ProbWinning(pbA, pbC):
    """Computes the probability that the car is behind door A:

    pbA: probability that Monty blinks if the car is behind A
    pbC: probability that Monty blinks if the car is behind C
    """
    pea = 0.5 * pbA
    pec = pbC

    pae = pea / (pea + pec)
    return pae


def main():
    print 'pae', 0.3 / (0.3 + 3.0 / 13)

    doorA = MakeUniformSuite(0.0, 1.0, 101, name='Door A')
    evidence = 3, 2
    Update(doorA, evidence)

    doorC = MakeUniformSuite(0.0, 1.0, 101, name='Door C')
    evidence = 3, 10
    Update(doorC, evidence)

    print TotalProbability(doorA, doorC, ProbWinning)

    # plot the posterior distributions
    myplot.Pmfs([doorA, doorC])
    myplot.Save(root='blinky',
                formats=['pdf', 'png'],
                title='Probability of blinking',
                xlabel='P(blink)',
                ylabel='Posterior probability')

if __name__ == '__main__':
    main()
