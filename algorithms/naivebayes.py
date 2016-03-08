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

def getlikelihood(instances, targets):
    likelihoods = {}
    if len(instances) != len(targets):
        print("error: class and features are of unequal lengths")
        return
    i = 0
    for instance in instances:
        conditional = instance + " | " + targets[i]
        if conditional in likelihoods:
            pass


def train(instances, target):



    pass



def test():
    pass