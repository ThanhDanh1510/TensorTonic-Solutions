import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x, q = np.asarray(x), np.asarray(q)
    result = np.percentile(x, q, method = 'linear')
    return result
    pass