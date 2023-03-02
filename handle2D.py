import numpy as np

IN_FILE = './machine.data'


#Convert data from 'machine.data' into 2 np arrays
def handle2D():
    arr1 = np.array([0])
    arr2 = np.array([0])
    with open(IN_FILE, 'r') as fileI:
        for line in fileI:
            line = line.rstrip('\n');
            commaSeparated = line.split(",")
            PRP = int(commaSeparated[8])
            ERP = int(commaSeparated[9])
            arr1 = np.vstack((arr1, [PRP]))
            arr2 = np.vstack((arr2, [ERP]))
    arr1 = np.delete(arr1, 0)
    arr2 = np.delete(arr2, 0)
    outputArray = np.array([arr1, arr2])
    return outputArray
