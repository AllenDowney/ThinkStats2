"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import pandas as pd
from cStringIO import StringIO

file_like = StringIO('foo')
colspecs = [(0, 3)]
frame = pd.read_fwf(file_like, colspecs=colspecs, header=None)
print frame


file_like = StringIO('foo')
colspecs = [(None, None)]
frame = pd.read_fwf(file_like, colspecs=colspecs, header=None)
print frame
