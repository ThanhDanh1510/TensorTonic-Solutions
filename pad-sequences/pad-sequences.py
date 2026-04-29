import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.zeros((0, max_len or 0))
    
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    padded_seqs = []
    
    for seq in seqs:
        seq_len = len(seq)
        
        if seq_len < max_len:
            padded = np.pad(seq, (0, max_len - seq_len), mode='constant', constant_values=pad_value)
        else:
            padded = seq[:max_len]
            
        padded_seqs.append(padded)
        
    return np.array(padded_seqs)