"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import pandas as pd
from cStringIO import StringIO

def test():
    d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)

    # this adds a column to df
    df['three'] = df.two + 1

    # this successfully modifies one
    df.one += 1

    # this seems to work but does not add a column to df
    df.four = df.two + 2

    print df.three
    print df.four
    print df

test()
