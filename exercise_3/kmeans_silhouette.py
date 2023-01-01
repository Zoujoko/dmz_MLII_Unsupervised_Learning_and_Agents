
"""
    Perform the k-means algorithm on toy data using scikit-learn
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
"""
import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from yellowbrick.cluster import SilhouetteVisualizer
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
fig, ax = plt.subplots(3, 2, figsize=(15,8))
for k in [2, 3, 4, 5, 6, 7]:
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=10)
    kmeans.fit(data)
    score = silhouette_score(data, kmeans.labels_)
    
    print("For n_clusters =", k,
          "The average silhouette_score is :", score)
    q, mod = divmod(k, 2)
    visualizer = SilhouetteVisualizer(kmeans, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(data)
visualizer.show()



# predict = kmeans.predict(data)
# plt.scatter(data[:, 0], data[:, 1], c=predict, s= 50, cmap='viridis')
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
# plt.show()