import numpy as np

from multidimensionalMean import multidimensionalMean

#A function that normalizes the attributes in a two-dimensional numpy array using standard normalization. 
def normalizeStandard(inp:np.ndarray):
    mn = multidimensionalMean(inp)  # already written mean function
    std = np.std(inp)  # might have to write the standard deviation function ourselves
    return (inp - mn) / std
