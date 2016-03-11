#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from algorithms.naivebayes import *

from myutils.csvtrainingdatareader import read_training_data
#from myutils.nfolddatasplitter import *
from algorithms.naivebayes import *
def main():

    instances = [
                    [1,1,1],
                    [1,0,1],
                    [1,0,0],
                    [0,1,1],
                    [0,0,0]
                 ]
    targets = [1,0,0,0,1]

    nbayes = naivebayes()
    traininginstancescount, classcounts, conditionalfeaturecounts = nbayes.train(instances,targets)

    maxlabel, posterior =  nbayes.test([1,1,0])
    print( maxlabel, posterior)


    trainingfilename = "hw2-data/naivebayes.csv"
    #read the instances and target output from training file
    instances,targets = read_training_data(trainingfilename)
    print(targets)

if __name__ == "__main__":main()