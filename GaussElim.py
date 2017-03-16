#!/usr/bin/env python

n = input("Number of equations = ")
equations = []

def neweq(n):
    'take n+1 values from an equation and append them into an array'
    values = []
    line = raw_input("Separate with space")
    newequation = line.split(" ")
    for i in range(n+1):
        newval = newequation.pop(0)
        x = float(newval)
        values.append(x)
    equations.append(values)

    
def Gauss():
    'print set of equations as a matrix'
    for eq in equations:
        print eq
    print "\n"
    

def divide(row, e):
    'divide all elements within row by e'
    divr = equations[row][e]
    for elem in range(n+1):
        equations[row][elem] /= divr


def subtract(i):
    'subtract row from array'
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
   #Gauss()      UNCOMMENT THIS TO SEE WORKING OUT
   
# Find the answer
answers = []
for cord in range(n):
    gene   = equations[cord][cord]
    answer = equations[cord][n] / gene
    answers.append(answer)
print answers
