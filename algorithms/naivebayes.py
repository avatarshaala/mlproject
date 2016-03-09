__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from myutils.frequencytable import *

def getpriors(targets):
    priors = {}
    for target in targets:
        updatefrequency(priors, target)
    n = len(targets)
    priors.update((x,y/n) for x, y in priors.items())

    return priors

'''This function calculates individual likelihood probabilities such as p(xi | ck) for each feature and class
and stores in a dictionary
'''
def train(instances, targets):
    conditionalfeaturecounts = {} #count of feature given the class
    classcounts = {} #frequency of each classes
    traininginstancescount = len(targets)
    if traininginstancescount != len(targets):
        print("error: class and features are of unequal lengths")
        return
    i = 0
    #count the features given target by iterating through each instance
    for instance in instances:
        features = instance.copy()
        j = 1
        #update class frequency table with the counts of each class
        updatefrequency(classcounts,targets[i])

        #update counts of each feature given target (key is x1=some value | y = some value)
        for feature in features:
            feature = "x{}={}".format(j,feature)
            j += 1
            condition = feature + " | " + "y={}".format(targets[i])
            #update the likelihood table with the condition counts of features
            updatefrequency(conditionalfeaturecounts,condition)
        i += 1

    return traininginstancescount, classcounts, conditionalfeaturecounts

def getlikelihoods(classcounts, conditionalfeaturecount, instance):

    features = instance.copy()

    #initialize likelihood for each class to 1
    likelihoods =  {label: 1 for label, count in classcounts.items()}

    #do for each label
    for label, count in classcounts.items():

        j = 1
        #do for each feature
        for feature in features:

            feature = "x{}={}".format(j,feature)
            condition = feature + " | " + "y={}".format(label)
            #multiply partial likelihood for each label with likelihood of feature for the label
            likelihoods[label] *= conditionalfeaturecount[condition]/classcounts[label]
            j += 1
    return likelihoods

def test(traininginstancescount, classcounts,conditionalfeaturecounts, instance):
    priors = classcounts.copy()
    n = traininginstancescount
    priors.update((x,y/n) for x, y in priors.items())

    print(priors)
    print(conditionalfeaturecounts)
    posteriors = getlikelihoods(classcounts, conditionalfeaturecounts, instance)
    print(posteriors)
    posteriors.update((x,priors[x] * y) for x, y in posteriors.items())
    print(posteriors)
    maxlabel = max(posteriors, key=lambda i: posteriors[i])
    return maxlabel, posteriors[maxlabel]