
"""
    Perform the k-means algorithm on toy data using scikit-learn
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
"""
import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pandas

# load the data
datapath = os.path.join("data", "data.npy")
data = np.load(datapath)

# use sklearn in order to perform the algorithm
"""
add lines here
"""

# ELBOW
# 
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=1)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# Plot the within-cluster sum of squared distances
plt.plot(range(1, 11), inertias, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Use the optimal number of clusters to fit a k-means model
optimal_k = 6  # Choose the optimal k based on the elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=1)
kmeans.fit(data)

predict = kmeans.predict(data)
plt.scatter(data[:, 0], data[:, 1], c=predict, s= 50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()