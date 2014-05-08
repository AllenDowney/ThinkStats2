"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from thinkstats.com

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math

class Gaussian(object):
    """Represents a Gaussian distribution"""

    def __init__(self, mu, sigma2):
        """Initializes.

        mu: mean
        sigma2: variance
        """
        self.mu = mu
        self.sigma2 = sigma2

    def __str__(self):
        """Returns a string representation."""
        return 'N(%g, %g)' % (self.mu, self.sigma2)

    @property
    def sigma(self):
        """Returns the standard deviation."""
        return math.sqrt(self.sigma2)

    def __add__(self, other):
        """Adds a number or other Gaussian.

        other: number or Gaussian

        returns: new Gaussian
        """
        if isinstance(other, Gaussian):
            return Gaussian(self.mu + other.mu, self.sigma2 + other.sigma2)
        else:
            return Gaussian(self.mu + other, self.sigma2)

    __radd__ = __add__

    def __mul__(self, factor):
        """Multiplies by a scalar.

        factor: number

        returns: new Gaussian
        """
        return Gaussian(factor * self.mu, factor**2 * self.sigma2)

    __rmul__ = __mul__

    def __div__(self, divisor):
        """Divides by a scalar.

        divisor: number

        returns: new Gaussian
        """
        return 1.0 / divisor * self


def main():
    d1 = Gaussian(1, 4)
    d2 = Gaussian(2, 9)
    print 'd1 ~', d1
    print 'd2 ~', d2
    print '3 * d1 ~', 3 * d1
    print 'd1 + d2 ~', d1 + d2

    n = 10
    d3 = sum([d2] * n)

    print 'sum of n from d2 ~', d3

    # exercise: for n values from d2, compute the distribution of
    # the sample mean and the standard error (which is the standard
    # deviation of the sample mean)

    # compare the result to sigma / sqrt(n)


if __name__ == '__main__':
    main()
