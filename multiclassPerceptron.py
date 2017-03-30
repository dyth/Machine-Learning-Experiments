#!/usr/bin/env python
"""train perceptron and plot graph of accuracy over time"""
import random
from perceptron import perceptron
from matplotlib import pyplot
from createData import point
from createData import createData


def train(perceptrons, point, labels):
    'train the perceptrons'
    for i in range(labels):
        if (point.label == i):
            perceptrons[i].train(point.position, 1.0)
        else:
            perceptrons[i].train(point.position, -1.0)
    return perceptrons

            
def evaluate(perceptrons, testing, labels):
    'evaluate % accuracy of perceptron'
    accuracy = 0.0
    for point in testing:
        predictions = [p.predict(point.position) for p in perceptrons]
        if (predictions.index(max(predictions)) == point.label):
            accuracy += 1.0
    return 100.0 * (accuracy / len(testing))



# number of labels; dimensionality of datapoints; learning rate
labels = 4
dimensionality = 10
learningRate = 0.1
samples = 10000

# create training and testing data
training, testing = createData(labels, dimensionality, samples)

# initialise perceptrons
perceptrons = [perceptron(dimensionality, learningRate) for _ in range(labels)]

# train perceptron point by point; evaluate its accuracy and add to history
history = []
for point in training:
    perceptrons = train(perceptrons, point, labels)
    history.append(evaluate(perceptrons, testing, labels))
    
# plot on graph
pyplot.plot(history)
pyplot.show()
