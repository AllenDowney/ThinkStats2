"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import csv
import datetime
import sys

import Cdf
import myplot

def ReadBirthdays(filename='birthdays.csv'):
    """Reads a CSV file of birthdays and returns a list of date objects.

    The first column of the file must contain dates in MM-DD format.

    Args:
      filename: string filename

    Returns:
      list of datetime.date objects"""
    fp = open(filename)
    reader = csv.reader(fp)
    bdays = []

    for t in reader:
        bday = t[0]
        month, day = [int(x) for x in bday.split('-')]
        date = datetime.date(2010, month, day)
        bdays.append(date)

    return bdays

def Diff(t):
    """Computes the differences between the adjacent elements of a sequence.

    Args:
      t: sequence of anything subtractable

    Returns:
      list of whatever is in t
    """
    diffs = []
    for i in range(len(t)-1):
        diff = t[i+1] - t[i]
        diffs.append(diff)
    return diffs


def Main(script):

    # read 'em and sort 'em
    birthdays = ReadBirthdays()
    birthdays.sort()

    # compute the intervals in days
    deltas = Diff(birthdays)
    days = [inter.days for inter in deltas]

    # make and plot the CCDF on a log scale.
    cdf = Cdf.MakeCdfFromList(days, name='intervals')
    scale = myplot.Cdf(cdf, transform='exponential')
    myplot.Save(root='intervals', 
                xlabel='days', 
                ylabel='ccdf', 
                **scale)

if __name__ == '__main__':
    Main(*sys.argv)
