from sklearn import tree
from sklearn import datasets
import numpy as np

def percentage(arr1, arr2):
    a1 = arr1.tolist()
    a2 = arr2.tolist()
#     print(arr1)
#     print(arr2)
    arrlen = len(a1)
    count = 0
    for i in range(0, arrlen):
        if (a1[i] == a2[i]):
            count+=1
    return count/arrlen

digits = datasets.load_digits()

max = int(len(digits.target)/2)
for i in range(1,max):

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(digits.data[:-i], digits.target[:-i])
    
#     print(clf.predict(digits.data[-i:]))
#     print(digits.target[-i:])
    print(percentage(clf.predict(digits.data[-i:]),digits.target[-i:]))



