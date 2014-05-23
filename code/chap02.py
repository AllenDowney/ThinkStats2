"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import numpy as np
import pandas


def main(script):
    """Code used while developing Chapter 2.

    script: string script name
    """
    array = np.random.randn(4, 2)
    df = pandas.DataFrame(array)
    print(df)

    columns = ['A', 'B']
    df = pandas.DataFrame(array, columns=columns)
    print(df)

    index = ['a', 'b', 'c', 'd']
    df = pandas.DataFrame(array, columns=columns, index=index)
    print(df)

    print(df['A'])

    print(df[0:1])

    print(df.loc['a'])
    print(df.iloc[0])

    indices = ['a', 'c']
    print(df.loc[indices])
    

if __name__ == '__main__':
    main(*sys.argv)
