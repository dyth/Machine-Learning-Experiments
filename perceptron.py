#!/usr/bin/env python

import random
from matplotlib import pyplot
import time

# build a binary separable space
# let the region be separated by 0 = x - y

n = 100 # number of data
xlist, ylist, zlist = [], [], []
for i in range(n):
    x, y = random.random(), random.random()
    z = x - y # the threshold
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)

# plot binary separable space
x_yes, y_yes, z_yes, x_no, y_no, z_no, zreal = [], [], [], [], [], [], []
for i in range(n):
    x, y, z = xlist[i], ylist[i], zlist[i] # z is the threshold
    if z > 0:
        x_yes.append(x)
        y_yes.append(y)
        z_yes.append(z)
        zreal.append(1)
    else:
        x_no.append(x)
        y_no.append(y)
        z_no.append(z)
        zreal.append(-1)
        
pyplot.xlim([0,1]) # x-axis limits
pyplot.ylim([0,1]) # y-axis limits
pyplot.scatter(x_yes,y_yes,marker="o",color="g")
pyplot.scatter(x_no,y_no,marker="o",color="r")
pyplot.ion()  # pyplot interactive mode on
pyplot.show() # create window

lineplot, = pyplot.plot([],[],color="k") # straight line plot

# BEGIN

# Separation line: 0 = a*x + b*y + c
a, b, c = random.random(), random.random(), random.random()

# taken new data point, adjust a, b and c.
for i in range(n):
    x, y, z = xlist[i], ylist[i], zlist[i] # threshold
    h = a*x + b*y + c - z # hypothesis -- difference in value
    a -= h*x
    b -= h*y
    c -= h        

    # draw the straight line graph for every iteration
    
    lineplot.set_xdata([0,1])
    lineplot.set_ydata([-c/b,(-c-a)/b])
    pyplot.title(str(i)+" "+str(a)+" "+str(b)+" "+str(c))
    pyplot.pause(0.1) # pause between each update of grap

raw_input("Complete")
