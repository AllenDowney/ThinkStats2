"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import thinkstats2


def CleanPregFrame(preg):
    """Recodes variables from the pregnancy frame.
    """
    # mother's age is encoded in centiyears; convert to years
    preg.agepreg /= 100.0

    # birthweight is stored in two columns, lbs and oz.
    # convert to a single column in lb
    
    args = ([51, 97, 98, 99], float('NaN'))
    preg.birthwgt_lb.replace(*args, inplace=True)
    preg.birthwgt_oz.replace(*args, inplace=True)
    preg['totalwgt_lb'] = preg.birthwgt_lb + preg.birthwgt_oz / 16.0    

    # due to a bug in ReadStataDct, the last variable gets clipped;
    # so for now set it to NA
    preg.cmintvw = 'NA'


def ReadFemPreg(dct_file = '2002FemPreg.dct', dat_file = '2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    preg = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanPregFrame(preg)

    return preg


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    preg = ReadFemPreg()

    assert len(preg) == 13593

    assert preg.caseid[13592] == 12571
    assert preg.pregordr.value_counts()[1] == 5033
    assert preg.nbrnaliv.value_counts()[1] == 8981
    assert preg.babysex.value_counts()[1] == 4641
    assert preg.birthwgt_lb.value_counts()[7] == 3049
    assert preg.birthwgt_oz.value_counts()[0] == 1037
    assert preg.prglngth.value_counts()[39] == 4744
    assert preg.outcome.value_counts()[1] == 9148
    assert preg.birthord.value_counts()[1] == 4413
    assert preg.agepreg.value_counts()[22.75] == 100
    assert preg.totalwgt_lb.value_counts()[7.5] == 302

    weights = preg.finalwgt.value_counts()
    key = max(weights.keys())
    assert preg.finalwgt.value_counts()[key] == 6

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
