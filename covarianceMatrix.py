import numpy as np

from multidimensionalMean import multidimensionalMean

#A function that computes the covariance matrix of a data set. 
def covarianceMatrix(inp:np.ndarray):
    n = inp.shape[1]
    means = np.sum(inp, axis=1) / n
    center = inp - means.reshape(-1, 1)

    cov = np.zeros((center.shape[0], center.shape[0]))
    for i in range(center.shape[0]):
        for j in range(i, center.shape[0]):
            cov[i][j] = np.sum(center[i] * center[j]) / (n - 1)
            cov[j][i] = cov[i][j]

    return cov
