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
    handleData();
    multidimensionalMean()
    sampleCovariance()
    attributeCorrelation()
    normalizeRange()
    normalizeStandard()
    covarianceMatrix()
    labelEncode()

if( __name__ == "__main__"):
    main()
