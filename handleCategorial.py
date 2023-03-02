
import numpy as np
import csv
IN_FILE = './machine.data'

def handleCategorical():
    with open(IN_FILE, 'r') as file:
        reader = csv.reader(file)
        data = [[row[0], row[1]] for row in reader]   # first 2 parts of our data set are the only categorical parts
    return data