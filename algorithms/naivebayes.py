__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

def getpriors(targets):
    priors = {}
    for target in targets:
        if target in priors:
            priors[target] += 1
        else:
            priors[target] = 1
    n = len(targets)
    priors.update((x,y/n) for x, y in priors.items())

    return priors
'''features are the notation (such as x, y, z for 3-D feature vector) for feature vector'''
def getlikelihood(instances, targets):
    likelihoods = {}
    if len(instances) != len(targets):
        print("error: class and features are of unequal lengths")
        return
    i = 0
    for instance in instances:
        features = instance.split(",")
        j = 1
        for feature in features:
            feature = "x{}={}".format(j,feature)
            conditional = feature + " | " + "y={}".format(targets[i])
            if conditional in likelihoods:
                pass


def train(instances, target):



    pass



def test():
    pass