import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.head())

# Adding the target column to dataframe which determines the class of the flower
df['target'] = iris.target
# print(df.head())

# Printing the data for points having class as 1 & 2
print(df[df.target == 1].head())
print(df[df.target == 2].head())

# separating the datasets
df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]

# plotting the data
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='blue', marker='.')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color='yellow', marker='*')
plt.show()

# splitting the data in x matrix and y list
X = df.drop(['target'], axis='columns')
y = df.target

# splitting the data in training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# creating the model
knn = KNeighborsClassifier(n_neighbors=10, metric='euclidean')

# training the model
knn.fit(X_train, y_train)

# testing the model
print("Accuracy Score: ", knn.score(X_test, y_test) * 100)

# confusion matrix
y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confustion Matrix: \n", cm)

# classification report
print("Classification Report: \n", classification_report(y_test, y_pred))
