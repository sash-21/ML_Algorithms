# The gradient descent algorithm written over here is in totally raw format and you would never use it as it is, people generally tend to use libraries like SKLearn where these algos are predefined.

import numpy as np


def gradient_descent(x, y):  # gradient descent function
    m_curr = b_curr = 0  # have to start with some value of m & b
    iterations = 10000  # stopping condition
    n = len(x)  # gradient
    learning_rate = 0.08  # length of each step (learning rate)

    if (len(x) == len(y)):
        for i in range(iterations):
            y_predicted = m_curr * x + b_curr

            # cost function (Mean Squared Error)
            cost = (1 / n) * sum([val**2 for val in (y - y_predicted)])

            # calculating the partial derivatives
            md = -(2 / n) * sum(x * (y - y_predicted))
            bd = -(2 / n) * sum(y - y_predicted)

            # adjust the values of m_curr & b_curr based on the learning rate
            m_curr = m_curr - learning_rate * md
            b_curr = b_curr - learning_rate * bd

            print(f"m_curr: {m_curr}, b_curr: {b_curr}, cost: {cost}, iteration: {i}")
    else:
        print("x & y values aren't the same")
        return


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
