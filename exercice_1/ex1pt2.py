import numpy as np

# Set the number of points to sample
n_max = 1000

# Set the mean and standard deviation for X and Y
mean_x = 75
std_x = 10
mean_y = 1.75
std_y = 0.1

# Initialize arrays to store the samples and the empirical averages
x = np.empty(n_max)
y = np.empty(n_max)
empirical_averages = np.empty((n_max, 2))

# Set the expected value of Z
expected_value = [mean_x, mean_y]

# Initialize an array to store the euclidean distances
euclidean_distances = np.empty(n_max)

# Sample the first n points and compute the empirical average for each n
for n in range(1, n_max+1):
  x[:n] = np.random.normal(mean_x, std_x, n)
  y[:n] = np.random.normal(mean_y, std_y, n)
  empirical_averages[n-1] = [x[:n].mean(), y[:n].mean()]
  euclidean_distances[n-1] = np.linalg.norm(empirical_averages[n-1] - expected_value)

# Plot the euclidean distances as a function of n
import matplotlib.pyplot as plt
plt.plot(range(1, n_max+1), euclidean_distances)
plt.xlabel('Number of samples')
plt.ylabel('Euclidean distance to expected value')
plt.show()
