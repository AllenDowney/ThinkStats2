"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import sys
import pandas as pd

import thinkstats2


def Summarize(df, column, title):
    """Print summary statistics male, female and all."""

    items = [
        ('all', df[column]),
        ('male', df[df.sex == 1][column]),
        ('female', df[df.sex == 2][column]),
        ]

    print(title)
    print('key\tn\tmean\tvar\tstd\tcv')
    for key, series in items:
        mean, var = series.mean(), series.var()
        std = math.sqrt(var)
        cv = std / mean
        t = key, len(series), mean, var, std, cv
        print('%s\t%d\t%4.2f\t%4.2f\t%4.2f\t%4.4f' % t)


def CleanBrfssFrame(df):
    """Recodes BRFSS variables.

    df: DataFrame
    """
    # clean age
    df.age.replace([7, 9], float('NaN'), inplace=True)

    # clean height
    df.htm3.replace([999], float('NaN'), inplace=True)

    # clean weight
    df.wtkg2.replace([99999], float('NaN'), inplace=True)
    df.wtkg2 /= 100.0

    # clean weight a year ago
    df.wtyrago.replace([7777, 9999], float('NaN'), inplace=True)
    df['wtyrago'] = df.wtyrago.apply(lambda x: x/2.2 if x < 9000 else x-9000)


def ReadBrfss(filename='CDBRFS08.ASC.gz', compression='gzip', nrows=None):
    """Reads the BRFSS data.

    filename: string
    compression: string
    nrows: int number of rows to read, or None for all

    returns: DataFrame
    """
    var_info = [
        ('age', 101, 102, int),
        ('sex', 143, 143, int),
        ('wtyrago', 127, 130, int),
        ('finalwt', 799, 808, int),
        ('wtkg2', 1254, 1258, int),
        ('htm3', 1251, 1253, int),
        ]
    columns = ['name', 'start', 'end', 'type']
    variables = pd.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = thinkstats2.FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(filename, compression=compression, nrows=nrows)
    CleanBrfssFrame(df)
    return df


def main(script, nrows=1000):
    """Tests the functions in this module.

    script: string script name
    """
    nrows = int(nrows)
    df = ReadBrfss(nrows=nrows)

    Summarize(df, 'htm3', 'Height (cm):')
    Summarize(df, 'wtkg2', 'Weight (kg):')
    Summarize(df, 'wtyrago', 'Weight year ago (kg):')

    if nrows == 1000:
        assert(df.age.value_counts()[40] == 28)
        assert(df.sex.value_counts()[2] == 668)
        assert(df.wtkg2.value_counts()[90.91] == 49)
        assert(df.wtyrago.value_counts()[160/2.2] == 49)
        assert(df.htm3.value_counts()[163] == 103)
        assert(df.finalwt.value_counts()[185.870345] == 13)
        print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
