import sklearn.datasets as data
import random
from sklearn import linear_model

flowers = data.load_iris()
training_indices = training_indices = [0,1,2,3,4,5,6,70,71,72,73,74,75,76,140,141,142,143,144,145,146]
training_data = []
training_classes = []

testing_indices = []
testing_data = []
testing_classes = []

size = len(flowers.data) - 1

# generate training data
# for ii in range(20) :
#     training_indices.append(random.randint(0,size))

for ii in range(50) :
    testing_indices.append(random.randint(0,size))

for jj in training_indices :
    training_data.append(flowers.data[jj])
    training_classes.append(flowers.target[jj])

for jj in testing_indices :
    testing_data.append(flowers.data[jj])
    testing_classes.append(flowers.target[jj])


clf = linear_model.LinearRegression()

clf.fit(training_data, training_classes)

predictions = clf.predict(testing_data)
print(predictions)
print(testing_classes)
scat = clf.score(testing_data, testing_classes)
print(scat)
