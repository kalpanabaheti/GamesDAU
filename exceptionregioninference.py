# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Modeling with the aid of scikit-learn
from sklearn.linear_model import LinearRegression

# Visualising mean and median to understand skew
plt.plot(summary[:,0], label='Mean')
plt.plot(summary[:,1], label='Median')
plt.xlabel('values')
plt.ylabel('DAU')
title = 'Summary'
plt.title(title)
plt.legend()
plt.show()

# Data preparation
means = summary[:,0]
x = np.array([i for i in range(len(means))])
xs = x.reshape(-1, 1)

# Linear Regression
model = LinearRegression()
results = model.fit(xs, means)

# Getting the intercept and coefficient
intercept = results.intercept_
coefficient = results.coef_[0]

# Print the results
print("Intercept:", intercept)
print("Coefficient:", coefficient)
