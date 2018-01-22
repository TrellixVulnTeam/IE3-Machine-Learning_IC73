import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, naive_bayes, linear_model
from sklearn.metrics import mean_squared_error, r2_score



diab = datasets.load_diabetes()


# Use only one feature
diab_x = diab.data[:, np.newaxis, 2]

#split into training and testing datasets
diab_x_train = diab_x[:-20]
diab_x_test = diab_x[-20:]

diab_y_train = diab.target[:-20]
diab_y_test = diab.target[-20:]


#create linear regression object
regr = linear_model.LinearRegression()

#train the linear_model
regr.fit(diab_x_train, diab_y_train)

#make predictions using the training set
diab_y_pred = regr.predict(diab_x_test)

lin_score = regr.score(diab_x_test, diab_y_test)
print("Linear Regression score: ", lin_score)

plt.scatter(diab_x_test, diab_y_test, color='black')
plt.plot(diab_x_test, diab_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

nb = naive_bayes.GaussianNB()
nb.fit(diab_x_train, diab_y_train)

nb_predict = nb.predict(diab_x_test)
nb_score = nb.score(diab_x_test, diab_y_test)
print("Naive Bayes Score: ", nb_score)


plt.scatter(diab_x_test, diab_y_test, color='black')
plt.plot(diab_x_test, nb_predict, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

logistic = linear_model.LogisticRegression()
logistic.fit(diab_x_train, diab_y_train)

logistic_predict = logistic.predict(diab_x_test)
logistic_score = logistic.score(diab_x_test, diab_y_test)
print("Logistic Regression Score: ", logistic_score)

plt.scatter(diab_x_test, diab_y_test, color='black')
plt.plot(diab_x_test, logistic_predict, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
