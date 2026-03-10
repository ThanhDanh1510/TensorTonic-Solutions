import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = [p if x_i == 1 else 1 - p for x_i in x]
    pmf = np.asarray(pmf)
    mean = p
    var = p*(1-p)
    return (pmf, mean, var)
    pass