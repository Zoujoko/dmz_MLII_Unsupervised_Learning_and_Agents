import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the dataset
df = pd.read_csv("Iris.csv")

# Histograms of quantitative variables
df.hist(figsize=(10, 8))
plt.show()

# Comment on important statistical aspects
print(df.describe())

# Study of potential outliers
df.plot(kind="box", figsize=(10, 8))
plt.show()

# Correlation matrix
sns.heatmap(df.corr(), annot=True)
plt.show()

# Study of categorical data
print(df["Species"].value_counts())

# Select only the numeric columns for clustering
X = df.iloc[:, 1:-1]

# Use the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

# Fit the k-means model and predict the cluster labels
kmeans = KMeans(n_clusters=3, init="k-means++", random_state=42)
pred_labels = kmeans.fit_predict(X)

# Add the predicted cluster labels to the dataframe
df["cluster"] = pred_labels

# Visualize the clusters
sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", hue="cluster", data=df)
plt.show()

score = silhouette_score(X, pred_labels)
print('Silhouette score: {:.3f}'.format(score))
