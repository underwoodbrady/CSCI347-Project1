import numpy as np

from multidimensionalMean import multidimensionalMean
from sampleCovariance import sampleCovariance
from attributeCorrelation import attributeCorrelation
from normalizeRange import normalizeRange
from normalizeStandard import normalizeStandard
from covarianceMatrix import covarianceMatrix
from labelEncode import labelEncode 

IN_FILE = './machine.data'

#Convert data from 'machine.data' into np arrays
def handleData():
    pass

#Call each of the above functions with the dataset
def main():
    multidimensionalMean()
    sampleCovariance()
    attributeCorrelation()
    normalizeRange()
    normalizeStandard()
    covarianceMatrix()
    labelEncode()

if( __name__ == "__main__"):
    main()
