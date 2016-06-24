__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from myutils.csvfilereader import read_csv_file
from algorithms.kmeans import *


def compress_file(infilename, outputfilename, k):
    instances = read_csv_file(infilename,hasheader=False)
    instances = [[float(x) for x in instance] for instance in instances]

    kmean = kmeans(instances,k)
    centroids, clusters = kmean.get_clusters()
    #print(centroids)
    outfile = open(outputfilename, "w")

    for instance in instances:
        center = kmean.get_cluster_center(centroids,instance)
        #print(center)
        strn = ""
        for val in center:
            strn += str(int(val)) + ","
        #print(strn.strip(","))
        outfile.write(strn.strip(",") + "\n")

    outfile.flush()
    outfile.close()

directory = "hw4-data/"
filename = "koala.txt"
k = 2
print("koala k2")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 5
print("koala k5")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 10
print("koala k10")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 20
print("koala k20")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)

filename = "penguins.txt"
k = 2
print("penguins k2")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 5
print("penguins k5")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 10
print("penguins k10")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)
k = 20
print("penguins k20")
compress_file(directory + filename, directory + str(k)+"_"+filename, k)

