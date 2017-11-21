import sklearn.datasets as data
import random
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

# sepal length
# sepal width
# petal length
# petal width

flowers = data.load_iris()
training_indices = [0,1,2,3,4,5,6,70,71,72,73,74,75,76,140,141,142,143,144,145,146]
training_data = []
training_classes = []

testing_indices = []
testing_data = []
testing_classes = []

size = len(flowers.data) - 1

# generate training data
# for ii in range(21) :
#     training_indices.append(random.randint(0,size))

for ii in range(50) :
    testing_indices.append(random.randint(0,size))

for jj in training_indices :
    training_data.append(flowers.data[jj])
    training_classes.append(flowers.target[jj])

for jj in testing_indices :
    testing_data.append(flowers.data[jj])
    testing_classes.append(flowers.target[jj])




penalty = None
alpha = .0001
fit_intercept = True
max_iterations = 1000
tolerance = .5
shuffle = True
verbose = 0
eta = .001
n_jobs = 4
random_state = None
class_weight = None
warm_start = False
n_iterations = None

clf = Perceptron(penalty, alpha, fit_intercept, max_iterations, tolerance, shuffle, verbose, eta, n_jobs, random_state, class_weight, warm_start, n_iterations)

clf.fit(training_data, training_classes)
predictions = clf.predict(testing_data)

print(predictions)
print(testing_classes)
scat = clf.score(testing_data, testing_classes)
print(scat)
