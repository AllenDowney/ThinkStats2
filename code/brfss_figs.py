"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import brfss
import cPickle
import continuous
import Cdf
import math
import matplotlib
import matplotlib.pyplot as pyplot
import myplot
import random
import rankit
import sys
import survey
import thinkstats


class Respondents(brfss.Respondents):
    """Represents the respondent table."""

    def MakeNormalModel(self, weights, root,
                   xmax=175, 
                   xlabel='adult weight (kg)',
                   axis=None):
        cdf = Cdf.MakeCdfFromList(weights)
                
        pyplot.clf()
        
        t = weights[:]
        t.sort()
        mu, var = thinkstats.TrimmedMeanVar(t)
        print 'n, Mean, Var', len(weights), mu, var
        
        sigma = math.sqrt(var)
        print 'Sigma', sigma

        xs, ps = continuous.RenderNormalCdf(mu, sigma, xmax)
        pyplot.plot(xs, ps, label='model', linewidth=4, color='0.7')
    
        xs, ps = cdf.Render()
        pyplot.plot(xs, ps, label='data', linewidth=2, color='blue')
     
        myplot.Save(root,
                    title = 'Adult weight',
                    xlabel = xlabel,
                    ylabel = 'CDF',
                    axis=axis or [0, xmax, 0, 1])
    
    def MakeFigures(self):
        """Generates CDFs and normal prob plots for weights and log weights."""
        weights = [record.wtkg2 for record in self.records
                   if record.wtkg2 != 'NA']
        self.MakeNormalModel(weights, root='brfss_weight_model')
        rankit.MakeNormalPlot(weights,
                              root='brfss_weight_normal',
                              title='Adult weight',
                              ylabel='Weight (kg)')
        
        log_weights = [math.log(weight) for weight in weights]
        xmax = math.log(175.0)
        axis = [3.5, 5.2, 0, 1]
        self.MakeNormalModel(log_weights, 
                             root='brfss_weight_log',
                             xmax=xmax,
                             xlabel='adult weight (log kg)',
                             axis=axis)
        rankit.MakeNormalPlot(log_weights, 
                              root='brfss_weight_lognormal',
                              title='Adult weight',
                              ylabel='Weight (log kg)')


def main(name):
    resp = Respondents()
    resp.ReadRecords()
    resp.MakeFigures()

    
if __name__ == '__main__':
    main(*sys.argv)
