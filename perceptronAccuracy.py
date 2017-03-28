#!/usr/bin/env python
"""train perceptron and plot graph of accuracy over time"""
import random
from perceptron import perceptron
from matplotlib import pyplot

def randomList(samples):
    'return randomly generated sample points'
    return [random.random() for _ in range(samples)]


def createData(samples, dimensionality):
    'return list of len(samples) with <dimensionality>, as well as threshold'
    # currently binary separable along 0 = x - y
    datapoints = [randomList(samples) for _ in range(dimensionality)]
    # zList is a threshold determining magnitude of classification
    #thresholds = [datapoints[0][i] - datapoints[1][i] for i in range(samples)]
    thresholds = [datapoints[0][i] - 0.5 for i in range(samples)]
    return datapoints, thresholds


def evaluate(perceptron, testPoints, testThreshold,
                 testSamples, dimensionality):
    'evaluate accuracy of perceptron'
    accuracy = 0.0
    for i in range(testSamples):
        testData = [testPoints[d][i] for d in range(dimensionality)]
        if (perceptron.classify(testData) * testThreshold[i] > 0.0):
            accuracy += 1.0
    accuracy = 100.0 * (accuracy / testSamples)
    return accuracy

    
# determine size and scale of problem
samples = 1000
testSamples = max(100, samples / 10)
dimensionality = 3

# create training and testing data
datapoints, thresholds = createData(samples, dimensionality)
testPoints, testThreshold = createData(testSamples, dimensionality)

# initialise perceptron
perceptron = perceptron(dimensionality)

history = []
for i in range(samples):
    # train perceptron one datapoint at a time
    datapoint = [datapoints[d][i] for d in range(dimensionality)]
    perceptron.train(datapoint, thresholds[i])

    # evaluate accuracy of perceptron using testing data, then append to history
    accuracy = evaluate(perceptron, testPoints, testThreshold,
                            testSamples, dimensionality)
    history.append(accuracy)
    
# plot on graph
pyplot.plot(history)
pyplot.show()
