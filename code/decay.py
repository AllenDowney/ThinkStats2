"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkbayes
import thinkplot

from math import exp

"""This file contains a partial solution to a problem from
MacKay, "Information Theory, Inference, and Learning Algorithms."

    Unstable particles are emitted from a source and decay at a
distance $x$, a real number that has an exponential probability
distribution with [parameter] $\lambda$.  Decay events can only be
observed if they occur in a window extending from $x=1$ cm to $x=20$
cm.  $N$ decays are observed at locations $\{ 1.5, 2, 3, 4, 5, 12 \}$
cm.  What is $\lambda$?

"""

class Decay(thinkbayes.Suite):
    """Represents hypotheses about the emission rate, lam."""

    def Likelihood(self, data, hypo):
        """Likelihood of the data given the hypothesis.

        Args:
            data: location of decay event in cm
            hypo: parameter of the expo distribution

        Returns:
            probability density of the data under the hypothesis
        """
        return ExpoCondPdf(data, hypo)


def ExpoCondPdf(x, lam, low=1.0, high=20.0):
    """Evaluates the conditional exponential PDF.

    Returns the probability density of x in the exponential PDF
    with the given parameter, with the condition that low < x < high.

    Args:
      x: float observed value
      lam: float parameter of the exponential distribution
      low: float, low end of the observable range
      high: float, high end of the observable range
    """
    factor = exp(-low * lam) - exp(-high * lam)
    p = lam * exp(-lam * x) / factor
    return p


def main():
    low = 0.001
    high = 1.5
    steps = 1001
    hypos = [low + (high-low) * i / (steps-1.0) for i in range(steps)]

    suite = Decay(hypos)
    data = [1.5, 2, 3, 4, 5, 12]

    suite.UpdateSet(data)
    print 'Mean of the posterior distribution:', suite.Mean()

    # plot the posterior distribution
    thinkplot.Pmf(suite)
    thinkplot.Show(title='Decay parameter',
                   xlabel='Parameter (inverse cm)',
                   ylabel='Posterior probability')


if __name__ == '__main__':
    main()
