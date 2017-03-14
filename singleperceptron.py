#!/usr/bin/env python
"""create binary seperable space and train perceptron"""
import random
from matplotlib import pyplot

def createDatapoints(samples):
    'return randomly generated sample points'
    dimension = [random.random() for _ in range(samples)]
    return dimension


def createData(samples, dimensionality):
    'return list of len(samples) with <dimensionality>, as well as threshold'
    # currently binary separable along 0 = x - y
    datapoints = [createDatapoints(samples) for _ in range(dimensionality)]
    # zList is a threshold determining magnitude of classification
    thresholds = [datapoints[0][i] - datapoints[1][i] for i in range(samples)]
    return datapoints, thresholds


def plotData(samples, datapoints, dimensionality):
    'plot binary separable space'
    # split data depending on where it is classified
    # in this example, still binary
    yes = [[] for _ in range(dimensionality)]
    no = [[] for _ in range(dimensionality)]
    
    for i in range(datapoints):
        x = xList[i]
        y = yList[i]
        if (zList[i] > 0):
            
            #[yes[d].append(x[i]) for d in range(dimensionality)]
            
            x_yes.append(x)
            y_yes.append(y)
        else:
            x_no.append(x)
            y_no.append(y)

    # set bound on range of x and y axes, then plot data
    pyplot.xlim([0, 1])
    pyplot.ylim([0, 1])
    pyplot.scatter(x_yes, y_yes, marker="o", color="g")
    pyplot.scatter(x_no, y_no, marker="o", color="r")
    
    lineplot, = pyplot.plot([], [], color="k") # straight line plot
    return lineplot

    
def train(x, y, z, a, b, c):
    """train on paramenters a, b, c, Separation line: 0 = a*x + b*y + c"""
    h = a*x + b*y + c - z # hypothesis -- difference in value
    a -= h*x
    b -= h*y
    c -= h
    return a, b, c


def update(lineplot, i, a, b, c):
    'update line on graph'
    lineplot.set_xdata([0, 1])
    lineplot.set_ydata([-c / b, (-c - a) / b])
    pyplot.title(str(i) + " " + str(a) + " " + str(b) + " " + str(c))
    return a, b, c

    
samples = 100
dimensionality = 2
datapoints, thresholds = createData(samples, dimensionality)



quit()

# initialise lineplot, turn pyplot interactive mode on and create window
lineplot = plotData(xList, yList, zList, samples, dimensionality)
pyplot.ion()
pyplot.show()

# initialise random values of starting point
a = random.random()
b = random.random()
c = random.random()

for i in range(samples):
    # train values of a, b and c on a new datapoint
    x, y, z = xList[i], yList[i], zList[i]
    a, b, c = train(x, y, z, a, b, c)
    # pause between each update of training before updating graph
    pyplot.pause(0.1)
    update(lineplot, i, a, b, c)

# leave final trained perceptron on screen before quitting
raw_input("Complete. Press RETURN to quit")
