import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# initializing the iris dataset of flowers
iris = load_iris()

# creating a data frame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.head())

# adding(appending) the target field in the dataframe too
df['target'] = iris.target
# print(df.head())

print(iris.target_names)  # 0 -> setosa, 1 -> versicolor, 2 -> virginica

# print(df[df.target == 2].head())

# adding another field for the names of flower
df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])
# print(df.head())

# separating the dataframes for all 3 types of the flower types
df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

# plotting the points for visualization
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='blue', marker='.')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color='red', marker='_')
# plt.show()

# diviiding in X & y
X = df.drop(['target', 'flower_name'], axis=1)
y = df.target

# splitting in train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# training the model
model = SVC()
model.fit(X_train, y_train)

# testing the model
print(model.score(X_test, y_test) * 100)
