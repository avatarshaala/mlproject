# import os
# import numpy as np
#
#
# class kmeans:
#     def __init__(self, data, k, centroids=[]):
#         self.data = data
#         self.k = k
#         self.centroids = centroids
#         if len(self.centroids) == 0:
#             self.centroids = self.get_k_random_data(self.data,self.k)
#
#     def get_clusters(self):
#
#         #centroids = []
#
#         #centroids = self.get_k_random_data(self.data,self.k)
#
#         previous_centroids = [[] for i in range(self.k)]
#
#         iterations = 0
#         while not (self.converged(self.centroids, previous_centroids, iterations)):
#             iterations += 1
#
#
#             clusters = [[] for i in range(self.k)]
#
#             # assign data points to clusters
#             clusters = self.get_new_centroids(self.data, self.centroids, clusters)
#
#             #get centroids here
#
#         print("The total number of data instances is: " + str(len(self.data)))
#         print("The total number of iterations necessary is: " + str(iterations))
#         print("The means of each cluster are: " + str(self.centroids))
#         print("The clusters are as follows:")
#         for cluster in clusters:
#             print("Cluster with a size of " + str(len(cluster)) + " starts here:")
#             print(np.array(cluster).tolist())
#             print("Cluster ends here.")
#
#         return
#
#     # Calculates euclidean distance between
#     # a data point and all the available cluster
#     # centroids.
#     def get_new_centroids(self, clusters):
#         for instance in self.data:
#             # Find which centroid is the closest
#             # to the given data point by comparing eucledian distance.
#             mu_index = min([(i[0], np.linalg.norm(instance-self.centroids[i[0]])) \
#                                 for i in enumerate(self.centroids)], key=lambda t:t[1])[0]
#             try:
#                 clusters[mu_index].append(instance)
#             except KeyError:
#                 clusters[mu_index] = [instance]
#
#         # If any cluster is empty then assign one point
#         # from data set randomly so as to not have empty
#         # clusters and 0 means.
#         for cluster in clusters:
#             if not cluster:
#                 cluster.append(self.data[np.random.randint(0, len(self.data), size=1)].flatten().tolist())
#
#
#                 # recalculate centroids
#             index = 0
#             centroids = [[] for i in range(self.k)]
#             for cluster in clusters:
#                 #previous_centroids[index] = self.centroids[index]
#                 centroids[index] = np.mean(cluster, axis=0).tolist()
#                 index += 1
#
#         return clusters
#
#
#     # randomize initial centroids
#     def get_k_random_data(self, k):
#         centroids = []
#         for cluster in range(0, k):
#             centroids.append(self.data[np.random.randint(0, len(self.data), size=1)].flatten().tolist())
#         return centroids
#
#
#     # check if clusters have converged
#     def converged(self,old_centroids, iterations):
#         MAX_ITERATIONS = 1000
#         if iterations > MAX_ITERATIONS:
#             return True
#         return old_centroids == self.centroids