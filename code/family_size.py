"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import thinkplot
import thinkstats2


def main():

    d = {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
    }

    # form the pmf
    pmf = thinkstats2.MakePmfFromDict(d, 'family size')
    print 'mean', pmf.Mean()
    print 'var', pmf.Var()
    
    # plot the Pmfs
    thinkplot.Pmf(pmf)
    thinkplot.Show(xlabel='Family size',
                   ylabel='PMF')
    
 
if __name__ == '__main__':
    main()
