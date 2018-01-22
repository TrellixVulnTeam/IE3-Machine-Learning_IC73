# Perceptron
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_wine
import numpy as np
from random import *
from sklearn.preprocessing import StandardScaler

wine = load_wine()

# Randomly generate 15 indices to remove from the dataset to serve as testing data
test = []
for i in range(20):
	ind = randint(0, 177)
	test.append(ind)

# Create training data
train_target = np.delete(wine.target, test)
train_data = np.delete(wine.data, test, axis = 0)

# Create testing data
test_target = wine.target[test]
test_data = wine.data[test]

scaler = StandardScaler()

# Fit only to the training data
scaler.fit(train_data)

# Apply the normalization to the data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

percepticon = Perceptron()

# Train the model on the data
percepticon.fit(train_data, train_target)

# Test it!
predictions = percepticon.predict(test_data)
score = percepticon.score(test_data, test_target)

# Compare predictions vs. target
print("Predictions: ", predictions)
print("Targets:     ", test_target)
print("Score: ", score)