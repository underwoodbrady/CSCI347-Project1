import numpy as np
import math

#A function that computes the correlation between two attributes that are input as two numpy vectors. 
def attributeCorrelation(vec1:np.array, vec2:np.array):
    vec1mean = sum(vec1)/len(vec1)
    vec2mean = sum(vec2)/len(vec2)
    numerator = 0
    denominatorLeft = 0
    denominatorRight = 0
    for v in range(len(vec1)):
        numerator += (vec1[v]-vec1mean)* (vec2[v]-vec2mean)
        denominatorLeft += (vec1[v]-vec1mean)**2
        denominatorRight += (vec2[v]-vec2mean)**2

    result = numerator/math.sqrt(denominatorLeft*denominatorRight)
    return result

print(attributeCorrelation(np.array([4,2,5,6,7]), np.array([4,2,5,6,7])))

