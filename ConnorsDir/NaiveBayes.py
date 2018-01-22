# Naive Bayes
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_wine
import numpy as np
from random import *

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

naive_baes = GaussianNB()

# Train the model on the data
naive_baes.fit(train_data, train_target)

# Test it!
predictions = naive_baes.predict(test_data)
score = naive_baes.score(test_data, test_target)

# Compare predictions vs. target
print("Predictions: ", predictions)
print("Targets:     ", test_target)
print("Score: ", score)