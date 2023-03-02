import numpy as np


fruits = np.array([['apple', 'banana', 'grape', 'apple', 'apple', 'grape'],['carrot', 'lettuce', 'lettuce', 'lettuce', 'tomato', 'cucumber']])

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


print(labelEncode(fruits[0]), labelEncode(fruits[1]))