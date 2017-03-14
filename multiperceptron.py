#!/usr/bin/env python
"""experiments in networks from two continous dimensions to multiple discrete"""
import random, time, csv
from matplotlib import pyplot
import perceptron


def createData(n, name):
    """create and classify n random data points, then write in .csv"""
    with open(name, 'wb') as openName:
        writer = csv.writer(openName, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for _ in range(n):
            x, y = random.random(), random.random()
            if ((y < x) and (y > 2.0 - 3.0 * x)):
                z = 0
            elif (2.0 - 3.0 * y > x):
                z = 1
            else:
                z = 2
            writer.writerow([str(x), str(y), str(z)])
        openName.close()

        
def addToDictionary(dictionary, key):
    if (key in dictionary):
        dictionary[key] += 1
    else:
        dictionary[key] = 1

        
def countFile(name):
    """open .csv and create dictionaries of frequencies"""
    dictionary = {}
    with open(name, 'rb') as openName:
        reader = csv.reader(openName, delimiter=' ', quotechar='|')
        for row in reader:
            if (row[2] == '0'):
                addToDictionary(dictionary, '0')
            elif (row[2] == '1'):
                addToDictionary(dictionary, '1')
            else:
                addToDictionary(dictionary, '2')


def csvToList(filename):
    """read csv and create required list"""
    points = []
    with open(filename, 'rb') as openName:
        reader = csv.reader(openName, delimiter=' ', quotechar='|')
        for row in reader:
            points.append([float(row[0]), float(row[1]), float(row[2])])
    return points


createData(100, 'twoToThree.csv')
points = csvToList('twoToThree.csv')
print points
