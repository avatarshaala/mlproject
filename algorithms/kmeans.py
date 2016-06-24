__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
import os
import numpy as np
from myutils.csvfilereader import read_training_data
# kmeans clustering algorithm
# data = set of data points
# k = number of clusters
# centroids = initial list of centroids (if provided)
#


class kmeans:
    def __init__(self, data, k):
        self.data = np.array(data)
        self.k = k
        print("value of k:",self.k)

    def get_clusters(self,centroids = None):
        if(centroids == None):
            centroids = []
        # print("CTR: ", len(centroids))

        #if nothing is initialized as centroid
        if len(centroids)== 0:
            centroids = self.randomize_centroids(centroids)

        # for i in enumerate(centroids):
        #     print(i[1])

        old_centroids = [[] for i in range(self.k)]

        iterations = 0
        while not (self.has_converged(centroids, old_centroids, iterations)):
            iterations += 1

            clusters = [[] for i in range(self.k)]

            # assign data points to clusters
            clusters = self.euclidean_dist(centroids, clusters)

            # recalculate centroids
            index = 0
            final_clusters = []
            for cluster in clusters:
                final_clusters.append(np.array(cluster).tolist())
                print("old centroid size: {} centroids size: {}, {}".format(len(old_centroids), len(centroids),index))
                old_centroids[index] = centroids[index]
                centroids[index] = np.mean(cluster, axis=0).tolist()
                index += 1

            print("iterations: ", iterations)
        '''
        print("The total number of data instances is: " + str(len(self.data)))
        print("The total number of iterations necessary is: " + str(iterations))
        print("The means of each cluster are: " + str(centroids))
        print("The clusters are as follows:")
        for cluster in clusters:
            print("Cluster with a size of " + str(len(cluster)) + " starts here:")
            print(np.array(cluster).tolist())
            print("Cluster ends here.")
        '''
        return centroids, final_clusters

    # Calculates euclidean distance between
    # a data point and all the available cluster
    # centroids.
    def euclidean_dist(self,centroids, clusters):
        for instance in self.data:
            # Find which centroid is the closest
            # to the given data point.

            mu_index = min([(i[0], np.linalg.norm(instance-centroids[i[0]])) \
                                for i in enumerate(centroids)], key=lambda t:t[1])[0]


            try:
                clusters[mu_index].append(instance)
            except KeyError:
                clusters[mu_index] = [instance]

        # If any cluster is empty then assign one point
        # from data set randomly so as to not have empty
        # clusters and 0 means.
        for cluster in clusters:
            if not cluster:
                cluster.append(self.data[np.random.randint(0, len(self.data), size=1)].flatten().tolist())

        return clusters


    # randomize initial centroids
    def randomize_centroids(self, centroids):
        for cluster in range(0, self.k):
            centroids.append(self.data[np.random.randint(0, len(self.data), size=1)].flatten().tolist())
        return centroids


    # check if clusters have converged
    def has_converged(self, centroids, old_centroids, iterations):
        MAX_ITERATIONS = 10
        if iterations > MAX_ITERATIONS:
            return True
        return old_centroids == centroids

    def get_cluster_center(self, centroids, instance):

        instance = np.array(instance)
        mu_index = min([(i[0], np.linalg.norm(instance-centroids[i[0]])) \
                        for i in enumerate(centroids)], key=lambda t:t[1])[0]
        return centroids[mu_index]

'''
#test example below

trainingfilename = "../testdata/iris.csv"
    #read the instances and target output from training file

instances,targets = read_training_data(trainingfilename)
instances = [[float(x) for x in instance] for instance in instances]

#print(instances)
k = 3
km = kmeans(instances,k)
centroids, clusters = km.get_clusters()
# print(np.array([1.5,3.5,3,3,2.7]))
cc= km.get_cluster_center(centroids,[1.5,3.5,3.3,2.7])
print(cc)
'''