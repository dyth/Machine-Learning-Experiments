# Machine Learning Experiments

Implementations and experiments concerning core machine learning ideas.

## Creating training and testing data
`createData.py` and `createData.pyc`: create data using the function

> createData(\<numberOfClasses\>, <\dimensionalityOfPoints\>, <\numberOfSamples\>)

When called by another program, it returns two lists -- training and testing data. List elements are instantiations of Point, a class with two fields: a location (a list) and a label.

## Perceptrons
* `binaryPerceptron.py`: visualisation of a perceptron in 2D classifying two classes
* `kernelperceptron.py`: a demonstration of how a perceptron can be used as a kernel function, combined with another perceptron
* `multiclassPerceptron.py`: supervised learning with variable numbers of classes. Plots a graph of training number vs accuracy after training is complete.
* `perceptron.py`: class of a perceptron

## Other programs
* `GaussElim.py`: Gaussian Elimination in python
* `NeuralNetwork.ml`: poly/ML implementation of a feedforward neural network with a quadratic cost function
* `SVM.py`: Support Vector Machine with sequential quadratic programming
* `naiveBayes.py`: implementation of the Naive Bayes algorithm
