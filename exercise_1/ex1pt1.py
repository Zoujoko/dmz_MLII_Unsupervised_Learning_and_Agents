import numpy as np

# Set the number of points to sample
n = 1000

# Set the mean and standard deviation for X and Y
mean_x = 75
std_x = 10
mean_y = 1.75
std_y = 0.1

# Sample n values for X and Y
x = np.random.normal(mean_x, std_x, n)
y = np.random.normal(mean_y, std_y, n)

# Plot the points in a 2-dimensional figure
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()