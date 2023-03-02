import numpy as np

from handleData import handleData
from multidimensionalMean import multidimensionalMean
from sampleCovariance import sampleCovariance
from attributeCorrelation import attributeCorrelation
from normalizeRange import normalizeRange
from normalizeStandard import normalizeStandard
from covarianceMatrix import covarianceMatrix
from labelEncode import labelEncode
from handle2D import handle2D

#Call each of the above functions with the dataset
def main():

    # x = np.array([40, 10, 50, 16])    # for testing
    # y = np.array([23, 59, 30, 7])
    # print(handleData())
    # print(handle2D())
    multidimensionalMean(handleData())
    # print(multidimensionalMean(handleData()))
    sampleCovariance(handle2D()[0], handle2D()[1])
    # print(sampleCovariance(handle2D()[0], handle2D()[1]))
    attributeCorrelation(handle2D()[0], handle2D()[1])
    # print(attributeCorrelation(handle2D()[0], handle2D()[1]))
    normalizeRange(handleData())
    # print(normalizeRange(handleData()))
    normalizeStandard(handleData())
    # print(normalizeStandard(handleData()))
    covarianceMatrix(handleData())
    # print(covarianceMatrix(handleData()))  # works the same as np.cov()
    labelEncode(handleData())
    # print(labelEncode(handleData()))


if( __name__ == "__main__"):
    main()
