import numpy as np

#A function that normalizes the attributes in a two-dimensional numpy array using range normalization. 
def normalizeRange(arr:np.ndarray):
    normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return normalized
