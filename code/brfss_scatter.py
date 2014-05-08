"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import matplotlib
import matplotlib.pyplot as pyplot
import random
import sys

import brfss
import myplot


class Respondents(brfss.Respondents):
    """Represents the respondent table."""

    def GetHeightWeight(self, jitter=0.0):
        """Get sequences of height and weight.

        Args:
            jitter: float magnitude of random noise added to heights

        Returns:
            tuple of sequences (heights, weights)
        """
        heights = []
        weights = []
        for r in self.records:
            if r.wtkg2 == 'NA' or r.htm3 == 'NA':
                continue
            
            height = r.htm3 + random.uniform(-jitter, jitter)
            
            heights.append(height)
            weights.append(r.wtkg2)
            
        return heights, weights

    def ScatterPlot(self, root, heights, weights, alpha=1.0):
        pyplot.scatter(heights, weights, alpha=alpha, edgecolors='none')
        myplot.Save(root=root,
                    xlabel='Height (cm)',
                    ylabel='Weight (kg)',
                    axis=[140, 210, 20, 200],
                    legend=False)
        
    def HexBin(self, root, heights, weights, cmap=matplotlib.cm.Blues):
        pyplot.hexbin(heights, weights, cmap=cmap)
        myplot.Save(root=root,
                    xlabel='Height (cm)',
                    ylabel='Weight (kg)',
                    axis=[140, 210, 20, 200],
                    legend=False)


def MakeFigures():
    resp = Respondents()
    resp.ReadRecords(n=1000)

    heights, weights = resp.GetHeightWeight(jitter=0.0)
    pyplot.clf()
    resp.ScatterPlot('scatter1', heights, weights)

    heights, weights = resp.GetHeightWeight(jitter=1.3)
    pyplot.clf()
    resp.ScatterPlot('scatter2', heights, weights)

    pyplot.clf()
    resp.ScatterPlot('scatter3', heights, weights, alpha=0.2)

    # read more respondents for the hexplot
    resp = Respondents()
    resp.ReadRecords(n=10000)
    heights, weights = resp.GetHeightWeight(jitter=1.3)

    pyplot.clf()
    resp.HexBin('scatter4', heights, weights)


def main(name):
    MakeFigures()


if __name__ == '__main__':
    main(*sys.argv)
