#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
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
    traininginstancescount, classcounts, conditionalfeaturecounts = train(instances,targets)

    maxlabel, posterior =  test(traininginstancescount,classcounts,conditionalfeaturecounts,[1,1,0])
    print( maxlabel, posterior)

if __name__ == "__main__":main()