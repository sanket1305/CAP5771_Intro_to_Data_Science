# WRITE YOUR CODE 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def train_and_save_kmeans(k: int):
    # load tfdif train data
    X_train_tfidf = np.load('data/tfidf_train.npy')

    # generate kmeans model
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42).fit(X_train_tfidf)

    print("Training K-Means clustering with " + str(k) + " clusters")
    print("Clustering inertia:", kmeans.inertia_)

    return kmeans

def visualize_clusters_pca():
    # load tfdif train data
    X_train_tfidf = np.load('data/tfidf_train.npy')

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_train_tfidf)

    labels = train_and_save_kmeans(23).labels_

    # Step 3: Plot the clusters
    plt.figure(figsize=(8, 6))

    # Scatter plot with x1, x2 as coordinates and color by the cluster labels
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=1)

    # Add title and labels
    plt.title('Data Classification using KMeans and PCA', fontsize=14)
    plt.xlabel('feature 1', fontsize=12)
    plt.ylabel('feature 2', fontsize=12)

    # Show the color bar to indicate the clusters
    plt.colorbar(label='Cluster Number')

    # Show the plot
    plt.savefig('output/cluster_visualization.png')

visualize_clusters_pca()