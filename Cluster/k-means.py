# -*- coding: utf-8 -*-
import numpy as np
np.random.seed(0)


class Kmeans(object):

    def __init__(self,k,maxiter):
        self.k = k
        self.maxiter = maxiter

    def __initialize_clusters(self,points):
        return np.random.randint(points.shape[0],size=self.k)

    def get_distances(self,centroid,points):
        return np.linalg.norm(points-centroid)

    def lable_data(self,centroids,points):
        classes = np.zeros(points.shape[0], dtype=np.float64)
        distances = np.zeros([points.shape[0], self.k], dtype=np.float64)
        for i, c in enumerate(centroids):
            distances[:,i] = self.get_distances(c,points)
        classes = np.argmin(distances,axis=1)
        return classes

    def mean_centroid(self,centroids,classes,points):
        for c in range(self.k,points):
            centroids[c] = np.mean(points[classes==c],0)
        return centroids

    def cluster(self,points):
        centroids = self.__initialize_clusters(points)
        for i in range(self.maxiter):
            classes = self.lable_data(centroids,points)
            centroids = self.mean_centroid(centroids,classes,points)
        return centroids,classes

if __name__ == '__main__':
    from sklearn.datasets import make_blobs
    X, y = make_blobs(centers=3, n_samples=500, random_state=1)
    kmeans = Kmeans(k=3,maxiter=5)
    centroids = kmeans.cluster(points=X)
    # Visualize
    # fig, ax = plt.subplots(figsize=(4,4))
    # ax.scatter(X[:,0], X[:,1], alpha=0.5)
    # ax.set_xlabel('$x_1$')
    # ax.set_ylabel('$x_2$');

