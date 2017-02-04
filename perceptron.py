#!/usr/bin/env python
"""perceptron class"""
import random, math

class perceptron:
    
    def __init__(self, n, lower, upper):
        self.parameters = createParameters(lower, upper)
        self.learningRate = 1.0

        
    def createParameters(self, n, lower, upper):
        """return list of length n of randomly generated parameters"""
        parameters = []
        for _ in range(n+1):
            parameters.append(random.random(lower, upper))
        return parameters
    
    def train(self, n, parameters, point, classification):
        #TODO: Change activation function
        """train on one point"""
        hypothesis = 0.0
        for i in range(len(point)):
            hypothesis += point[i]*parameters[0]
        sign = math.copysign(1.0, hypothesis)
        for i in len(point):
            parameters[i] += learningRate*sign*point[i]
        parameters[-1] += learningRate*sign
        return parameters
