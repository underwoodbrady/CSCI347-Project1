import numpy as np

from handleAllData import handleAllData, separateCategorical

#Encodes data through basic label encoding
def labelEncode(arr):
    values = {}
    output = []
    inc = 1
    for i in range(len(arr)):
        if values.get(arr[i]) != None:
            output.append(values.get(arr[i]))
        else:
            values[arr[i]] = inc
            output.append(inc)
            inc +=1
    return output


#pulls in dataset and separates categorical data
allData = handleAllData()
categorical = separateCategorical(allData)

#encodes each column of categorical data separately
firstEncoded = labelEncode(categorical[0])
secondEncoded = labelEncode (categorical[1])

#replaces original dataset with new encodings
def replaceEncoding():
    for i in range(len(allData)):
        allData[i][0] = firstEncoded[i]
        allData[i][1] = secondEncoded[i]

replaceEncoding()

#prints new and improved dataset
print(allData)

OUTPUT_FILE = "encoded-machine.data"

#creates new CSV with encoded machine.data
def createNewCSV():
    with open(OUTPUT_FILE, 'a') as fileO:
        for row in allData:
            for i, el in enumerate(row):
                if i == 9:
                    fileO.write(el)
                else:
                    fileO.write(el+",")
            fileO.write("\n")

createNewCSV()

