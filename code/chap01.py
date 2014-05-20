"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import nsfg
import thinkstats2


def main(script):
    """Code used while developing Chapter 1.

    script: string script name
    """
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    # print the sequence of outcomes for one caseid
    caseid = 10229
    indices = preg_map[caseid]
    print(caseid, preg.outcome[indices].values)


if __name__ == '__main__':
    main(*sys.argv)
