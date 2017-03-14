#!/usr/bin/env python
"""create binary seperable space and train perceptron"""
import random
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
    'plot binary separable space'
    # split data into classes yes and no depending on classification
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
    # set bound on range of x and y axes, then plot data
    pyplot.xlim([0, 1])
    pyplot.ylim([0, 1])
    pyplot.scatter(yes[0], yes[1], marker="o", color="g")
    pyplot.scatter(no[0], no[1], marker="o", color="r")
    # return a straight line plot within the data
    lineplot, = pyplot.plot([], [], color="k")
    return lineplot


def error(datapoint, threshold, weights, dimensionality):
    'create linear hypothesis between datapoint and weights'
    hypothesis = 0.0
    for i in range(dimensionality):
        hypothesis += datapoint[i] * weights[i]
    hypothesis += (weights[-1] - threshold)
    return hypothesis


def train(datapoint, hypothesis, weights, dimensionality):
    'alter weight depending on datapoint'
    for i in range(dimensionality):
        weights[i] -= hypothesis * datapoint[i]
    weights[-1] -= hypothesis
    return weights
 

def update(lineplot, i, weights):
    'update line on graph'
    a, b, c = weights
    lineplot.set_xdata([0, 1])
    lineplot.set_ydata([-c / b, (-c - a) / b])
    pyplot.title(str(i) + " " + str(a) + " " + str(b) + " " + str(c))


    
# determine size and scale of problem
samples = 100
dimensionality = 2

# create data
datapoints, thresholds = createData(samples, dimensionality)

# separate data and initialise lineplot
yes, no = separateData(samples, datapoints, thresholds, dimensionality)
lineplot = plotData(yes, no)

# turn pyplot interactive mode on and create window
pyplot.ion()
pyplot.show()

# initialise random values of starting point
weights = randomList(dimensionality + 1)

for i in range(samples):
    # train values of a, b and c on a new datapoint
    datapoint = [datapoints[d][i] for d in range(dimensionality)]
    hypothesis = error(datapoint, thresholds[i], weights, dimensionality)
    weights = train(datapoint, hypothesis, weights, dimensionality)
    
    # pause between each update of training before updating graph
    pyplot.pause(0.1)
    update(lineplot, i, weights)

# leave final trained perceptron on screen before quitting
raw_input("Complete. Press RETURN to quit")
