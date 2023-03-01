import numpy as np

#Implement hash map functionality
#A function that label-encodes a two-dimensional categorical data array that is passed in as input. 
def labelEncode(inp:np.ndarray):
    hash1 = []
    hash2 = []
    for i in range(len(inp)):
        if inp[i][0] in hash1:
            print(inp[i][0], "1 included")

        else:
            print(inp[i][0], "1 gotta add")
            hash1.append(inp[i][0])

        if inp[i][1] in hash2:
            print(inp[i][1], "2 included")

        else:
            print(inp[i][1], "2 gotta add")
            hash2.append(inp[i][1])

    print(hash1, hash2)

labelEncode(np.array([["categorical", "array"],["categorical", "dog"]]))