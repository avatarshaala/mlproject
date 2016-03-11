#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from random import shuffle
from algorithms.naivebayes import *
'''current implementation of cross validation only handles categorical outputS'''
def do_nfolds_cross_validations(model, folds, instances,targets):

    if len(instances) != len(targets):
        print("Error: Number of instances should be equal to number of targets")
        return
    foldslist = get_fold_indices(len(instances), folds, shuffled=True)

    confusionmatrix = {}
    for fold in foldslist:
        testindices = fold[0]
        trainindices = fold[1]

        traininstances = [instances[i] for i in trainindices]
        traintargets = [targets[i] for i in trainindices]

        testinstances = [instances[i] for i in testindices]
        testtargets = [targets[i] for i in testindices]

        model.train(traininstances,traintargets)
        #test each test instance
        for i in range(len(testinstances)):
            output = model.test(testinstances[i])

            if type(output) != type(1) and type(output) != type(1.2):#if output is not integer or float (i.e output is tuple or array)
                output = output[0]
            #create confusion matrix
            key = "{}:{}".format(testtargets[i],output)
            if key in confusionmatrix:
                confusionmatrix[key] +=1
            else:
                confusionmatrix[key] = 1

    print(confusionmatrix)
    return confusionmatrix



'''
 56 data points
        10 folds
        each fold contains 5 data points in general
        but 56 % 10 = 6 therefore the extra 6 data points are distributed among the folds
          0   1   2   3 .............55   56
        |___|___|___|___|___|___|___|___|___|

        folds:
             0           1         2     .................8         9
        |__________|__________|__________|__________|__________|__________|

        0          5          11         17         23

        0  5  11  17  23  29  34  39  44  49

'''

def get_fold_indices(datalength, numoffolds, shuffled=False):

    #datalist = [i for i in range(datalength)]

    allindices = [i for i in range(0,datalength)]
    if shuffled:
        shuffle(allindices)
    foldslist = []
    foldlength = int(datalength / numoffolds)
    #each fold gets one more data point until residue is zero
    residue = datalength % numoffolds
    testmax = -1
    testmin = 0
    for i in range(0, numoffolds):
        share = 0
        if residue > 0:
            share = 1
            residue -= 1
        #testmin = i * (foldlength + share)
        #testmax = testmin + (foldlength + share) - 1
        testmin = testmax + 1
        testmax = testmin + (foldlength + share)-1
        testindices = [allindices[j] for j in range(testmin,testmax + 1)]
        trainindices = sorted(list(set(allindices)-set(testindices)))
        foldslist.append((testindices,trainindices))

    return foldslist

'''
#test code below

lst = get_fold_indices(56, 10, shuffled = True)
print(lst[3])

print("\n\n")
for i in range(len(lst)):
    print("{}: {}".format(i,lst[i]))

'''

