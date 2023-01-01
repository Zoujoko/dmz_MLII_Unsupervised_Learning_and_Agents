import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Assume that X is a numpy array with the original data and y is a numpy array with the labels
X = np.load("data.npy")
y = np.load("labels.npy")

# Perform PCA on the data
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# Perform t-SNE on the data
tsne = TSNE(n_components=3)
X_tsne = tsne.fit_transform(X)

# Plot the PCA projection in 2D
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.title("PCA projection in 2D")

# Plot the PCA projection in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y)
plt.title("PCA projection in 3D")

# Plot the t-SNE projection in 2D
plt.figure()
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
plt.title("t-SNE projection in 2D")

# Plot the t-SNE projection in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_tsne[:, 0], X_tsne[:, 1], X_tsne[:, 2], c=y)
plt.title("t-SNE projection in 3D")

plt.show()