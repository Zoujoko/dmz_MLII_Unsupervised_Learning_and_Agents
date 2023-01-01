from sklearn.cluster import AgglomerativeClustering
import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from yellowbrick.cluster import SilhouetteVisualizer
import pandas as pandasi
import scipy.cluster.hierarchy as sch

# load the data
datapath = os.path.join("data", "data.npy")
data = np.load(datapath)


cluster = AgglomerativeClustering(
    n_clusters=6, affinity='euclidean', linkage='ward')

cluster.fit(data)
labels = cluster.labels_
plt.figure(figsize=(10, 10))
# dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
# plt.title('Dendrogram')
# plt.xlabel('Customers')
# plt.ylabel('Euclidean distances')
# plt.show()

fig, ax = plt.subplots(3, 2, figsize=(15,8))
for k in [2, 3, 4, 5, 6, 7]:
    cluster =  AgglomerativeClustering(
    n_clusters=k, affinity='euclidean', linkage='ward')
    cluster.fit(data)
    cluster_labels =  cluster.fit_predict(data)
    score = silhouette_score(data, cluster_labels)
    q, mod = divmod(k, 2)
    visualizer = SilhouetteVisualizer(cluster, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(data)
visualizer.show()


plt.figure(figsize=(10, 7))
plt.scatter(data[labels == 0, 0], data[labels == 0, 1], s = 100, c = 'blue', label = 'Type 1')
plt.scatter(data[labels == 1, 0], data[labels == 1, 1], s = 100, c = 'yellow', label = 'Type 2')
plt.scatter(data[labels == 2, 0], data[labels == 2, 1], s = 100, c = 'green', label = 'Type 3')
plt.scatter(data[labels == 3, 0], data[labels == 3, 1], s = 100, c = 'black', label = 'Type 4')
plt.scatter(data[labels == 4, 0], data[labels == 4, 1], s = 100, c = 'red', label = 'Type 5')
plt.scatter(data[labels == 5, 0], data[labels == 5, 1], s = 100, c = 'pink', label = 'Type 6')
plt.legend()
plt.show()