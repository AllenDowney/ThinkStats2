"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from thinkstats.com

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import random

class RandomVariable(object):
    """Parent class for all random variables."""
    def sample(self, n):
        return [self.generate() for i in range(n)]


class Exponential(RandomVariable):
    def __init__(self, lam):
        self.lam = lam

    def generate(self):
        return random.expovariate(self.lam)


class Erlang(RandomVariable):
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.expo = Exponential(lam)

    def generate(self):
        total = 0
        for i in range(self.k):
            total += self.expo.generate()
        return total


def main():
    erlang = Erlang(0.7, 3)
    print erlang.sample(3)


if __name__ == '__main__':
    main()
