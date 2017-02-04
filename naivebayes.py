#!/usr/bin/env python
"""Multinormal Naive Bayes using sklearn"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
import numpy as np

# create points and their parent distributions. Multinomial only works for positive real values.
X = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
Y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

# create gaussian classifier and train on x, y values
#modelMultinomial = MultinomialNB()
modelBernoulli = BernoulliNB()
modelGaussian = GaussianNB()
#modelMultinomial.fit(X, Y)
modelBernoulli.fit(X, Y)
modelGaussian.fit(X, Y)

# return predictions for data points
#print modelMultinomial.predict([[1,2],[3,4]])
print modelBernoulli.predict([[1,2],[3,4]])
print modelGaussian.predict([[1,2],[3,4]])
