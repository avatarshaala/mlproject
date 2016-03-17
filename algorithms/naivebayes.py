__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from myutils.frequencytable import *

'''Naive Bayes calculates posterior probability p(Ck | X) as:

p(Ck | X) = p(Ck)P(X | Ck) / p(X)
where Ck = class k
    p(Ck) = prior of class k and p(X | Ck) = likelihood of feature X given Ck

    X = x1, x2, x3......,xn
Also p(X | Ck) = p(x1 | Ck)p(x2 | Ck)p(x3 | Ck).......p(xn | Ck)
For classification we obtain Class Ck for which posterior term p(Ck)p(X | Ck) is maximum

We calculate p(x1 | Ck ) = count(x1,Ck)/count(Ck) in the training data
In the program we denote:
count(x,c) as Count_xc and
count(c) as Count_c

The smoothing is done by Laplace( add one) smoothing (n = 1)
 The counts are adjusted by assuming each feature value and class co-occur at least once in the training corpus.
 For example if we want to count co-occurance of a value of x1 with a class Ck in the corpus,
 we add 1 to count of original co-occurance of that value of x1 with Ck (numerator); this enforces us to add
  |x1| 1's with the original count of the class Ck in the denominator (the number of possible values that x1 can take.

  Thus the probability calculation after smoothing will be,

                    count(x1,Ck) + n
  p(x1 | Ck) = --------------------------
                    count(Ck) + n * |x1|

 n = 1 for add one smoothing
'''

from math import log
class naivebayes:

    def __init__(self, loglikelihood = False, smoothed=True):
        self.__Counts_c__ = {}
        self.__Count_xc__ = {}#count of cooccurance of a feature and a class. x represents feature and c represents class
        self.__traininginstancescount__ = 0 # count of training data
        self.__smoothed__ = smoothed
        self.__featuresranges__ = {} #possible values each feature con take for example: x1 = {0,1}, x2 = {1,0}, x3= {0,1,2} etc
        self.loglikelihood = loglikelihood


    def setfeaturesranges(self, feature, value):
        if feature not in self.__featuresranges__:
            self.__featuresranges__[feature] = {value}
        else:
            self.__featuresranges__[feature].add(value)

    '''Function that returns priors of each class if default parameter is used else returns prior of a particular class'''
    def getpriors(self,label=None):

        if label != None:
            return {label: self.__Counts_c__[label] / self.__traininginstancescount__}

        priors = self.__Counts_c__.copy()
        priors.update((x,y/self.__traininginstancescount__) for x, y in priors.items())

        return priors

    '''Function that returns likelihood of the instance given the class or likelihood of the instance for all classes in default'''
    def getlikelihoods(self,instance, label = None):

        features = instance.copy()
        #print(print(label))
        '''define a local scope function to calculate likelihood of a given data instance with if given label'''
        def likelihood(label,features, likelihoods):
            j = 1
            #print(label)
            #do for each feature
            for feature in features:

                feature = "x{}={}".format(j,feature)
                condition = feature + " | " + "y={}".format(label)
                #print(condition)
                #multiply partial likelihood for each label with likelihood of feature for the label
                n = 0#smoothing constant
                if self.__smoothed__:
                    n = 1 #add one smoothing
                jointcount = 0
                if condition in self.__Count_xc__:
                    jointcount = self.__Count_xc__[condition]

                partial = (jointcount + n)/(self.__Counts_c__[label] + n * len(self.__featuresranges__["x{}".format(j)]))
                if self.loglikelihood:
                    likelihoods[label] += log(partial,2)
                else:
                    likelihoods[label] *= partial
                #print("likelihood for ", label, likelihoods[label])
                j += 1

        '''--------------------------------'''

        if label != None:
            likelihoods = {label:1}
            likelihood(label,features, likelihoods)
            return likelihoods

        '''initialize likelihood for each class to initial value'''
        init = 1
        if self.loglikelihood:
            init = 0
        likelihoods =  {label: init for label, count in self.__Counts_c__.items()}
        #do for each label
        for label, count in self.__Counts_c__.items():
            likelihood(label,features,likelihoods)

        return likelihoods

    def train(self,instances, targets):

        #print(targets)
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
            updatefrequency(self.__Counts_c__, targets[i])

            #update counts of each feature given target (key is x1=some value | y = some value)
            for featurevalue in features:
                featurevalue = "x{}={}".format(j,featurevalue)
                self.setfeaturesranges("x{}".format(j),featurevalue)
                j += 1
                condition = featurevalue + " | " + "y={}".format(targets[i])
                #update the likelihood table with the condition counts of features
                updatefrequency(self.__Count_xc__, condition)
            i += 1

        return self.__traininginstancescount__, self.__Counts_c__, self.__Count_xc__

    '''returns pair of maximum likely class and its probability'''
    def test(self,instance):

        #global __classcounts__
        #global __traininginstancescount__

        priors = self.__Counts_c__.copy()
        n = self.__traininginstancescount__
        priors.update((x,y/n) for x, y in priors.items())
        posteriors = self.getlikelihoods(instance)
        '''use priors'''
        '''
        if self.loglikelihood:
            posteriors.update((x,log(priors[x],2) + y) for x, y in posteriors.items())
        else:
            posteriors.update((x,priors[x] * y) for x, y in posteriors.items())
        '''
        '''--------'''
        maxlabel = max(posteriors, key=lambda i: posteriors[i])

        return maxlabel, posteriors[maxlabel]