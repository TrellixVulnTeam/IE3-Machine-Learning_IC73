from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

#import dataset
wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

#display data: wine of 3 cultivators with 13 features
#print(wine)
print("data points: ", wine.shape[0], "\nfeatures: ", wine.shape[1]-1)
X = wine.drop('Cultivator',axis=1)
y = wine['Cultivator']

#splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

#data pre-processing
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)

predictions = mlp.predict(X_test)
print("Confusion Matrix: \n", confusion_matrix(y_test,predictions))
print("Classification Report: \n", classification_report(y_test,predictions))