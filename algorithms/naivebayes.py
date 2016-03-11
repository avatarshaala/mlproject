__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from myutils.frequencytable import *
class naivebayes:

    def __init__(self):
        self.__classcounts__ = {}
        self.__conditionalfeaturecounts__ = {}#count of feature given the class
        self.__traininginstancescount__ = 0 # count of training data

    '''Function that returns priors of each class if default parameter is used else returns prior of a particular class'''
    def getpriors(self,label=None):

        if label != None:
            return {label:self.__classcounts__[label]/self.__traininginstancescount__}

        priors = self.__classcounts__.copy()
        priors.update((x,y/self.__traininginstancescount__) for x, y in priors.items())

        return priors

    '''Function that returns likelihood of the instance given the class or likelihood of the instance for all classes in default'''
    def getlikelihoods(self,instance, label = None):

        features = instance.copy()
        #print(print(label))
        #global __classcounts__
        #global __conditionalfeaturecounts__

        '''define a local scope function to calculate likelihood of a given data instance with if given label'''
        def likelihood(label,features, likelihoods):
            j = 1
            #do for each feature
            for feature in features:

                feature = "x{}={}".format(j,feature)
                condition = feature + " | " + "y={}".format(label)
                #print(condition)
                #multiply partial likelihood for each label with likelihood of feature for the label
                likelihoods[label] *= self.__conditionalfeaturecounts__[condition]/self.__classcounts__[label]
                #print("likelihood for ", label, likelihoods[label])
                j += 1

        '''--------------------------------'''

        if label != None:
            likelihoods = {label:1}
            likelihood(label,features, likelihoods)
            return likelihoods

        #initialize likelihood for each class to 1
        likelihoods =  {label: 1 for label, count in self.__classcounts__.items()}
        #do for each label
        for label, count in self.__classcounts__.items():
            likelihood(label,features,likelihoods)

        return likelihoods

    def train(self,instances, targets):

        #global __conditionalfeaturecounts__
        #global __classcounts__
        #global __traininginstancescount__
        self.__traininginstancescount__ = len(instances)

        if self.__traininginstancescount__ != len(targets):
            print("error: class and features are of unequal lengths")
            return
        i = 0
        #count the features given target by iterating through each instance
        #print(targets)
        for instance in instances:
            features = instance.copy()
            #print(features)
            j = 1
            #update class frequency table with the counts of each class
            updatefrequency(self.__classcounts__,targets[i])

            #update counts of each feature given target (key is x1=some value | y = some value)
            for feature in features:
                feature = "x{}={}".format(j,feature)
                j += 1
                condition = feature + " | " + "y={}".format(targets[i])
                #update the likelihood table with the condition counts of features
                updatefrequency(self.__conditionalfeaturecounts__,condition)
            i += 1

        return self.__traininginstancescount__, self.__classcounts__, self.__conditionalfeaturecounts__

    '''returns pair of maximum likely class and its probability'''
    def test(self,instance):

        #global __classcounts__
        #global __traininginstancescount__

        priors = self.__classcounts__.copy()
        n = self.__traininginstancescount__
        priors.update((x,y/n) for x, y in priors.items())
        posteriors = self.getlikelihoods(instance)
        posteriors.update((x,priors[x] * y) for x, y in posteriors.items())
        maxlabel = max(posteriors, key=lambda i: posteriors[i])

        return maxlabel, posteriors[maxlabel]