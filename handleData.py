import numpy as np

IN_FILE = './machine.data'


#Convert data from 'machine.data' into np arrays
def handleData():
    outputArray = np.array([0,0]);
    with open(IN_FILE, 'r') as fileI:
        for line in fileI:
            line = line.rstrip('\n');
            commaSeparated = line.split(",")
            PRP = int(commaSeparated[8])
            ERP = int(commaSeparated[9])
            outputArray = np.vstack((outputArray,[PRP,ERP]))
    outputArray = np.delete(outputArray, 0, 0)
    return outputArray

output = handleData()

print(output)