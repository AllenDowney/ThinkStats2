"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows = None):
    """ Read the FemRecp data file.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """
    Clean the FemResp data.

    df: DataFrame
    """
    pass

def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = ReadFemResp()
    pregnum = resp.pregnum

    # compare value counts with codebook 
    # https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
    pregnum_value_counts = pregnum.value_counts().sort_index()
    assert(pregnum_value_counts[0] == 2610)
    assert(pregnum_value_counts[1] == 1267)
    assert(pregnum_value_counts[2] == 1432)
    assert(pregnum_value_counts[3] == 1110)
    assert(pregnum_value_counts[4] == 611)
    assert(pregnum_value_counts[5] == 305)
    assert(pregnum_value_counts[6] == 150)
    assert(pregnum_value_counts[7:].sum() == 158)

    # cross-validation 
    preg = nsfg.ReadFemPreg()

    # validate total counts with number ob preg records.
    assert(pregnum.sum() == len(preg))

    # validate each casies
    preg_map = nsfg.MakePregMap(preg)
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        assert(pregnum == len(indices))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
