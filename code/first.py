"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import nsfg


def MakeFrames():
    """Reads pregnancy data and partitions first babies and others.

    returns: DataFrames (all live births, first babies, others)
    """
    preg = nsfg.ReadFemPreg()

    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    assert len(live) == 9148
    assert len(firsts) == 4413
    assert len(others) == 4735

    return live, firsts, others


def Summarize():
    """Prints summary statistics for first babies and others.
    """
    live, firsts, others = MakeFrames()

    print(len(live), 'live births')
    print(len(firsts), 'first live births')
    print(len(others), 'other live births')

    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()

    print('Mean gestation in weeks:')
    print('First babies', mean1)
    print('Others', mean2)
    
    print('Difference in weeks', mean1 - mean2)
    print('Difference in days', (mean1 - mean2) * 7.0)


def main(_script):
    Summarize()
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
