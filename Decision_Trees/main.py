import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("salaries.csv")
# print(df.head())

inputs = df.drop('salary_more_then_100k', axis='columns')  # this will contain the features
target = df['salary_more_then_100k']  # this will contain the decision value

le = LabelEncoder()  # initializing label encoder class

# label encoding the classes in the features before training them in the ML model
inputs['company_n'] = le.fit_transform(inputs['company'])
inputs['job_n'] = le.fit_transform(inputs['job'])
inputs['degree_n'] = le.fit_transform(inputs['degree'])

# creating new input matrix without the old columns
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')

# initializing the model
dt = DecisionTreeClassifier(criterion='entropy')

# training the model
dt.fit(inputs_n, target)

# this would be 1.0 or 100% because we didn't split the dataset and also the dataset it quite simple
print("Model Score: ", dt.score(inputs_n, target))

# Prediction for Sales Executive in Google with Masters Degree
print(dt.predict([[2, 2, 1]]))
