"""This file contains code related to "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import csv


def read_csv(filename, constructor):
    """Reads a CSV file, returns the header line and a list of objects.

    filename: string filename
    """
    fp = open(filename)
    reader = csv.reader(fp)

    header = reader.next()
    names = [s.lower() for s in header]

    objs = [make_object(t, names, constructor) for t in reader]
    fp.close()

    return objs


def write_csv(filename, header, data):
    """Writes a CSV file

    filename: string filename
    header: list of strings
    data: list of rows
    """
    fp = open(filename, 'w')
    writer = csv.writer(fp)
    writer.writerow(header)

    for t in data:
        writer.writerow(t)
    fp.close()


def print_cols(cols):
    """Prints the index and first two elements for each column.

    cols: list of columns
    """
    for i, col in enumerate(cols):
        print i, col[0], col[1]


def make_col_dict(cols, names):
    """Selects columns from a dataset and returns a map from name to column.

    cols: list of columns
    names: list of names
    """
    col_dict = {}
    for name, col in zip(names, cols):
        col_dict[name] = col
    return col_dict


def make_object(row, names, constructor):
    """Turns a row of values into an object.

    row: row of values
    names: list of attribute names
    constructor: function that makes the objects

    Returns: new object
    """
    obj = constructor()
    for name, val in zip(names, row):
        func = constructor.convert.get(name, int)
        try:
            val = func(val)
        except:
            pass
        setattr(obj, name, val)
    obj.clean()
    return obj

