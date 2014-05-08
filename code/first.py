"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import survey
import thinkstats2


def PartitionRecords(table):
    """Divides records into two lists: first babies and others.

    Only live births are included

    Args:
        table: pregnancy Table
    """
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        # skip non-live births
        if p.outcome != 1:
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)

    return firsts, others


def Process(table):
    """Runs analysis on the given table.
    
    Args:
        table: table object
    """
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = thinkstats2.Mean(table.lengths)


def MakeTables(data_dir='.'):
    """Reads survey data and returns tables for first babies and others."""
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    firsts, others = PartitionRecords(table)
    
    return table, firsts, others


def ProcessTables(*tables):
    """Processes a list of tables
    
    Args:
        tables: gathered argument tuple of Tuples
    """
    for table in tables:
        Process(table)
        
        
def Summarize(data_dir):
    """Prints summary statistics for first babies and others.
    
    Returns:
        tuple of Tables
    """
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)
        
    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:' 
    print 'First babies', mu1 
    print 'Others', mu2
    
    print 'Difference in days', (mu1 - mu2) * 7.0


def main(name, data_dir='.'):
    Summarize(data_dir)
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
