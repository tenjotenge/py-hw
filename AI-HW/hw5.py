import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Sample data
data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Print the data
print("Data:")
print(data)

# Create a function to create a text-based scatter plot
def scatter_plot(data, title):
    min_x, min_y = np.min(data, axis=0)
    max_x, max_y = np.max(data, axis=0)

    rows = []
    for y in np.arange(max_y, min_y - 1, -1):
        row = []
        for x in np.arange(min_x, max_x + 1):
            if [x, y] in data.tolist():
                row.append("X")
            else:
                row.append(" ")
        rows.append("".join(row))
    print("\n" + title)
    for row in rows:
        print(row)

# K-Means Clustering
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
kmeans_labels = kmeans.predict(data)
kmeans_centroids = kmeans.cluster_centers_

# Print K-Means results with scatter plot
scatter_plot(data, "K-Means Clustering")
print("Cluster Labels:", kmeans_labels)
print("Centroid Coordinates:", kmeans_centroids)

# Hierarchical Clustering
linkage_matrix = linkage(data, method='complete')

# Print Hierarchical Clustering results
print("\nHierarchical Clustering")
dendrogram(linkage_matrix)
plt.title("Hierarchical Clustering")
plt.show()

# DBSCAN Clustering
dbscan = DBSCAN(eps=2, min_samples=2)
dbscan_labels = dbscan.fit_predict(data)

# Print DBSCAN results with scatter plot
scatter_plot(data, "DBSCAN Clustering")
print("Cluster Labels:", dbscan_labels)
