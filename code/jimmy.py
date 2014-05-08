"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import random
import thinkstats2


def SimulateSample(expected, cdf, num_nuts, factor=10, stir=-1):
    """Generates a Hist of simulated nuts.
    
    Args:
      expected: Pmf of expected values
      cdf: cdf of expected values
      num_nuts: number of nuts in the sample
      factor: how much to multiply the frequencies
      stir: how much to stir the simulated vat of nuts 
            (-1 means perfect mixing)

    Returns:
      Hist object
    """
    if stir == -1:
        t = cdf.Sample(num_nuts)
    else:
        vat = MakeVat(expected, num_nuts, factor=factor, stir=stir)
        t = vat[:num_nuts]

    #print stir, PercentAdjacent(t)
    hist = thinkstats2.MakeHistFromList(t)
    return hist


def ChiSquared(expected, observed):
    """Compute the Chi-squared statistic for two tables.
    
    Args:
      expected: Hist of expected values
      observed: Hist of observed values
      
    Returns:
      float chi-squared statistic
    """
    total = 0.0
    for x, exp in expected.Items():
        obs = observed.Freq(x)
        total += (obs - exp)**2 / exp
    return total


def Test(expected, observed, num_trials=1000, stir=-1):
    """Run a simulation to estimate the p-value of the observed values.

    Args:
      expected: Hist of expected values
      observed: Hist of observed values
      num_trials: how many simulations to run
      stir: how much to stir the simulated vat of nuts 
            (-1 means perfect mixing)

    Returns:
      float p-value
    """

    # compute the chi-squared stat
    threshold = ChiSquared(expected, observed)
    print 'chi-squared', threshold

    print 'simulated %d trials' % num_trials
    chi2s = []
    count = 0.0
    num_nuts = observed.Total()
    cdf = thinkstats2.MakeCdfFromHist(expected)

    for _ in range(num_trials):
        simulated = SimulateSample(expected, cdf, num_nuts, stir=stir)
        chi2 = ChiSquared(expected, simulated)
        chi2s.append(chi2)
        if chi2 >= threshold:
            count += 1
            
    print 'max chi2', max(chi2s)
    
    pvalue = count / num_trials
    print 'p-value', pvalue

    return pvalue


def ConvertToCount(sample, count_per):
    """Convert from weight to count.

    sample: Hist or Pmf that maps from category to weight in pounds
    count_per: dictionary that maps from category to count per ounce
    """
    for value, count in sample.Items():
        sample.Mult(value, 16 * count_per[value])


def MakeVat(expected, num_nuts, factor=10, stir=0.0):
    """Makes a list of nuts with the given amount of stirring.

    Args:
      expected: Hist of expected values
      num_nuts: number of nuts in the sample
      factor: how much to multiply the frequencies
      stir: how much to stir the simulated vat of nuts, in number
            of swaps per nut (-1 means perfect mixing)

    Returns: list of nuts
    """
    t = []
    for value, freq in expected.Items():
        t.extend([value] * int(freq * factor))

    if stir == -1:
        random.shuffle(t)
    else:
        [RandomSwap(t) for i in xrange(int(num_nuts*factor*stir))]
    
    return t


def RandomSwap(t):
    """Chooses two random elements of the list and swaps them."""
    i, j = [random.randrange(len(t)) for i in range(2)]
    t[i], t[j] = t[j], t[i]


def PercentAdjacent(t):
    """Computes the fraction of adjacent pairs that are the same."""
    count = 0.0
    for i in range(len(t) - 1):
        if t[i] == t[i+1]:
            count += 1
    return count / len(t)
            

def main():
    # make a Hist of observed values
    count_per = dict(cashew=17, brazil=7, almond=22, peanut=28)
    #count_per = dict(cashew=12, brazil=5, almond=18, peanut=24)
    sample = dict(cashew=6, brazil=3, almond=5, peanut=6)

    observed = thinkstats2.MakeHistFromDict(sample)
    ConvertToCount(observed, count_per)

    advertised = dict(cashew=40, brazil=15, almond=20, peanut=25)
    expected = thinkstats2.MakePmfFromDict(advertised)
    ConvertToCount(expected, count_per)
    expected.Normalize(observed.Total())

    for value, e in expected.Items():
        o = observed.Freq(value)
        print value, e, o, 100 * (o - e)/ e, '%'

    num_nuts = observed.Total()

    for stir in [1.1, 1.15, 1.2, 1.25, 1.3, -1]:
        vat = MakeVat(expected, num_nuts, factor=10, stir=stir)
        print stir, PercentAdjacent(vat)
        Test(expected, observed, num_trials=100, stir=stir)

if __name__ == "__main__":
    main()
