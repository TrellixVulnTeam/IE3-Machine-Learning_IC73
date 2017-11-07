# Messing around with Decision Trees

from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
from random import *

iris = load_iris()

# Randomly generate 15 indices to remove from the dataset to serve as testing data
test = []
for i in range(15):
	ind = randint(0, 149)
	test.append(ind)

# Create training data
train_target = np.delete(iris.target, test)
train_data = np.delete(iris.data, test, axis = 0)

# Create testing data
test_target = iris.target[test]
test_data = iris.data[test]

# Make the decision tree and train it
dTree = tree.DecisionTreeClassifier()
dTree.fit(train_data, train_target)

# How well does it work?
print("Testing Targets: ", test_target)
print("Predicted Targets: ", dTree.predict(test_data))