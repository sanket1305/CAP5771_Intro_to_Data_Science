import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def train_and_save_kmeans(k: int):
    # load tfdif train data
    X_train_tfidf = np.load('data/tfidf_train.npy')

    # generate kmeans model
    kmeans = KMeans(n_clusters=k, init='k-means++').fit(X_train_tfidf)

    print("Training K-Means clustering with " + str(k) + " clusters")
    print("Clustering inertia:", kmeans.inertia_)

    return kmeans

def elbow_method():
    inertia_values = []

    # for range of k_values extract inertia
    for k in range(5, 31):
        kmeans = train_and_save_kmeans(k)
        inertia_values.append(kmeans.inertia_)
    
    # Plot the elbow curve
    plt.plot(range(5, 31), inertia_values, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia')
    # plt.show()
    plt.savefig('output/elbow_method.png')

elbow_method()