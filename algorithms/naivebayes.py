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




def train(instances, targets, alpha, iterations, initial_weights=[], stop_after_convergence=True):

    pass



def test():
    pass