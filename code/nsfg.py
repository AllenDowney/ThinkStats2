"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys
import re

import pandas as pd


def CleanPregFrame(frame):
    """Recodes variables from the pregnancy frame.
    """
    # mother's age is encoded in centiyears; convert to years
    frame.agepreg /= 100.0

    # birthweight is stored in two columns, lbs and oz.
    # convert to a single column in lb
    frame.totalwgt_lb = frame.birthwgt_lb + frame.birthwgt_oz / 16.0    

    # due to a bug in ReadStataDct, the last variable gets clipped;
    # so for now set it to NA
    frame.cmintvw = 'NA'


class Dictionary(object):
    """Represents a set of variables in a fixed width file."""

    def __init__(self, variables, colspecs, names):
        """Initializes.

        variables: list of (start, vtype, name, fstring, long_desc) tuples
        colspecs: list of (start, end) index tuples
        names: list of string variable names
        """
        self.variables = variables
        self.colspecs = colspecs
        self.names = names


def ReadStataDct(dct_file):
    """Reads a Stata dictionary file.

    returns: Dictionary object
    """
    type_map = dict(byte=int, int=int, float=float, double=float)

    variables = []
    for line in open(dct_file):
        match = re.search( r'_column\(([^)]*)\)', line)
        if match:
            start = int(match.group(1))
            t = line.split()
            vtype, name, fstring = t[1:4]
            if vtype.startswith('str'):
                vtype = str
            else:
                vtype = type_map[vtype]
            long_desc = ' '.join(t[4:]).strip('"')
            variables.append((start, vtype, name, fstring, long_desc))
            
    colspecs = []
    names = []
    for i in range(len(variables)):
        start, vtype, name, fstring, long_desc = variables[i]
        names.append(name)
        try:
            end = variables[i+1][0]
            colspecs.append((start-1, end-1))
        except IndexError:
            # Note: this won't work properly until Pandas Issue 7079 is
            # resolved so pd.read_fwf accepts None as a colspec

            # In the meantime, it lops one character off the end of the
            # last field.

            # TODO: replace -1 with None (see DocString above)
            colspecs.append((start-1, -1))

    return Dictionary(variables, colspecs, names)


def ReadNsfg(dat_file, dct, compression='gzip'):
    """Reads an NSFG file.

    dat_file: string filename
    dct: Dictionary object
    compression: string

    returns: DataFrame
    """
    preg_frame = pd.read_fwf(dat_file,
                             compression=compression,
                             colspecs=dct.colspecs, 
                             names=dct.names,
                             header=None)
    return preg_frame


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    dct_file = '2002FemPreg.dct'
    dat_file = '2002FemPreg.dat.gz'

    dct = ReadStataDct(dct_file)
    preg_frame = ReadNsfg(dat_file, dct)
    CleanPregFrame(preg_frame)

    assert len(preg_frame) == 13593

    assert preg_frame.caseid[13592] == 12571
    assert preg_frame.pregordr.value_counts()[1] == 5033
    assert preg_frame.nbrnaliv.value_counts()[1] == 8981
    assert preg_frame.babysex.value_counts()[1] == 4641
    assert preg_frame.birthwgt_lb.value_counts()[7] == 3049
    assert preg_frame.birthwgt_oz.value_counts()[0] == 1037
    assert preg_frame.prglngth.value_counts()[39] == 4744
    assert preg_frame.outcome.value_counts()[1] == 9148
    assert preg_frame.birthord.value_counts()[1] == 4413
    assert preg_frame.agepreg.value_counts()[22.75] == 100

    weights = preg_frame.finalwgt.value_counts()
    key = max(weights.keys())
    assert preg_frame.finalwgt.value_counts()[key] == 6

    print '%s: All tests passed.' % script


if __name__ == '__main__':
    main(*sys.argv)
