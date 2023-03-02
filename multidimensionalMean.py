import numpy as np

#A function that computes the mean of a numerical, multidimensional data set input as a 2-dimensional numpy array
def multidimensionalMean(arr:np.ndarray):
    count = 0
    total = 0
    for index, value in np.ndenumerate(arr):
        count += 1
        total += value
    return total / count


