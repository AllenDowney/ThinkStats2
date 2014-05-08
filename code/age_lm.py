"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""
Results:

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 117.7817     0.3408 345.562  < 2e-16 ***
first        -2.2472     0.4909  -4.578 4.75e-06 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 23.38 on 9082 degrees of freedom
Multiple R-squared: 0.002302,	Adjusted R-squared: 0.002193 
F-statistic: 20.96 on 1 and 9082 DF,  p-value: 4.754e-06 

## With just first, we confirm that first babies are lighter.

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 109.52288    1.12557  97.304  < 2e-16 ***
ages          0.28773    0.04405   6.531 6.87e-11 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 

Residual standard error: 23.35 on 9082 degrees of freedom
Multiple R-squared: 0.004675,	Adjusted R-squared: 0.004565 
F-statistic: 42.66 on 1 and 9082 DF,  p-value: 6.868e-11 


## With just ages, we confirm that younger women have lighter babies.
## The slope and intercept are the same as in agemodel.py.


Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 111.1561     1.2854  86.474  < 2e-16 ***
first        -1.3599     0.5175  -2.628   0.0086 ** 
ages          0.2485     0.0465   5.345 9.26e-08 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 

Residual standard error: 23.34 on 9081 degrees of freedom
Multiple R-squared: 0.005432,	Adjusted R-squared: 0.005212 
F-statistic:  24.8 on 2 and 9081 DF,  p-value: 1.821e-11 


## With first and ages, the effect of first gets smaller by about 40%


Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 93.226968   4.554625  20.469  < 2e-16 ***
ages         1.598195   0.357644   4.469 7.97e-06 ***
ages2       -0.025098   0.006797  -3.692 0.000224 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 

Residual standard error: 23.33 on 9081 degrees of freedom
Multiple R-squared: 0.006167,	Adjusted R-squared: 0.005948 
F-statistic: 28.18 on 2 and 9081 DF,  p-value: 6.331e-13 

## With ages and ages2 we get a non-linear model that explains
## just a little bit more of the variance.


Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 95.881747   4.719302  20.317  < 2e-16 ***
first       -1.118630   0.522119  -2.142 0.032181 *  
ages         1.460500   0.363303   4.020 5.87e-05 ***
ages2       -0.023078   0.006861  -3.364 0.000772 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 

Residual standard error: 23.33 on 9080 degrees of freedom
Multiple R-squared: 0.006669,	Adjusted R-squared: 0.006341 
F-statistic: 20.32 on 3 and 9080 DF,  p-value: 4.039e-13 

## With all three variables, the effect of first is smaller still,
## and on the border of statistical significance.

## Bottom line: first babies are lighter than other babies;  About
## 50% of this effect is explained by mother's age, but the other
## half looks like it is legit.

Note: this analysis uses the lm (linear model) function provided by
rpy2, which is the Python interface to the R statistical software
system.  You can read about R at  http://rpy.sourceforge.net/

If you are running Ubuntu, you can install R and rpy to by running

sudo apt-get install python-rpy2

"""

import rpy2.robjects as robjects
r = robjects.r

import agemodel


def GetAgeWeightFirst(table):
    """Get sequences of mother's age, birth weight, and first baby flag.

    Args:
        table: Table object

    Returns:
        tuple of sequences (ages, weights, first_bool)
    """
    ages = []
    weights = []
    first_bool = []
    for r in table.records:
        if 'NA' in [r.agepreg, r.totalwgt_oz, r.birthord]:
            continue

        # first is 1.0 for first babies; 0.0 for others
        if r.birthord == 1:
            first = 1.0
        else:
            first = 0.0
        
        ages.append(r.agepreg)
        weights.append(r.totalwgt_oz)
        first_bool.append(first)

    return ages, weights, first_bool


def RunModel(model, print_flag=True):
    """Submits model to r.lm and returns the result."""
    model = r(model)
    res = r.lm(model)
    if print_flag:
        PrintSummary(res)
    return res


def PrintSummary(res):
    """Prints results from r.lm (just the parts we want)."""
    flag = False
    lines = r.summary(res)
    lines = str(lines)

    for line in lines.split('\n'):
        # skip everything until we get to coefficients
        if line.startswith('Coefficients'):
            flag = True
        if flag:
            print line
    print


def main(script, model_number=0):

    model_number = int(model_number)

    # get the data
    pool, firsts, others = agemodel.MakeTables()
    ages, weights, first_bool = GetAgeWeightFirst(pool)
    ages2 = [age**2 for age in ages]

    # put the data into the R environment
    robjects.globalenv['weights'] = robjects.FloatVector(weights)
    robjects.globalenv['ages'] = robjects.FloatVector(ages)
    robjects.globalenv['ages2'] = robjects.FloatVector(ages2)
    robjects.globalenv['first'] = robjects.FloatVector(first_bool)

    # run the models
    models = ['weights ~ first',
              'weights ~ ages',
              'ages ~ first',
              'weights ~ first + ages',
              'weights ~ ages + ages2',
              'weights ~ first + ages + ages2']

    model = models[model_number]
    print model
    RunModel(model)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
