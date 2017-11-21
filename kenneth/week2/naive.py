from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB, GaussianNB

iris = datasets.load_iris()

bnb = GaussianNB()

y_pred = bnb.fit(iris.data, iris.target).predict(iris.data)

print("number of mislabeled points out of a total %d points: %d" % (iris.data.shape[0], (iris.target!= y_pred).sum()))
