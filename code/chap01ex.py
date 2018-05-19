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

def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg()
    return df

def CleanFemPreg():
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def ValidatePregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, preg_num in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        if len(indices) != preg_num:
            print(caseid, len(indices), preg_num)
            return False
    return True

def main(script):
    """Tests the functions in this module.
    
    script: string script name
    """
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
