import numpy as np

from multidimensionalMean import multidimensionalMean

#A function that computes the sample covariance between two attributes that are input as one-dimensional numpy vectors 
def sampleCovariance(vec1:np.array, vec2:np.array):
    n = len(vec1)
    mean_x = multidimensionalMean(vec1)  # using previously written mean function
    mean_y = multidimensionalMean(vec2)
    covariance = 0
    for i in range(n):
        covariance += (vec1[i] - mean_x) * (vec2[i] - mean_y)
    covariance /= n - 1
    return covariance
