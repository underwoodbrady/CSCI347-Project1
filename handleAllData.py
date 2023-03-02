import numpy as np

IN_FILE = './machine.data'

#Convert data from 'machine.data' into np arrays
def handleAllData():
    outputArray = np.array([0,0,0,0,0,0,0,0,0,0])
    with open(IN_FILE, 'r') as fileI:
        for line in fileI:
            line = line.rstrip('\n')
            commaSeparated = line.split(",")
            outputArray = np.vstack((outputArray, commaSeparated))
    outputArray = np.delete(outputArray, 0, 0)
    return outputArray


def separateCategorical(inp):
    categorical1 = []
    categorical2 = []
    for i in range(len(inp)):
        categorical1.append(inp[i][0])
        categorical2.append(inp[i][1])
    return np.array([categorical1,categorical2])

