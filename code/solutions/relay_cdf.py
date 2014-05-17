"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import relay
import Cdf
import myplot


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    # plot the distribution of actual speeds
    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')

    myplot.Cdf(cdf)
    myplot.Save(root='relay_cdf',
                title='CDF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')


if __name__ == '__main__':
    main()
