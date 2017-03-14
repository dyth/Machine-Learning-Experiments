#!/usr/bin/env python

n = input("Number of equations = ")
equations = []

# take n+1 values from an equation and appends them into an array
def neweq(n):
    values = []
    line = raw_input("Separate with space")
    newequation = line.split(" ")
    for i in range(n+1):
        newval = newequation.pop(0)
        x = float(newval)
        values.append(x)
    equations.append(values)

# print set of equations in a nice matrix form
def Gauss():
    for eq in equations:
        print eq
    print " "

# divide a row by the element e
def divide(row, e):
    divr = equations[row][e]
    for elem in range(n+1):
        equations[row][elem] /= divr

# subtract the row from the array
def subtract(i):
    for row in range(n):
        for elem in range(n+1):
            if row != i:
                equations[row][elem] -= equations[i][elem]

# generate n sets of equations                
for i in range(n):
    neweq(n)
# Change a row to a unit in a direction
for elem in range(n):
    for row in range(n):
        divide(row, elem)
# Take the difference of a row
    subtract(elem)
#    Gauss()      UNCOMMENT THIS TO SEE WORKING OUT
# Find the answer
answers = []
for cord in range(n):
    gene   = equations[cord][cord]
    answer = equations[cord][n] / gene
    answers.append(answer)
print answers
