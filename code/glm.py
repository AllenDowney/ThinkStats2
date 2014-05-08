"""Interface to rpy2.glm

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import rpy2.robjects as robjects
r = robjects.r

def linear_model(model, print_flag=True):
    """Submits model to r.lm and returns the result."""
    model = r(model)
    res = r.lm(model)
    if print_flag:
        print_summary(res)
    return res


def logit_model(model,
                family=robjects.r.binomial(),
                weights=None,
                print_flag=True):
    """Submits model to r.glm and returns the result."""
    model = r(model)
    if weights is None:
        res = r.glm(model, family=family)
    else:
        weight_vector = robjects.FloatVector(weights)
        res = r.glm(model, family=family, weights=weight_vector)

    if print_flag:
        print_summary(res)
    return res


def print_summary(res):
    """Prints results from r.lm (just the parts we want)."""
    flag = False
    lines = r.summary(res)
    lines = str(lines)

    for line in lines.split('\n'):
        # skip everything until we get to coefficients
        if line.startswith('Coefficients'):
            flag = True
        if line.startswith('Signif'):
            continue
        if flag:
            print line
    print


def get_coeffs(res):
    """Gets just the lines that contain the estimates.

    res: R glm result object

    Returns: list of (name, estimate, error, z-value) tuples and AIC
    """
    flag = False
    lines = r.summary(res)
    lines = str(lines)

    res = []
    aic = None

    for line in lines.split('\n'):
        line = line.strip()
        if line.startswith('---'):
            flag = False
        if line.startswith('AIC'):
            t = line.split()
            aic = float(t[1])
        if flag:
            t = line.split()
            var = t[0]
            est = float(t[1])
            error = float(t[2])
            z = float(t[3])
            res.append((var, est, error, z))
        if line.startswith('Estimate'):
            flag = True

    return res, aic

def inject_col_dict(col_dict, prefix=''):
    """Copies data columns into the R global environment.
    
    col_dict: map from attribute name to column of data
    prefix: string prepended to the attribute names
    """
    for name, col in col_dict.iteritems():
        robjects.globalenv[prefix+name] = robjects.FloatVector(col)


