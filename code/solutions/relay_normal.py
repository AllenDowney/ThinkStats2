"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""This program generates a normal probability plot for the distribution
of running speeds in a road race.

The results suggest that the distribution is bimodal, with a small
number of fast runners who seem to belong to a different normal
distribution.

I conjecture that these are people who have trained at a competitive
level.  Among them, the distribution is normal, but there is a gap
between them and the rest of the population.

"""

import relay
import rankit


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    rankit.MakeNormalPlot(speeds,
                          root='relay_normal',
                          ylabel='Speed (MPH)')


if __name__ == '__main__':
    main()
