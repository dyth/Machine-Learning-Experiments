#!/usr/bin/env python
"""perceptron class"""
import random, math

class perceptron:
    
    def __init__(self, dimensionality):
        # create initial random weights and random bias
        self.dimensionality = dimensionality
        self.weights = [random.random() for _ in range(dimensionality)]
        self.bias = random.random()

    def error(self, datapoint, threshold):
        'create linear hypothesis between datapoint and weights'
        hypothesis = self.bias - threshold
        for i in range(self.dimensionality):
            hypothesis += datapoint[i] * self.weights[i]
        return hypothesis

    def train(self, datapoint, hypothesis):
        'alter weight depending on datapoint'
        for i in range(self.dimensionality):
            self.weights[i] -= hypothesis * datapoint[i]
        self.bias -= hypothesis
