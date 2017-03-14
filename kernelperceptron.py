#!/usr/bin/env python

import random
import time
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

# build a space that is binary separable by 0 = x - y

def drawHyperplane(axes, h):
    """
    Draws hyperplane on axes
    """
    x, y = np.arange(-0.5, 1.5, 0.1), np.arange(-0.5, 1.5, 0.1) # initalise x, y
    X, Y = np.meshgrid(x, y)  # create 'base grid'
    Z = 0 # output z values
    axes.plot_wireframe(X, Y, Z)

    
"""
Randomly generate test data and assign parities
"""
n = 100 # number of data
xlist, ylist, zlist = [], [], []
for i in range(n):
    x, y = random.random(), random.random()
    z = x - y # the threshold
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
x_yes, y_yes, x_no, y_no = [], [], [], []
for i in range(n):
    x, y, z = xlist[i], ylist[i], zlist[i] # z is the threshold
    if z > 0:
        x_yes.append(x)
        y_yes.append(y)
    else:
        x_no.append(x)
        y_no.append(y)


"""
Create figure and interactive axes
"""
figure = pyplot.figure()
axes = figure.add_subplot(111, projection='3d')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('Kernel Value')
pyplot.ion()


"""
Begin training
"""
# Hyperplane of form: 0 = a*x + b*y + c
a, b, c = random.random(), random.random(), random.random()

for i in range(n):
    # take new data point, adjust a, b, c.
    x, y, z = xlist[i], ylist[i], zlist[i] # threshold
    h = a*x + b*y + c - z # hypothesis
    a -= h*x
    b -= h*y
    c -= h
    h_yes, h_no = [], []
    
    # transform data by kernel function -- plot (x, y, h+z)
    for i in range(len(x_yes)):
        h_yes.append(a*x_yes[i] + b*y_yes[i] + c)
    for i in range(len(x_no)):
        h_no.append(a*x_no[i] + b*y_no[i] + c)

    # plot everything
    pyplot.cla()
    pyplot.title(str(i)+" "+str(a)+" "+str(b)+" "+str(c)+" "+str(h))
    axes.scatter(x_yes, y_yes, h_yes, c='g', marker='o')
    axes.scatter(x_no, y_no, h_no, c='r', marker='o')
    drawHyperplane(axes, h)
    pyplot.pause(0.05)
    
raw_input("Complete")
