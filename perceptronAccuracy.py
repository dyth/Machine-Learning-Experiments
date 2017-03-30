#!/usr/bin/env python
"""train perceptron and plot graph of accuracy over time"""
import random
from perceptron import perceptron
from matplotlib import pyplot


class point:

    def randomList(self, n):
        'return list of len(n) of randomly generated floats in range {0, 1}'
        return [random.random() for _ in range(n)]

    def classifyData(self, position):
        'give class of data in the range of {0, range}'
        # currently binary separable along 0 = x - y
        # for now return magnitude
        if (position[0] - position[1] > 0):
            return 1.0
        else:
            return -1.0
    
    def __init__(self, dimensionality):
        'store position and coordinates'
        self.position = self.randomList(dimensionality)
        self.label = self.classifyData(self.position)
        

        
def createData(samples, dimensionality):
    'return list of len(samples) of points'
    return [point(dimensionality) for _ in range(samples)]


def evaluate(perceptron, testPoints, testSamples):
    'evaluate % accuracy of perceptron'
    accuracy = 0.0
    for point in testPoints:
        if (perceptron.classify(point.position) * point.label > 0.0):
            accuracy += 1.0
    return 100.0 * (accuracy / testSamples)



# determine size and scale of problem
samples = 1000
testSamples = max(100, samples / 10)
dimensionality = 2
learningRate = 0.2

# create training and testing data
datapoints = createData(samples, dimensionality)
testPoints = createData(testSamples, dimensionality)

# initialise perceptron
perceptron = perceptron(dimensionality, learningRate)

history = []
for point in datapoints:
    # train perceptron on a datapoint, then evaluate its accuracy
    perceptron.train(point.position, point.label)
    history.append(evaluate(perceptron, testPoints, testSamples))
    
# plot on graph
pyplot.plot(history)
pyplot.show()
