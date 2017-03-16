#!/usr/bin/env python
"""create binary seperable space and train perceptron"""
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
    thresholds = [datapoints[0][i] - datapoints[1][i] for i in range(samples)]
    return datapoints, thresholds


def separateData(samples, datapoints, thresholds, dimensionality):
    'split data into classes yes and no depending on classification'
    # in this example, it is still binary
    yes = [[] for _ in range(dimensionality)]
    no = [[] for _ in range(dimensionality)]
    for i in range(samples):
        if (thresholds[i] > 0):
            [yes[d].append(datapoints[d][i]) for d in range(dimensionality)]
        else:
            [no[d].append(datapoints[d][i]) for d in range(dimensionality)]
    return yes, no


def plotData(yes, no):
    'plot the lists yes and no within the same axes'
    # set bound on range of x and y axes
    pyplot.xlim([0, 1])
    pyplot.ylim([0, 1])
    # plot data
    pyplot.scatter(yes[0], yes[1], marker="o", color="g")
    pyplot.scatter(no[0], no[1], marker="o", color="r")
    # return a straight line plot within the data
    lineplot, = pyplot.plot([], [], color="k")
    return lineplot


def update(lineplot, i, weights, bias):
    'update line on graph'
    a, b = weights
    c = bias
    lineplot.set_xdata([0, 1])
    lineplot.set_ydata([-c / b, (-c - a) / b])
    pyplot.title(str(i) + " " + str(a) + " " + str(b) + " " + str(c))


    
# determine size and scale of problem
samples = 100
dimensionality = 2

# create training data, separate data into categories
datapoints, thresholds = createData(samples, dimensionality)
yes, no = separateData(samples, datapoints, thresholds, dimensionality)

# create testing data
testPoints, testThreshold = createData(samples / 10, dimensionality)

# turn pyplot interactive mode on, create window and initialise lineplot
pyplot.ion()
pyplot.show()
lineplot = plotData(yes, no)

# initialise perceptron
perceptron = perceptron(dimensionality)

# train perceptron datapoint by datapoint
for i in range(samples):
    datapoint = [datapoints[d][i] for d in range(dimensionality)]
    perceptron.train(datapoint, thresholds[i])

    # evaluate testing data
    for i in range(len(testPoints)):
        print perceptron.classify(testPoints[i]), testThreshold[i]

    
    # pause between each training cycle
    pyplot.pause(0.05)
    update(lineplot, i, perceptron.weights, perceptron.bias)

# leave final trained perceptron on screen before quitting
raw_input("Complete. Press RETURN to quit")
