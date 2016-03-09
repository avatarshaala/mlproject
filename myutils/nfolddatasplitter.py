#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
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

def get_fold_indices(datalength, numoffolds):

    validationlist = []
    foldlength = int(datalength / numoffolds)
    #each fold gets one more data point until residue is zero
    residue = datalength % numoffolds
    allindices = set([i for i in range(0,datalength)])
    for i in range(0, numoffolds):
        share = 0
        if residue > 0:
            share = 1
        residue -= 1
        testmin = i * (foldlength + share)
        testmax = testmin + (foldlength + share) - 1
        testindices = [j for j in range(testmin,testmax + 1)]
        trainindices = sorted(list(allindices-set(testindices)))
        validationlist.append((testindices,trainindices))

    return validationlist


#test code below
lst = get_fold_indices(56, 10)

print(lst[8])
