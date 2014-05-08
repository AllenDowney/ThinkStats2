"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import sys
import survey
import thinkstats


class Respondents(survey.Table):
    """Represents the respondent table."""

    def ReadRecords(self, data_dir='.', n=None):
        filename = self.GetFilename()
        self.ReadFile(data_dir,
                      filename,
                      self.GetFields(), 
                      survey.Respondent,
                      n)
        self.Recode()

    def GetFilename(self):
        """Get the name of the data file.

        This function can be overridden by child classes.

        The BRFSS data is available from thinkstats.com/CDBRFS08.ASC.gz

        """
        return 'CDBRFS08.ASC.gz'

    def GetFields(self):
        """Returns a tuple specifying the fields to extract.
        
        BRFSS codebook 
        http://www.cdc.gov/brfss/technical_infodata/surveydata/2008.htm

        The elements of the tuple are field, start, end, case.

                field is the name of the variable
                start and end are the indices as specified in the NSFG docs
                case is a callable that converts the result to int, float, etc.
        """
        return [
            ('age', 101, 102, int),
            ('weight2', 119, 122, int),
            ('wtyrago', 127, 130, int),
            ('wtkg2', 1254, 1258, int),
            ('htm3', 1251, 1253, int),
            ('sex', 143, 143, int),
            ]

    def Recode(self):
        """Recode variables that need cleaning."""

        def CleanWeight(weight):
            if weight in [7777, 9999]:
                return 'NA'
            elif weight < 1000:
                return weight / 2.2
            elif 9000 < weight < 9999:
                return weight - 9000
            else:
                return weight

        for rec in self.records:
            # recode wtkg2
            if rec.wtkg2 in ['NA', 99999]:
                rec.wtkg2 = 'NA'
            else:
                rec.wtkg2 /= 100.0

            # recode wtyrago
            rec.weight2 = CleanWeight(rec.weight2)
            rec.wtyrago = CleanWeight(rec.wtyrago)

            # recode htm3
            if rec.htm3 == 999:
                rec.htm3 = 'NA'

            # recode age
            if rec.age in [7, 9]:
                rec.age = 'NA'


    def SummarizeHeight(self):
        """Print summary statistics for male and female height."""

        # make a dictionary that maps from gender code to list of heights
        d = {1:[], 2:[], 'all':[]}
        [d[r.sex].append(r.htm3) for r in self.records if r.htm3 != 'NA']
        [d['all'].append(r.htm3) for r in self.records if r.htm3 != 'NA']
        
        print 'Height (cm):'
        print 'key n     mean     var    sigma     cv'
        for key, t in d.iteritems():
            mu, var = thinkstats.TrimmedMeanVar(t)
            sigma = math.sqrt(var)
            cv = sigma / mu
            print key, len(t), mu, var, sigma, cv

        return d

    def SummarizeWeight(self):
        """Print summary statistics for male and female weight."""

        # make a dictionary that maps from gender code to list of weights
        d = {1:[], 2:[], 'all':[]}
        [d[r.sex].append(r.weight2) for r in self.records if r.weight2 != 'NA']
        [d['all'].append(r.weight2) for r in self.records if r.weight2 != 'NA']

        print 'Weight (kg):'
        print 'key n     mean     var    sigma     cv'
        for key, t in d.iteritems():
            mu, var = thinkstats.TrimmedMeanVar(t)
            sigma = math.sqrt(var)
            cv = sigma / mu
            print key, len(t), mu, var, sigma, cv


    def SummarizeWeightChange(self):
        """Print the mean reported change in weight in kg."""
        
        data = [(r.weight2, r.wtyrago) for r in self.records
                if r.weight2 != 'NA' and r.wtyrago != 'NA']
        
        changes = [(curr - prev) for curr, prev in data]
            
        print 'Mean change', thinkstats.Mean(changes)
        
    
def main(name, data_dir='.'):
    resp = Respondents()
    resp.ReadRecords(data_dir)
    resp.SummarizeHeight()
    resp.SummarizeWeight()
    resp.SummarizeWeightChange()
    
if __name__ == '__main__':
    main(*sys.argv)
