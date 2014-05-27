"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function


def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank

scores = [55, 66, 77, 88, 99]
your_score = 88

print('score, percentile rank')
for score in scores:
    print(score, PercentileRank(scores, score))
print()

def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores.sort()
    index = percentile_rank * (len(scores)-1) / 100
    return scores[index]

print('prank, score, score')
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print(percentile_rank, 
          Percentile(scores, percentile_rank),
          Percentile2(scores, percentile_rank))


def EvalCdf(t, x):
    """Computes CDF(x) in a sample.

    t: sequence
    x: value

    returns: cumulative probability
    """
    count = 0.0
    for value in t:
        if value <= x:
            count += 1.0

    prob = count / len(t)
    return prob

t = [1, 2, 2, 3, 5]

print('x', 'CDF(x)')
for x in range(0, 7):
    print(x, EvalCdf(x, t))
