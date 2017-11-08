from sklearn import tree
from sklearn.datasets import load_wine
import graphviz

# classes in the dataset:
# class0 
# class1
# class2

# Classifiers:
# gini - measure of how often a randomly chosen element from a set would be incorrectly labeled
# alcohol - alcohol content in the wine
# proline - the most abundant amino acid in grape juice and wine
# hue - color of the wine
# flavanoids - diverse group of plant chemicals found in all fruits and vegetables
# magnesium - Mg content

wine = load_wine()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(wine.data, wine.target)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=wine.feature_names,
class_names=wine.target_names,filled=True,
rounded=True, special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("wine")
