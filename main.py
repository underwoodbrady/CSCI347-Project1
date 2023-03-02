import numpy as np

from handleData import handleData
from multidimensionalMean import multidimensionalMean
from sampleCovariance import sampleCovariance
from attributeCorrelation import attributeCorrelation
from normalizeRange import normalizeRange
from normalizeStandard import normalizeStandard
from covarianceMatrix import covarianceMatrix
from labelEncode import labelEncode 

#Call each of the above functions with the dataset
def main():
    x = np.array([40, 10, 50, 16])
    y = np.array([23, 59, 30, 7])
    handleData();
    multidimensionalMean(x)
    #print(sampleCovariance(x, y))
    #print(np.cov(x, y))
    sampleCovariance(x, y)
    attributeCorrelation(x, y)
    normalizeRange(x)
    normalizeStandard(x)
    covarianceMatrix(handleData())
    #labelEncode()

if( __name__ == "__main__"):
    main()
