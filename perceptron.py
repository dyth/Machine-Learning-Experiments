#!/usr/bin/env python
"""perceptron class"""
import random, math

class perceptron:
    
    def __init__(self, dimensionality, learningRate):
        'create initial random weights and random bias'
        self.learningRate = learningRate
        self.dimensionality = dimensionality
        self.weights = [random.random() for _ in range(dimensionality)]
        self.bias = random.random()


    def activate(self, value):
        'activation function is sigmoidal'
        return math.tanh(value)

    def predict(self, datapoint):
        'classify datapoint into a class'
        hypothesis = self.bias
        for i in range(self.dimensionality):
            hypothesis += datapoint[i] * self.weights[i]
        return self.activate(hypothesis)
        
    def error(self, datapoint, threshold):
        'create linear hypothesis between datapoint and weights'
        return threshold - self.predict(datapoint)

    def adjust(self, datapoint, hypothesis):
        'adjust weight depending on datapoint'
        for i in range(self.dimensionality):
            self.weights[i] += self.learningRate * hypothesis * datapoint[i]
        self.bias += self.learningRate * hypothesis

    def train(self, datapoint, threshold):
        'train by adjusting weights depending on hypothesis'
        hypothesis = self.error(datapoint, threshold)
        self.adjust(datapoint, hypothesis)
