import numpy as np

import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node, returning a standard float.
    """
    if len(y) == 0:
        return 0.0
        
    _, counts = np.unique(y, return_counts = True)
    probs = counts / len(y)
    
    probs = probs[probs > 0]
    
    entropy = -np.sum(probs * np.log2(probs))
    
    return float(entropy)
    pass