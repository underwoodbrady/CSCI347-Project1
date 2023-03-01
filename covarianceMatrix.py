import numpy as np

from multidimensionalMean import multidimensionalMean

#A function that computes the covariance matrix of a data set. 
def covarianceMatrix(inp:np.ndarray):
    means = multidimensionalMean(inp)
    centered = inp - means.reshape(-1, 1)
    
    n = centered.shape[1]
    cov_mat = np.zeros((centered.shape[0], centered.shape[0]))
    for i in range(centered.shape[0]):
        for j in range(centered.shape[0]):
            cov_mat[i][j] = np.sum(centered[i] * centered[j]) / (n - 1)

    return cov_mat
