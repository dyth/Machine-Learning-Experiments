#!/usr/bin/env python
"""
Support Vector Machine using SLSQP -- sequential quadratic programming
"""
import random
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


# randomly generate n training data samples and parities
n, xlist, ylist, zlist = 100, [], [], []
x_yes, y_yes, x_no, y_no = [], [], [], []
for i in range(n):
    x, y = random.random(), random.random()
    xlist.append(x)
    ylist.append(y)
    if (x - y > 0):
        x_yes.append(x)
        y_yes.append(y)
        zlist.append(1)
    else:
        x_no.append(x)
        y_no.append(y)
        zlist.append(-1)
        

# constraint and Lagrangian
cons = ({'type': 'eq',
         'fun' : lambda x: sum([x[i]*zlist[i] for i in range(n)])})
def SVMLagrangian(a):
    acc = 0.0
    for i in range(len(xlist)):
        for j in range(len(xlist)):
            dotprod = (xlist[i]*xlist[j] + ylist[i]*ylist[j])
            acc += a[i]*a[j]*zlist[i]*zlist[j]*dotprod
    return 0.5*acc - sum(a)

# x0 inital vector a 0 vector, bounds (b) all greater than 0
x0, b = [0 for _ in range(n)], [(0, None) for _ in range(n)]

# Optimisation, return r.x
r = minimize(SVMLagrangian, x0, bounds=b, constraints=cons, method='SLSQP',
             options={'disp': True})

a = sum([xlist[i]*r.x[i]*zlist[i] for i in range(n)])
b = sum([ylist[i]*r.x[i]*zlist[i] for i in range(n)])
print a, b

pyplot.xlim([0,1]) # x-axis limits
pyplot.ylim([0,1]) # y-axis limits
pyplot.scatter(x_yes,y_yes,marker="o",color="g")
pyplot.scatter(x_no,y_no,marker="o",color="r")

lineplot, = pyplot.plot([],[],color="k")
lineplot.set_xdata([0,1])
lineplot.set_ydata([0,-a/b])

pyplot.show()
